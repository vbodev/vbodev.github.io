---
title: Tools
---
[[Tools|RU]] | [[en/Administration/4.Tools/Tools|EN]] | [[de/Administration/4.Tools/Tools|DE]]

## NextCloud

Nextcloud is a **self-hosted platform** for file storage and collaboration, similar to Google Drive/Dropbox, but **under your control**.
What it typically includes:
- **Files and folders**: uploading, syncing, sharing via links and access rights.
- **Calendar, contacts, tasks** (via apps).
- **Collaborative document editing** (integrations with OnlyOffice/Collabora).
- **Access from PC and phone**: web interface + clients for Windows/Linux/macOS/Android/iOS.
- **Security and management**: users/groups, permissions, audit, encryption (depending on configuration), 2FA.
The key idea: **your own "cloud server"** on your server/VPS/home, where data stays with you, not with a public provider.
## Opnsense

OPNsense is an **open-source firewall and router** (FreeBSD-based), installed on a server/mini-PC or virtual machine to manage the network.
Key capabilities:
- **Firewall/NAT**, routing, VLAN
- **VPN** (IPsec, OpenVPN, WireGuard)
- **IDS/IPS** (attack detection/prevention), traffic filtering
- **Web interface** for configuration, logs, and monitoring
Simply put: OPNsense is a "smart network gateway" for home or office — an alternative to pfSense and commercial UTM solutions.
## Puppet

Puppet is a **configuration management and automation** tool (Infrastructure as Code) that allows you to **centrally define the state of servers**: which packages are installed, which services are running, what configs should exist and with what permissions.
Simply: you describe "how it should be", and Puppet regularly brings machines to that state and maintains uniformity across the infrastructure.
## Wazuh

Wazuh is an open-source cybersecurity platform for host and event monitoring (essentially HIDS/XDR + SIEM functions): it collects and analyzes logs from servers and workstations, detects threats and suspicious activity, monitors file integrity (FIM), searches for vulnerabilities, and helps with compliance.
Typically deployed as agents on hosts plus a central server with dashboard and alerts.
## Zabbix

Zabbix is an open-source distributed enterprise-class monitoring solution.

Zabbix is software for monitoring numerous network parameters, the health and integrity of servers, virtual machines, applications, services, databases, websites, cloud environments, and much more. Zabbix uses a flexible notification mechanism that allows users to configure email-based notification for virtually any event. This allows quick reaction to server problems. Zabbix offers excellent reporting and data visualization features based on historical data. This makes Zabbix ideal for capacity planning.

Zabbix supports both pollers and trappers. All Zabbix reports and statistics, as well as configuration parameters, are accessible via the web interface. The web interface enables access to the state of your network and the health of your servers from anywhere. Properly configured, Zabbix can play an important role in monitoring the IT infrastructure. This is true both for small organizations with a few servers and large organizations with many servers.

Zabbix is free. Zabbix is written and distributed under the AGPL-3.0 license. This means its source code is freely distributed and available to an unlimited number of people.
