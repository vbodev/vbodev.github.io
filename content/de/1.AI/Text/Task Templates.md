---
title: "Task Templates"
tags: [ai, text, prompt, templates]
---
[[ru/1.AI/Text/Task Templates|RU]] | [[en/1.AI/Text/Task Templates|EN]] | [[de/1.AI/Text/Task Templates|DE]]

## 1. Beispiel: Blogartikel schreiben 

```markdown
# Aufgabe: Blogartikel schreiben

## Thema
Wie man ChatGPT zur Automatisierung von Entwickleraufgaben nutzt

## Zielgruppe
Entwickler auf Junior- und Middle-Level

## Umfang
1000–1200 Wörter

## Struktur
1. Einleitung
2. Beispiele für die Verwendung von ChatGPT in der täglichen Entwicklung
3. Integration mit VS Code / Postman / n8n
4. Potenzielle Fehler und Einschränkungen
5. Fazit und Tipps

## Stil
Halbformal, mit Codebeispielen, Humor und freundlichem Ton

## Zusätzlich
Erwähne die Möglichkeiten von ChatGPT-4 und ChatGPT in der Desktop-Anwendung

```
## 2. Beispiel: Python-Code generieren

```Markdown
# Aufgabe: Python-Code für Datenanalyse generieren

## Ziel
Ein Python-Skript erstellen, das eine CSV-Datei liest, Daten analysiert (Durchschnitt, Median, Standardabweichung) und ein Verteilungsdiagramm erstellt.

## Eingangsdaten
- CSV-Datei mit einer Spalte numerischer Werte.
- Dateiname: `data.csv`
- Spaltenname: `value`

## Ausgabe
- Statistische Metriken: Durchschnitt, Median, Standardabweichung
- Gespeichertes Diagramm: `histogram.png`

## Anforderungen
- Bibliotheken verwenden: pandas, matplotlib
- Code sollte klar sein und Kommentare enthalten

## Zusätzlich
- Erstelle ein Histogramm mit 20 Bins

```
## 3. Beispiel: Bild generieren

```markdown
# Aufgabe: Bild generieren

## Bildtyp
Fantastisches Porträt eines Mädchens im Cyberpunk-Stil

## Beschreibung
- Junges Mädchen mit violetten Haaren
- Neonlichter, Nachtstadt im Hintergrund
- Cyber-Brille und metallischer Kragen
- Emotion: Selbstvertrauen und Unabhängigkeit

## Größe
1024x1024 Pixel

## Stil
Realistisch + etwas Anime

## Zusätzlich
Hintergrund sollte leicht verschwommen sein, Hauptfokus – auf dem Gesicht

```
## 4. Beispiel: Spezifikation: Landing Page für IT-Unternehmen

```markdown
# Spezifikation: Landing Page für IT-Unternehmen

## Firmenname
NextGenSoft

## Ziel
Kundenakquise für Softwareentwicklungsdienstleistungen

## Website-Blöcke
- Header mit Logo und Navigation
- Haupt-Banner (mit Slogan und Button)
- Dienstleistungen (3 Karten)
- Über das Unternehmen (Text + Foto)
- Kontaktformular
- Footer mit Kontakten

## Design
- Farben: Blau, Weiß, Grau
- Stil: Minimalismus, serifenlose Schriftarten

## Responsivität
Ja (Mobile- und Desktop-Versionen)

## Technologien
HTML, CSS (Tailwind oder Bootstrap), JS (Vanilla)

## Frist
1 Woche
```
## 5. Aufgaben-Vorlage
````markdown
# 📌 Aufgabenname
[FÜGE_KURZE_AUFGABENBESCHREIBUNG_EIN]

---

## 🎯 Ziel
[BESCHREIBE_WARUM_DIESE_AUFGABE_BENÖTIGT_WIRD_UND_DAS_ERWARTETE_ERGEBNIS]

---

## 🧱 Projektkontext
- Sprache: [Delphi / Python / Java / andere]
- IDE / Framework: [RAD Studio / PyCharm / n8n / andere]
- Haupttechnologien: [Virtual TreeView, SQLLite, REST API, JSON usw.]
- Modulname (falls vorhanden): [DATEINAME.pas]

