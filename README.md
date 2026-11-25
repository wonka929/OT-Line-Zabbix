# OT Line Zabbix

Testa linea di rete OT: scopre i device (ARP + PROFINET DCP + EtherNet/IP CIP),
li **classifica** (Allen-Bradley, Siemens, EtherNet-IP, PROFINET, PC, generic),
risolve gli **hostname** (NBNS/mDNS), effettua le **letture identificative**
(Siemens SZL, Allen-Bradley Logix, WAGO via Modbus TCP),
sincronizza gli **host Zabbix via API** (un host per device, template per tipo)
e invia lo stato via **trapper Sender**.

## Classificazione

| Scoperta | Regola | Tipo | Template Zabbix |
|---|---|---|---|
| CIP (`pycomm3`) | vendor Rockwell/Allen-Bradley | `allen_bradley` | OT / Allen-Bradley PLC |
| DCP (`pnio_dcp`) | OUI/vendor Siemens | `siemens` | OT / Siemens PLC |
| DCP | altri vendor PROFINET | `profinet` | OT / PROFINET device |
| CIP | altri vendor EtherNet/IP | `ethernetip` | OT / EtherNet-IP device |
| Solo ARP | OUI vendor PC noto | `pc` | OT / Generic device |
| Solo ARP | il resto | `generic` | OT / Generic device |

Merge protocolli (stesso MAC/IP): vincono **PROFINET > CIP > ARP**.

Letture base (configurabili in `reads:`):
- **Siemens**: SZL porta 102 (`s7_info.py`) → firmware, serial, modulo → inventario host
- **Allen-Bradley Logix**: `LogixDriver.info` → keyswitch (`ab.keyswitch`), nome, revision
- **WAGO senza CIP/PROFINET**: registri identificativi via **Modbus TCP** (`wago.py`,
  porta 502, registri `0x2010-0x2014` + descrizione `0x2020`) → product type, firmware,
  descrizione. Il vendor si riconosce dall'OUI MAC.

## Hostname

Se il device non espone hostname nei protocolli, viene risolto via **UDP unicast**
(nessun broadcast, nessun DNS):
- **NBNS** (`hostname_netbios`): packet NBSTAT wildcard verso il broadcast della rete locale
- **mDNS** (`hostname_mdns`): query PTR (QU) verso ip:5353
- cache positiva 1h, ThreadPool(8); se resta vuoto, `name` resta vuoto
  (il nome visivo Zabbix cade sul nome tecnico `ot-<ip>`)

## Zabbix: nomi e inventario

- **Nome tecnico** (host): `ot-<ip>` (es. `ot-192-168-1-10`) — univoco, usato per il sync
- **Nome visivo** (visibile/cercabile): hostname del device; per i **WAGO** il
  `product_type` (es. `750-362`); in caso di duplicati (batch o altri host Zabbix)
  suffix `(mac)` con fallback `(ip)`, poi `-2`
- **Inventario**: serial, mac, model (product_type), software (firmware), vendor;
  il campo **Notes non viene toccato** dallo script (libero per uso manuale)
- Tag `line:`, `type:`, `vendor:`, `protocol:`, `mac:`
- Device non visto per `disable_after` cicli → host **disabilitato** (mai cancellato)

## Come funziona

- **ogni `intervals.status_sec` (60s)**: sweep ARP + ping fallback → `dev.reachable`, `dev.last_seen`
- **ogni `intervals.discovery_sec` (900s)**:
  1. ARP su ogni interfaccia (`line.iface`, `auto` = tutte le IPv4 escluso loopback)
  2. PROFINET DCP `identify_all()` su ogni interfaccia
  3. CIP ListIdentity **unicast per-IP** (pre-check porta `discovery.cip_port`) sui IP
     candidati visti da ARP/DCP + `cip_extra_ips` — il broadcast 255.255.255.255 non
     funziona sulle linee senza router (fallback opzionale `cip_broadcast_fallback`)
  4. hostname NBNS/mDNS sui device senza nome
  5. letture base (SZL / Logix / WAGO Modbus) → sync API Zabbix
     (host create/update/enable/disable) → invio valori trapper

