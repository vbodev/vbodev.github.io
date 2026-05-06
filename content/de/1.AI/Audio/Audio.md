---
title: "Audio"
tags: [ai, audio, python, whisper]
---
[[ru/1.AI/Audio/Audio|RU]] | [[en/1.AI/Audio/Audio|EN]] | [[de/1.AI/Audio/Audio|DE]]

## 🧠 1. **OpenAI Whisper (Original)**

**Sprache:** Python  
**Entwickler:** OpenAI  
**Architektur:** Transformer-basiertes Modell (tiny → large-v3)  
**Link:** [openai/whisper](https://github.com/openai/whisper)  
### 💡 Besonderheiten

- Dies ist die **Referenzimplementierung**, auf der alle anderen Versionen basieren.   
- Sehr **genau**, besonders bei den Modellen `medium` und `large`.
- Unterstützt **über 100 Sprachen**, einschließlich Ukrainisch und Russisch.
- Funktioniert über `ffmpeg` und erfordert eine vorab aufgenommene Datei (kein Streaming).
- **Keine eingebaute Speaker-Diarisierung** (Speaker Diarization muss separat hinzugefügt werden, z.B. über `pyannote.audio`).
### ⚙️ Leistung

- **Langsame Inferenz**: selbst auf GPU nicht ideal für Echtzeit.
- Verwendet **FP32 (float32)**, kann mit FP16 auf GPU beschleunigt werden.
- Funktioniert auf CPU, aber langsam.

## ⚡ 2. **whisper.cpp**

**Sprache:** C++ (mit Python-Bindings)  
**Entwickler:** Georgi Gerganov  
**Ziel:** Schnelle und leichtgewichtige Ausführung von Whisper ohne Python-Abhängigkeiten  
**Link:** [whisper.cpp](https://github.com/ggml-org/whisper.cpp)  
### 💡 Besonderheiten

- Komplett in **C++** neu geschrieben mit **Quantisierung (int8/int4)** – dies beschleunigt die Verarbeitung radikal.
- **Kann in Echtzeit ausgeführt werden** sogar auf CPU (einschließlich Raspberry Pi und ESP32-ähnliche Geräte).
- Hat **Streaming-API** – Audio kann in Stücken zugeführt werden und liefert Teilergebnisse.
- Unterstützung für **GPU (CUDA, Metal, OpenCL)** hinzugefügt, aber nicht immer stabil.
- **Keine eingebaute Speaker-Diarisierung**, nur Text.
### ⚙️ Leistung

- **Sehr schnell**, besonders im `int8`-Modus.
- Ideal für **Echtzeit**, besonders wenn Speaker unwichtig sind.
- Kann direkt in C++-Anwendungen eingebettet werden, ohne Python.

## 🚀 3. **Faster Whisper**

**Sprache:** Python  
**Entwickler:** Guillaume Klein (basierend auf Whisper + CTranslate2)  
**Architektur:** CTranslate2 – Hochleistungs-Inferenz-Engine auf C++  
**Link:** [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)  
### 💡 Besonderheiten

- Vollständig kompatibel mit OpenAI Whisper, aber:
    - Verwendet **CTranslate2**, daher 2–5× schneller als das Original.
    - Unterstützt **FP16 und INT8**, läuft hervorragend auf GPU und CPU.
- Unterstützt **Streaming-Inferenz (Echtzeit)**.
- Kann **Batch-Processing** verwenden (beschleunigt bei der Verarbeitung langer Aufnahmen).
- **Unterstützt Integration mit Diarisierung** (über `pyannote.audio`).
### ⚙️ Leistung

- **2–4× schneller als das Original** auf CPU und GPU.
- Gut geeignet für **Echtzeit**, besonders mit GPU.
- Geringerer Speicherverbrauch.
- Einfach in Python-Systeme zu integrieren (Flask, FastAPI usw.).

## 🔊 4. **WhisperX**

**Sprache:** Python  
**Entwickler:** Max Bain (University of Oxford)  
**Ziel:** Erweiterung von Whisper für genaue **Diarisierung und Alignment**  
**Link:** [WhisperX](https://github.com/m-bain/whisperX)  
### 💡 Besonderheiten

- Verwendet **Faster Whisper** für Transkription.
- Fügt hinzu:
    - **Speaker Diarization** (über `pyannote.audio`)
    - **Phoneme-Level Alignment** (genaue Synchronisation von Wörtern mit Zeitstempeln)
- Kann GPU für die gesamte Pipeline nutzen.
- Unterstützt **mehrsprachige Modelle** und erkennt Sprache automatisch.
- Kann **lange Aufnahmen** verarbeiten und die Struktur „wer wann gesprochen hat" liefern.
### ⚙️ Leistung

- Etwas langsamer als Faster Whisper (wegen zusätzlicher Schritte), aber **viel funktionaler**.
- Nicht ideal für Echtzeit (arbeitet normalerweise mit Chunks von 15–30 Sek.).
- Jedoch kann „fast Echtzeit" erreicht werden, wenn kurze Audio-Puffer verarbeitet werden.

## **📊 Vergleichstabelle**

| Merkmal                         | **OpenAI Whisper** | **whisper.cpp**          | **Faster Whisper**           | **WhisperX**               |
| ------------------------------- | ------------------ | ------------------------ | ---------------------------- | -------------------------- |
| **Sprache**                     | Python             | C++ (Python-Bindings)    | Python                       | Python                     |
| **Geschwindigkeit**             | ❌ Langsam          | ✅✅ Sehr schnell          | ✅ Schnell                    | ⚙️ Mittel                  |
| **Genauigkeit**                 | ✅✅ Ausgezeichnet   | ✅ Gut                    | ✅✅ Ausgezeichnet             | ✅✅ Ausgezeichnet           |
| **Echtzeit (Streaming)**        | ❌ Nein             | ✅ Ja                     | ✅ Ja                         | ⚙️ Teilweise               |
| **GPU-Unterstützung**           | ✅ Ja               | ⚙️ Teilweise             | ✅ Ja (CUDA/OpenVINO)         | ✅ Ja                       |
| **CPU-Unterstützung**           | ⚙️ Ja, aber langsam | ✅ Ausgezeichnet          | ✅ Ja (mit Quantisierung)     | ✅ Ja                       |
| **Speaker Diarization**         | ❌ Nein             | ❌ Nein                   | ⚙️ Über pyannote             | ✅ Eingebaut                |
| **Alignment**                   | ❌ Nein             | ❌ Nein                   | ❌ Nein                       | ✅ Ja                       |
| **Speicherverbrauch**           | 🧱 Hoch            | 🪶 Niedrig               | ⚖️ Mittel                    | 🧱 Hoch                    |
| **Einfache Integration**        | ✅ Einfach          | ⚙️ Benötigt Kompilierung | ✅ Einfach                    | ⚙️ Mittel                  |
| **Optimal für**                 | Genauigkeit        | Echtzeit auf CPU         | Echtzeit + Genauigkeit       | Multi-Speaker-Dialoge      |
