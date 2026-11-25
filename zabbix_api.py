#!/usr/bin/env python3
"""Client Zabbix 7.0 JSON-RPC (API token, header Bearer).
Crea/aggiorna/disabilita host un-device-per-host con template per tipo.
"""

import logging

import requests

log = logging.getLogger("ot.zabbix_api")

HOST_IFACE_TYPE_AGENT = 1


def technical_name(cfg, ip):
    prefix = cfg["zabbix"].get("host_prefix", "ot-")
    return prefix + str(ip).replace(".", "-")


class ZabbixApi:
    def __init__(self, api_url, api_token, dry_run=False):
        self.url = api_url
        self.token = api_token
        self.dry_run = dry_run
        self._id = 0
        self._template_cache = {}

    def call(self, method, params):
        if self.dry_run:
            log.info("[dry-run] API %s %s", method, params)
            return None

        self._id += 1
        payload = {"jsonrpc": "2.0", "method": method, "params": params,
                   "id": self._id, "auth": self.token}
        headers = {"Content-Type": "application/json-rpc",
                   "Authorization": f"Bearer {self.token}"}
        resp = requests.post(self.url, json=payload, headers=headers, timeout=30)
        resp.raise_for_status()
        body = resp.json()
        if "error" in body:
            raise RuntimeError(f"Zabbix API error [{method}]: {body['error']}")
        return body.get("result")

    def ensure_group(self, name):
        groups = self.call("hostgroup.get", {"output": ["groupid", "name"],
                                             "filter": {"name": [name]}})
        if self.dry_run:
            return "0"
        if groups:
            return groups[0]["groupid"]
        created = self.call("hostgroup.create", {"name": name})
        log.info("Creato host group '%s' (groupid=%s)", name, created["groupids"][0])
        return created["groupids"][0]

    def get_template_id(self, name):
        if name in self._template_cache:
            return self._template_cache[name]
        result = self.call("template.get", {"output": ["templateid"],
                                            "filter": {"host": [name]}})
        if self.dry_run:
            return "0"
        if not result:
            raise RuntimeError(f"Template Zabbix non trovato: '{name}' (importalo da templates/*.yaml)")
        self._template_cache[name] = result[0]["templateid"]
        return self._template_cache[name]

    def get_line_hosts(self, line_name):
        """Host tecnici della linea, mappati per nome tecnico."""
        if self.dry_run:
            return {}
        hosts = self.call("host.get", {
            "output": ["hostid", "host", "name", "status"],
            "selectParentTemplates": ["templateid", "name"],
            "selectTags": ["tag", "value"],
            "selectInventory": "extend",
            "tag": {"tag": "line", "value": line_name},
        }) or []
        return {h["host"]: h for h in hosts}

    def _assign_visible_names(self, devices, cfg, existing):
        """Nome visivo univoco per device: i WAGO usano il product_type (facile da
        cercare su Zabbix); altrimenti il nome, se vuoto il nome tecnico.
        Se duplicato (nella batch o gia' usato da altri host Zabbix) appende il MAC
        (globale, evita collisioni tra linee con stesso nome+IP); se il MAC manca, l'IP."""
        reserved = set()
        if not self.dry_run:
            all_hosts = self.call("host.get", {"output": ["host", "name"]}) or []
            managed = {technical_name(cfg, d["ip"]) for d in devices if d.get("ip")}
            # i nomi gia' assegnati a host di questa batch sono riassegnati qui sotto
            reserved = {h["name"] for h in all_hosts if h["host"] not in managed}

        names = {}
        used = set()
        for dev in sorted(devices, key=lambda d: d.get("ip") or ""):
            ip = dev.get("ip")
            if not ip:
                continue
            host = technical_name(cfg, ip)
            if "wago" in (dev.get("vendor") or "").lower() and dev.get("product_type"):
                base = dev["product_type"]
            else:
                base = (dev.get("name") or "").strip() or host
            suffix = (dev.get("mac") or "").strip() or ip
            candidate = base
            if candidate in reserved or candidate in used:
                candidate = f"{base} ({suffix})"
                n = 2
                while candidate in reserved or candidate in used:
                    candidate = f"{base} ({suffix}-{n})"
                    n += 1
            names[host] = candidate
            used.add(candidate)
        return names

    @staticmethod
    def _desired_tags(dev, line_name):
        tags = [
            {"tag": "line", "value": line_name},
            {"tag": "type", "value": dev["type"]},
        ]
        for tag, value in (("vendor", dev.get("vendor")),
                           ("protocol", dev.get("protocol")),
                           ("mac", dev.get("mac"))):
            if value:
                tags.append({"tag": tag, "value": str(value)})
        return tags

    @staticmethod
    def _desired_inventory(dev):
        inv = {"type": dev["type"]}
        if dev.get("name"):
            inv["name"] = dev["name"]
        if dev.get("serial"):
            inv["serialno_a"] = dev["serial"]
        if dev.get("mac"):
            inv["macaddress_a"] = dev["mac"]
        if dev.get("product_type"):
            inv["model"] = dev["product_type"]
        if dev.get("firmware"):
            inv["software"] = dev["firmware"]
        # notes: mai toccato dallo script (campo libero per uso manuale)
        if dev.get("vendor"):
            inv["vendor"] = dev["vendor"]
        return inv

    @staticmethod
    def _tags_equal(existing, desired):
        ex = {(t["tag"], t["value"]) for t in existing or []}
        de = {(t["tag"], t["value"]) for t in desired}
        return ex == de

    @staticmethod
    def _inventory_equal(existing, desired):
        existing = existing or {}
        return all(str(existing.get(k, "")) == str(v) for k, v in desired.items())

    def sync(self, devices, cfg, unseen_counts):
        """Sincronizza gli host Zabbix con i device scoperti.
        unseen_counts: dict nome_tecnico -> cicli discovery senza risposta (aggiornato in-place).
        Ritorna l'insieme dei nomi tecnici a cui inviare i valori trapper (host abilitati)."""
        line = cfg["line"]
        zbx = cfg["zabbix"]
        line_name = line["name"]
        disable_after = int(cfg["intervals"].get("disable_after", 3))

        groupid = self.ensure_group(line["host_group"])
        existing = self.get_line_hosts(line_name)

        # template id per tipo (lazy, solo i tipi presenti)
        template_ids = {}
        for dev in devices:
            tname = dev["type"]
            if tname not in template_ids:
                template_ids[tname] = self.get_template_id(cfg["templates"][tname])

        sendable = set()
        seen_names = set()
        visible_names = self._assign_visible_names(devices, cfg, existing)

        for dev in devices:
            ip = dev.get("ip")
            if not ip:
                log.warning("Device senza IP ignorato: %s", dev)
                continue

            host = technical_name(cfg, ip)
            seen_names.add(host)
            unseen_counts[host] = 0

            visible = visible_names[host]
            tags = self._desired_tags(dev, line_name)
            inventory = self._desired_inventory(dev)
            template = [{"templateid": template_ids[dev["type"]]}]

            current = existing.get(host)

            if current is None:
                result = self.call("host.create", {
                    "host": host,
                    "name": visible,
                    "groups": [{"groupid": groupid}],
                    "interfaces": [{
                        "type": HOST_IFACE_TYPE_AGENT, "main": 1, "useip": 1,
                        "ip": ip, "dns": "", "port": "10051",
                    }],
                    "templates": template,
                    "tags": tags,
                    "inventory_mode": 0,
                    "inventory": inventory,
                })
                if not self.dry_run:
                    log.info("Creato host %s (tipo=%s, ip=%s) hostid=%s",
                             host, dev["type"], ip, result["hostids"][0])
                sendable.add(host)
                continue

            sendable.add(host)

            update = {"hostid": current["hostid"]}
            fields = []

            if current.get("name") != visible:
                update["name"] = visible
                fields.append(f"nome->{visible}")

            if current.get("status") == "1":
                update["status"] = 0
                fields.append("riabilitato")

            current_templates = {t["name"] for t in current.get("parentTemplates", [])}
            desired_tname = cfg["templates"][dev["type"]]
            if current_templates != {desired_tname}:
                update["templates"] = template
                fields.append(f"template->{desired_tname}")

            if not self._tags_equal(current.get("tags"), tags):
                update["tags"] = tags
                fields.append("tags")

            if not self._inventory_equal(current.get("inventory"), inventory):
                update["inventory"] = inventory
                update["inventory_mode"] = 0
                fields.append("inventory")

            if len(update) > 1:
                self.call("host.update", update)
                if not self.dry_run:
                    log.info("Aggiornato host %s: %s", host, ", ".join(fields))

        # dispositivi spariti
        for host, count in unseen_counts.items():
            if host in seen_names:
                continue
            unseen_counts[host] = count + 1
            current = existing.get(host)
            if not current or current.get("status") == "1":
                continue
            if unseen_counts[host] >= disable_after:
                self.call("host.update", {"hostid": current["hostid"], "status": 1})
                if not self.dry_run:
                    log.warning("Disabilitato host %s (non visto da %d cicli)",
                                host, unseen_counts[host])
                sendable.discard(host)
            else:
                sendable.add(host)  # ancora attivo, continua a ricevere stato

        # non mandare valori a host disabilitati
        for host in list(sendable):
            current = existing.get(host)
            if current and current.get("status") == "1" and unseen_counts.get(host, 0) >= disable_after:
                sendable.discard(host)

        return sendable
