# New session - 2026-10-22T12:35:11.866Z

**Session ID:** ses_e9c644885ffemm9ed4qf88nngN
**Created:** 22/10/2026, 14:35:11
**Updated:** 22/10/2026, 15:50:25

---

## User

Guarda il progetto nella cartella. Credo ci sia un errore nell'api perchè richiama dei parametri di inventario che non esistono. I parametri sono visibili in questa pagina: https://www.zabbix.com/documentation/7.4/en/manual/api/reference/host/create

---

## Assistant (Build · MiMo-V2.6-Flash Free · 24.9s)

_Thinking:_

The user is asking me to look at the project in the current folder. They think there's an error in the API because it calls inventory parameters that don't exist. They say the parameters are visible at the Zabbix documentation page for host/create API reference.

Let me first explore the project structure, then fetch the documentation page to compare parameters.

**Tool: bash**

**Input:**
```json
{
  "command": "Get-ChildItem -Force | Select-Object Name, Mode, Length"
}
```

**Output:**
```

[32;1mName                 [0m[32;1m Mode [0m[32;1m Length[0m
[32;1m----                 [0m [32;1m---- [0m [32;1m------[0m
deploy                d---- 
templates             d---- 
.gitignore            -a--- 44
config.yaml.example   -a--- 2419
discovery-zabbix.json -a--- 625647
discovery.py          -a--- 8080
mac_vendors_db.py     -a--- 1403877
main.py               -a--- 6804
readers.py            -a--- 2362
README.md             -a--- 3581
requirements.txt      -a--- 59
s7_info.py            -a--- 8254
zabbix_api.py         -a--- 8877
zabbix_sender.py      -a--- 965


```

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://www.zabbix.com/documentation/7.4/en/manual/api/reference/host/create",
  "format": "markdown"
}
```

**Output:**
```
            host.create                                    

