---
title: Tools
---
[[Tools|RU]] | [[en/Administration/4.Tools/Tools|EN]] | [[de/Administration/4.Tools/Tools|DE]]

## NextCloud

Nextcloud ist eine **selbst gehostete (self-hosted) Plattform** für Dateispeicherung und Zusammenarbeit, ähnlich wie Google Drive/Dropbox, aber **unter deiner Kontrolle**.
Was sie typischerweise umfasst:
- **Dateien und Ordner**: Hochladen, Synchronisieren, Teilen über Links und Zugriffsrechte.
- **Kalender, Kontakte, Aufgaben** (über Apps).
- **Gemeinsame Dokumentenbearbeitung** (Integrationen mit OnlyOffice/Collabora).
- **Zugriff vom PC und Telefon**: Web-Interface + Clients für Windows/Linux/macOS/Android/iOS.
- **Sicherheit und Verwaltung**: Benutzer/Gruppen, Rechte, Audit, Verschlüsselung (je nach Konfiguration), 2FA.
Kernidee: **Deine eigene "Cloud" auf deinem Server/VPS/Zuhause**, wo die Daten bei dir bleiben und nicht bei einem öffentlichen Anbieter.
## Opnsense

OPNsense ist eine **Open-Source-Firewall und Router** (FreeBSD-basiert), die auf einem Server/Mini-PC oder einer virtuellen Maschine installiert wird, um das Netzwerk zu verwalten.
Hauptfunktionen:
- **Firewall/NAT**, Routing, VLAN
- **VPN** (IPsec, OpenVPN, WireGuard)
- **IDS/IPS** (Angriffserkennung/-prävention), Verkehrsfilterung
- **Web-Interface** zur Konfiguration, Protokolle und Monitoring
Kurz: OPNsense ist ein "intelligentes Netzwerk-Gateway" für zuhause oder das Büro, eine Alternative zu pfSense und kommerziellen UTM-Lösungen.
## Puppet

Puppet ist ein Tool für **Konfigurationsmanagement und Automatisierung** (Infrastructure as Code), das es ermöglicht, **den Zustand von Servern zentral zu definieren**: welche Pakete installiert sind, welche Dienste laufen, welche Konfigurationen vorhanden sein sollen und mit welchen Berechtigungen.
Kurz: Du beschreibst "wie es sein soll", und Puppet bringt Maschinen regelmäßig in diesen Zustand und sorgt für Einheitlichkeit in der Infrastruktur.
## Wazuh

Wazuh ist eine Open-Source-Cybersicherheitsplattform für Host- und Ereignisüberwachung (im Wesentlichen HIDS/XDR + SIEM-Funktionen): Es sammelt und analysiert Logs von Servern und Workstations, erkennt Bedrohungen und verdächtige Aktivitäten, überwacht die Dateiintegrität (FIM), sucht nach Schwachstellen und hilft bei der Compliance-Erfüllung.
Typischerweise wird es als Agenten auf Hosts plus zentralem Server mit Dashboard und Alerts eingesetzt.
## Zabbix

Zabbix ist eine Open-Source-Lösung für verteiltes Monitoring auf Enterprise-Niveau.

Zabbix ist eine Software zur Überwachung zahlreicher Netzwerkparameter, der Verfügbarkeit und Integrität von Servern, virtuellen Maschinen, Anwendungen, Diensten, Datenbanken, Websites, Cloud-Umgebungen und vielem mehr. Zabbix verwendet einen flexiblen Benachrichtigungsmechanismus, mit dem Benutzer E-Mail-basierte Benachrichtigungen für nahezu jedes Ereignis konfigurieren können. Dies ermöglicht eine schnelle Reaktion auf Serverprobleme. Zabbix bietet hervorragende Reporting- und Datenvisualisierungsfunktionen auf Basis historischer Daten. Damit ist Zabbix ideal für die Kapazitätsplanung.

Zabbix unterstützt sowohl Poller als auch Trapper. Alle Zabbix-Reports und Statistiken sowie Konfigurationsparameter sind über das Web-Interface zugänglich. Das Web-Interface ermöglicht den Zugriff auf den Zustand deines Netzwerks und die Verfügbarkeit deiner Server von überall. Richtig konfiguriert kann Zabbix eine wichtige Rolle im Monitoring der IT-Infrastruktur spielen. Das gilt sowohl für kleine Organisationen mit wenigen Servern als auch für große Organisationen mit vielen Servern.

Zabbix ist kostenlos. Zabbix ist unter der AGPL-3.0-Lizenz geschrieben und vertrieben. Das bedeutet, dass sein Quellcode frei verteilt und einem unbegrenzten Personenkreis zugänglich ist.