## Installazione

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # Linux
pip install -r requirements.txt
cp config.yaml.example config.yaml   # Windows: copy
```

Prerequisiti:
- **Windows**: Npcap con "WinPcap API-compatible Mode" (installer: https://nmap.org/npcap/)
- **Linux**: eseguire come root (raw socket per scapy/DCP)

## Configurazione Zabbix (7.0 LTS)

1. Importa i template: **Data collection → Templates → Import** →
   `templates/OT_Line_Zabbix_templates.yaml`
2. Crea un **API token**: **Administration → Users → API tokens** (utente con permessi
   su host group `OT/*`)
3. In `config.yaml` compila `zabbix.sender_host`, `zabbix.api_url`, `zabbix.api_token`
   (oppure la env `ZABBIX_API_TOKEN`)
4. (Consigliato) Sui template, limita la macro `{$TRAPPER.ALLOWED_HOSTS}` all'IP della
   testa linea invece di `0.0.0.0/0`

## Esecuzione

```bash
python main.py --dry-run --once     # scopre e classifica senza toccare Zabbix
python main.py --once               # un ciclo discovery reale (crea gli host)
python main.py                      # loop continuo
python main.py --iface 192.168.1.5  # forza l'interfaccia di scoperta
python main.py --iface eth0,eth1    # più interfacce (o discovery.ifaces in config)
```

Opzioni rilevanti di `config.yaml`:
- `line.iface`: `auto` (default) | nome/IP singolo | lista `eth0,eth1`
- `discovery.cip_port` / `cip_port_timeout` / `cip_extra_ips` / `cip_broadcast_fallback`
- `hostname`, `hostname_netbios`, `hostname_mdns`, `hostname_system`, `hostname_timeout_sec`
- `reads.s7_szl`, `reads.ab_keyswitch`, `reads.wago_modbus`,
  `reads.wago_modbus_port`, `reads.wago_modbus_timeout`

## Deploy come servizio

- **Linux**: copia `deploy/ot-line.service` in `/etc/systemd/system/`,
  adatta `WorkingDirectory`/`ExecStart`, poi `systemctl enable --now ot-line`
- **Windows**: `powershell -ExecutionPolicy Bypass -File deploy\install_task.ps1 -PythonExe <python.exe>`
  (task "OT_Line_Zabbix" avviato come SYSTEM all'avvio)

## Deploy come pacchetto Debian

Per creare il pacchetto DEB del software, bisogna creare questa directory così fatta:

```
[drwxr-xr-x root     4.0K]  .
[drwxr-xr-x root     4.0K]  ./DEBIAN
[-rw-r--r-- root      273]  ./DEBIAN/control
[-rwxr-xr-x root      127]  ./DEBIAN/postrm
[-rwxr-xr-x root      116]  ./DEBIAN/prerm
[drwxr-xr-x root     4.0K]  ./bin
[-rwxr-xr-x root      21M]  ./bin/ot-line-zabbix
[drwxr-xr-x root     4.0K]  ./etc
[drwxr-xr-x root     4.0K]  ./etc/ot-line-zabbix
[-rw-r--r-- root     2.9K]  ./etc/ot-line-zabbix/config.yaml
[drwxr-xr-x root     4.0K]  ./lib
[drwxr-xr-x root     4.0K]  ./lib/systemd
[drwxr-xr-x root     4.0K]  ./lib/systemd/system
[-rw-r--r-- root      370]  ./lib/systemd/system/ot-line-zabbix.service
```

A quel punto bisogna compilare il pacchetto con il comando:

```
sudo dpkg -i ot-line-zabbix.deb
```

La directory con i file in questo momento è in OT_Line_Zabbix\dist\ot-line-zabbix-deb
Bisogna controllare però che i permessi siano corretti: wsl non gestisce i permessi su filesystem NTFS per cui bisogna spostare la cartella nella home di wsl, cambiare i permessi e compilare il file deb da lì.


## Troubleshooting

- `Identify`/arping fallisce su Windows → Npcap installato e servizio pcap in esecuzione
- `processed=0` dal Sender → host/item non ancora nel config cache di Zabbix (attendi 30-60s)
  o `{$TRAPPER.ALLOWED_HOSTS}` non include l'IP della testa linea
- `Template non trovato` → importare prima lo YAML dei template
- `auto` fallisce con più NIC → specifica `line.iface` (nome o IP)