[![logo](/documentation/7.4/images/logo.svg)

# Docs

](https://www.zabbix.com "Zabbix")

Version: 7.4 (current)

-   Supported
-   [7.4 (current)](/documentation/7.4/../current/en/manual/api/reference/host/create)
-   [7.0](/documentation/7.4/../7.0/en/manual/api/reference/host/create)
-   [6.0](/documentation/7.4/../6.0/en/manual/api/reference/host/create)
-   In development
-   [8.0 (devel)](/documentation/7.4/../devel/en/manual/api/reference/host/create)
-   Unsupported
-   [7.2](/documentation/7.4/../7.2/en/manual/api/reference/host/create)
-   [6.4](/documentation/7.4/../6.4/en/manual/api/reference/host/create)
-   [6.2](/documentation/7.4/../6.2/en/manual/api/reference/host/create)
-   [5.4](/documentation/7.4/../5.4/en/manual/api/reference/host/create)
-   [5.2](/documentation/7.4/../5.2/en/manual/api/reference/host/create)
-   [5.0](/documentation/7.4/../5.0/en/manual/api/reference/host/create)
-   [4.4](/documentation/7.4/../4.4/en/manual/api/reference/host/create)
-   [4.2](/documentation/7.4/../4.2/en/manual/api/reference/host/create)
-   [4.0](/documentation/7.4/../4.0/en/manual/api/reference/host/create)
-   [3.4](/documentation/7.4/../3.4/en/manual/api/reference/host/create)
-   [3.2](/documentation/7.4/../3.2/en/manual/api/reference/host/create)
-   [3.0](/documentation/7.4/../3.0/en/manual/api/reference/host/create)
-   [2.4](/documentation/7.4/../2.4/en/manual/api/reference/host/create)
-   [2.2](/documentation/7.4/../2.2/en/manual/api/reference/host/create)
-   [2.0](/documentation/7.4/../2.0/en/manual/api/reference/host/create)
-   [1.8](/documentation/7.4/../1.8/en/manual/api/reference/host/create)
-   General
-   [info](/documentation/7.4/../info/en)
-   [guidelines](/documentation/7.4/../guidelines/en)

Language: English

-   [English](/documentation/7.4/en/manual/api/reference/host/create)
-   [日本語](/documentation/7.4/jp/manual/api/reference/host/create)
-   [Português](/documentation/7.4/pt/manual/api/reference/host/create)
-   [Español](/documentation/7.4/es/manual/api/reference/host/create)
-   [Français](/documentation/7.4/fr/manual/api/reference/host/create)
-   [Latviešu](/documentation/7.4/lv/manual/api/reference/host/create)
-   [中文](/documentation/7.4/zh/manual/api/reference/host/create)
-   [Polski](/documentation/7.4/pl/manual/api/reference/host/create)
-   [Italiano](/documentation/7.4/it/manual/api/reference/host/create)
-   [Deutsch](/documentation/7.4/de/manual/api/reference/host/create)
-   [Русский](/documentation/7.4/ru/manual/api/reference/host/create)
-   [Català](/documentation/7.4/ca/manual/api/reference/host/create)
-   [Srpski](/documentation/7.4/sr/manual/api/reference/host/create)

[Download Zabbix Manual in PDF](/documentation/7.4/downloads/Zabbix_Documentation_7.4.en.pdf)

Theme:

-   [Light](#)
-   [Dark](#)
-   [System](#)

[User manual](/documentation/7.4/en/manual)

[1 Introduction](/documentation/7.4/en/manual/introduction)

[1 Manual structure](/documentation/7.4/en/manual/introduction/manual_structure)

[2 What is Zabbix](/documentation/7.4/en/manual/introduction/about)

[3 Zabbix features](/documentation/7.4/en/manual/introduction/features)

[4 Zabbix overview](/documentation/7.4/en/manual/introduction/overview)

[5 What's new in Zabbix 7.4.0](/documentation/7.4/en/manual/introduction/whatsnew)

[6 What's new in Zabbix 7.4.x](/documentation/7.4/en/manual/introduction/whatsnew_minor)

[2 Definitions](/documentation/7.4/en/manual/definitions)

[3 Zabbix processes](/documentation/7.4/en/manual/concepts)

[1 Server](/documentation/7.4/en/manual/concepts/server)

[1 High availability](/documentation/7.4/en/manual/concepts/server/ha)

[2 Agent](/documentation/7.4/en/manual/concepts/agent)

[3 Agent 2](/documentation/7.4/en/manual/concepts/agent2)

[4 Proxy](/documentation/7.4/en/manual/concepts/proxy)

[5 Java gateway](/documentation/7.4/en/manual/concepts/java)

[1 Setup from RHEL packages](/documentation/7.4/en/manual/concepts/java/from_rhel)

[2 Setup from Debian/Ubuntu packages](/documentation/7.4/en/manual/concepts/java/from_debian_ubuntu)

[3 Setup from sources](/documentation/7.4/en/manual/concepts/java/from_sources)

[6 Sender](/documentation/7.4/en/manual/concepts/sender)

[7 Get](/documentation/7.4/en/manual/concepts/get)

[8 JS](/documentation/7.4/en/manual/concepts/js)

[9 Web service](/documentation/7.4/en/manual/concepts/web_service)

[4 Installation and first steps](/documentation/7.4/en/manual/installation)

[1 Getting Zabbix](/documentation/7.4/en/manual/installation/getting_zabbix)

[2 Requirements](/documentation/7.4/en/manual/installation/requirements)

[3 Installation from sources](/documentation/7.4/en/manual/installation/install)

[1 Building Zabbix agent on Windows](/documentation/7.4/en/manual/installation/install/win_agent)

[2 Building Zabbix agent 2 on Windows](/documentation/7.4/en/manual/installation/install/building_zabbix_agent_2_on_windows)

[3 Building Zabbix agent on macOS](/documentation/7.4/en/manual/installation/install/mac_agent)

[4 Installation from packages](/documentation/7.4/en/manual/installation/install_from_packages)

[1 Windows agent installation from MSI](/documentation/7.4/en/manual/installation/install_from_packages/win_msi)

[2 macOS agent installation from PKG](/documentation/7.4/en/manual/installation/install_from_packages/mac_pkg)

[3 Unstable releases](/documentation/7.4/en/manual/installation/install_from_packages/unstable)

[5 Installation from containers](/documentation/7.4/en/manual/installation/containers)

[6 Installation on public cloud platforms](/documentation/7.4/en/manual/installation/install_cloud_platforms)

[1 AWS deployment guide for Zabbix server](/documentation/7.4/en/manual/installation/install_cloud_platforms/aws_deployment_guide)

[2 AWS deployment guide for Zabbix proxy](/documentation/7.4/en/manual/installation/install_cloud_platforms/aws_deployment_guide_proxy)

[3 Azure deployment guide for Zabbix server](/documentation/7.4/en/manual/installation/install_cloud_platforms/azure_deployment_guide)

[4 Azure deployment guide for Zabbix proxy](/documentation/7.4/en/manual/installation/install_cloud_platforms/azure_deployment_guide_proxy)

[5 Google Cloud deployment guide](/documentation/7.4/en/manual/installation/install_cloud_platforms/cloud_google)

[7 Web interface installation](/documentation/7.4/en/manual/installation/frontend)

[8 Upgrade procedure](/documentation/7.4/en/manual/installation/upgrade)

[1 Upgrade from sources](/documentation/7.4/en/manual/installation/upgrade/sources)

[2 Upgrade from packages](/documentation/7.4/en/manual/installation/upgrade/packages)

[1 Red Hat Enterprise Linux](/documentation/7.4/en/manual/installation/upgrade/packages/rhel)

[2 Debian/Ubuntu](/documentation/7.4/en/manual/installation/upgrade/packages/debian_ubuntu)

[3 Upgrade from containers](/documentation/7.4/en/manual/installation/upgrade/containers)

[9 Known issues](/documentation/7.4/en/manual/installation/known_issues)

[1 Compilation issues](/documentation/7.4/en/manual/installation/known_issues/compilation_issues)

[2 Escaping-related upgrade issues](/documentation/7.4/en/manual/installation/known_issues/db_upgrade_escaping)

[10 Template changes](/documentation/7.4/en/manual/installation/template_changes)

[11 Upgrade notes for 7.4.0](/documentation/7.4/en/manual/installation/upgrade_notes)

[12 Upgrade notes for 7.4.x](/documentation/7.4/en/manual/installation/upgrade_notes_minor)

[5 Quickstart](/documentation/7.4/en/manual/quickstart)

[1 Login and configuring user](/documentation/7.4/en/manual/quickstart/login)

[2 New host](/documentation/7.4/en/manual/quickstart/host)

[3 New item](/documentation/7.4/en/manual/quickstart/item)

[4 New trigger](/documentation/7.4/en/manual/quickstart/trigger)

[5 Receiving problem notification](/documentation/7.4/en/manual/quickstart/notification)

[6 New template](/documentation/7.4/en/manual/quickstart/template)

[6 Zabbix appliance](/documentation/7.4/en/manual/appliance)

[7 Configuration](/documentation/7.4/en/manual/config)

[1 Hosts and host groups](/documentation/7.4/en/manual/config/hosts)

[1 Host Wizard](/documentation/7.4/en/manual/config/hosts/host_wizard)

[2 Configuring a host](/documentation/7.4/en/manual/config/hosts/host)

[3 Configuring a host group](/documentation/7.4/en/manual/config/hosts/host_groups)

[4 Inventory](/documentation/7.4/en/manual/config/hosts/inventory)

[5 Mass update](/documentation/7.4/en/manual/config/hosts/hostupdate)

[2 Items](/documentation/7.4/en/manual/config/items)

[1 Creating an item](/documentation/7.4/en/manual/config/items/item)

[1 Item key format](/documentation/7.4/en/manual/config/items/item/key)

[2 Custom intervals](/documentation/7.4/en/manual/config/items/item/custom_intervals)

[2 Item value preprocessing](/documentation/7.4/en/manual/config/items/preprocessing)

[1 Preprocessing testing](/documentation/7.4/en/manual/config/items/preprocessing/testing)

[2 Preprocessing details](/documentation/7.4/en/manual/config/items/preprocessing/preprocessing_details)

[3 Preprocessing examples](/documentation/7.4/en/manual/config/items/preprocessing/examples)

[4 JSONPath functionality](/documentation/7.4/en/manual/config/items/preprocessing/jsonpath_functionality)

[1 Escaping special characters from LLD macro values in JSONPath](/documentation/7.4/en/manual/config/items/preprocessing/jsonpath_functionality/escaping_lld_macros)

[5 JavaScript preprocessing](/documentation/7.4/en/manual/config/items/preprocessing/javascript)

[1 Additional JavaScript objects](/documentation/7.4/en/manual/config/items/preprocessing/javascript/javascript_objects)

[2 Browser item JavaScript objects](/documentation/7.4/en/manual/config/items/preprocessing/javascript/browser_item_javascript_objects)

[6 CSV to JSON preprocessing](/documentation/7.4/en/manual/config/items/preprocessing/csv_to_json)

[3 Item types](/documentation/7.4/en/manual/config/items/itemtypes)

[1 Zabbix agent](/documentation/7.4/en/manual/config/items/itemtypes/zabbix_agent)

[1 Zabbix agent 2](/documentation/7.4/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2)

[2 Windows Zabbix agent](/documentation/7.4/en/manual/config/items/itemtypes/zabbix_agent/win_keys)

[3 Log file monitoring](/documentation/7.4/en/manual/config/items/itemtypes/zabbix_agent/log_items)

[2 Simple check](/documentation/7.4/en/manual/config/items/itemtypes/simple_checks)

[1 VMware monitoring item keys](/documentation/7.4/en/manual/config/items/itemtypes/simple_checks/vmware_keys)

[3 SNMP agent](/documentation/7.4/en/manual/config/items/itemtypes/snmp)

[1 Dynamic indexes](/documentation/7.4/en/manual/config/items/itemtypes/snmp/dynamicindex)

[2 Special OIDs](/documentation/7.4/en/manual/config/items/itemtypes/snmp/special_mibs)

[3 MIB files](/documentation/7.4/en/manual/config/items/itemtypes/snmp/mibs)

[4 SNMP trap](/documentation/7.4/en/manual/config/items/itemtypes/snmptrap)

[5 Zabbix internal](/documentation/7.4/en/manual/config/items/itemtypes/internal)

[6 Zabbix trapper](/documentation/7.4/en/manual/config/items/itemtypes/trapper)

[7 External check](/documentation/7.4/en/manual/config/items/itemtypes/external)

[8 Database monitor](/documentation/7.4/en/manual/config/items/itemtypes/odbc_checks)

[9 HTTP agent](/documentation/7.4/en/manual/config/items/itemtypes/http)

[1 Prometheus check](/documentation/7.4/en/manual/config/items/itemtypes/http/prometheus)

[10 IPMI agent](/documentation/7.4/en/manual/config/items/itemtypes/ipmi)

[11 SSH agent](/documentation/7.4/en/manual/config/items/itemtypes/ssh_checks)

[12 Telnet agent](/documentation/7.4/en/manual/config/items/itemtypes/telnet_checks)

[13 JMX agent](/documentation/7.4/en/manual/config/items/itemtypes/jmx_monitoring)

[14 Calculated item](/documentation/7.4/en/manual/config/items/itemtypes/calculated)

[1 Aggregate calculations](/documentation/7.4/en/manual/config/items/itemtypes/calculated/aggregate)

[15 Dependent item](/documentation/7.4/en/manual/config/items/itemtypes/dependent_items)

[16 Script item](/documentation/7.4/en/manual/config/items/itemtypes/script)

[17 Browser item](/documentation/7.4/en/manual/config/items/itemtypes/browser)

[4 History and trends](/documentation/7.4/en/manual/config/items/history_and_trends)

[5 User parameters](/documentation/7.4/en/manual/config/items/userparameters)

[1 Extending Zabbix agents](/documentation/7.4/en/manual/config/items/userparameters/extending_agent)

[6 Windows performance counters](/documentation/7.4/en/manual/config/items/perfcounters)

[7 Mass update](/documentation/7.4/en/manual/config/items/itemupdate)

[8 Value mapping](/documentation/7.4/en/manual/config/items/mapping)

[9 Queue](/documentation/7.4/en/manual/config/items/queue)

[10 Value cache](/documentation/7.4/en/manual/config/items/value_cache)

[11 Execute now](/documentation/7.4/en/manual/config/items/check_now)

[12 Restricting agent checks](/documentation/7.4/en/manual/config/items/restrict_checks)

[3 Triggers](/documentation/7.4/en/manual/config/triggers)

[1 Configuring a trigger](/documentation/7.4/en/manual/config/triggers/trigger)

[2 Trigger expression](/documentation/7.4/en/manual/config/triggers/expression)

[3 Trigger dependencies](/documentation/7.4/en/manual/config/triggers/dependencies)

[4 Trigger severity](/documentation/7.4/en/manual/config/triggers/severity)

[5 Customizing trigger severities](/documentation/7.4/en/manual/config/triggers/customseverities)

[6 Mass update](/documentation/7.4/en/manual/config/triggers/update)

[7 Predictive trigger functions](/documentation/7.4/en/manual/config/triggers/prediction)

[4 Events](/documentation/7.4/en/manual/config/events)

[1 Trigger event generation](/documentation/7.4/en/manual/config/events/trigger_events)

[2 Other event sources](/documentation/7.4/en/manual/config/events/sources)

[3 Manual closing of problems](/documentation/7.4/en/manual/config/events/manual_close)

[5 Event correlation](/documentation/7.4/en/manual/config/event_correlation)

[1 Trigger-based event correlation](/documentation/7.4/en/manual/config/event_correlation/trigger)

[2 Global event correlation](/documentation/7.4/en/manual/config/event_correlation/global)

[6 Tagging](/documentation/7.4/en/manual/config/tagging)

[7 Visualization](/documentation/7.4/en/manual/config/visualization)

[1 Graphs](/documentation/7.4/en/manual/config/visualization/graphs)

[1 Simple graphs](/documentation/7.4/en/manual/config/visualization/graphs/simple)

[2 Custom graphs](/documentation/7.4/en/manual/config/visualization/graphs/custom)

[3 Ad-hoc graphs](/documentation/7.4/en/manual/config/visualization/graphs/adhoc)

[2 Network maps](/documentation/7.4/en/manual/config/visualization/maps)

[1 Configuring a network map](/documentation/7.4/en/manual/config/visualization/maps/map)

[2 Host group elements](/documentation/7.4/en/manual/config/visualization/maps/host_groups)

[3 Link indicators](/documentation/7.4/en/manual/config/visualization/maps/links)

[3 Dashboards](/documentation/7.4/en/manual/config/visualization/dashboard)

[8 Templates and template groups](/documentation/7.4/en/manual/config/templates)

[1 Configuring a template](/documentation/7.4/en/manual/config/templates/template)

[2 Configuring a template group](/documentation/7.4/en/manual/config/templates/template_groups)

[3 Linking/unlinking](/documentation/7.4/en/manual/config/templates/linking)

[4 Nesting](/documentation/7.4/en/manual/config/templates/nesting)

[5 Mass update](/documentation/7.4/en/manual/config/templates/mass)

[9 Templates out of the box](/documentation/7.4/en/manual/config/templates_out_of_the_box)

[1 Zabbix agent template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/zabbix_agent)

[2 Zabbix agent 2 template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/zabbix_agent2)

[3 HTTP template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/http)

[4 IPMI template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/ipmi)

[5 JMX template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/jmx)

[6 ODBC template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/odbc_checks)

[7 Standardized templates for network devices](/documentation/7.4/en/manual/config/templates_out_of_the_box/network_devices)

[8 VMware template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/vmware)

[10 Notifications upon events](/documentation/7.4/en/manual/config/notifications)

[1 Media types](/documentation/7.4/en/manual/config/notifications/media)

[1 Email](/documentation/7.4/en/manual/config/notifications/media/email)

[1 Automated Gmail/Office365 media types](/documentation/7.4/en/manual/config/notifications/media/email/gmail_office)

[2 SMS](/documentation/7.4/en/manual/config/notifications/media/sms)

[3 Custom alert scripts](/documentation/7.4/en/manual/config/notifications/media/script)

[4 Webhook](/documentation/7.4/en/manual/config/notifications/media/webhook)

[1 Webhook script examples](/documentation/7.4/en/manual/config/notifications/media/webhook/webhook_examples)

[2 Actions](/documentation/7.4/en/manual/config/notifications/action)

[1 Conditions](/documentation/7.4/en/manual/config/notifications/action/conditions)

[2 Operations](/documentation/7.4/en/manual/config/notifications/action/operation)

[1 Sending message](/documentation/7.4/en/manual/config/notifications/action/operation/message)

[2 Remote commands](/documentation/7.4/en/manual/config/notifications/action/operation/remote_command)

[3 Additional operations](/documentation/7.4/en/manual/config/notifications/action/operation/other)

[4 Using macros in messages](/documentation/7.4/en/manual/config/notifications/action/operation/macros)

[3 Recovery operations](/documentation/7.4/en/manual/config/notifications/action/recovery_operations)

[4 Update operations](/documentation/7.4/en/manual/config/notifications/action/update_operations)

[5 Escalations](/documentation/7.4/en/manual/config/notifications/action/escalations)

[3 Receiving notification on unsupported items](/documentation/7.4/en/manual/config/notifications/unsupported_item)

[11 Macros](/documentation/7.4/en/manual/config/macros)

[1 Macro functions](/documentation/7.4/en/manual/config/macros/macro_functions)

[2 User macros](/documentation/7.4/en/manual/config/macros/user_macros)

[3 User macros with context](/documentation/7.4/en/manual/config/macros/user_macros_context)

[4 Secret user macros](/documentation/7.4/en/manual/config/macros/secret_macros)

[5 Low-level discovery macros](/documentation/7.4/en/manual/config/macros/lld_macros)

[6 Expression macros](/documentation/7.4/en/manual/config/macros/expression_macros)

[12 Users and user groups](/documentation/7.4/en/manual/config/users_and_usergroups)

[1 Configuring a user](/documentation/7.4/en/manual/config/users_and_usergroups/user)

[2 Permissions](/documentation/7.4/en/manual/config/users_and_usergroups/permissions)

[3 User groups](/documentation/7.4/en/manual/config/users_and_usergroups/usergroup)

[13 Storage of secrets](/documentation/7.4/en/manual/config/secrets)

[1 CyberArk configuration](/documentation/7.4/en/manual/config/secrets/cyberark)

[2 HashiCorp configuration](/documentation/7.4/en/manual/config/secrets/hashicorp)

[14 Scheduled reports](/documentation/7.4/en/manual/config/reports)

[15 Data export](/documentation/7.4/en/manual/config/export)

[1 Export to files](/documentation/7.4/en/manual/config/export/files)

[2 Streaming to external systems](/documentation/7.4/en/manual/config/export/streaming)

[3 SNMP gateway](/documentation/7.4/en/manual/config/export/snmp_gateway)

[8 Service monitoring](/documentation/7.4/en/manual/it_services)

[1 Service tree](/documentation/7.4/en/manual/it_services/service_tree)

[2 SLA](/documentation/7.4/en/manual/it_services/sla)

[3 Setup example](/documentation/7.4/en/manual/it_services/example)

[9 Web monitoring](/documentation/7.4/en/manual/web_monitoring)

[1 Web monitoring items](/documentation/7.4/en/manual/web_monitoring/items)

[2 Real-life scenario](/documentation/7.4/en/manual/web_monitoring/example)

[10 Virtual machine monitoring](/documentation/7.4/en/manual/vm_monitoring)

[1 VMware monitoring item keys](/documentation/7.4/en/manual/vm_monitoring/vmware_keys)

[2 Virtual machine discovery key fields](/documentation/7.4/en/manual/vm_monitoring/discovery_fields)

[3 JSON examples for VMware items](/documentation/7.4/en/manual/vm_monitoring/vmware_json)

[4 VMware monitoring setup example](/documentation/7.4/en/manual/vm_monitoring/example)

[11 Maintenance](/documentation/7.4/en/manual/maintenance)

[12 Regular expressions](/documentation/7.4/en/manual/regular_expressions)

[13 Problem acknowledgment](/documentation/7.4/en/manual/acknowledgment)

[1 Problem suppression](/documentation/7.4/en/manual/acknowledgment/suppression)

[14 Configuration export/import](/documentation/7.4/en/manual/xml_export_import)

[1 Template groups](/documentation/7.4/en/manual/xml_export_import/templategroups)

[2 Host groups](/documentation/7.4/en/manual/xml_export_import/hostgroups)

[3 Templates](/documentation/7.4/en/manual/xml_export_import/templates)

[4 Hosts](/documentation/7.4/en/manual/xml_export_import/hosts)

[5 Network maps](/documentation/7.4/en/manual/xml_export_import/maps)

[6 Media types](/documentation/7.4/en/manual/xml_export_import/media)

[15 Discovery](/documentation/7.4/en/manual/discovery)

[1 Network discovery](/documentation/7.4/en/manual/discovery/network_discovery)

[1 Configuring a network discovery rule](/documentation/7.4/en/manual/discovery/network_discovery/rule)

[2 Active agent autoregistration](/documentation/7.4/en/manual/discovery/auto_registration)

[3 Low-level discovery](/documentation/7.4/en/manual/discovery/low_level_discovery)

[1 Item prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/item_prototypes)

[2 Trigger prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/trigger_prototypes)

[3 Graph prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/graph_prototypes)

[4 Host prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/host_prototypes)

[5 Discovery prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/discovery_prototypes)

[6 Notes on low-level discovery](/documentation/7.4/en/manual/discovery/low_level_discovery/notes)

[7 Discovery rules](/documentation/7.4/en/manual/discovery/low_level_discovery/examples)

[1 Discovery of mounted filesystems](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/mounted_filesystems)

[2 Discovery of network interfaces](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/network_interfaces)

[3 Discovery of CPUs and CPU cores](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/cpu)

[4 Discovery of SNMP OIDs](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/snmp_oids_walk)

[5 Discovery of SNMP OIDs (legacy)](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/snmp_oids)

[6 Discovery of JMX objects](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/jmx)

[7 Discovery of IPMI sensors](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/ipmi_sensors)

[8 Discovery of systemd services](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/systemd)

[9 Discovery of Windows services](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/windows_services)

[10 Discovery of Windows performance counter instances](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/windows_perf_instances)

[11 Discovery using WMI queries](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/wmi)

[12 Discovery using ODBC SQL queries](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/sql_queries)

[13 Discovery using Prometheus data](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/prometheus)

[14 Discovery of block devices](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/devices)

[15 Discovery of host interfaces in Zabbix](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/host_interfaces)

[8 Custom LLD rules](/documentation/7.4/en/manual/discovery/low_level_discovery/custom_rules)

[16 Distributed monitoring](/documentation/7.4/en/manual/distributed_monitoring)

[1 Proxies](/documentation/7.4/en/manual/distributed_monitoring/proxies)

[1 Synchronization of monitoring configuration](/documentation/7.4/en/manual/distributed_monitoring/proxies/sync)

[2 Proxy load balancing and high availability](/documentation/7.4/en/manual/distributed_monitoring/proxies/ha)

[17 Encryption](/documentation/7.4/en/manual/encryption)

[1 Using certificates](/documentation/7.4/en/manual/encryption/using_certificates)

[2 Using pre-shared keys](/documentation/7.4/en/manual/encryption/using_pre_shared_keys)

[3 Troubleshooting](/documentation/7.4/en/manual/encryption/troubleshooting)

[1 Connection type or permission problems](/documentation/7.4/en/manual/encryption/troubleshooting/connection_permission_problems)

[2 Certificate problems](/documentation/7.4/en/manual/encryption/troubleshooting/certificate_problems)

[3 PSK problems](/documentation/7.4/en/manual/encryption/troubleshooting/psk_problems)

[18 Web interface](/documentation/7.4/en/manual/web_interface)

[1 Menu](/documentation/7.4/en/manual/web_interface/menu)

[1 Event menu](/documentation/7.4/en/manual/web_interface/menu/event_menu)

[2 Host menu](/documentation/7.4/en/manual/web_interface/menu/host_menu)

[3 Item menu](/documentation/7.4/en/manual/web_interface/menu/item_menu)

[2 Frontend sections](/documentation/7.4/en/manual/web_interface/frontend_sections)

[1 Dashboards](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards)

[1 Dashboard widgets](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets)

[1 Action log](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/action_log)

[2 Clock](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/clock)

[3 Discovery status](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/discovery_status)

[4 Favorite graphs](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/favorite_graphs)

[5 Favorite maps](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/favorite_maps)

[6 Gauge](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge)

[7 Geomap](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/geomap)

[8 Graph](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/graph)

[9 Graph (classic)](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_classic)

[10 Graph prototype](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_prototype)

[11 Honeycomb](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/honeycomb)

[12 Host availability](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/host_availability)

[13 Host card](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/host_card)

[14 Host navigator](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/host_navigator)

[15 Item card](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/item_card)

[16 Item history](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history)

[17 Item navigator](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/item_navigator)

[18 Item value](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/item_value)

[19 Map](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/map)

[20 Map navigation tree](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/map_tree)

[21 Pie chart](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/pie_chart)

[22 Problem hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/problem_hosts)

[23 Problems](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/problems)

[24 Problems by severity](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/problems_severity)

[25 SLA report](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/sla_report)

[26 System information](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/system)

[27 Top hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/top_hosts)

[28 Top items](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/top_items)

[29 Top triggers](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/top_triggers)

[30 Trigger overview](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/trigger_overview)

[31 URL](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/url)

[32 Web monitoring](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/web_monitoring)

[2 Monitoring](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring)

[1 Problems](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/problems)

[1 Cause and symptom problems](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/problems/cause_and_symptom)

[2 Hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/hosts)

[1 Graphs](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/hosts/graphs)

[2 Host dashboards](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/hosts/dashboards)

[3 Web scenarios](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/hosts/web)

[3 Latest data](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/latest_data)

[4 Maps](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/maps)

[5 Discovery](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/discovery)

[3 Services](/documentation/7.4/en/manual/web_interface/frontend_sections/services)

[1 Services](/documentation/7.4/en/manual/web_interface/frontend_sections/services/service)

[2 SLA](/documentation/7.4/en/manual/web_interface/frontend_sections/services/sla)

[3 SLA report](/documentation/7.4/en/manual/web_interface/frontend_sections/services/sla_report)

[4 Inventory](/documentation/7.4/en/manual/web_interface/frontend_sections/inventory)

[1 Overview](/documentation/7.4/en/manual/web_interface/frontend_sections/inventory/overview)

[2 Hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/inventory/hosts)

[5 Reports](/documentation/7.4/en/manual/web_interface/frontend_sections/reports)

[1 System information](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/status_of_zabbix)

[2 Scheduled reports](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/scheduled)

[3 Availability report](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/availability)

[4 Top 100 triggers](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/triggers_top)

[5 Audit log](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/audit_log)

[6 Action log](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/action_log)

[7 Notifications](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/notifications)

[6 Data collection](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection)

[1 Template groups](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templategroups)

[2 Host groups](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hostgroups)

[3 Templates](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates)

[1 Items](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/items)

[2 Triggers](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/triggers)

[3 Graphs](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/graphs)

[4 Discovery rules](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery)

[1 Item prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/item_prototypes)

[2 Trigger prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/trigger_prototypes)

[3 Graph prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/graph_prototypes)

[4 Host prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/host_prototypes)

[5 Discovery prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/discovery_prototypes)

[5 Web scenarios](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/web)

[4 Hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts)

[1 Items](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/items)

[2 Triggers](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/triggers)

[3 Graphs](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/graphs)

[4 Discovery rules](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery)

[1 Item prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/item_prototypes)

[2 Trigger prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/trigger_prototypes)

[3 Graph prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/graph_prototypes)

[4 Host prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/host_prototypes)

[5 Discovery prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/discovery_prototypes)

[5 Web scenarios](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/web)

[5 Maintenance](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/maintenance)

[6 Event correlation](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/correlation)

[7 Discovery](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/discovery)

[7 Alerts](/documentation/7.4/en/manual/web_interface/frontend_sections/alerts)

[1 Actions](/documentation/7.4/en/manual/web_interface/frontend_sections/alerts/actions)

[2 Media types](/documentation/7.4/en/manual/web_interface/frontend_sections/alerts/mediatypes)

[3 Scripts](/documentation/7.4/en/manual/web_interface/frontend_sections/alerts/scripts)

[8 Users](/documentation/7.4/en/manual/web_interface/frontend_sections/users)

[1 User groups](/documentation/7.4/en/manual/web_interface/frontend_sections/users/user_groups)

[2 User roles](/documentation/7.4/en/manual/web_interface/frontend_sections/users/user_roles)

[3 Users](/documentation/7.4/en/manual/web_interface/frontend_sections/users/user_list)

[4 API tokens](/documentation/7.4/en/manual/web_interface/frontend_sections/users/api_tokens)

[5 Authentication](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication)

[1 HTTP](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication/http)

[2 LDAP](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication/ldap)

[3 SAML](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication/saml)

[4 MFA](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication/mfa)

[9 Administration](/documentation/7.4/en/manual/web_interface/frontend_sections/administration)

[1 General](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/general)

[2 Audit log](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/audit_log)

[3 Housekeeping](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/housekeeping)

[4 Proxies](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/proxies)

[5 Proxy groups](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/proxy_groups)

[6 Macros](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/macros)

[7 Queue](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/queue)

[3 User settings](/documentation/7.4/en/manual/web_interface/user_profile)

[1 Global notifications](/documentation/7.4/en/manual/web_interface/user_profile/global_notifications)

[2 Sound in browsers](/documentation/7.4/en/manual/web_interface/user_profile/sound)

[4 Global search](/documentation/7.4/en/manual/web_interface/global_search)

[5 Frontend maintenance mode](/documentation/7.4/en/manual/web_interface/maintenance_mode)

[6 Page parameters](/documentation/7.4/en/manual/web_interface/page_parameters)

[7 Definitions](/documentation/7.4/en/manual/web_interface/definitions)

[8 Creating your own theme](/documentation/7.4/en/manual/web_interface/theming)

[9 Debug mode](/documentation/7.4/en/manual/web_interface/debug_mode)

[10 Cookies used by Zabbix](/documentation/7.4/en/manual/web_interface/cookies)

[11 Time zones](/documentation/7.4/en/manual/web_interface/time_zone)

[12 Resetting password](/documentation/7.4/en/manual/web_interface/password_reset)

[13 Time period selector](/documentation/7.4/en/manual/web_interface/time_period_selector)

[19 Best practices](/documentation/7.4/en/manual/best_practices)

[1 Security best practices](/documentation/7.4/en/manual/best_practices/security)

[1 Access control](/documentation/7.4/en/manual/best_practices/security/access_control)

[1 Securing MySQL/MariaDB](/documentation/7.4/en/manual/best_practices/security/access_control/mysql)

[2 Securing PostgreSQL/TimescaleDB](/documentation/7.4/en/manual/best_practices/security/access_control/postgresql)

[2 Cryptography](/documentation/7.4/en/manual/best_practices/security/cryptography)

[3 Web server](/documentation/7.4/en/manual/best_practices/security/web_server)

[2 Configuration best practices](/documentation/7.4/en/manual/best_practices/configuration)

[20 API](/documentation/7.4/en/manual/api)

[Appendix 1. Reference commentary](/documentation/7.4/en/manual/api/reference_commentary)

[Appendix 2. Changes from 7.2 to 7.4](/documentation/7.4/en/manual/api/changes)

[Appendix 3. Changes in 7.4](/documentation/7.4/en/manual/api/changes_minor)

[Method reference](/documentation/7.4/en/manual/api/reference)

[API info](/documentation/7.4/en/manual/api/reference/apiinfo)

[apiinfo.version](/documentation/7.4/en/manual/api/reference/apiinfo/version)

[Action](/documentation/7.4/en/manual/api/reference/action)

[Action object](/documentation/7.4/en/manual/api/reference/action/object)

[action.create](/documentation/7.4/en/manual/api/reference/action/create)

[action.delete](/documentation/7.4/en/manual/api/reference/action/delete)

[action.get](/documentation/7.4/en/manual/api/reference/action/get)

[action.update](/documentation/7.4/en/manual/api/reference/action/update)

[Alert](/documentation/7.4/en/manual/api/reference/alert)

[Alert object](/documentation/7.4/en/manual/api/reference/alert/object)

[alert.get](/documentation/7.4/en/manual/api/reference/alert/get)

[Audit log](/documentation/7.4/en/manual/api/reference/auditlog)

[Audit log object](/documentation/7.4/en/manual/api/reference/auditlog/object)

[auditlog.get](/documentation/7.4/en/manual/api/reference/auditlog/get)

[Authentication](/documentation/7.4/en/manual/api/reference/authentication)

[Authentication object](/documentation/7.4/en/manual/api/reference/authentication/object)

[authentication.get](/documentation/7.4/en/manual/api/reference/authentication/get)

[authentication.update](/documentation/7.4/en/manual/api/reference/authentication/update)

[Autoregistration](/documentation/7.4/en/manual/api/reference/autoregistration)

[Autoregistration object](/documentation/7.4/en/manual/api/reference/autoregistration/object)

[autoregistration.get](/documentation/7.4/en/manual/api/reference/autoregistration/get)

[autoregistration.update](/documentation/7.4/en/manual/api/reference/autoregistration/update)

[Configuration](/documentation/7.4/en/manual/api/reference/configuration)

[configuration.export](/documentation/7.4/en/manual/api/reference/configuration/export)

[configuration.import](/documentation/7.4/en/manual/api/reference/configuration/import)

[configuration.importcompare](/documentation/7.4/en/manual/api/reference/configuration/importcompare)

[Connector](/documentation/7.4/en/manual/api/reference/connector)

[Connector object](/documentation/7.4/en/manual/api/reference/connector/object)

[connector.create](/documentation/7.4/en/manual/api/reference/connector/create)

[connector.delete](/documentation/7.4/en/manual/api/reference/connector/delete)

[connector.get](/documentation/7.4/en/manual/api/reference/connector/get)

[connector.update](/documentation/7.4/en/manual/api/reference/connector/update)

[Correlation](/documentation/7.4/en/manual/api/reference/correlation)

[Correlation object](/documentation/7.4/en/manual/api/reference/correlation/object)

[correlation.create](/documentation/7.4/en/manual/api/reference/correlation/create)

[correlation.delete](/documentation/7.4/en/manual/api/reference/correlation/delete)

[correlation.get](/documentation/7.4/en/manual/api/reference/correlation/get)

[correlation.update](/documentation/7.4/en/manual/api/reference/correlation/update)

[Dashboard](/documentation/7.4/en/manual/api/reference/dashboard)

[Dashboard object](/documentation/7.4/en/manual/api/reference/dashboard/object)

[dashboard.create](/documentation/7.4/en/manual/api/reference/dashboard/create)

[dashboard.delete](/documentation/7.4/en/manual/api/reference/dashboard/delete)

[dashboard.get](/documentation/7.4/en/manual/api/reference/dashboard/get)

[dashboard.update](/documentation/7.4/en/manual/api/reference/dashboard/update)

[Dashboard widget fields](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields)

[1 Action log](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/action_log)

[2 Clock](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/clock)

[3 Discovery status](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/discovery_status)

[4 Favorite graphs](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/favorite_graphs)

[5 Favorite maps](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/favorite_maps)

[6 Gauge](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/gauge)

[7 Geomap](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/geomap)

[8 Graph](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/graph)

[9 Graph (classic)](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/graph_classic)

[10 Graph prototype](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/graph_prototype)

[11 Honeycomb](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/honeycomb)

[12 Host availability](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/host_availability)

[13 Host card](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/host_card)

[14 Host navigator](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/host_navigator)

[15 Item card](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/item_card)

[16 Item history](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/item_history)

[17 Item navigator](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/item_navigator)

[18 Item value](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/item_value)

[19 Map](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/map)

[20 Map navigation tree](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/map_tree)

[21 Pie chart](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/pie_chart)

[22 Problem hosts](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/problem_hosts)

[23 Problems](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/problems)

[24 Problems by severity](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/problems_severity)

[25 SLA report](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/sla_report)

[26 System information](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/system)

[27 Top hosts](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/top_hosts)

[28 Top items](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/top_items)

[29 Top triggers](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/top_triggers)

[30 Trigger overview](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/trigger_overview)

[31 URL](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/url)

[32 Web monitoring](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/web_monitoring)

[Discovered host](/documentation/7.4/en/manual/api/reference/dhost)

[Discovered host object](/documentation/7.4/en/manual/api/reference/dhost/object)

[dhost.get](/documentation/7.4/en/manual/api/reference/dhost/get)

[Discovered service](/documentation/7.4/en/manual/api/reference/dservice)

[Discovered service object](/documentation/7.4/en/manual/api/reference/dservice/object)

[dservice.get](/documentation/7.4/en/manual/api/reference/dservice/get)

[Discovery check](/documentation/7.4/en/manual/api/reference/dcheck)

[Discovery check object](/documentation/7.4/en/manual/api/reference/dcheck/object)

[dcheck.get](/documentation/7.4/en/manual/api/reference/dcheck/get)

[Discovery rule](/documentation/7.4/en/manual/api/reference/drule)

[Discovery rule object](/documentation/7.4/en/manual/api/reference/drule/object)

[drule.create](/documentation/7.4/en/manual/api/reference/drule/create)

[drule.delete](/documentation/7.4/en/manual/api/reference/drule/delete)

[drule.get](/documentation/7.4/en/manual/api/reference/drule/get)

[drule.update](/documentation/7.4/en/manual/api/reference/drule/update)

[Event](/documentation/7.4/en/manual/api/reference/event)

[Event object](/documentation/7.4/en/manual/api/reference/event/object)

[event.acknowledge](/documentation/7.4/en/manual/api/reference/event/acknowledge)

[event.get](/documentation/7.4/en/manual/api/reference/event/get)

[Graph](/documentation/7.4/en/manual/api/reference/graph)

[Graph object](/documentation/7.4/en/manual/api/reference/graph/object)

[graph.create](/documentation/7.4/en/manual/api/reference/graph/create)

[graph.delete](/documentation/7.4/en/manual/api/reference/graph/delete)

[graph.get](/documentation/7.4/en/manual/api/reference/graph/get)

[graph.update](/documentation/7.4/en/manual/api/reference/graph/update)

[Graph item](/documentation/7.4/en/manual/api/reference/graphitem)

[Graph item object](/documentation/7.4/en/manual/api/reference/graphitem/object)

[graphitem.get](/documentation/7.4/en/manual/api/reference/graphitem/get)

[Graph prototype](/documentation/7.4/en/manual/api/reference/graphprototype)

[Graph prototype object](/documentation/7.4/en/manual/api/reference/graphprototype/object)

[graphprototype.create](/documentation/7.4/en/manual/api/reference/graphprototype/create)

[graphprototype.delete](/documentation/7.4/en/manual/api/reference/graphprototype/delete)

[graphprototype.get](/documentation/7.4/en/manual/api/reference/graphprototype/get)

[graphprototype.update](/documentation/7.4/en/manual/api/reference/graphprototype/update)

[High availability node](/documentation/7.4/en/manual/api/reference/hanode)

[High availability node object](/documentation/7.4/en/manual/api/reference/hanode/object)

[hanode.get](/documentation/7.4/en/manual/api/reference/hanode/get)

[History](/documentation/7.4/en/manual/api/reference/history)

[History object](/documentation/7.4/en/manual/api/reference/history/object)

[history.clear](/documentation/7.4/en/manual/api/reference/history/clear)

[history.get](/documentation/7.4/en/manual/api/reference/history/get)

[history.push](/documentation/7.4/en/manual/api/reference/history/push)

[Host](/documentation/7.4/en/manual/api/reference/host)

[Host object](/documentation/7.4/en/manual/api/reference/host/object)

[host.create](/documentation/7.4/en/manual/api/reference/host/create)

[host.delete](/documentation/7.4/en/manual/api/reference/host/delete)

[host.get](/documentation/7.4/en/manual/api/reference/host/get)

[host.massadd](/documentation/7.4/en/manual/api/reference/host/massadd)

[host.massremove](/documentation/7.4/en/manual/api/reference/host/massremove)

[host.massupdate](/documentation/7.4/en/manual/api/reference/host/massupdate)

[host.update](/documentation/7.4/en/manual/api/reference/host/update)

[Host group](/documentation/7.4/en/manual/api/reference/hostgroup)

[Host group object](/documentation/7.4/en/manual/api/reference/hostgroup/object)

[hostgroup.create](/documentation/7.4/en/manual/api/reference/hostgroup/create)

[hostgroup.delete](/documentation/7.4/en/manual/api/reference/hostgroup/delete)

[hostgroup.get](/documentation/7.4/en/manual/api/reference/hostgroup/get)

[hostgroup.massadd](/documentation/7.4/en/manual/api/reference/hostgroup/massadd)

[hostgroup.massremove](/documentation/7.4/en/manual/api/reference/hostgroup/massremove)

[hostgroup.massupdate](/documentation/7.4/en/manual/api/reference/hostgroup/massupdate)

[hostgroup.propagate](/documentation/7.4/en/manual/api/reference/hostgroup/propagate)

[hostgroup.update](/documentation/7.4/en/manual/api/reference/hostgroup/update)

[Host interface](/documentation/7.4/en/manual/api/reference/hostinterface)


...41559 bytes truncated...

The tool call succeeded but the output was truncated. Full output saved to: C:\Users\f.manghi\.local\share\opencode\tool-output\tool_1639c1668001lKRTGWU7qphIVA
Use the Task tool to have explore agent process this file with Grep and Read (with offset/limit). Do NOT read the full file yourself - delegate to save context.
```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 5.8s)

_Thinking:_

The webfetch was truncated. I need to read the saved output file to see the actual host.create parameter list, focusing on the inventory-related parameters. Let me also read the project's zabbix_api.py file to see what inventory parameters it sends.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\f.manghi\\Desktop\\Tools\\GITHUB\\OT_Line_Zabbix\\zabbix_api.py"
}
```

**Output:**
```
<path>C:\Users\f.manghi\Desktop\Tools\GITHUB\OT_Line_Zabbix\zabbix_api.py</path>
<type>file</type>
<content>
1: #!/usr/bin/env python3
2: """Client Zabbix 7.0 JSON-RPC (API token, header Bearer).
3: Crea/aggiorna/disabilita host un-device-per-host con template per tipo.
4: """
5: 
6: import logging
7: 
8: import requests
9: 
10: log = logging.getLogger("ot.zabbix_api")
11: 
12: HOST_IFACE_TYPE_AGENT = 1
13: 
14: 
15: def technical_name(cfg, ip):
16:     prefix = cfg["zabbix"].get("host_prefix", "ot-")
17:     return prefix + str(ip).replace(".", "-")
18: 
19: 
20: class ZabbixApi:
21:     def __init__(self, api_url, api_token, dry_run=False):
22:         self.url = api_url
23:         self.token = api_token
24:         self.dry_run = dry_run
25:         self._id = 0
26:         self._template_cache = {}
27: 
28:     def call(self, method, params):
29:         if self.dry_run:
30:             log.info("[dry-run] API %s %s", method, params)
31:             return None
32: 
33:         self._id += 1
34:         payload = {"jsonrpc": "2.0", "method": method, "params": params,
35:                    "id": self._id, "auth": self.token}
36:         headers = {"Content-Type": "application/json-rpc",
37:                    "Authorization": f"Bearer {self.token}"}
38:         resp = requests.post(self.url, json=payload, headers=headers, timeout=30)
39:         resp.raise_for_status()
40:         body = resp.json()
41:         if "error" in body:
42:             raise RuntimeError(f"Zabbix API error [{method}]: {body['error']}")
43:         return body.get("result")
44: 
45:     def ensure_group(self, name):
46:         groups = self.call("hostgroup.get", {"output": ["groupid", "name"],
47:                                              "filter": {"name": [name]}})
48:         if self.dry_run:
49:             return "0"
50:         if groups:
51:             return groups[0]["groupid"]
52:         created = self.call("hostgroup.create", {"name": name})
53:         log.info("Creato host group '%s' (groupid=%s)", name, created["groupids"][0])
54:         return created["groupids"][0]
55: 
56:     def get_template_id(self, name):
57:         if name in self._template_cache:
58:             return self._template_cache[name]
59:         result = self.call("template.get", {"output": ["templateid"],
60:                                             "filter": {"host": [name]}})
61:         if self.dry_run:
62:             return "0"
63:         if not result:
64:             raise RuntimeError(f"Template Zabbix non trovato: '{name}' (importalo da templates/*.yaml)")
65:         self._template_cache[name] = result[0]["templateid"]
66:         return self._template_cache[name]
67: 
68:     def get_line_hosts(self, line_name):
69:         """Host tecnici della linea, mappati per nome tecnico."""
70:         if self.dry_run:
71:             return {}
72:         hosts = self.call("host.get", {
73:             "output": ["hostid", "host", "name", "status"],
74:             "selectParentTemplates": ["templateid", "name"],
75:             "selectTags": ["tag", "value"],
76:             "selectInventory": "extend",
77:             "tag": {"tag": "line", "value": line_name},
78:         }) or []
79:         return {h["host"]: h for h in hosts}
80: 
81:     @staticmethod
82:     def _desired_tags(dev, line_name):
83:         tags = [
84:             {"tag": "line", "value": line_name},
85:             {"tag": "type", "value": dev["type"]},
86:         ]
87:         for tag, value in (("vendor", dev.get("vendor")),
88:                            ("protocol", dev.get("protocol")),
89:                            ("mac", dev.get("mac"))):
90:             if value:
91:                 tags.append({"tag": tag, "value": str(value)})
92:         return tags
93: 
94:     @staticmethod
95:     def _desired_inventory(dev):
96:         inv = {"type": dev["type"]}
97:         if dev.get("name"):
98:             inv["name"] = dev["name"]
99:         if dev.get("serial"):
100:             inv["serial"] = dev["serial"]
101:         if dev.get("mac"):
102:             inv["macaddress"] = dev["mac"]
103:         if dev.get("product_type"):
104:             inv["device"] = dev["product_type"]
105:         if dev.get("firmware"):
106:             inv["software"] = dev["firmware"]
107:         notes = []
108:         if dev.get("vendor"):
109:             notes.append(f"Vendor: {dev['vendor']}")
110:         if dev.get("system_name"):
111:             notes.append(f"System name: {dev['system_name']}")
112:         if notes:
113:             inv["notes"] = "; ".join(notes)
114:         return inv
115: 
116:     @staticmethod
117:     def _tags_equal(existing, desired):
118:         ex = {(t["tag"], t["value"]) for t in existing or []}
119:         de = {(t["tag"], t["value"]) for t in desired}
120:         return ex == de
121: 
122:     @staticmethod
123:     def _inventory_equal(existing, desired):
124:         existing = existing or {}
125:         return all(str(existing.get(k, "")) == str(v) for k, v in desired.items())
126: 
127:     def sync(self, devices, cfg, unseen_counts):
128:         """Sincronizza gli host Zabbix con i device scoperti.
129:         unseen_counts: dict nome_tecnico -> cicli discovery senza risposta (aggiornato in-place).
130:         Ritorna l'insieme dei nomi tecnici a cui inviare i valori trapper (host abilitati)."""
131:         line = cfg["line"]
132:         zbx = cfg["zabbix"]
133:         line_name = line["name"]
134:         disable_after = int(cfg["intervals"].get("disable_after", 3))
135: 
136:         groupid = self.ensure_group(line["host_group"])
137:         existing = self.get_line_hosts(line_name)
138: 
139:         # template id per tipo (lazy, solo i tipi presenti)
140:         template_ids = {}
141:         for dev in devices:
142:             tname = dev["type"]
143:             if tname not in template_ids:
144:                 template_ids[tname] = self.get_template_id(cfg["templates"][tname])
145: 
146:         sendable = set()
147:         seen_names = set()
148: 
149:         for dev in devices:
150:             ip = dev.get("ip")
151:             if not ip:
152:                 log.warning("Device senza IP ignorato: %s", dev)
153:                 continue
154: 
155:             host = technical_name(cfg, ip)
156:             seen_names.add(host)
157:             unseen_counts[host] = 0
158: 
159:             visible = dev.get("name") or host
160:             tags = self._desired_tags(dev, line_name)
161:             inventory = self._desired_inventory(dev)
162:             template = [{"templateid": template_ids[dev["type"]]}]
163: 
164:             current = existing.get(host)
165: 
166:             if current is None:
167:                 result = self.call("host.create", {
168:                     "host": host,
169:                     "name": visible,
170:                     "groups": [{"groupid": groupid}],
171:                     "interfaces": [{
172:                         "type": HOST_IFACE_TYPE_AGENT, "main": 1, "useip": 1,
173:                         "ip": ip, "dns": "", "port": "10051",
174:                     }],
175:                     "templates": template,
176:                     "tags": tags,
177:                     "inventory_mode": 0,
178:                     "inventory": inventory,
179:                 })
180:                 if not self.dry_run:
181:                     log.info("Creato host %s (tipo=%s, ip=%s) hostid=%s",
182:                              host, dev["type"], ip, result["hostids"][0])
183:                 sendable.add(host)
184:                 continue
185: 
186:             sendable.add(host)
187: 
188:             update = {"hostid": current["hostid"]}
189:             fields = []
190: 
191:             if current.get("status") == "1":
192:                 update["status"] = 0
193:                 fields.append("riabilitato")
194: 
195:             current_templates = {t["name"] for t in current.get("parentTemplates", [])}
196:             desired_tname = cfg["templates"][dev["type"]]
197:             if current_templates != {desired_tname}:
198:                 update["templates"] = template
199:                 fields.append(f"template->{desired_tname}")
200: 
201:             if not self._tags_equal(current.get("tags"), tags):
202:                 update["tags"] = tags
203:                 fields.append("tags")
204: 
205:             if not self._inventory_equal(current.get("inventory"), inventory):
206:                 update["inventory"] = inventory
207:                 update["inventory_mode"] = 0
208:                 fields.append("inventory")
209: 
210:             if len(update) > 1:
211:                 self.call("host.update", update)
212:                 if not self.dry_run:
213:                     log.info("Aggiornato host %s: %s", host, ", ".join(fields))
214: 
215:         # dispositivi spariti
216:         for host, count in unseen_counts.items():
217:             if host in seen_names:
218:                 continue
219:             unseen_counts[host] = count + 1
220:             current = existing.get(host)
221:             if not current or current.get("status") == "1":
222:                 continue
223:             if unseen_counts[host] >= disable_after:
224:                 self.call("host.update", {"hostid": current["hostid"], "status": 1})
225:                 if not self.dry_run:
226:                     log.warning("Disabilitato host %s (non visto da %d cicli)",
227:                                 host, unseen_counts[host])
228:                 sendable.discard(host)
229:             else:
230:                 sendable.add(host)  # ancora attivo, continua a ricevere stato
231: 
232:         # non mandare valori a host disabilitati
233:         for host in list(sendable):
234:             current = existing.get(host)
235:             if current and current.get("status") == "1" and unseen_counts.get(host, 0) >= disable_after:
236:                 sendable.discard(host)
237: 
238:         return sendable

(End of file - total 238 lines)
</content>
```

**Tool: bash**

**Input:**
```json
{
  "command": "rg -n \"inventory\" \"C:\\Users\\f.manghi\\.local\\share\\opencode\\tool-output\\tool_1639c1668001lKRTGWU7qphIVA\" | Select-Object -First 50"
}
```

**Output:**
```
[31;1mrg: [31;1mIl termine 'rg' non � riconosciuto come nome di un cmdlet, di una funzione, di un file di script o di un programma eseguibile.[0m
[31;1m[31;1mVerificare l'ortografia del nome, che il percorso sia incluso e corretto, quindi riprovare.[0m

```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 15.2s)

_Thinking:_

I need to check the inventory fields used in the code against the Zabbix 7.4 host.create documentation. The code uses these inventory fields:
- type
- name
- serial
- macaddress
- device
- software
- notes

Now let me check what the actual Zabbix inventory fields are. From my knowledge of Zabbix inventory mode fields (standard inventory fields):
- type (Device type)
- name (Device name)
- alias (Alias)
- os (OS)
- serial (Serial number A)
- serialno_a (Serial number A)
- serialno_b (Serial number B)
- macaddress (MAC address A)
- macaddress_a (MAC address A)
- macaddress_b (MAC address B)
- hwaddr (MAC address B? no...)

Actually, let me recall the official Zabbix host inventory fields. In host object, inventory fields are:

type, name, alias, os, serialno_a, serialno_b, macaddress_a, macaddress_b, hwaddr, location, location_lat, location_lon, notes, chassis, model, tag, agent_dns, agent_site, agent_ipmi, agent_devices, agent_version, vendor, application, url, generator, deployment_status, hw_arch, hw_model, hw_name, sw_os, sw_app_1..4, sw_group, sw_owner, sw_sw, sw_vendor, maintenance, maintenance_since, maintenance_expires, url_a..d, deployed_by, site_name, site_notes, outline, pdc_id, oob_ip, ...

Actually, I should check the fetched page. The webfetch output was truncated - the important parameter list was in the truncated part. Let me search the saved output file for the inventory section.

**Tool: bash**

**Input:**
```json
{
  "command": "Get-Content \"C:\\Users\\f.manghi\\.local\\share\\opencode\\tool-output\\tool_1639c1668001lKRTGWU7qphIVA\" | Select-String -Pattern \"inventory\" -Context 2,15 | Select-Object -First 10"
}
```

**Output:**
```

  [3 Configuring a host group](/documentation/7.4/en/manual/config/hosts/host_groups)
  
> [4 [7mInventory[0m](/documentation/7.4/en/manual/config/hosts/inventory)[0m
[7m[0m  [0m
[7m[0m  [5 Mass update](/documentation/7.4/en/manual/config/hosts/hostupdate)[0m
[7m[0m  [0m
[7m[0m  [2 Items](/documentation/7.4/en/manual/config/items)[0m
[7m[0m  [0m
[7m[0m  [1 Creating an item](/documentation/7.4/en/manual/config/items/item)[0m
[7m[0m  [0m
[7m[0m  [1 Item key format](/documentation/7.4/en/manual/config/items/item/key)[0m
[7m[0m  [0m
[7m[0m  [2 Custom intervals](/documentation/7.4/en/manual/config/items/item/custom_intervals)[0m
[7m[0m  [0m
[7m[0m  [2 Item value preprocessing](/documentation/7.4/en/manual/config/items/preprocessing)[0m
[7m[0m  [0m
[7m[0m  [1 Preprocessing testing](/documentation/7.4/en/manual/config/items/preprocessing/testing)[0m
[7m[0m  [0m
  [3 SLA report](/documentation/7.4/en/manual/web_interface/frontend_sections/services/sla_report)
  
> [4 [7mInventory[0m](/documentation/7.4/en/manual/web_interface/frontend_sections/inventory)[0m
[7m[0m  [0m
> [1 Overview](/documentation/7.4/en/manual/web_interface/frontend_sections/[7minventory[0m/overview)[0m
[7m[0m  [0m
> [2 Hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/[7minventory[0m/hosts)[0m
[7m[0m  [0m
[7m[0m  [5 Reports](/documentation/7.4/en/manual/web_interface/frontend_sections/reports)[0m
[7m[0m  [0m
[7m[0m  [1 System information](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/status_of_zabbix)[0m
[7m[0m  [0m
[7m[0m  [2 Scheduled reports](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/scheduled)[0m
[7m[0m  [0m
[7m[0m  [3 Availability report](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/availability)[0m
[7m[0m  [0m
[7m[0m  [4 Top 100 triggers](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/triggers_top)[0m
[7m[0m  [0m
[7m[0m  [5 Audit log](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/audit_log)[0m
[7m[0m  [0m
[7m[0m  [6 Action log](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/action_log)[0m
[7m[0m  [0m
  [User macros](/documentation/7.4/en/manual/api/reference/usermacro/object) to be created for the host.
  
> [7minventory[0m
[7m[0m  [0m
[7m[0m  object[0m
[7m[0m  [0m
> [Host [7minventory[0m](/documentation/7.4/en/manual/api/reference/host/object#host-inventory) properties.[0m
[7m[0m  [0m
[7m[0m  ### Return values[0m
[7m[0m  [0m
[7m [0m[7m [0m[7m[0m`(object)` [0m[7m[0mReturns [0m[7m[0man [0m[7m[0mobject [0m[7m[0mcontaining [0m[7m[0mthe [0m[7m[0mIDs [0m[7m[0mof [0m[7m[0mthe [0m[7m[0mcreated [0m[7m[0mhosts [0m[7m[0munder [0m[7m[0mthe [0m[7m[0m`hostids` [0m[7m[0mproperty. [0m[7m[0mThe [0m[7m[0morder [0m[7m[0mof [0m[7m[0mthe [0m
[7m[0mreturned [0m[7m[0mIDs [0m[7m[0mmatches [0m[7m[0mthe [0m[7m[0morder [0m[7m[0mof [0m[7m[0mthe [0m[7m[0mpassed [0m[7m[0mhosts.[0m
[7m[0m  [0m
[7m[0m  ### Examples[0m
[7m[0m  [0m
[7m[0m  #### Creating a host[0m
[7m[0m  [0m
> Create a host called "Linux server" with an IP interface and tags, add it to a group, link a template to it and set 
the MAC addresses in the host [7minventory[0m.[0m
[7m[0m  [0m
[7m[0m  [Request](/documentation/7.4/en/manual/api#performing-requests):[0m
[7m[0m  [0m
[7m[0m  ```[0m
[7m[0m  {[0m
[7m[0m      "jsonrpc": "2.0",[0m
[7m[0m      "method": "host.create",[0m
[7m[0m      "params": {[0m
[7m[0m          "host": "Linux server",[0m
[7m[0m          "interfaces": [[0m
[7m[0m              {[0m
[7m[0m                  "type": 1,[0m
[7m[0m                  "main": 1,[0m
[7m[0m                  "useip": 1,[0m
[7m[0m                  "ip": "192.168.3.1",[0m
              }
          ],
>         "[7minventory[0m_mode": 0,[0m
>         "[7minventory[0m": {[0m
[7m[0m              "macaddress_a": "01234",[0m
[7m[0m              "macaddress_b": "56768"[0m
[7m[0m          }[0m
[7m[0m      },[0m
[7m[0m      "id": 1[0m
[7m[0m  }[0m
[7m[0m  ```[0m
[7m[0m  [0m
[7m[0m  Response:[0m
[7m[0m  [0m
[7m[0m  ```[0m
[7m[0m  {[0m
[7m[0m      "jsonrpc": "2.0",[0m
[7m[0m      "result": {[0m
[7m[0m          "hostids": [[0m
  -   [User macro](/documentation/7.4/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)
  -   [Host interface](/documentation/7.4/en/manual/api/reference/hostinterface/object#host-interface)
> -   [Host [7minventory[0m](object#host-inventory)[0m
[7m[0m  -   [Host tag](object#host-tag)[0m
[7m[0m  -   [Proxy](/documentation/7.4/en/manual/api/reference/proxy/object#proxy)[0m
[7m[0m  -   [Proxy group](/documentation/7.4/en/manual/api/reference/proxygroup/object#proxy-group)[0m
[7m[0m  [0m
[7m[0m  ### Source[0m
[7m[0m  [0m
[7m[0m  CHost::create() in *ui/include/classes/api/services/CHost.php*.[0m
[7m[0m  [0m
[7m[0m  ### What's next?[0m
[7m[0m  [0m
[7m[0m  [host.delete](/documentation/7.4/en/manual/api/reference/host/delete)[0m
[7m[0m  [0m
[7m[0m  ### Did you find what you needed?[0m
[7m[0m  [0m
[7m[0m  -   0[0m


```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 13.1s)

_Thinking:_

The host.create docs reference "Host inventory" properties in the Host object page. I need to fetch that page to see the exact valid inventory field names. The valid fields in Zabbix host inventory are like:

- type
- name
- alias
- os
- serialno_a
- serialno_b
- macaddress_a
- macaddress_b
- hwaddr
- location
- location_lat
- location_lon
- notes
- chassis
- model
- tag
- agent_dns
- agent_site
- agent_ipmi
- agent_devices
- agent_version
- vendor
- application
- url
- generator
- deployment_status
- hw_arch
- hw_model
- hw_name
- sw_os
- sw_app_1 through sw_app_4
- sw_group
- sw_owner
- sw_sw
- sw_vendor
- maintenance
- maintenance_since
- maintenance_expires
- url_a through url_d
- oob_ip
- oob_netmask
- oob_router
- address
- ping
- site_name
- site_notes
- type_fqdn
- pdc_id
- inventory_mode (not in inventory object)

The code in `_desired_inventory` uses:
- `type` — valid (Device type)
- `name` — valid (Device name)
- `serial` — INVALID. Should be `serialno_a` (Serial number A). Actually wait — let me double check. In Zabbix, the inventory field is `serialno_a` and `serialno_b`. There's no `serial`. Correct.
- `macaddress` — INVALID. Should be `macaddress_a` or `macaddress_b`. The docs example uses `macaddress_a`/`macaddress_b`. Correct.
- `device` — INVALID? Is there a `device` inventory field? I don't recall `device`. Hmm... Let me check the host object page. Fields like `hw_model`, `model`... Actually I don't think `device` is valid. Let me verify with the Host object docs.
- `software` — INVALID? There's `sw_sw` (Software applications), `sw_os`, `sw_vendor`, `sw_group`, `sw_owner`, `sw_app_1`..`sw_app_4`. There's no `software`. Let me verify.
- `notes` — valid (Notes)

Also for the update path: `host.update` also accepts inventory.

I should fetch the Host object page to confirm exact field names: https://www.zabbix.com/documentation/7.4/en/manual/api/reference/host/object#host-inventory

Let me fetch that page.

**Tool: webfetch**

**Input:**
```json
{
  "format": "markdown",
  "url": "https://www.zabbix.com/documentation/7.4/en/manual/api/reference/host/object"
}
```

**Output:**
```
            Host object                                    

[![logo](/documentation/7.4/images/logo.svg)

# Docs

](https://www.zabbix.com "Zabbix")

Version: 7.4 (current)

-   Supported
-   [7.4 (current)](/documentation/7.4/../current/en/manual/api/reference/host/object)
-   [7.0](/documentation/7.4/../7.0/en/manual/api/reference/host/object)
-   [6.0](/documentation/7.4/../6.0/en/manual/api/reference/host/object)
-   In development
-   [8.0 (devel)](/documentation/7.4/../devel/en/manual/api/reference/host/object)
-   Unsupported
-   [7.2](/documentation/7.4/../7.2/en/manual/api/reference/host/object)
-   [6.4](/documentation/7.4/../6.4/en/manual/api/reference/host/object)
-   [6.2](/documentation/7.4/../6.2/en/manual/api/reference/host/object)
-   [5.4](/documentation/7.4/../5.4/en/manual/api/reference/host/object)
-   [5.2](/documentation/7.4/../5.2/en/manual/api/reference/host/object)
-   [5.0](/documentation/7.4/../5.0/en/manual/api/reference/host/object)
-   [4.4](/documentation/7.4/../4.4/en/manual/api/reference/host/object)
-   [4.2](/documentation/7.4/../4.2/en/manual/api/reference/host/object)
-   [4.0](/documentation/7.4/../4.0/en/manual/api/reference/host/object)
-   [3.4](/documentation/7.4/../3.4/en/manual/api/reference/host/object)
-   [3.2](/documentation/7.4/../3.2/en/manual/api/reference/host/object)
-   [3.0](/documentation/7.4/../3.0/en/manual/api/reference/host/object)
-   [2.4](/documentation/7.4/../2.4/en/manual/api/reference/host/object)
-   [2.2](/documentation/7.4/../2.2/en/manual/api/reference/host/object)
-   [2.0](/documentation/7.4/../2.0/en/manual/api/reference/host/object)
-   [1.8](/documentation/7.4/../1.8/en/manual/api/reference/host/object)
-   General
-   [info](/documentation/7.4/../info/en)
-   [guidelines](/documentation/7.4/../guidelines/en)

Language: English

-   [English](/documentation/7.4/en/manual/api/reference/host/object)
-   [日本語](/documentation/7.4/jp/manual/api/reference/host/object)
-   [Português](/documentation/7.4/pt/manual/api/reference/host/object)
-   [Español](/documentation/7.4/es/manual/api/reference/host/object)
-   [Français](/documentation/7.4/fr/manual/api/reference/host/object)
-   [Latviešu](/documentation/7.4/lv/manual/api/reference/host/object)
-   [中文](/documentation/7.4/zh/manual/api/reference/host/object)
-   [Polski](/documentation/7.4/pl/manual/api/reference/host/object)
-   [Italiano](/documentation/7.4/it/manual/api/reference/host/object)
-   [Deutsch](/documentation/7.4/de/manual/api/reference/host/object)
-   [Русский](/documentation/7.4/ru/manual/api/reference/host/object)
-   [Català](/documentation/7.4/ca/manual/api/reference/host/object)
-   [Srpski](/documentation/7.4/sr/manual/api/reference/host/object)

[Download Zabbix Manual in PDF](/documentation/7.4/downloads/Zabbix_Documentation_7.4.en.pdf)

Theme:

-   [Light](#)
-   [Dark](#)
-   [System](#)

[User manual](/documentation/7.4/en/manual)

[1 Introduction](/documentation/7.4/en/manual/introduction)

[1 Manual structure](/documentation/7.4/en/manual/introduction/manual_structure)

[2 What is Zabbix](/documentation/7.4/en/manual/introduction/about)

[3 Zabbix features](/documentation/7.4/en/manual/introduction/features)

[4 Zabbix overview](/documentation/7.4/en/manual/introduction/overview)

[5 What's new in Zabbix 7.4.0](/documentation/7.4/en/manual/introduction/whatsnew)

[6 What's new in Zabbix 7.4.x](/documentation/7.4/en/manual/introduction/whatsnew_minor)

[2 Definitions](/documentation/7.4/en/manual/definitions)

[3 Zabbix processes](/documentation/7.4/en/manual/concepts)

[1 Server](/documentation/7.4/en/manual/concepts/server)

[1 High availability](/documentation/7.4/en/manual/concepts/server/ha)

[2 Agent](/documentation/7.4/en/manual/concepts/agent)

[3 Agent 2](/documentation/7.4/en/manual/concepts/agent2)

[4 Proxy](/documentation/7.4/en/manual/concepts/proxy)

[5 Java gateway](/documentation/7.4/en/manual/concepts/java)

[1 Setup from RHEL packages](/documentation/7.4/en/manual/concepts/java/from_rhel)

[2 Setup from Debian/Ubuntu packages](/documentation/7.4/en/manual/concepts/java/from_debian_ubuntu)

[3 Setup from sources](/documentation/7.4/en/manual/concepts/java/from_sources)

[6 Sender](/documentation/7.4/en/manual/concepts/sender)

[7 Get](/documentation/7.4/en/manual/concepts/get)

[8 JS](/documentation/7.4/en/manual/concepts/js)

[9 Web service](/documentation/7.4/en/manual/concepts/web_service)

[4 Installation and first steps](/documentation/7.4/en/manual/installation)

[1 Getting Zabbix](/documentation/7.4/en/manual/installation/getting_zabbix)

[2 Requirements](/documentation/7.4/en/manual/installation/requirements)

[3 Installation from sources](/documentation/7.4/en/manual/installation/install)

[1 Building Zabbix agent on Windows](/documentation/7.4/en/manual/installation/install/win_agent)

[2 Building Zabbix agent 2 on Windows](/documentation/7.4/en/manual/installation/install/building_zabbix_agent_2_on_windows)

[3 Building Zabbix agent on macOS](/documentation/7.4/en/manual/installation/install/mac_agent)

[4 Installation from packages](/documentation/7.4/en/manual/installation/install_from_packages)

[1 Windows agent installation from MSI](/documentation/7.4/en/manual/installation/install_from_packages/win_msi)

[2 macOS agent installation from PKG](/documentation/7.4/en/manual/installation/install_from_packages/mac_pkg)

[3 Unstable releases](/documentation/7.4/en/manual/installation/install_from_packages/unstable)

[5 Installation from containers](/documentation/7.4/en/manual/installation/containers)

[6 Installation on public cloud platforms](/documentation/7.4/en/manual/installation/install_cloud_platforms)

[1 AWS deployment guide for Zabbix server](/documentation/7.4/en/manual/installation/install_cloud_platforms/aws_deployment_guide)

[2 AWS deployment guide for Zabbix proxy](/documentation/7.4/en/manual/installation/install_cloud_platforms/aws_deployment_guide_proxy)

[3 Azure deployment guide for Zabbix server](/documentation/7.4/en/manual/installation/install_cloud_platforms/azure_deployment_guide)

[4 Azure deployment guide for Zabbix proxy](/documentation/7.4/en/manual/installation/install_cloud_platforms/azure_deployment_guide_proxy)

[5 Google Cloud deployment guide](/documentation/7.4/en/manual/installation/install_cloud_platforms/cloud_google)

[7 Web interface installation](/documentation/7.4/en/manual/installation/frontend)

[8 Upgrade procedure](/documentation/7.4/en/manual/installation/upgrade)

[1 Upgrade from sources](/documentation/7.4/en/manual/installation/upgrade/sources)

[2 Upgrade from packages](/documentation/7.4/en/manual/installation/upgrade/packages)

[1 Red Hat Enterprise Linux](/documentation/7.4/en/manual/installation/upgrade/packages/rhel)

[2 Debian/Ubuntu](/documentation/7.4/en/manual/installation/upgrade/packages/debian_ubuntu)

[3 Upgrade from containers](/documentation/7.4/en/manual/installation/upgrade/containers)

[9 Known issues](/documentation/7.4/en/manual/installation/known_issues)

[1 Compilation issues](/documentation/7.4/en/manual/installation/known_issues/compilation_issues)

[2 Escaping-related upgrade issues](/documentation/7.4/en/manual/installation/known_issues/db_upgrade_escaping)

[10 Template changes](/documentation/7.4/en/manual/installation/template_changes)

[11 Upgrade notes for 7.4.0](/documentation/7.4/en/manual/installation/upgrade_notes)

[12 Upgrade notes for 7.4.x](/documentation/7.4/en/manual/installation/upgrade_notes_minor)

[5 Quickstart](/documentation/7.4/en/manual/quickstart)

[1 Login and configuring user](/documentation/7.4/en/manual/quickstart/login)

[2 New host](/documentation/7.4/en/manual/quickstart/host)

[3 New item](/documentation/7.4/en/manual/quickstart/item)

[4 New trigger](/documentation/7.4/en/manual/quickstart/trigger)

[5 Receiving problem notification](/documentation/7.4/en/manual/quickstart/notification)

[6 New template](/documentation/7.4/en/manual/quickstart/template)

[6 Zabbix appliance](/documentation/7.4/en/manual/appliance)

[7 Configuration](/documentation/7.4/en/manual/config)

[1 Hosts and host groups](/documentation/7.4/en/manual/config/hosts)

[1 Host Wizard](/documentation/7.4/en/manual/config/hosts/host_wizard)

[2 Configuring a host](/documentation/7.4/en/manual/config/hosts/host)

[3 Configuring a host group](/documentation/7.4/en/manual/config/hosts/host_groups)

[4 Inventory](/documentation/7.4/en/manual/config/hosts/inventory)

[5 Mass update](/documentation/7.4/en/manual/config/hosts/hostupdate)

[2 Items](/documentation/7.4/en/manual/config/items)

[1 Creating an item](/documentation/7.4/en/manual/config/items/item)

[1 Item key format](/documentation/7.4/en/manual/config/items/item/key)

[2 Custom intervals](/documentation/7.4/en/manual/config/items/item/custom_intervals)

[2 Item value preprocessing](/documentation/7.4/en/manual/config/items/preprocessing)

[1 Preprocessing testing](/documentation/7.4/en/manual/config/items/preprocessing/testing)

[2 Preprocessing details](/documentation/7.4/en/manual/config/items/preprocessing/preprocessing_details)

[3 Preprocessing examples](/documentation/7.4/en/manual/config/items/preprocessing/examples)

[4 JSONPath functionality](/documentation/7.4/en/manual/config/items/preprocessing/jsonpath_functionality)

[1 Escaping special characters from LLD macro values in JSONPath](/documentation/7.4/en/manual/config/items/preprocessing/jsonpath_functionality/escaping_lld_macros)

[5 JavaScript preprocessing](/documentation/7.4/en/manual/config/items/preprocessing/javascript)

[1 Additional JavaScript objects](/documentation/7.4/en/manual/config/items/preprocessing/javascript/javascript_objects)

[2 Browser item JavaScript objects](/documentation/7.4/en/manual/config/items/preprocessing/javascript/browser_item_javascript_objects)

[6 CSV to JSON preprocessing](/documentation/7.4/en/manual/config/items/preprocessing/csv_to_json)

[3 Item types](/documentation/7.4/en/manual/config/items/itemtypes)

[1 Zabbix agent](/documentation/7.4/en/manual/config/items/itemtypes/zabbix_agent)

[1 Zabbix agent 2](/documentation/7.4/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2)

[2 Windows Zabbix agent](/documentation/7.4/en/manual/config/items/itemtypes/zabbix_agent/win_keys)

[3 Log file monitoring](/documentation/7.4/en/manual/config/items/itemtypes/zabbix_agent/log_items)

[2 Simple check](/documentation/7.4/en/manual/config/items/itemtypes/simple_checks)

[1 VMware monitoring item keys](/documentation/7.4/en/manual/config/items/itemtypes/simple_checks/vmware_keys)

[3 SNMP agent](/documentation/7.4/en/manual/config/items/itemtypes/snmp)

[1 Dynamic indexes](/documentation/7.4/en/manual/config/items/itemtypes/snmp/dynamicindex)

[2 Special OIDs](/documentation/7.4/en/manual/config/items/itemtypes/snmp/special_mibs)

[3 MIB files](/documentation/7.4/en/manual/config/items/itemtypes/snmp/mibs)

[4 SNMP trap](/documentation/7.4/en/manual/config/items/itemtypes/snmptrap)

[5 Zabbix internal](/documentation/7.4/en/manual/config/items/itemtypes/internal)

[6 Zabbix trapper](/documentation/7.4/en/manual/config/items/itemtypes/trapper)

[7 External check](/documentation/7.4/en/manual/config/items/itemtypes/external)

[8 Database monitor](/documentation/7.4/en/manual/config/items/itemtypes/odbc_checks)

[9 HTTP agent](/documentation/7.4/en/manual/config/items/itemtypes/http)

[1 Prometheus check](/documentation/7.4/en/manual/config/items/itemtypes/http/prometheus)

[10 IPMI agent](/documentation/7.4/en/manual/config/items/itemtypes/ipmi)

[11 SSH agent](/documentation/7.4/en/manual/config/items/itemtypes/ssh_checks)

[12 Telnet agent](/documentation/7.4/en/manual/config/items/itemtypes/telnet_checks)

[13 JMX agent](/documentation/7.4/en/manual/config/items/itemtypes/jmx_monitoring)

[14 Calculated item](/documentation/7.4/en/manual/config/items/itemtypes/calculated)

[1 Aggregate calculations](/documentation/7.4/en/manual/config/items/itemtypes/calculated/aggregate)

[15 Dependent item](/documentation/7.4/en/manual/config/items/itemtypes/dependent_items)

[16 Script item](/documentation/7.4/en/manual/config/items/itemtypes/script)

[17 Browser item](/documentation/7.4/en/manual/config/items/itemtypes/browser)

[4 History and trends](/documentation/7.4/en/manual/config/items/history_and_trends)

[5 User parameters](/documentation/7.4/en/manual/config/items/userparameters)

[1 Extending Zabbix agents](/documentation/7.4/en/manual/config/items/userparameters/extending_agent)

[6 Windows performance counters](/documentation/7.4/en/manual/config/items/perfcounters)

[7 Mass update](/documentation/7.4/en/manual/config/items/itemupdate)

[8 Value mapping](/documentation/7.4/en/manual/config/items/mapping)

[9 Queue](/documentation/7.4/en/manual/config/items/queue)

[10 Value cache](/documentation/7.4/en/manual/config/items/value_cache)

[11 Execute now](/documentation/7.4/en/manual/config/items/check_now)

[12 Restricting agent checks](/documentation/7.4/en/manual/config/items/restrict_checks)

[3 Triggers](/documentation/7.4/en/manual/config/triggers)

[1 Configuring a trigger](/documentation/7.4/en/manual/config/triggers/trigger)

[2 Trigger expression](/documentation/7.4/en/manual/config/triggers/expression)

[3 Trigger dependencies](/documentation/7.4/en/manual/config/triggers/dependencies)

[4 Trigger severity](/documentation/7.4/en/manual/config/triggers/severity)

[5 Customizing trigger severities](/documentation/7.4/en/manual/config/triggers/customseverities)

[6 Mass update](/documentation/7.4/en/manual/config/triggers/update)

[7 Predictive trigger functions](/documentation/7.4/en/manual/config/triggers/prediction)

[4 Events](/documentation/7.4/en/manual/config/events)

[1 Trigger event generation](/documentation/7.4/en/manual/config/events/trigger_events)

[2 Other event sources](/documentation/7.4/en/manual/config/events/sources)

[3 Manual closing of problems](/documentation/7.4/en/manual/config/events/manual_close)

[5 Event correlation](/documentation/7.4/en/manual/config/event_correlation)

[1 Trigger-based event correlation](/documentation/7.4/en/manual/config/event_correlation/trigger)

[2 Global event correlation](/documentation/7.4/en/manual/config/event_correlation/global)

[6 Tagging](/documentation/7.4/en/manual/config/tagging)

[7 Visualization](/documentation/7.4/en/manual/config/visualization)

[1 Graphs](/documentation/7.4/en/manual/config/visualization/graphs)

[1 Simple graphs](/documentation/7.4/en/manual/config/visualization/graphs/simple)

[2 Custom graphs](/documentation/7.4/en/manual/config/visualization/graphs/custom)

[3 Ad-hoc graphs](/documentation/7.4/en/manual/config/visualization/graphs/adhoc)

[2 Network maps](/documentation/7.4/en/manual/config/visualization/maps)

[1 Configuring a network map](/documentation/7.4/en/manual/config/visualization/maps/map)

[2 Host group elements](/documentation/7.4/en/manual/config/visualization/maps/host_groups)

[3 Link indicators](/documentation/7.4/en/manual/config/visualization/maps/links)

[3 Dashboards](/documentation/7.4/en/manual/config/visualization/dashboard)

[8 Templates and template groups](/documentation/7.4/en/manual/config/templates)

[1 Configuring a template](/documentation/7.4/en/manual/config/templates/template)

[2 Configuring a template group](/documentation/7.4/en/manual/config/templates/template_groups)

[3 Linking/unlinking](/documentation/7.4/en/manual/config/templates/linking)

[4 Nesting](/documentation/7.4/en/manual/config/templates/nesting)

[5 Mass update](/documentation/7.4/en/manual/config/templates/mass)

[9 Templates out of the box](/documentation/7.4/en/manual/config/templates_out_of_the_box)

[1 Zabbix agent template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/zabbix_agent)

[2 Zabbix agent 2 template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/zabbix_agent2)

[3 HTTP template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/http)

[4 IPMI template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/ipmi)

[5 JMX template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/jmx)

[6 ODBC template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/odbc_checks)

[7 Standardized templates for network devices](/documentation/7.4/en/manual/config/templates_out_of_the_box/network_devices)

[8 VMware template operation](/documentation/7.4/en/manual/config/templates_out_of_the_box/vmware)

[10 Notifications upon events](/documentation/7.4/en/manual/config/notifications)

[1 Media types](/documentation/7.4/en/manual/config/notifications/media)

[1 Email](/documentation/7.4/en/manual/config/notifications/media/email)

[1 Automated Gmail/Office365 media types](/documentation/7.4/en/manual/config/notifications/media/email/gmail_office)

[2 SMS](/documentation/7.4/en/manual/config/notifications/media/sms)

[3 Custom alert scripts](/documentation/7.4/en/manual/config/notifications/media/script)

[4 Webhook](/documentation/7.4/en/manual/config/notifications/media/webhook)

[1 Webhook script examples](/documentation/7.4/en/manual/config/notifications/media/webhook/webhook_examples)

[2 Actions](/documentation/7.4/en/manual/config/notifications/action)

[1 Conditions](/documentation/7.4/en/manual/config/notifications/action/conditions)

[2 Operations](/documentation/7.4/en/manual/config/notifications/action/operation)

[1 Sending message](/documentation/7.4/en/manual/config/notifications/action/operation/message)

[2 Remote commands](/documentation/7.4/en/manual/config/notifications/action/operation/remote_command)

[3 Additional operations](/documentation/7.4/en/manual/config/notifications/action/operation/other)

[4 Using macros in messages](/documentation/7.4/en/manual/config/notifications/action/operation/macros)

[3 Recovery operations](/documentation/7.4/en/manual/config/notifications/action/recovery_operations)

[4 Update operations](/documentation/7.4/en/manual/config/notifications/action/update_operations)

[5 Escalations](/documentation/7.4/en/manual/config/notifications/action/escalations)

[3 Receiving notification on unsupported items](/documentation/7.4/en/manual/config/notifications/unsupported_item)

[11 Macros](/documentation/7.4/en/manual/config/macros)

[1 Macro functions](/documentation/7.4/en/manual/config/macros/macro_functions)

[2 User macros](/documentation/7.4/en/manual/config/macros/user_macros)

[3 User macros with context](/documentation/7.4/en/manual/config/macros/user_macros_context)

[4 Secret user macros](/documentation/7.4/en/manual/config/macros/secret_macros)

[5 Low-level discovery macros](/documentation/7.4/en/manual/config/macros/lld_macros)

[6 Expression macros](/documentation/7.4/en/manual/config/macros/expression_macros)

[12 Users and user groups](/documentation/7.4/en/manual/config/users_and_usergroups)

[1 Configuring a user](/documentation/7.4/en/manual/config/users_and_usergroups/user)

[2 Permissions](/documentation/7.4/en/manual/config/users_and_usergroups/permissions)

[3 User groups](/documentation/7.4/en/manual/config/users_and_usergroups/usergroup)

[13 Storage of secrets](/documentation/7.4/en/manual/config/secrets)

[1 CyberArk configuration](/documentation/7.4/en/manual/config/secrets/cyberark)

[2 HashiCorp configuration](/documentation/7.4/en/manual/config/secrets/hashicorp)

[14 Scheduled reports](/documentation/7.4/en/manual/config/reports)

[15 Data export](/documentation/7.4/en/manual/config/export)

[1 Export to files](/documentation/7.4/en/manual/config/export/files)

[2 Streaming to external systems](/documentation/7.4/en/manual/config/export/streaming)

[3 SNMP gateway](/documentation/7.4/en/manual/config/export/snmp_gateway)

[8 Service monitoring](/documentation/7.4/en/manual/it_services)

[1 Service tree](/documentation/7.4/en/manual/it_services/service_tree)

[2 SLA](/documentation/7.4/en/manual/it_services/sla)

[3 Setup example](/documentation/7.4/en/manual/it_services/example)

[9 Web monitoring](/documentation/7.4/en/manual/web_monitoring)

[1 Web monitoring items](/documentation/7.4/en/manual/web_monitoring/items)

[2 Real-life scenario](/documentation/7.4/en/manual/web_monitoring/example)

[10 Virtual machine monitoring](/documentation/7.4/en/manual/vm_monitoring)

[1 VMware monitoring item keys](/documentation/7.4/en/manual/vm_monitoring/vmware_keys)

[2 Virtual machine discovery key fields](/documentation/7.4/en/manual/vm_monitoring/discovery_fields)

[3 JSON examples for VMware items](/documentation/7.4/en/manual/vm_monitoring/vmware_json)

[4 VMware monitoring setup example](/documentation/7.4/en/manual/vm_monitoring/example)

[11 Maintenance](/documentation/7.4/en/manual/maintenance)

[12 Regular expressions](/documentation/7.4/en/manual/regular_expressions)

[13 Problem acknowledgment](/documentation/7.4/en/manual/acknowledgment)

[1 Problem suppression](/documentation/7.4/en/manual/acknowledgment/suppression)

[14 Configuration export/import](/documentation/7.4/en/manual/xml_export_import)

[1 Template groups](/documentation/7.4/en/manual/xml_export_import/templategroups)

[2 Host groups](/documentation/7.4/en/manual/xml_export_import/hostgroups)

[3 Templates](/documentation/7.4/en/manual/xml_export_import/templates)

[4 Hosts](/documentation/7.4/en/manual/xml_export_import/hosts)

[5 Network maps](/documentation/7.4/en/manual/xml_export_import/maps)

[6 Media types](/documentation/7.4/en/manual/xml_export_import/media)

[15 Discovery](/documentation/7.4/en/manual/discovery)

[1 Network discovery](/documentation/7.4/en/manual/discovery/network_discovery)

[1 Configuring a network discovery rule](/documentation/7.4/en/manual/discovery/network_discovery/rule)

[2 Active agent autoregistration](/documentation/7.4/en/manual/discovery/auto_registration)

[3 Low-level discovery](/documentation/7.4/en/manual/discovery/low_level_discovery)

[1 Item prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/item_prototypes)

[2 Trigger prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/trigger_prototypes)

[3 Graph prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/graph_prototypes)

[4 Host prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/host_prototypes)

[5 Discovery prototypes](/documentation/7.4/en/manual/discovery/low_level_discovery/discovery_prototypes)

[6 Notes on low-level discovery](/documentation/7.4/en/manual/discovery/low_level_discovery/notes)

[7 Discovery rules](/documentation/7.4/en/manual/discovery/low_level_discovery/examples)

[1 Discovery of mounted filesystems](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/mounted_filesystems)

[2 Discovery of network interfaces](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/network_interfaces)

[3 Discovery of CPUs and CPU cores](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/cpu)

[4 Discovery of SNMP OIDs](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/snmp_oids_walk)

[5 Discovery of SNMP OIDs (legacy)](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/snmp_oids)

[6 Discovery of JMX objects](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/jmx)

[7 Discovery of IPMI sensors](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/ipmi_sensors)

[8 Discovery of systemd services](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/systemd)

[9 Discovery of Windows services](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/windows_services)

[10 Discovery of Windows performance counter instances](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/windows_perf_instances)

[11 Discovery using WMI queries](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/wmi)

[12 Discovery using ODBC SQL queries](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/sql_queries)

[13 Discovery using Prometheus data](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/prometheus)

[14 Discovery of block devices](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/devices)

[15 Discovery of host interfaces in Zabbix](/documentation/7.4/en/manual/discovery/low_level_discovery/examples/host_interfaces)

[8 Custom LLD rules](/documentation/7.4/en/manual/discovery/low_level_discovery/custom_rules)

[16 Distributed monitoring](/documentation/7.4/en/manual/distributed_monitoring)

[1 Proxies](/documentation/7.4/en/manual/distributed_monitoring/proxies)

[1 Synchronization of monitoring configuration](/documentation/7.4/en/manual/distributed_monitoring/proxies/sync)

[2 Proxy load balancing and high availability](/documentation/7.4/en/manual/distributed_monitoring/proxies/ha)

[17 Encryption](/documentation/7.4/en/manual/encryption)

[1 Using certificates](/documentation/7.4/en/manual/encryption/using_certificates)

[2 Using pre-shared keys](/documentation/7.4/en/manual/encryption/using_pre_shared_keys)

[3 Troubleshooting](/documentation/7.4/en/manual/encryption/troubleshooting)

[1 Connection type or permission problems](/documentation/7.4/en/manual/encryption/troubleshooting/connection_permission_problems)

[2 Certificate problems](/documentation/7.4/en/manual/encryption/troubleshooting/certificate_problems)

[3 PSK problems](/documentation/7.4/en/manual/encryption/troubleshooting/psk_problems)

[18 Web interface](/documentation/7.4/en/manual/web_interface)

[1 Menu](/documentation/7.4/en/manual/web_interface/menu)

[1 Event menu](/documentation/7.4/en/manual/web_interface/menu/event_menu)

[2 Host menu](/documentation/7.4/en/manual/web_interface/menu/host_menu)

[3 Item menu](/documentation/7.4/en/manual/web_interface/menu/item_menu)

[2 Frontend sections](/documentation/7.4/en/manual/web_interface/frontend_sections)

[1 Dashboards](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards)

[1 Dashboard widgets](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets)

[1 Action log](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/action_log)

[2 Clock](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/clock)

[3 Discovery status](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/discovery_status)

[4 Favorite graphs](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/favorite_graphs)

[5 Favorite maps](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/favorite_maps)

[6 Gauge](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge)

[7 Geomap](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/geomap)

[8 Graph](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/graph)

[9 Graph (classic)](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_classic)

[10 Graph prototype](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_prototype)

[11 Honeycomb](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/honeycomb)

[12 Host availability](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/host_availability)

[13 Host card](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/host_card)

[14 Host navigator](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/host_navigator)

[15 Item card](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/item_card)

[16 Item history](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history)

[17 Item navigator](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/item_navigator)

[18 Item value](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/item_value)

[19 Map](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/map)

[20 Map navigation tree](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/map_tree)

[21 Pie chart](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/pie_chart)

[22 Problem hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/problem_hosts)

[23 Problems](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/problems)

[24 Problems by severity](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/problems_severity)

[25 SLA report](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/sla_report)

[26 System information](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/system)

[27 Top hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/top_hosts)

[28 Top items](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/top_items)

[29 Top triggers](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/top_triggers)

[30 Trigger overview](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/trigger_overview)

[31 URL](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/url)

[32 Web monitoring](/documentation/7.4/en/manual/web_interface/frontend_sections/dashboards/widgets/web_monitoring)

[2 Monitoring](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring)

[1 Problems](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/problems)

[1 Cause and symptom problems](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/problems/cause_and_symptom)

[2 Hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/hosts)

[1 Graphs](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/hosts/graphs)

[2 Host dashboards](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/hosts/dashboards)

[3 Web scenarios](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/hosts/web)

[3 Latest data](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/latest_data)

[4 Maps](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/maps)

[5 Discovery](/documentation/7.4/en/manual/web_interface/frontend_sections/monitoring/discovery)

[3 Services](/documentation/7.4/en/manual/web_interface/frontend_sections/services)

[1 Services](/documentation/7.4/en/manual/web_interface/frontend_sections/services/service)

[2 SLA](/documentation/7.4/en/manual/web_interface/frontend_sections/services/sla)

[3 SLA report](/documentation/7.4/en/manual/web_interface/frontend_sections/services/sla_report)

[4 Inventory](/documentation/7.4/en/manual/web_interface/frontend_sections/inventory)

[1 Overview](/documentation/7.4/en/manual/web_interface/frontend_sections/inventory/overview)

[2 Hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/inventory/hosts)

[5 Reports](/documentation/7.4/en/manual/web_interface/frontend_sections/reports)

[1 System information](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/status_of_zabbix)

[2 Scheduled reports](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/scheduled)

[3 Availability report](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/availability)

[4 Top 100 triggers](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/triggers_top)

[5 Audit log](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/audit_log)

[6 Action log](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/action_log)

[7 Notifications](/documentation/7.4/en/manual/web_interface/frontend_sections/reports/notifications)

[6 Data collection](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection)

[1 Template groups](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templategroups)

[2 Host groups](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hostgroups)

[3 Templates](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates)

[1 Items](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/items)

[2 Triggers](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/triggers)

[3 Graphs](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/graphs)

[4 Discovery rules](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery)

[1 Item prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/item_prototypes)

[2 Trigger prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/trigger_prototypes)

[3 Graph prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/graph_prototypes)

[4 Host prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/host_prototypes)

[5 Discovery prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/discovery_prototypes)

[5 Web scenarios](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/templates/web)

[4 Hosts](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts)

[1 Items](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/items)

[2 Triggers](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/triggers)

[3 Graphs](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/graphs)

[4 Discovery rules](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery)

[1 Item prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/item_prototypes)

[2 Trigger prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/trigger_prototypes)

[3 Graph prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/graph_prototypes)

[4 Host prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/host_prototypes)

[5 Discovery prototypes](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/discovery_prototypes)

[5 Web scenarios](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/hosts/web)

[5 Maintenance](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/maintenance)

[6 Event correlation](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/correlation)

[7 Discovery](/documentation/7.4/en/manual/web_interface/frontend_sections/data_collection/discovery)

[7 Alerts](/documentation/7.4/en/manual/web_interface/frontend_sections/alerts)

[1 Actions](/documentation/7.4/en/manual/web_interface/frontend_sections/alerts/actions)

[2 Media types](/documentation/7.4/en/manual/web_interface/frontend_sections/alerts/mediatypes)

[3 Scripts](/documentation/7.4/en/manual/web_interface/frontend_sections/alerts/scripts)

[8 Users](/documentation/7.4/en/manual/web_interface/frontend_sections/users)

[1 User groups](/documentation/7.4/en/manual/web_interface/frontend_sections/users/user_groups)

[2 User roles](/documentation/7.4/en/manual/web_interface/frontend_sections/users/user_roles)

[3 Users](/documentation/7.4/en/manual/web_interface/frontend_sections/users/user_list)

[4 API tokens](/documentation/7.4/en/manual/web_interface/frontend_sections/users/api_tokens)

[5 Authentication](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication)

[1 HTTP](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication/http)

[2 LDAP](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication/ldap)

[3 SAML](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication/saml)

[4 MFA](/documentation/7.4/en/manual/web_interface/frontend_sections/users/authentication/mfa)

[9 Administration](/documentation/7.4/en/manual/web_interface/frontend_sections/administration)

[1 General](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/general)

[2 Audit log](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/audit_log)

[3 Housekeeping](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/housekeeping)

[4 Proxies](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/proxies)

[5 Proxy groups](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/proxy_groups)

[6 Macros](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/macros)

[7 Queue](/documentation/7.4/en/manual/web_interface/frontend_sections/administration/queue)

[3 User settings](/documentation/7.4/en/manual/web_interface/user_profile)

[1 Global notifications](/documentation/7.4/en/manual/web_interface/user_profile/global_notifications)

[2 Sound in browsers](/documentation/7.4/en/manual/web_interface/user_profile/sound)

[4 Global search](/documentation/7.4/en/manual/web_interface/global_search)

[5 Frontend maintenance mode](/documentation/7.4/en/manual/web_interface/maintenance_mode)

[6 Page parameters](/documentation/7.4/en/manual/web_interface/page_parameters)

[7 Definitions](/documentation/7.4/en/manual/web_interface/definitions)

[8 Creating your own theme](/documentation/7.4/en/manual/web_interface/theming)

[9 Debug mode](/documentation/7.4/en/manual/web_interface/debug_mode)

[10 Cookies used by Zabbix](/documentation/7.4/en/manual/web_interface/cookies)

[11 Time zones](/documentation/7.4/en/manual/web_interface/time_zone)

[12 Resetting password](/documentation/7.4/en/manual/web_interface/password_reset)

[13 Time period selector](/documentation/7.4/en/manual/web_interface/time_period_selector)

[19 Best practices](/documentation/7.4/en/manual/best_practices)

[1 Security best practices](/documentation/7.4/en/manual/best_practices/security)

[1 Access control](/documentation/7.4/en/manual/best_practices/security/access_control)

[1 Securing MySQL/MariaDB](/documentation/7.4/en/manual/best_practices/security/access_control/mysql)

[2 Securing PostgreSQL/TimescaleDB](/documentation/7.4/en/manual/best_practices/security/access_control/postgresql)

[2 Cryptography](/documentation/7.4/en/manual/best_practices/security/cryptography)

[3 Web server](/documentation/7.4/en/manual/best_practices/security/web_server)

[2 Configuration best practices](/documentation/7.4/en/manual/best_practices/configuration)

[20 API](/documentation/7.4/en/manual/api)

[Appendix 1. Reference commentary](/documentation/7.4/en/manual/api/reference_commentary)

[Appendix 2. Changes from 7.2 to 7.4](/documentation/7.4/en/manual/api/changes)

[Appendix 3. Changes in 7.4](/documentation/7.4/en/manual/api/changes_minor)

[Method reference](/documentation/7.4/en/manual/api/reference)

[API info](/documentation/7.4/en/manual/api/reference/apiinfo)

[apiinfo.version](/documentation/7.4/en/manual/api/reference/apiinfo/version)

[Action](/documentation/7.4/en/manual/api/reference/action)

[Action object](/documentation/7.4/en/manual/api/reference/action/object)

[action.create](/documentation/7.4/en/manual/api/reference/action/create)

[action.delete](/documentation/7.4/en/manual/api/reference/action/delete)

[action.get](/documentation/7.4/en/manual/api/reference/action/get)

[action.update](/documentation/7.4/en/manual/api/reference/action/update)

[Alert](/documentation/7.4/en/manual/api/reference/alert)

[Alert object](/documentation/7.4/en/manual/api/reference/alert/object)

[alert.get](/documentation/7.4/en/manual/api/reference/alert/get)

[Audit log](/documentation/7.4/en/manual/api/reference/auditlog)

[Audit log object](/documentation/7.4/en/manual/api/reference/auditlog/object)

[auditlog.get](/documentation/7.4/en/manual/api/reference/auditlog/get)

[Authentication](/documentation/7.4/en/manual/api/reference/authentication)

[Authentication object](/documentation/7.4/en/manual/api/reference/authentication/object)

[authentication.get](/documentation/7.4/en/manual/api/reference/authentication/get)

[authentication.update](/documentation/7.4/en/manual/api/reference/authentication/update)

[Autoregistration](/documentation/7.4/en/manual/api/reference/autoregistration)

[Autoregistration object](/documentation/7.4/en/manual/api/reference/autoregistration/object)

[autoregistration.get](/documentation/7.4/en/manual/api/reference/autoregistration/get)

[autoregistration.update](/documentation/7.4/en/manual/api/reference/autoregistration/update)

[Configuration](/documentation/7.4/en/manual/api/reference/configuration)

[configuration.export](/documentation/7.4/en/manual/api/reference/configuration/export)

[configuration.import](/documentation/7.4/en/manual/api/reference/configuration/import)

[configuration.importcompare](/documentation/7.4/en/manual/api/reference/configuration/importcompare)

[Connector](/documentation/7.4/en/manual/api/reference/connector)

[Connector object](/documentation/7.4/en/manual/api/reference/connector/object)

[connector.create](/documentation/7.4/en/manual/api/reference/connector/create)

[connector.delete](/documentation/7.4/en/manual/api/reference/connector/delete)

[connector.get](/documentation/7.4/en/manual/api/reference/connector/get)

[connector.update](/documentation/7.4/en/manual/api/reference/connector/update)

[Correlation](/documentation/7.4/en/manual/api/reference/correlation)

[Correlation object](/documentation/7.4/en/manual/api/reference/correlation/object)

[correlation.create](/documentation/7.4/en/manual/api/reference/correlation/create)

[correlation.delete](/documentation/7.4/en/manual/api/reference/correlation/delete)

[correlation.get](/documentation/7.4/en/manual/api/reference/correlation/get)

[correlation.update](/documentation/7.4/en/manual/api/reference/correlation/update)

[Dashboard](/documentation/7.4/en/manual/api/reference/dashboard)

[Dashboard object](/documentation/7.4/en/manual/api/reference/dashboard/object)

[dashboard.create](/documentation/7.4/en/manual/api/reference/dashboard/create)

[dashboard.delete](/documentation/7.4/en/manual/api/reference/dashboard/delete)

[dashboard.get](/documentation/7.4/en/manual/api/reference/dashboard/get)

[dashboard.update](/documentation/7.4/en/manual/api/reference/dashboard/update)

[Dashboard widget fields](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields)

[1 Action log](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/action_log)

[2 Clock](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/clock)

[3 Discovery status](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/discovery_status)

[4 Favorite graphs](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/favorite_graphs)

[5 Favorite maps](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/favorite_maps)

[6 Gauge](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/gauge)

[7 Geomap](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/geomap)

[8 Graph](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/graph)

[9 Graph (classic)](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/graph_classic)

[10 Graph prototype](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/graph_prototype)

[11 Honeycomb](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/honeycomb)

[12 Host availability](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/host_availability)

[13 Host card](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/host_card)

[14 Host navigator](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/host_navigator)

[15 Item card](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/item_card)

[16 Item history](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/item_history)

[17 Item navigator](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/item_navigator)

[18 Item value](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/item_value)

[19 Map](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/map)

[20 Map navigation tree](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/map_tree)

[21 Pie chart](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/pie_chart)

[22 Problem hosts](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/problem_hosts)

[23 Problems](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/problems)

[24 Problems by severity](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/problems_severity)

[25 SLA report](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/sla_report)

[26 System information](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/system)

[27 Top hosts](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/top_hosts)

[28 Top items](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/top_items)

[29 Top triggers](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/top_triggers)

[30 Trigger overview](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/trigger_overview)

[31 URL](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/url)

[32 Web monitoring](/documentation/7.4/en/manual/api/reference/dashboard/widget_fields/web_monitoring)

[Discovered host](/documentation/7.4/en/manual/api/reference/dhost)

[Discovered host object](/documentation/7.4/en/manual/api/reference/dhost/object)

[dhost.get](/documentation/7.4/en/manual/api/reference/dhost/get)

[Discovered service](/documentation/7.4/en/manual/api/reference/dservice)

[Discovered service object](/documentation/7.4/en/manual/api/reference/dservice/object)

[dservice.get](/documentation/7.4/en/manual/api/reference/dservice/get)

[Discovery check](/documentation/7.4/en/manual/api/reference/dcheck)

[Discovery check object](/documentation/7.4/en/manual/api/reference/dcheck/object)

[dcheck.get](/documentation/7.4/en/manual/api/reference/dcheck/get)

[Discovery rule](/documentation/7.4/en/manual/api/reference/drule)

[Discovery rule object](/documentation/7.4/en/manual/api/reference/drule/object)

[drule.create](/documentation/7.4/en/manual/api/reference/drule/create)

[drule.delete](/documentation/7.4/en/manual/api/reference/drule/delete)

[drule.get](/documentation/7.4/en/manual/api/reference/drule/get)

[drule.update](/documentation/7.4/en/manual/api/reference/drule/update)

[Event](/documentation/7.4/en/manual/api/reference/event)

[Event object](/documentation/7.4/en/manual/api/reference/event/object)

[event.acknowledge](/documentation/7.4/en/manual/api/reference/event/acknowledge)

[event.get](/documentation/7.4/en/manual/api/reference/event/get)

[Graph](/documentation/7.4/en/manual/api/reference/graph)

[Graph object](/documentation/7.4/en/manual/api/reference/graph/object)

[graph.create](/documentation/7.4/en/manual/api/reference/graph/create)

[graph.delete](/documentation/7.4/en/manual/api/reference/graph/delete)

[graph.get](/documentation/7.4/en/manual/api/reference/graph/get)

[graph.update](/documentation/7.4/en/manual/api/reference/graph/update)

[Graph item](/documentation/7.4/en/manual/api/reference/graphitem)

[Graph item object](/documentation/7.4/en/manual/api/reference/graphitem/object)

[graphitem.get](/documentation/7.4/en/manual/api/reference/graphitem/get)

[Graph prototype](/documentation/7.4/en/manual/api/reference/graphprototype)

[Graph prototype object](/documentation/7.4/en/manual/api/reference/graphprototype/object)

[graphprototype.create](/documentation/7.4/en/manual/api/reference/graphprototype/create)

[graphprototype.delete](/documentation/7.4/en/manual/api/reference/graphprototype/delete)

[graphprototype.get](/documentation/7.4/en/manual/api/reference/graphprototype/get)

[graphprototype.update](/documentation/7.4/en/manual/api/reference/graphprototype/update)

[High availability node](/documentation/7.4/en/manual/api/reference/hanode)

[High availability node object](/documentation/7.4/en/manual/api/reference/hanode/object)

[hanode.get](/documentation/7.4/en/manual/api/reference/hanode/get)

[History](/documentation/7.4/en/manual/api/reference/history)

[History object](/documentation/7.4/en/manual/api/reference/history/object)

[history.clear](/documentation/7.4/en/manual/api/reference/history/clear)

[history.get](/documentation/7.4/en/manual/api/reference/history/get)

[history.push](/documentation/7.4/en/manual/api/reference/history/push)

[Host](/documentation/7.4/en/manual/api/reference/host)

[Host object](/documentation/7.4/en/manual/api/reference/host/object)

[host.create](/documentation/7.4/en/manual/api/reference/host/create)

[host.delete](/documentation/7.4/en/manual/api/reference/host/delete)

[host.get](/documentation/7.4/en/manual/api/reference/host/get)

[host.massadd](/documentation/7.4/en/manual/api/reference/host/massadd)

[host.massremove](/documentation/7.4/en/manual/api/reference/host/massremove)

[host.massupdate](/documentation/7.4/en/manual/api/reference/host/massupdate)

[host.update](/documentation/7.4/en/manual/api/reference/host/update)

[Host group](/documentation/7.4/en/manual/api/reference/hostgroup)

[Host group object](/documentation/7.4/en/manual/api/reference/hostgroup/object)

[hostgroup.create](/documentation/7.4/en/manual/api/reference/hostgroup/create)

[hostgroup.delete](/documentation/7.4/en/manual/api/reference/hostgroup/delete)

[hostgroup.get](/documentation/7.4/en/manual/api/reference/hostgroup/get)

[hostgroup.massadd](/documentation/7.4/en/manual/api/reference/hostgroup/massadd)

[hostgroup.massremove](/documentation/7.4/en/manual/api/reference/hostgroup/massremove)

[hostgroup.massupdate](/documentation/7.4/en/manual/api/reference/hostgroup/massupdate)

[hostgroup.propagate](/documentation/7.4/en/manual/api/reference/hostgroup/propagate)

[hostgroup.update](/documentation/7.4/en/manual/api/reference/hostgroup/update)

[Host interface](/documentation/7.4/en/manual/api/reference/hostinterface)


...44062 bytes truncated...

The tool call succeeded but the output was truncated. Full output saved to: C:\Users\f.manghi\.local\share\opencode\tool-output\tool_1639c9e21001xOlK7QGu40Vbaw
Use the Task tool to have explore agent process this file with Grep and Read (with offset/limit). Do NOT read the full file yourself - delegate to save context.
```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 6.3s)

_Thinking:_

The page content was truncated before the Host inventory section. Let me search the saved output file for the inventory fields list.

**Tool: bash**

**Input:**
```json
{
  "command": "$f=\"C:\\Users\\f.manghi\\.local\\share\\opencode\\tool-output\\tool_1639c9e21001xOlK7QGu40Vbaw\"; Select-String -Path $f -Pattern \"macaddress_a|serialno_a|host-inventory\" | Select-Object -First 20 | ForEach-Object { $_.LineNumber.ToString() + \": \" + $_.Line }"
}
```

**Output:**
```
1946:     -   [Host inventory](#host-inventory)

```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 4.9s)

_Thinking:_

The Host inventory section exists around line 1946. Let me read the file around that line to get the full list of inventory fields.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\f.manghi\\.local\\share\\opencode\\tool-output\\tool_1639c9e21001xOlK7QGu40Vbaw",
  "offset": 1946,
  "limit": 200
}
```

**Output:**
```
<path>C:\Users\f.manghi\.local\share\opencode\tool-output\tool_1639c9e21001xOlK7QGu40Vbaw</path>
<type>file</type>
<content>
1946:     -   [Host inventory](#host-inventory)
1947:     -   [Host tag](#host-tag)
1948: 
1949: # Host object
1950: 
1951: The following objects are directly related to the host API.
1952: 
1953: ### Host
1954: 
1955: The host object has the following properties.
1956: 
1957:   
1958: 
1959: Property
1960: 
1961: [Type](/documentation/7.4/en/manual/api/reference_commentary#data-types)
1962: 
1963: Description
1964: 
1965: hostid
1966: 
1967: ID
1968: 
1969: ID of the host.  
1970:   
1971: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
1972: \- *read-only*  
1973: \- *required* for update operations
1974: 
1975: host
1976: 
1977: string
1978: 
1979: Technical name of the host.  
1980:   
1981: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
1982: \- *required* for create operations
1983: 
1984: description
1985: 
1986: text
1987: 
1988: Description of the host.
1989: 
1990: flags
1991: 
1992: integer
1993: 
1994: [Origin](/documentation/7.4/en/manual/api/reference_commentary#entity-origin-flags) of the host.  
1995:   
1996: Possible values:  
1997: 0 - a plain host;  
1998: 4 - a host converted from prototype.  
1999:   
2000: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
2001: \- *read-only*
2002: 
2003: inventory\_mode
2004: 
2005: integer
2006: 
2007: Host inventory population mode.  
2008:   
2009: Possible values:  
2010: \-1 - *(default)* disabled;  
2011: 0 - manual;  
2012: 1 - automatic.
2013: 
2014: ipmi\_authtype
2015: 
2016: integer
2017: 
2018: IPMI authentication algorithm.  
2019:   
2020: Possible values:  
2021: \-1 - *(default)* default;  
2022: 0 - none;  
2023: 1 - MD2;  
2024: 2 - MD5  
2025: 4 - straight;  
2026: 5 - OEM;  
2027: 6 - RMCP+.
2028: 
2029: ipmi\_password
2030: 
2031: string
2032: 
2033: IPMI password.
2034: 
2035: ipmi\_privilege
2036: 
2037: integer
2038: 
2039: IPMI privilege level.  
2040:   
2041: Possible values:  
2042: 1 - callback;  
2043: 2 - *(default)* user;  
2044: 3 - operator;  
2045: 4 - admin;  
2046: 5 - OEM.
2047: 
2048: ipmi\_username
2049: 
2050: string
2051: 
2052: IPMI username.
2053: 
2054: maintenance\_from
2055: 
2056: timestamp
2057: 
2058: Starting time of the effective maintenance.  
2059:   
2060: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
2061: \- *read-only*
2062: 
2063: maintenance\_status
2064: 
2065: integer
2066: 
2067: Effective maintenance status.  
2068:   
2069: Possible values:  
2070: 0 - *(default)* no maintenance;  
2071: 1 - maintenance in effect.  
2072:   
2073: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
2074: \- *read-only*
2075: 
2076: maintenance\_type
2077: 
2078: integer
2079: 
2080: Effective maintenance type.  
2081:   
2082: Possible values:  
2083: 0 - *(default)* maintenance with data collection;  
2084: 1 - maintenance without data collection.  
2085:   
2086: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
2087: \- *read-only*
2088: 
2089: maintenanceid
2090: 
2091: ID
2092: 
2093: ID of the maintenance that is currently in effect on the host.  
2094:   
2095: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
2096: \- *read-only*
2097: 
2098: name
2099: 
2100: string
2101: 
2102: Visible name of the host.  
2103:   
2104: Default: `host` property value.
2105: 
2106: monitored\_by
2107: 
2108: integer
2109: 
2110: Source that is used to monitor the host.  
2111:   
2112: Possible values:  
2113: 0 - *(default)* Zabbix server;  
2114: 1 - Proxy;  
2115: 2 - Proxy group.
2116: 
2117: proxyid
2118: 
2119: ID
2120: 
2121: ID of the proxy that is used to monitor the host.  
2122:   
2123: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
2124: \- *required* if `monitored_by` is set to "Proxy"
2125: 
2126: proxy\_groupid
2127: 
2128: ID
2129: 
2130: ID of the proxy group that is used to monitor the host.  
2131:   
2132: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
2133: \- *required* if `monitored_by` is set to "Proxy group"
2134: 
2135: status
2136: 
2137: integer
2138: 
2139: Status and function of the host.  
2140:   
2141: Possible values:  
2142: 0 - *(default)* enabled;  
2143: 1 - disabled.
2144: 
2145: tls\_connect

(Showing lines 1946-2145 of 3056. Use offset=2146 to continue.)
</content>
```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 5.3s)

_Thinking:_

I need to find the Host inventory section. Let me search for "Host inventory" heading within the file.

**Tool: bash**

**Input:**
```json
{
  "command": "$f=\"C:\\Users\\f.manghi\\.local\\share\\opencode\\tool-output\\tool_1639c9e21001xOlK7QGu40Vbaw\"; Select-String -Path $f -Pattern \"^# Host inventory|^## Host inventory|Host inventory$\" | ForEach-Object { $_.LineNumber.ToString() + \": \" + $_.Line }"
}
```

**Output:**
```
2226: ### Host inventory

```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 10.9s)

_Thinking:_

Found the Host inventory section starting at line 2226. Let me read from there to get the full list of inventory fields.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\f.manghi\\.local\\share\\opencode\\tool-output\\tool_1639c9e21001xOlK7QGu40Vbaw",
  "limit": 400,
  "offset": 2226
}
```

**Output:**
```
<path>C:\Users\f.manghi\.local\share\opencode\tool-output\tool_1639c9e21001xOlK7QGu40Vbaw</path>
<type>file</type>
<content>
2226: ### Host inventory
2227: 
2228: The host inventory object has the following properties.
2229: 
2230: Each property has it's own unique ID number, which is used to associate host inventory fields with items.
2231: 
2232:     
2233: 
2234: ID
2235: 
2236: Property
2237: 
2238: [Type](/documentation/7.4/en/manual/api/reference_commentary#data-types)
2239: 
2240: Description
2241: 
2242: Maximum length
2243: 
2244: 4
2245: 
2246: alias
2247: 
2248: string
2249: 
2250: Alias.
2251: 
2252: 128 characters
2253: 
2254: 11
2255: 
2256: asset\_tag
2257: 
2258: string
2259: 
2260: Asset tag.
2261: 
2262: 64 characters
2263: 
2264: 28
2265: 
2266: chassis
2267: 
2268: string
2269: 
2270: Chassis.
2271: 
2272: 64 characters
2273: 
2274: 23
2275: 
2276: contact
2277: 
2278: string
2279: 
2280: Contact person.
2281: 
2282: 65535 characters for SQL databases
2283: 
2284: 32
2285: 
2286: contract\_number
2287: 
2288: string
2289: 
2290: Contract number.
2291: 
2292: 64 characters
2293: 
2294: 47
2295: 
2296: date\_hw\_decomm
2297: 
2298: string
2299: 
2300: HW decommissioning date.
2301: 
2302: 64 characters
2303: 
2304: 46
2305: 
2306: date\_hw\_expiry
2307: 
2308: string
2309: 
2310: HW maintenance expiry date.
2311: 
2312: 64 characters
2313: 
2314: 45
2315: 
2316: date\_hw\_install
2317: 
2318: string
2319: 
2320: HW installation date.
2321: 
2322: 64 characters
2323: 
2324: 44
2325: 
2326: date\_hw\_purchase
2327: 
2328: string
2329: 
2330: HW purchase date.
2331: 
2332: 64 characters
2333: 
2334: 34
2335: 
2336: deployment\_status
2337: 
2338: string
2339: 
2340: Deployment status.
2341: 
2342: 64 characters
2343: 
2344: 14
2345: 
2346: hardware
2347: 
2348: string
2349: 
2350: Hardware.
2351: 
2352: 255 characters
2353: 
2354: 15
2355: 
2356: hardware\_full
2357: 
2358: string
2359: 
2360: Detailed hardware.
2361: 
2362: 65535 characters for SQL databases
2363: 
2364: 39
2365: 
2366: host\_netmask
2367: 
2368: string
2369: 
2370: Host subnet mask.
2371: 
2372: 39 characters
2373: 
2374: 38
2375: 
2376: host\_networks
2377: 
2378: string
2379: 
2380: Host networks.
2381: 
2382: 65535 characters for SQL databases
2383: 
2384: 40
2385: 
2386: host\_router
2387: 
2388: string
2389: 
2390: Host router.
2391: 
2392: 39 characters
2393: 
2394: 30
2395: 
2396: hw\_arch
2397: 
2398: string
2399: 
2400: HW architecture.
2401: 
2402: 32 characters
2403: 
2404: 33
2405: 
2406: installer\_name
2407: 
2408: string
2409: 
2410: Installer name.
2411: 
2412: 64 characters
2413: 
2414: 24
2415: 
2416: location
2417: 
2418: string
2419: 
2420: Location.
2421: 
2422: 65535 characters for SQL databases
2423: 
2424: 25
2425: 
2426: location\_lat
2427: 
2428: string
2429: 
2430: Location latitude.
2431: 
2432: 16 characters
2433: 
2434: 26
2435: 
2436: location\_lon
2437: 
2438: string
2439: 
2440: Location longitude.
2441: 
2442: 16 characters
2443: 
2444: 12
2445: 
2446: macaddress\_a
2447: 
2448: string
2449: 
2450: MAC address A.
2451: 
2452: 64 characters
2453: 
2454: 13
2455: 
2456: macaddress\_b
2457: 
2458: string
2459: 
2460: MAC address B.
2461: 
2462: 64 characters
2463: 
2464: 29
2465: 
2466: model
2467: 
2468: string
2469: 
2470: Model.
2471: 
2472: 64 characters
2473: 
2474: 3
2475: 
2476: name
2477: 
2478: string
2479: 
2480: Name.
2481: 
2482: 128 characters
2483: 
2484: 27
2485: 
2486: notes
2487: 
2488: string
2489: 
2490: Notes.
2491: 
2492: 65535 characters for SQL databases
2493: 
2494: 41
2495: 
2496: oob\_ip
2497: 
2498: string
2499: 
2500: OOB IP address.
2501: 
2502: 39 characters
2503: 
2504: 42
2505: 
2506: oob\_netmask
2507: 
2508: string
2509: 
2510: OOB host subnet mask.
2511: 
2512: 39 characters
2513: 
2514: 43
2515: 
2516: oob\_router
2517: 
2518: string
2519: 
2520: OOB router.
2521: 
2522: 39 characters
2523: 
2524: 5
2525: 
2526: os
2527: 
2528: string
2529: 
2530: OS name.
2531: 
2532: 128 characters
2533: 
2534: 6
2535: 
2536: os\_full
2537: 
2538: string
2539: 
2540: Detailed OS name.
2541: 
2542: 255 characters
2543: 
2544: 7
2545: 
2546: os\_short
2547: 
2548: string
2549: 
2550: Short OS name.
2551: 
2552: 128 characters
2553: 
2554: 61
2555: 
2556: poc\_1\_cell
2557: 
2558: string
2559: 
2560: Primary POC mobile number.
2561: 
2562: 64 characters
2563: 
2564: 58
2565: 
2566: poc\_1\_email
2567: 
2568: string
2569: 
2570: Primary email.
2571: 
2572: 128 characters
2573: 
2574: 57
2575: 
2576: poc\_1\_name
2577: 
2578: string
2579: 
2580: Primary POC name.
2581: 
2582: 128 characters
2583: 
2584: 63
2585: 
2586: poc\_1\_notes
2587: 
2588: string
2589: 
2590: Primary POC notes.
2591: 
2592: 65535 characters for SQL databases
2593: 
2594: 59
2595: 
2596: poc\_1\_phone\_a
2597: 
2598: string
2599: 
2600: Primary POC phone A.
2601: 
2602: 64 characters
2603: 
2604: 60
2605: 
2606: poc\_1\_phone\_b
2607: 
2608: string
2609: 
2610: Primary POC phone B.
2611: 
2612: 64 characters
2613: 
2614: 62
2615: 
2616: poc\_1\_screen
2617: 
2618: string
2619: 
2620: Primary POC screen name.
2621: 
2622: 64 characters
2623: 
2624: 68
2625: 

(Showing lines 2226-2625 of 3056. Use offset=2626 to continue.)
</content>
```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 3.7s)

_Thinking:_

I've confirmed the valid inventory fields. Let me continue reading to see the rest of the fields (serialno_a, serialno_b, software, etc.).

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\f.manghi\\.local\\share\\opencode\\tool-output\\tool_1639c9e21001xOlK7QGu40Vbaw",
  "limit": 250,
  "offset": 2626
}
```

**Output:**
```
<path>C:\Users\f.manghi\.local\share\opencode\tool-output\tool_1639c9e21001xOlK7QGu40Vbaw</path>
<type>file</type>
<content>
2626: poc\_2\_cell
2627: 
2628: string
2629: 
2630: Secondary POC mobile number.
2631: 
2632: 64 characters
2633: 
2634: 65
2635: 
2636: poc\_2\_email
2637: 
2638: string
2639: 
2640: Secondary POC email.
2641: 
2642: 128 characters
2643: 
2644: 64
2645: 
2646: poc\_2\_name
2647: 
2648: string
2649: 
2650: Secondary POC name.
2651: 
2652: 128 characters
2653: 
2654: 70
2655: 
2656: poc\_2\_notes
2657: 
2658: string
2659: 
2660: Secondary POC notes.
2661: 
2662: 65535 characters for SQL databases
2663: 
2664: 66
2665: 
2666: poc\_2\_phone\_a
2667: 
2668: string
2669: 
2670: Secondary POC phone A.
2671: 
2672: 64 characters
2673: 
2674: 67
2675: 
2676: poc\_2\_phone\_b
2677: 
2678: string
2679: 
2680: Secondary POC phone B.
2681: 
2682: 64 characters
2683: 
2684: 69
2685: 
2686: poc\_2\_screen
2687: 
2688: string
2689: 
2690: Secondary POC screen name.
2691: 
2692: 64 characters
2693: 
2694: 8
2695: 
2696: serialno\_a
2697: 
2698: string
2699: 
2700: Serial number A.
2701: 
2702: 64 characters
2703: 
2704: 9
2705: 
2706: serialno\_b
2707: 
2708: string
2709: 
2710: Serial number B.
2711: 
2712: 64 characters
2713: 
2714: 48
2715: 
2716: site\_address\_a
2717: 
2718: string
2719: 
2720: Site address A.
2721: 
2722: 128 characters
2723: 
2724: 49
2725: 
2726: site\_address\_b
2727: 
2728: string
2729: 
2730: Site address B.
2731: 
2732: 128 characters
2733: 
2734: 50
2735: 
2736: site\_address\_c
2737: 
2738: string
2739: 
2740: Site address C.
2741: 
2742: 128 characters
2743: 
2744: 51
2745: 
2746: site\_city
2747: 
2748: string
2749: 
2750: Site city.
2751: 
2752: 128 characters
2753: 
2754: 53
2755: 
2756: site\_country
2757: 
2758: string
2759: 
2760: Site country.
2761: 
2762: 64 characters
2763: 
2764: 56
2765: 
2766: site\_notes
2767: 
2768: string
2769: 
2770: Site notes.
2771: 
2772: 65535 characters for SQL databases
2773: 
2774: 55
2775: 
2776: site\_rack
2777: 
2778: string
2779: 
2780: Site rack location.
2781: 
2782: 128 characters
2783: 
2784: 52
2785: 
2786: site\_state
2787: 
2788: string
2789: 
2790: Site state.
2791: 
2792: 64 characters
2793: 
2794: 54
2795: 
2796: site\_zip
2797: 
2798: string
2799: 
2800: Site ZIP/postal code.
2801: 
2802: 64 characters
2803: 
2804: 16
2805: 
2806: software
2807: 
2808: string
2809: 
2810: Software.
2811: 
2812: 255 characters
2813: 
2814: 18
2815: 
2816: software\_app\_a
2817: 
2818: string
2819: 
2820: Software application A.
2821: 
2822: 64 characters
2823: 
2824: 19
2825: 
2826: software\_app\_b
2827: 
2828: string
2829: 
2830: Software application B.
2831: 
2832: 64 characters
2833: 
2834: 20
2835: 
2836: software\_app\_c
2837: 
2838: string
2839: 
2840: Software application C.
2841: 
2842: 64 characters
2843: 
2844: 21
2845: 
2846: software\_app\_d
2847: 
2848: string
2849: 
2850: Software application D.
2851: 
2852: 64 characters
2853: 
2854: 22
2855: 
2856: software\_app\_e
2857: 
2858: string
2859: 
2860: Software application E.
2861: 
2862: 64 characters
2863: 
2864: 17
2865: 
2866: software\_full
2867: 
2868: string
2869: 
2870: Software details.
2871: 
2872: 65535 characters for SQL databases
2873: 
2874: 10
2875: 

(Showing lines 2626-2875 of 3056. Use offset=2876 to continue.)
</content>
```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 7.6s)

_Thinking:_

Interesting! In Zabbix 7.4, the inventory fields are actually:
- `serialno_a` (Serial number A) — NOT `serial`
- `macaddress_a` (MAC address A) — NOT `macaddress`
- `software` — actually EXISTS in 7.4! Interesting. Let me check the rest of the list.
- `type` — need to check. Let me continue reading.
- `name` — exists (Name,128 chars)
- `notes` — exists
- `device` — need to check if it exists.

Let me read the remaining part to see `type`, `tag`, `url`, `vendor`, etc.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\f.manghi\\.local\\share\\opencode\\tool-output\\tool_1639c9e21001xOlK7QGu40Vbaw",
  "limit": 180,
  "offset": 2876
}
```

**Output:**
```
<path>C:\Users\f.manghi\.local\share\opencode\tool-output\tool_1639c9e21001xOlK7QGu40Vbaw</path>
<type>file</type>
<content>
2876: tag
2877: 
2878: string
2879: 
2880: Tag.
2881: 
2882: 64 characters
2883: 
2884: 1
2885: 
2886: type
2887: 
2888: string
2889: 
2890: Type.
2891: 
2892: 64 characters
2893: 
2894: 2
2895: 
2896: type\_full
2897: 
2898: string
2899: 
2900: Type details.
2901: 
2902: 64 characters
2903: 
2904: 35
2905: 
2906: url\_a
2907: 
2908: string
2909: 
2910: URL A.
2911: 
2912: 2048 characters
2913: 
2914: 36
2915: 
2916: url\_b
2917: 
2918: string
2919: 
2920: URL B.
2921: 
2922: 2048 characters
2923: 
2924: 37
2925: 
2926: url\_c
2927: 
2928: string
2929: 
2930: URL C.
2931: 
2932: 2048 characters
2933: 
2934: 31
2935: 
2936: vendor
2937: 
2938: string
2939: 
2940: Vendor.
2941: 
2942: 64 characters
2943: 
2944: ### Host tag
2945: 
2946: The host tag object has the following properties.
2947: 
2948:   
2949: 
2950: Property
2951: 
2952: [Type](/documentation/7.4/en/manual/api/reference_commentary#data-types)
2953: 
2954: Description
2955: 
2956: tag
2957: 
2958: string
2959: 
2960: Host tag name.  
2961:   
2962: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
2963: \- *required*
2964: 
2965: value
2966: 
2967: string
2968: 
2969: Host tag value.
2970: 
2971: automatic
2972: 
2973: integer
2974: 
2975: Type of host tag.  
2976:   
2977: Possible values:  
2978: 0 - *(default)* manual (tag created by user);  
2979: 1 - automatic (tag created by low-level discovery)  
2980:   
2981: [Property behavior](/documentation/7.4/en/manual/api/reference_commentary#property-behavior):  
2982: \- *read-only*
2983: 
2984: ### What’s next?
2985: 
2986: [host.create](/documentation/7.4/en/manual/api/reference/host/create)
2987: 
2988: ### Did you find what you needed?
2989: 
2990: -   0
2991: -   1
2992: -   2
2993: -   3
2994: -   4
2995: -   5
2996: -   6
2997: -   7
2998: -   8
2999: -   9
3000: -   10
3001: 
3002: Not at all
3003: 
3004: Completely
3005: 
3006: Can you tell us more about your rating?
3007: 
3008: Your input is anonymous and helps us improve the documentation.
3009: 
3010:   Send feedback
3011: 
3012: ### Help us improve this page
3013: 
3014: Select the text you'd like to improve and press **Ctrl + Enter****Command + Enter** to send feedback to our editors.
3015: 
3016: ### Search tip
3017: 
3018: Press **Ctrl + Alt + H****Command + Option + H** to toggle search highlight
3019: 
3020: ### Need help?
3021: 
3022: [Technical Support](https://www.zabbix.com/support)
3023: 
3024: [All services](https://www.zabbix.com/services)
3025: 
3026: [Professional Training](https://www.zabbix.com/training?language=english)
3027: 
3028: [Zabbix Forum](https://www.zabbix.com/forum/)
3029: 
3030: © 2001-2026 by Zabbix SIA. All rights reserved. [License](https://www.zabbix.com/documentation/info/en/license)
3031: 
3032: [](#)
3033: 
3034: Copy
3035: 
3036: Copied
3037: 
3038: Suggest edit
3039: 
3040: ### Suggest edit
3041: 
3042:    
3043: 
3044: Cancel Report
3045: 
3046: ### Suggest an example
3047: 
3048:     
3049: 
3050: Cancel Report
3051: 
3052: ### Thank you!
3053: 
3054: Your feedback has been sent. We appreciate you taking the time to help improve Zabbix documentation. Your suggestion has been sent to the editors. We appreciate you taking the time to help improve Zabbix documentation. Something happened wrong. Please try again next time.
3055: 

(Showing lines 2876-3055 of 3056. Use offset=3056 to continue.)
</content>
```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 45.8s)

_Thinking:_

Now I have the full list of valid Zabbix 7.4 host inventory fields:

- alias
- asset_tag
- chassis
- contact
- contract_number
- date_hw_decomm
- date_hw_expiry
- date_hw_install
- date_hw_purchase
- deployment_status
- hardware
- hardware_full
- host_netmask
- host_networks
- host_router
- hw_arch
- installer_name
- location
- location_lat
- location_lon
- macaddress_a
- macaddress_b
- model
- name
- notes
- oob_ip
- oob_netmask
- oob_router
- os
- os_full
- os_short
- poc_1_cell, poc_1_email, poc_1_name, poc_1_notes, poc_1_phone_a, poc_1_phone_b, poc_1_screen
- poc_2_cell, poc_2_email, poc_2_name, poc_2_notes, poc_2_phone_a, poc_2_phone_b, poc_2_screen
- serialno_a
- serialno_b
- site_address_a/b/c, site_city, site_country, site_notes, site_rack, site_state, site_zip
- software
- software_app_a..e
- software_full
- tag
- type
- type_full
- url_a, url_b, url_c
- vendor

Interesting! In Zabbix 7.4, `software` DOES exist (in older versions it was `sw`?). Actually wait — let me check. In Zabbix 6.0, the field was `sw` I believe. Let me check the 7.4 list I just read: yes, `software` (id 16, "Software", 255 chars). So `software` is valid in 7.4.

Wait, but the code targets Zabbix 7.0 per the docstring ("Client Zabbix 7.0 JSON-RPC"). Hmm. In 7.0, was the field `sw` or `software`? Let me check the 7.0 docs to be sure. Actually the user explicitly pointed to the 7.4 page. But the docstring says 7.0. Let me check 7.0 host object inventory fields to see if `software` exists there too.

Actually, in older Zabbix versions (5.x/6.x), the inventory fields were: type, type_full, name, alias, os, os_full, os_short, serialno_a, serialno_b, macaddress_a, macaddress_b, hardware, hardware_full, software, software_full, ... Hmm, actually I recall `software` has existed for a long time. Let me verify quickly for 7.0.

Now the code's `_desired_inventory` uses:
1. `type` — VALID (Type)
2. `name` — VALID (Name)
3. `serial` — INVALID. Should be `serialno_a`
4. `macaddress` — INVALID. Should be `macaddress_a`
5. `device` — INVALID. Not in the list. Should map to... `model`? or `hardware`? The code maps `product_type` → `device`. Best mapping: `hardware` (Hardware, 255 chars) or `model` (Model, 64 chars) or `type_full`. Product type suggests `type_full` or `hardware`. I'd say `model` or `hardware`. Let's think: `dev["product_type"]` — product type like "S7-1200", "CNC" etc. Mapping to `type_full` ("Type details") seems most semantically appropriate, or `hardware`. Hmm.
6. `software` — VALID in 7.4 (Software). Code maps `firmware` → `software`. That's valid per7.4 docs. But wait — need to check 7.0 docs too since the client targets 7.0. Actually let me check whether `software` exists in 7.0. I believe in Zabbix the field was renamed at some point? Let me recall: Zabbix inventory field IDs: 1=type, 2=type_full, 3=model, 4=alias, 5=os (no...). Actually from the 7.4 doc IDs: type=1, type_full=2, model=3, alias=4, os=5, os_full=6, os_short=7, serialno_a=8, serialno_b=9, software=10, hardware=11, ...

Hmm wait, in the old Zabbix the fields were: 1 type, 2 type_full, 3 model, 4 alias, 5 os, 6 os_full, 7 os_short, 8 serialno_a, 9 serialno_b, 10 sw, 11 hw, 12 macaddress_a, 13 macaddress_b... Actually I recall `sw` and `hw` were the old names in the UI? No — in the DB the columns were inventory fields as generic key/value (host_inventory table). The API property names in docs: for6.0 I think they were `software` and `hardware` too? Let me quickly check 7.0 docs to be safe since the client says 7.0.

Actually, the user pointed to the 7.4 page. The main errors are clearly `serial`, `macaddress`, and `device`. `notes` is valid. `name` is valid. `type` is valid.

Let me double-check `software` in 7.0 docs to be thorough. I'll fetch the 7.0 host object page and grep for the inventory fields. Actually, to save context, I could use the explore agent... but a targeted webfetch of the 7.0 page will also be huge (3000+ lines). Let me instead fetch and have the output saved to file, then grep.

Actually the webfetch tool truncates and saves to a file, then I can grep. That worked fine. But each fetch costs a lot of context (the truncated output itself is large). The nav menu is huge (~1900 lines before content). 

Alternative: I could just check7.0 quickly. Actually, my knowledge: Zabbix 6.0/7.0 host inventory API fields include `software` (Software) — yes, I'm fairly confident `software` and `hardware` have been the API names for a long time (the UI labels are "Software applications A/B..." for software_app_*). Actually hold on. In older Zabbix docs (4.0/5.0), the fields were listed as: type, type_full, name, alias, os, os_full, os_short, serialno_a, serialno_b, macaddress_a, macaddress_b, hardware, hardware_full, software, software_full, ... yes `software` exists.

Hmm, but actually I recall in Zabbix 7.4 they may have renamed some fields? The 7.4 doc I read shows `software` (id 16). And there's no `sw` field. Fine.

So the invalid fields in the code:
1. `serial` → should be `serialno_a`
2. `macaddress` → should be `macaddress_a`
3. `device` → does not exist; `product_type` should map to an existing field like `model` or `type_full` or `hardware`

`software` and `notes`, `type`, `name` are valid.

Also worth checking: does `host.create` reject unknown inventory properties with an error? Yes — Zabbix API validates inventory properties and returns "Invalid parameter: unexpected object ...". Actually for unknown inventory keys it returns something like `Invalid parameter "/1/inventory/serial": unexpected parameter name.` So the create would fail.

Let me also check discovery.py or other files for other API calls with inventory fields. Let me grep the project for inventory usage.

Also check if there's an `inventory` usage elsewhere (e.g., in discovery.py building device dicts). The `dev` fields come from discovery; `_desired_inventory` maps them.

Now, what should `product_type` map to? Options: `model` (Model, 64 chars), `hardware` (Hardware, 255 chars), `type_full` (Type details, 64 chars). Semantically "product_type" is the product type/model. I'd map to `model`. Hmm, but `type` is already used for dev["type"] (device category like "plc", "hmi"). `type_full` would be "Type details" — good for product type. Or `model`.Zabbix inventory semantics:
- type: Device type (e.g., "Router")
- type_full: Type details
- model: Model
- hardware: Hardware
- vendor: Vendor

`product_type` from discovery — e.g., Siemens S7-1200 → this is the product/model. I'd map to `model`. And firmware → `software` is fine (Software field exists).

Actually wait — let me reconsider. Maybe better to keep it minimal and just fix the invalid names:
- `serial` → `serialno_a`
- `macaddress` → `macaddress_a`
- `device` → `model` (or `type_full`)

Let me check what discovery.py provides to understand the data better. Let me grep for product_type and firmware in discovery.py.

Also I should check README/config to understand context. Let me grep.

Also, there's a second consideration: the `_inventory_equal` comparison compares desired keys against `current["inventory"]` returned by `selectInventory: extend`. The returned inventory includes all fields (or only non-empty ones?). With selectInventory extend, Zabbix returns all inventory fields including empty ones ("" for unset? Actually it returns only fields with values? Let me recall: selectInventory returns the inventory object with all properties, empty strings for unset ones I believe). Either way, after fixing field names, comparison works since existing.get(k) matches.

But note: if the API previously failed on create with invalid fields, maybe the user saw errors. Also for update: host.update with invalid inventory field names also fails.

Let me also check whether there might be other API misuse: the interface port "10051" — for agent interfaces the default port is 10050;10051 is the server port. But interfaces on a host are agent ports (10050). They use trapper sender though (zabbix_sender sends to server port 10051 directly, bypassing host interface). The host interface port is used for active/passive agent checks — 10051 would be wrong for agent checks, but templates might use Zabbix agent items... Actually the user only asked about inventory parameters. I'll mention only if relevant... The user asked specifically about inventory params. I should stay focused: fix inventory fields. Maybe briefly note port 10051 if templates use agent items — but that's out of scope; keep focused.

Let me look at discovery.py to see the device fields available (product_type, firmware, serial, mac, etc.) to make sure mapping is right.

**Tool: bash**

**Input:**
```json
{
  "command": "Get-ChildItem -Recurse -File | Where-Object { $_.Extension -in \".py\",\".yaml\",\".example\",\".md\" } | Select-String -Pattern \"product_type|firmware|serial|macaddress|inventory\" | ForEach-Object { $_.Path.Replace((Get-Location).Path + [IO.Path]::DirectorySeparatorChar, \"\") + \":\" + $_.LineNumber + \": \" + $_.Line.Trim() }"
}
```

**Output:**
```
config.yaml.example:44: # Siemens: SZL via porta 102 (module, version, serial, system name)
discovery.py:85: "product_type": "",
discovery.py:86: "firmware": "",
discovery.py:87: "serial": "",
discovery.py:117: "product_type": str(getattr(dev, "family", "") or ""),
discovery.py:118: "firmware": "",
discovery.py:119: "serial": "",
discovery.py:147: firmware = f"{rev.get('major', 0)}.{rev.get('minor', 0)}"
discovery.py:149: firmware = str(rev)
discovery.py:159: "product_type": str(device.get("product_type") or ""),
discovery.py:160: "firmware": firmware,
discovery.py:161: "serial": str(device.get("serial") or ""),
mac_vendors_db.py:5639: "000620":"Serial System Ltd.",
mac_vendors_db.py:27673: "64E84F":"Serialway Communication Technology Co. Ltd",
mac_vendors_db.py:30019: "00A05C":"INVENTORY CONVERSION, INC./",
mac_vendors_db.py:36317: "0021E3":"SerialTek LLC",
readers.py:12: """SZL S7: module, version, serial, system name. Restituisce dict (vuoto se fallisce)."""
readers.py:22: "firmware": data.get("Version", ""),
readers.py:23: "serial": data.get("Serial Number", ""),
readers.py:24: "product_type": data.get("Module") or data.get("Module Type", ""),
readers.py:30: """LogixDriver.info: keyswitch/mode, nome PLC, revision, serial.
readers.py:45: "firmware": str(rev),
readers.py:46: "serial": str(info.get("serial", "") or ""),
readers.py:47: "product_type": str(info.get("device_type") or info.get("product_type") or ""),
README.md:20: - **Siemens**: SZL porta 102 (`s7_info.py`)  firmware, serial, modulo  inventario host
README.md:30: tag `line:`, `type:`, `vendor:`, `protocol:`, `mac:`; inventario (serial, mac, firmware...)
s7_info.py:133: "Serial Number": 175 + offset,
s7_info.py:180: # Step 5: Second SZL request (system name, serial, etc.)
zabbix_api.py:76: "selectInventory": "extend",
zabbix_api.py:95: def _desired_inventory(dev):
zabbix_api.py:99: if dev.get("serial"):
zabbix_api.py:100: inv["serial"] = dev["serial"]
zabbix_api.py:102: inv["macaddress"] = dev["mac"]
zabbix_api.py:103: if dev.get("product_type"):
zabbix_api.py:104: inv["device"] = dev["product_type"]
zabbix_api.py:105: if dev.get("firmware"):
zabbix_api.py:106: inv["software"] = dev["firmware"]
zabbix_api.py:123: def _inventory_equal(existing, desired):
zabbix_api.py:161: inventory = self._desired_inventory(dev)
zabbix_api.py:177: "inventory_mode": 0,
zabbix_api.py:178: "inventory": inventory,
zabbix_api.py:205: if not self._inventory_equal(current.get("inventory"), inventory):
zabbix_api.py:206: update["inventory"] = inventory
zabbix_api.py:207: update["inventory_mode"] = 0
zabbix_api.py:208: fields.append("inventory")

```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 45.9s)

_Thinking:_

Confirmed the invalid fields in `_desired_inventory` (zabbix_api.py:95-114):

- `serial` → INVALID, should be `serialno_a`
- `macaddress` → INVALID, should be `macaddress_a`
- `device` → INVALID, does not exist. `product_type` → should map to `model` or `type_full`
- `software` → VALID per 7.4 docs (Software, 255 chars). Code maps firmware → software. Valid.
- `type` → VALID
- `name` → VALID
- `notes` → VALID

Wait — I should double check `software` in Zabbix 7.0 since the docstring says "Client Zabbix 7.0". In7.4, `software` exists (ID 16). In older versions (6.0), the field was `software`? Let me check the 7.0 docs quickly. Actually, historically in Zabbix the inventory field names in the API have been: `sw` was never an API name I think. Let me verify quickly with the 7.0 host object docs — but fetching costs a lot of context (huge nav).

Actually, from my knowledge: Zabbix 5.0/6.0/7.0 host inventory API fields: type, type_full, name, alias, os, os_full, os_short, serialno_a, serialno_b, macaddress_a, macaddress_b, hardware, hardware_full, software, software_full, software_app_a..e, ... — yes `software` has existed for a long time (the UI label "Software"). Hmm, actually wait. In the Zabbix UI, inventory fields are labeled: "Type", "Type details", "Name", "Alias", "OS", "OS details", "OS short name", "Serial number A", "Serial number B", "MAC address A", "MAC address B", "Hardware", "Hardware details", "Software", "Software details", "Software application A-E", ... Yes, `software` is a long-standing field.

Hmm, but actually I want to double check: in some versions the API doc listed them with escaped underscores like `software`. Yes.

But wait — the user said "richiama dei parametri di inventario che non esistono" (it calls inventory parameters that don't exist). Plural. So `serial`, `macaddress`, `device` are the three invalid ones. `software` is valid.

Let me also verify `notes` — yes, valid (Notes,65535 chars).

Now, mapping decisions:
1. `serial` → `serialno_a` (Serial number A)
2. `macaddress` → `macaddress_a` (MAC address A)
3. `device` (from product_type) → options: `model`, `hardware`, `type_full`. 

`product_type` from Siemens SZL is "Module" type e.g. "6ES7 214-1AG40-0XB0" or module name; from Logix is `device_type`. "Model" fits best semantically for product type. `type_full` = "Type details" also plausible. I'll use `model` — it's the product model/type.

Actually, let me think about which is most appropriate:
- `type`: Device type (code already uses dev["type"] = device category e.g. "plc")
- `type_full`: Type details — could hold product_type
- `model`: Model — product_type like "S7-1200" or "1769-L32E"

`model` seems right for product_type.

Also `firmware` → `software`: valid. Could also be `software_full` or `os`... but `software` (Software, 255 chars) is fine and valid.

Hmm, one consideration: firmware is more like software version — `software` works.

Also note: maximum lengths — serialno_a 64, macaddress_a 64, model 64, software 255, name 128, notes 65535, type 64. Values from discovery should fit.

Also the `_inventory_equal` comparison: `current.get("inventory")` from selectInventory extend returns dict with all fields (including empty strings for unset? Actually Zabbix returns only non-empty inventory fields? Let me recall — selectInventory returns the full inventory object with empty strings for fields not set? I believe it returns all fields, with empty string for unset ones... Actually no: Zabbix's selectInventory returns inventory fields with their values; empty fields are included as ""? Hmm.

From experience: `"inventory": {"type": "", "name": "", ...}` — actually when selectInventory=extend, Zabbix returns all inventory properties, empty ones as empty string? Let me think... I recall that host.get with selectInventory returns an object containing only the fields that have values? No — I'm fairly sure it returns all fields with empty strings for unset. Hmm, actually I've seen responses where only non-empty fields are returned... 

It doesn't matter much for correctness of the fix: `_inventory_equal` does `existing.get(k, "")` so if field is missing it compares "" == value → update triggered if desired non-empty. Fine either way.

One more thing: the docstring says "Client Zabbix 7.0" but user linked7.4. The fix applies to both.

Now also check `main.py` and others for any other API calls with inventory? The grep showed only zabbix_api.py. Also check `host.create` params validity overall:
- host, name, groups, interfaces, templates, tags, inventory_mode, inventory — all valid per host.create docs.

Interface: type 1 (agent), main 1, useip 1, ip, dns "", port "10051" — valid params. Port 10051 is unusual for an agent interface (default 10050), but that's not what the user asked about. I might mention it briefly? The user asked specifically about inventory params. Keep focused, but a one-line note could be useful... The instructions say avoid tangents. I'll mention only if relevant — actually templates in this project likely use Zabbix agent items or trapper items. Let me check the templates quickly to see if port matters. Actually let's not go down that path — the user asked specifically about inventory. But if templates use agent items with default port, interface port 10051 would break agent checks... Let me do a quick check of templates folder to be thorough about API errors — no wait, port isn't an API error; the API accepts any port. Focus on inventory.

Also, should I check `type` field length64 — dev["type"] is like "plc"/"hmi" — fine.

Now make the edit to `_desired_inventory`:

```python
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
    notes = []
    ...
```

Wait — also check `dev.get("name")` → inventory "name" (Name, 128 chars) valid. But note: there's also host "name" (visible name) — inventory name is device name, fine.

Also, is there a `vendor` field in inventory? Yes — `vendor` exists (id 31). The code puts vendor in notes instead. Could map vendor → inv["vendor"], but that's an enhancement, not a bug fix. Keep minimal — just fix non-existent fields. Actually, hmm — would it be better? The user asked to fix the error of non-existent params. Minimal fix: rename invalid keys. I'll do that.

Let me also double check whether `software` exists in Zabbix 7.0 docs (since client targets 7.0). To be safe, let me fetch the 7.0 host object page... that's another huge output. Alternatively use the API changes appendix. Actually, I'm quite confident `software` has existed since ancient versions (1.8 even). The field IDs: software=10, hardware=11 — these have been stable. I'll skip the extra fetch.

Hmm, actually wait. Let me reconsider `device` — is there really no `device` inventory field? From the full list I read: alias, asset_tag, chassis, contact, contract_number, date_hw_decomm, date_hw_expiry, date_hw_install, date_hw_purchase, deployment_status, hardware, hardware_full, host_netmask, host_networks, host_router, hw_arch, installer_name, location, location_lat, location_lon, macaddress_a, macaddress_b, model, name, notes, oob_ip, oob_netmask, oob_router, os, os_full, os_short, poc_1_*, poc_2_*, serialno_a, serialno_b, site_*, software, software_app_*, software_full, tag, type, type_full, url_a/b/c, vendor.

No `device`, no `serial`, no `macaddress`. Confirmed.

Also check: does `host.update` accept the same inventory property names? Yes, same Host object.

Also — one more potential issue: in `sync()`, for existing hosts, `current.get("inventory")` — with selectInventory extend, keys are the valid names. After the fix, `_inventory_equal` compares desired (valid names) against existing — good. Before the fix, existing would never contain "serial"/"macaddress"/"device" so it would keep trying to update every cycle with invalid params → API error each time. That matches the user's report.

Let me now make the edit. Also update the README mention? README line 30 says "inventario (serial, mac, firmware...)" — that's describing device fields generically, not API fields. Line 20: "firmware, serial, modulo → inventario host". These are conceptual, fine to leave.

Docstring says Zabbix 7.0 — user linked 7.4. Not an issue.

Should I run any tests? No test suite visible. requirements.txt, no tests. I could do a quick python syntax check: `python -m py_compile zabbix_api.py`.

Let me make the edit.

Confermato. Ho confrontato i campi usati in `zabbix_api.py:95-114` con la lista ufficiale dei campi inventory dell'host object (Zabbix 7.4):

| Usato nel codice | Esiste? | Campo corretto |
|---|---|---|
| `type` | ✅ | — |
| `name` | ✅ | — |
| `serial` | ❌ | `serialno_a` |
| `macaddress` | ❌ | `macaddress_a` |
| `device` | ❌ | `model` |
| `software` | ✅ | — |
| `notes` | ✅ | — |

Correggo:

**Tool: edit**

**Input:**
```json
{
  "filePath": "C:\\Users\\f.manghi\\Desktop\\Tools\\GITHUB\\OT_Line_Zabbix\\zabbix_api.py",
  "oldString": "        if dev.get(\"serial\"):\n            inv[\"serial\"] = dev[\"serial\"]\n        if dev.get(\"mac\"):\n            inv[\"macaddress\"] = dev[\"mac\"]\n        if dev.get(\"product_type\"):\n            inv[\"device\"] = dev[\"product_type\"]",
  "newString": "        if dev.get(\"serial\"):\n            inv[\"serialno_a\"] = dev[\"serial\"]\n        if dev.get(\"mac\"):\n            inv[\"macaddress_a\"] = dev[\"mac\"]\n        if dev.get(\"product_type\"):\n            inv[\"model\"] = dev[\"product_type\"]"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 6.8s)

_Thinking:_

Let me verify the syntax compiles.

**Tool: bash**

**Input:**
```json
{
  "command": "python -m py_compile zabbix_api.py && echo OK"
}
```

**Output:**
```
OK

```

---

## Assistant (Build · MiMo-V2.6-Flash Free · 6.3s)

_Thinking:_

The fix is applied. Let me summarize concisely in Italian (the user writes in Italian).

Corretto in `zabbix_api.py:99-104`. La funzione `_desired_inventory` inviava 3 chiavi inventario inesistenti, causa dell'errore API su `host.create`/`host.update`:

- `serial` → `serialno_a` (Serial number A)
- `macaddress` → `macaddress_a` (MAC address A)
- `device` → `model` (Model)

`type`, `name`, `software` e `notes` erano già validi. Effetto collaterale positivo: prima del fix l'host veniva ricreato/aggiornato a ogni ciclo con campi non validi; ora il confronto `_inventory_equal` funziona anche contro `selectInventory` restituito da `host.get`.

---