---

## 📂 Struktur/Dateien, in denen gearbeitet werden soll
- `PFAD_ZUR_DATEI_1`
- `PFAD_ZUR_DATEI_2`

---

## 🛠️ Was implementiert werden soll
1. [WAS_ZU_TUN_IST_1]
2. [WAS_ZU_TUN_IST_2]
3. [WAS_ZU_TUN_IST_3]

---

## ✅ Anforderungen
- [ANFORDERUNG_1]
- [ANFORDERUNG_2]
- [ANFORDERUNG_3]

---

## 📈 Erwartetes Ergebnis
- [ERWARTETES_ERGEBNIS_1]
- [ERWARTETES_ERGEBNIS_2]

---

## 🧪 Testdaten (falls vorhanden)
```pascal
// Beispiel in Delphi
Task := TTaskNode.Create;
Task.Typ := 'Document';
Task.Status := 'In Progress';
```

---

## ✨ Zusätzlich
- Alternative vorschlagen: [Ja / Nein]
- Code-Dokumentation benötigt: [Ja / Nein]
- Verwendungsbeispiel: [Ja / Nein]

---

## 💬 Antwortformat von ChatGPT
- Vollständiger Quellcode
- Beschreibung der Schritte und Logik
- Zusätzlich: generiertes Verwendungsbeispiel (falls erforderlich)
````

## 6. Python-Aufgaben-Vorlage

````markdown
# 🐍 Python-Aufgabe

## 📌 Aufgabenname
[BEISPIEL: CSV-Analyse und Datenvisualisierung]

## 🎯 Ziel
[Beschreibe, warum das Skript geschrieben wird und wie das Ergebnis verwendet wird]

## 📚 Kontext
- Sprache: Python
- Version: [3.10+]
- Verwendete Bibliotheken: [pandas, matplotlib, requests usw.]
- Wo wird es ausgeführt: [lokal / Server / Jupyter Notebook]

## 🛠 Was implementiert werden soll
1. [CSV-Datei lesen]
2. [Verteilungsdiagramm erstellen]
3. [Ergebnis in Datei speichern]

## ✅ Anforderungen
- [Code mit Kommentaren]
- [Fehlerbehandlung]
- [Eingabe-/Ausgabeformat muss angegeben werden]

## 🔍 Beispiel Eingangsdaten
```csv
value
12
34
23
...
```

## 📤 Beispiel Ausgangsdaten
- Durchschnitt: 23.1
- Diagramm: `histogram.png`

## 💬 Antwortformat von ChatGPT
- Vollständiger Code
- Erklärung der Logik
````

## 7. Java-Aufgaben-Vorlage

````markdown
# ☕ Java-Aufgabe

## 📌 Aufgabenname
[BEISPIEL: JSON-Verarbeitung aus REST-API]

## 🎯 Ziel
[Beschreibe, warum das Programm geschrieben wird und wie es verwendet wird]

## 📚 Kontext
- Sprache: Java
- Version: [Java 11+]
- Verwendete Bibliotheken: [Jackson, HttpClient, Spring usw.]
- IDE: [IntelliJ IDEA / Eclipse / VS Code]

## 🛠 Was implementiert werden soll
1. [HTTP-GET-Anfrage an API durchführen]
2. [JSON parsen]
3. [Daten in Konsole oder GUI ausgeben]

## ✅ Anforderungen
- [Fehlerbehandlung]
- [Code sollte lesbar und strukturiert sein]
- [Maven/Gradle-Unterstützung (falls erforderlich)]

## 🔍 Beispiel API-Antwort
```json
{
  "user": "Vitaliy",
  "active": true
}
```

## 📤 Beispiel erwartete Ausgabe
```
Benutzer: Vitaliy
Status: aktiv
```

## 💬 Antwortformat von ChatGPT
- Vollständiger Quellcode
- Schritt-für-Schritt-Erklärung
````

