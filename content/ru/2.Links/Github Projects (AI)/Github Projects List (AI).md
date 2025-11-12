---
title: Github Projects List (AI)
---

#git #github #projects

## 1. LLM / Agent infrastructure

Инструменты и фреймворки для запуска, оркестрации и эксплуатации LLM/агентов — базовый слой для приложений на больших моделях.

| Название                | Ссылка                                                                                       | Коротко                                                      |
| ----------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| LocalAI                 | [github.com/mudler/LocalAI](https://github.com/mudler/LocalAI)                               | Self-hosted LLM-инфраструктура, drop-in замена облачным API. |
| Litgpt                  | [github.com/Lightning-AI/litgpt](https://github.com/Lightning-AI/litgpt)                     | Коллекция инструментов и примеров работы с LLM.              |
| Letta (MemGPT)          | [github.com/letta-ai/letta](https://github.com/letta-ai/letta)                               | Фреймворк для сервисов на LLM с поддержкой памяти.           |
| OpenAI Realtime Agents  | [github.com/openai/openai-realtime-agents](https://github.com/openai/openai-realtime-agents) | Демонстрация агентов поверх Realtime API.                    |
| Golf-mcp                | [github.com/golf-mcp/golf](https://github.com/golf-mcp/golf)                                 | MCP (Model Context Protocol) server framework для агентов.   |
| Excel MCP Server        | [github.com/haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)     | MCP-сервер для работы с Excel (интеграция LLM ↔ Excel).      |
| Plandex-AI              | [github.com/plandex-ai/plandex](https://github.com/plandex-ai/plandex)                       | Open source AI coding agent.                                 |
| Agent Zero AI framework | [github.com/agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)                     | Фреймворк для создания автономных AI-агентов.                |
| 12-factor-agents        | [github.com/humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)     | Принципы построения production-ready LLM приложений.         |
| Memary                  | [github.com/kingjulio8238/Memary](https://github.com/kingjulio8238/Memary)                   | Open memory layer для автономных агентов.                    |
## 2. Speech & Audio LLMs

Библиотеки и UI для STT/TTS, real-time транскрипции, голосовых LLM и диаризации.

| Название                | Ссылка                                                                                       | Коротко                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| OpenAI Whisper          | [github.com/openai/whisper](https://github.com/openai/whisper)                               | Оригинальная модель распознавания речи от OpenAI.                    |
| whisper.cpp             | [github.com/ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)                   | C/C++ оптимизация Whisper — работает на CPU.                         |
| Faster Whisper          | [github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)               | Быстрее оригинала (CTranslate2).                                     |
| WhisperX                | [github.com/m-bain/whisperX](https://github.com/m-bain/whisperX)                             | Whisper + alignment + diarization для видео/подкастов.               |
| RealtimeSTT             | [github.com/KoljaB/RealtimeSTT](https://github.com/KoljaB/RealtimeSTT)                       | Низколатентная транскрипция с VAD, wakeword и instant transcription. |
| Ichigo                  | [github.com/homebrewltd/ichigo](https://github.com/homebrewltd/ichigo)                       | Локальный голосовой AI (голосовые ассистенты).                       |
| VOSK                    | [github.com/alphacep/vosk](https://github.com/alphacep/vosk)                                 | Лёгкая оффлайн STT-библиотека (много платформ).                      |
| Voice-Pro: Gradio WebUI | [github.com/abus-aikorea/voice-pro](https://github.com/abus-aikorea/voice-pro)               | Gradio UI для Whisper/Faster-Whisper и TTS/translation.              |
| Step-Audio2             | [github.com/stepfun-ai/Step-Audio2](https://github.com/stepfun-ai/Step-Audio2)               | End-to-end audio LLM для глубинного аудио-понимания.                 |
| CosyVoice               | [github.com/FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice)                 | Многоязычный нейрогенератор голоса.                                  |
| LibreTranslate          | [github.com/LibreTranslate/LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) | open-source API машинного перевода                                   |
| Spotube                 | [github.com/KRTirtho/spotube](https://github.com/KRTirtho/spotube)                           | кроссплатформенный клиент для Spotify / YouTube / Piped.video        |
## 3. Vision / Video / NVR

Проекты для детекции, стриминга, обработка видео, NVR и CV-исследования.

| Название                       | Ссылка                                                                                                                 | Коротко                                                                                 |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Frigate (NVR)                  | [github.com/blakeblackshear/frigate](https://github.com/blakeblackshear/frigate)                                       | NVR с детекцией объектов для камер.                                                     |
| Go2RTC                         | [github.com/AlexxIT/go2rtc](https://github.com/AlexxIT/go2rtc)                                                         | Инструмент для стриминга и пересылки потоков с камер.                                   |
| Superstreamer                  | [github.com/matvp91/superstreamer](https://github.com/matvp91/superstreamer)                                           | Обработка и стриминг видео в реальном времени.                                          |
| PaperVision                    | [github.com/deltacv/PaperVision](https://github.com/deltacv/PaperVision)                                               | OpenCV-адаптации и CV-алгоритмы.                                                        |
| Claude Vision Object Detection | [github.com/Doriandarko/Claude-Vision-Object-Detection](https://github.com/Doriandarko/Claude-Vision-Object-Detection) | Обнаружение объектов (Claude Vision примеры).                                           |
| Deep-Live-Cam                  | [github.com/hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)                                       | Real-time face swap / deepfake инструменты.                                             |
| DeepFace                       | [github.com/serengil/deepface](https://github.com/serengil/deepface)                                                   | Лёгкая библиотека для распознавания лиц и атрибутов.                                    |
| Roboflow - notebooks           | [github.com/roboflow/notebooks](https://github.com/roboflow/notebooks)                                                 | Туториалы state-of-the-art CV моделей (YOLO, SAM и др.).                                |
| Wifi-3d-fusion                 | [github.com/MaliosDark/wifi-3d-fusion](https://github.com/MaliosDark/wifi-3d-fusion)                                   | Исследовательский проект: WiFi+CV для 3D-позы.                                          |
| LLAMA OCR (npm)                | [www.npmjs.com/package/llama-ocr](https://www.npmjs.com/package/llama-ocr)                                             | OCR-пакет (npm).                                                                        |
| OHIF Medical Imaging Viewer    | [github.com/OHIF/Viewers](https://github.com/OHIF/Viewers)                                                             | просмотрщик медицинских изображений (DICOM)                                             |
| FaceFusion                     | [github.com/facefusion/facefusion](https://github.com/facefusion/facefusion)                                           | платформа для манипуляций с лицами / face fusion.                                       |
| MagicQuill                     | [github.com/magic-quill/MagicQuill](https://github.com/magic-quill/MagicQuill)                                         | система для редактирования изображений с AI.                                            |
| PromptFix                      | [github.com/yeates/PromptFix](https://github.com/yeates/PromptFix)                                                     | инструмент для «починки»/улучшения промптов (может пригодиться при image→LLM workflow). |
## 4. Web / Frontend / Full-Stack Frameworks

Инструменты для создания веб-интерфейсов, frontend-frameworks и full-stack шаблоны.

| Название                    | Ссылка                                                                                                   | Коротко                                             |
| --------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Svelte                      | [github.com/sveltejs/svelte](https://github.com/sveltejs/svelte)                                         | Современный фронтенд-фреймворк.                     |
| Reflex                      | [github.com/reflex-dev/reflex](https://github.com/reflex-dev/reflex)                                     | Python-фреймворк для web-apps (React-like).         |
| Full-stack-fastapi-template | [github.com/fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | Шаблон для полноценного FastAPI фронта + бэка.      |
| Rio: WebApps                | [github.com/rio-labs/rio](https://github.com/rio-labs/rio)                                               | WebApps на Python без JS/HTML.                      |
| Dioxus                      | [github.com/DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus)                                     | Fullstack фреймворк (Rust).                         |
| Webstudio                   | [github.com/webstudio-is/webstudio](https://github.com/webstudio-is/webstudio)                           | Визуальный билд-инструмент для сайтов.              |
| PyUIBuilder                 | [github.com/PaulleDemon/PyUIBuilder](https://github.com/PaulleDemon/PyUIBuilder)                         | GUI builder для Tkinter/CustomTkinter и др.         |
| 9ui                         | [github.com/borabaloglu/9ui](https://github.com/borabaloglu/9ui)                                         | Набор красивых компонентов UI (Tailwind + Base UI). |
| MidsceneJS                  | [github.com/web-infra-dev/midscene](https://github.com/web-infra-dev/midscene)                           | SDK автоматизации страницы с выводом JSON.          |
| Homepage (gethomepage)      | [github.com/gethomepage/homepage](https://github.com/gethomepage/homepage)                               | настраиваемая стартовая страница / дашборд          |
## 5. Data, ETL, Databases and Analytics

Инструменты для интеграции данных, визуализации, семантического поиска и аналитики.

| Название          | Ссылка                                                                                     | Коротко                                              |
| ----------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Airbyte           | [github.com/airbytehq/airbyte](https://github.com/airbytehq/airbyte)                       | Платформа для ETL/ELT интеграций.                    |
| Apache Superset   | [github.com/apache/superset](https://github.com/apache/superset)                           | BI и дашборды с широкими возможностями визуализации. |
| SurrealDB         | [github.com/surrealdb/surrealdb](https://github.com/surrealdb/surrealdb)                   | Документ-графовая распределённая БД для realtime.    |
| TXTAI / txtai     | [github.com/neuml/txtai](https://github.com/neuml/txtai)                                   | Семантическая поисковая база и RAG-слой.             |
| Pandas-AI         | [github.com/Sinaptik-AI/pandas-ai](https://github.com/Sinaptik-AI/pandas-ai)               | Conversational data analysis (Pandas + LLM).         |
| LLM Graph Builder | [github.com/neo4j-labs/llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder) | Построение графов из неструктурированных данных.     |
| Airbyte (повтор)  | [github.com/airbytehq/airbyte](https://github.com/airbytehq/airbyte)                       | (ETL — уже выше)                                     |
| Timelinize        | [github.com/timelinize/timelinize](https://github.com/timelinize/timelinize)               | Аггрегатор данных с разных аккаунтов в timeline.     |
## 6. Infrastructure, orchestration, DevOps & PaaS

Сервис-мэш, PaaS, background jobs, self-hosted платформы и деплой-инструменты.

| Название                | Ссылка                                                                                         | Коротко                                               |
| ----------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Istio                   | [github.com/istio/istio](https://github.com/istio/istio)                                       | Service Mesh (connect, secure, observe services).     |
| Zane-Ops                | [github.com/zane-ops/zane-ops](https://github.com/zane-ops/zane-ops)                           | Self-hosted PaaS для деплоя приложений.               |
| Trigger.dev             | [github.com/triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev)           | Платформа фоновых задач.                              |
| Steel-browser           | [github.com/steel-dev/steel-browser](https://github.com/steel-dev/steel-browser)               | Браузер/инструмент для автоматизаций (dev tool).      |
| Browser Use             | [github.com/browser-use/browser-use](https://github.com/browser-use/browser-use)               | Инструменты browser automation.                       |
| Rio (повтор)            | [github.com/rio-labs/rio](https://github.com/rio-labs/rio)                                     | WebApps hosting in Python.                            |
| CasaOS                  | [github.com/IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS)                       | Личный облачный дашборд (self-host).                  |
| WatchYourLAN            | [github.com/aceberg/WatchYourLAN](https://github.com/aceberg/WatchYourLAN)                     | Лёгкий сканер сети с нотификациями.                   |
| Local File Organizer    | [github.com/QiuYannnn/Local-File-Organizer](https://github.com/QiuYannnn/Local-File-Organizer) | Утилита для упорядочивания файлов локально.           |
| Docker Windows (dockur) | [github.com/dockur/windows](https://github.com/dockur/windows)                                 | Windows в Docker (dev/песочница).                     |
| Lightpanda-io/browser   | [github.com/lightpanda-io/browser](https://github.com/lightpanda-io/browser)                   | браузерный проект (automation)                        |
| Webpilot (Webpilot-AI)  | [github.com/webpilot-ai/Webpilot](https://github.com/webpilot-ai/Webpilot)                     | открытый «Copilot for Web» для автоматизации/парсинга |
| Nanobrowser             | [github.com/nanobrowser/nanobrowser](https://github.com/nanobrowser/nanobrowser)               | расширение для AI-веб-автоматизации                   |
## 7. Developer tools and AI tools

CLI-утилиты, редакторы, UI-builders, JSON-инструменты и полезные мелочи для dev-workflow.

| Название                 | Ссылка                                                                                           | Коротко                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| JSON Crack (Editor)      | [github.com/AykutSarac/jsoncrack.com](https://github.com/AykutSarac/jsoncrack.com)               | Визуальный редактор и визуализация JSON.            |
| Just                     | [github.com/casey/just](https://github.com/casey/just)                                           | «Make»-альтернатива — runner для команд (justfile). |
| PyUIBuilder (повтор)     | [github.com/PaulleDemon/PyUIBuilder](https://github.com/PaulleDemon/PyUIBuilder)                 | GUI builder (см. выше).                             |
| AutomaApp                | [github.com/AutomaApp/automa](https://github.com/AutomaApp/automa)                               | Автоматизация в браузере (extension).               |
| Nanobrowser              | [github.com/nanobrowser/nanobrowser](https://github.com/nanobrowser/nanobrowser)                 | Расширение для AI-веб-автоматизации.                |
| MarkitDown / MarkPDFDown | [github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)                       | Инструменты для конвертации в Markdown / PDF→MD.    |
| MarkPDFDown (альт)       | [github.com/MarkPDFdown/markpdfdown](https://github.com/MarkPDFdown/markpdfdown)                 | PDF→Markdown + LLM визуалка.                        |
| MidsceneJS (повтор)      | [github.com/web-infra-dev/midscene](https://github.com/web-infra-dev/midscene)                   | Web automation SDK.                                 |
| Awesome AI Web Search    | [github.com/felladrin/awesome-ai-web-search](https://github.com/felladrin/awesome-ai-web-search) | подборка инструментов AI для веб-поиска             |
## 8. Documentation, tutorials (Guides & Books)

Собрания знаний, учебные дорожные карты и туториалы по CS, ML и системному дизайну.

| Название                             | Ссылка                                                                                                         | Коротко                                               |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| build-your-own-x                     | [github.com/codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)             | Руководства «построй своё…» для инженеров.            |
| System-design-101                    | [https://github.com/ByteByteGoHq/system-design-101](https://github.com/ByteByteGoHq/system-design-101)         | Материалы по системному дизайну.                      |
| The Data Scientist's Toolbox (Drive) | (Google Drive)                                                                                                 | Сборник книг и материалов по Data Science.            |
| The Book Of Secret Knowledge         | [github.com/trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | Коллекция хитростей, one-liners и утилит.             |
| Roboflow notebooks                   | [github.com/roboflow/notebooks](https://github.com/roboflow/notebooks)                                         | CV-туториалы и практики.                              |
| Math (ossu)                          | [github.com/ossu/math](https://github.com/ossu/math)                                                           | Путь к самообразованию в математике.                  |
| Roadmap.sh                           | [github.com/kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap)               | community-дорожные карты и ресурсы для разработчиков. |
| Roboflow                             | [github.com/roboflow/notebooks](https://github.com/roboflow/notebooks)                                         | туториалы state-of-the-art CV.                        |
| The Book Of Secret Knowledge         | [github.com/trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | сборник гайдов, one-liners и полезностей              |
## 9. Documents, PDF and text

Инструменты для работы с PDF, документами, заметками и резюме.

| Название                     | Ссылка                                                                                                                                                         | Коротко                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| MarkitDown / MarkPDFDown     | [github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)<br>[github.com/MarkPDFdown/markpdfdown](https://github.com/MarkPDFdown/markpdfdown) | Конвертация документов в Markdown, LLM-помощь. |
| Stirling-PDF                 | [github.com/Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)                                                                       | PDF-working tools.                             |
| Reactive-Resume              | [github.com/AmruthPillai/Reactive-Resume](https://github.com/AmruthPillai/Reactive-Resume)                                                                     | Шаблон/приложение для резюме.                  |
| Wallabag                     | [github.com/wallabag/wallabag](https://github.com/wallabag/wallabag)                                                                                           | Self-hosted Save-for-later для статей.         |
| Harper (Automattic / harper) | [github.com/Automattic/harper](https://github.com/Automattic/harper)                                                                                           | Offline grammar checker (Rust).                |
## 10. Products, applications and no-code / low-code

Готовые приложения, конструкторы форм, CMS-альтернативы и no-code платформы.

| Название   | Ссылка                                                                                           | Коротко                                 |
| ---------- | ------------------------------------------------------------------------------------------------ | --------------------------------------- |
| Typebot    | [github.com/baptisteArno/typebot.io](https://github.com/baptisteArno/typebot.io)                 | Конструктор чат-ботов (no-code).        |
| Appsmith   | [github.com/appsmithorg/appsmith](https://github.com/appsmithorg/appsmith)                       | Low-code internal apps builder.         |
| HeyForm    | [github.com/heyform/heyform](https://github.com/heyform/heyform)                                 | Конструктор форм.                       |
| Formbricks | [github.com/formbricks/formbricks](https://github.com/formbricks/formbricks)                     | Open source Qualtrics-альтернатива.     |
| Spree      | [github.com/spree/spree](https://github.com/spree/spree)                                         | Open source eCommerce платформа.        |
| PocketBase | [github.com/pocketbase/pocketbase](https://github.com/pocketbase/pocketbase)                     | Lightweight backend (auth, db, files).  |
| Focalboard | [github.com/mattermost-community/focalboard](https://github.com/mattermost-community/focalboard) | Self-hosted альтернатива Trello/Notion. |
| Plane      | [github.com/makeplane/plane](https://github.com/makeplane/plane)                                 | Project management tool.                |
| Webstudio  | [github.com/webstudio-is/webstudio](https://github.com/webstudio-is/webstudio)                   | Визуальный сайт-билдер.                 |
| Maxun      | [github.com/getmaxun/maxun](https://github.com/getmaxun/maxun)                                   | No-code web data extraction.            |
| GDevelop   | [github.com/4ian/GDevelop](https://github.com/4ian/GDevelop)                                     | игровой движок                          |
## 11. ERP, applications and Fintech

Системы и платформы для бизнеса, ERP, MES, торговли и интеграции.

| Название          | Ссылка                                                                   | Коротко                                        |
| ----------------- | ------------------------------------------------------------------------ | ---------------------------------------------- |
| ERPNext           | [github.com/frappe/erpnext](https://github.com/frappe/erpnext)           | Open source ERP.                               |
| Carbon            | [github.com/crbnos/carbon](https://github.com/crbnos/carbon)             | ERP/MES/QMS для производства.                  |
| Airbyte (повтор)  | [github.com/airbytehq/airbyte](https://github.com/airbytehq/airbyte)     | ETL для бизнес-интеграций.                     |
| Spree (eCommerce) | [github.com/spree/spree](https://github.com/spree/spree)                 | eCommerce платформа.                           |
| Freqtrade         | [github.com/freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | open-source крипто-трейдинг-бот (algo trading) |
## 12. Экспериментальные / исследовательские проекты & ML-platforms

Исследования, ускорение численных вычислений, модели и инфраструктура для экспертов.

| Название             | Ссылка                                                                                               | Коротко                                                 |
| -------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Cupy                 | [github.com/cupy/cupy](https://github.com/cupy/cupy)                                                 | NumPy на GPU.                                           |
| Qwen3-Coder          | [github.com/QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder)                               | Кодовая версия Qwen3 (LLM).                             |
| NovaSky / SkyThought | [github.com/NovaSky-AI/SkyThought](https://github.com/NovaSky-AI/SkyThought)                         | Train your own preview model (O1).                      |
| TransformerLab App   | [github.com/transformerlab/transformerlab-app](https://github.com/transformerlab/transformerlab-app) | Интерфейс для тренировки/оценки LLM+diffusion локально. |
| Julep                | [github.com/julep-ai/julep](https://github.com/julep-ai/julep)                                       | Serverless AI workflows.                                |
| Cupy (повтор)        | [github.com/cupy/cupy](https://github.com/cupy/cupy)                                                 | GPU NumPy (см. выше).                                   |
| Google genai-toolbox | [github.com/googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox)                   | MCP toolbox / AI infra от Google.                       |
| microsoft/BitNet     | [github.com/microsoft/BitNet](https://github.com/microsoft/BitNet)                                   | 1-bit inference framework (quant inference).            |
| OpenCoder-llm        | [github.com/OpenCoder-llm/OpenCoder-llm](https://github.com/OpenCoder-llm/OpenCoder-llm)             | Cookbook для code-LLM.                                  |

## Others
- **OpenAI Gradio App** — [github.com/gradio-app/openai-gradio](https://github.com/gradio-app/openai-gradio) — UI для быстрых демо и интерфейсов к моделям.
- **Open Canvas (langchain)** — [github.com/langchain-ai/open-canvas](https://github.com/langchain-ai/open-canvas) — визуальная canvas-среда для RAG/LLM-workflow.
- **OpenAI Java API Library** — [github.com/openai/openai-java](https://github.com/openai/openai-java) — официальная Java-библиотека OpenAI (важно для Java-интеграций).
- **Google Gemini — Starter Applets** — [github.com/google-gemini/starter-applets](https://github.com/google-gemini/starter-applets) — стартовые апплеты / примеры для Google AI Studio.
- **ArchiveBox** — [github.com/ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) — автономный архиватор веб-страниц (self-hosted).
- **Awesome LLM Apps** — [github.com/Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — коллекция LLM-приложений и RAG-примеров.
- **DRM Watch 3** — [github.com/drfailov/DRM_Watch_v3/tree/main](https://github.com/drfailov/DRM_Watch_v3/tree/main) — был в исходном списке (специфичный проект).

[Awesome-World-Models](https://github.com/knightnemo/Awesome-World-Models) — Важные работы по теме _world modelling_, то есть тех исследований и приложений, где система учится «модели мира», чтобы предсказывать, симулировать или понимать окружающую среду.
[Hugging Face Agents Course](https://github.com/huggingface/agents-course) — курс от Hugging Face, посвящённый созданию и применению «агентов» (AI-агентов) с использованием современных языковых моделей.
[System Prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) — Репозиторий представляет собой большую коллекцию системных подсказок (system prompts) и конфигураций моделей, извлечённых из множества коммерческих или полуоткрытых инструментов ИИ-агентов и редакторов кода.
[Frappe Builder](https://github.com/frappe/builder) — визуальный «low-code» конструктор сайтов.
[Cyberdesk](https://github.com/cyberdesk-hq/cyberdesk) — “open source virtual desktops for AI agents” (виртуальные десктопы с открытым исходным кодом, для ИИ-агентов)
[Skyfall-GS](https://github.com/jayin92/Skyfall-GS)  — система, которая позволяет **извлекать трёхмерные городские сцены** из спутниковых изображений, с хорошей геометрией и текстурами, и делать их «исследуемыми»
[Agent-S](https://github.com/simular-ai/Agent-S) — фреймворк с открытым исходным кодом, цель которого: позволить искусственным агентам **автономно взаимодействовать с компьютером** так, как это делает человек.
[Android Code Studio](https://github.com/AndroidCSOfficial/android-code-studio) — IDE для Android-устройств, предназначенная для разработки полноценных Android-приложений прямо на устройстве.
[BrowserOS](https://github.com/browseros-ai/BrowserOS) — это проект с открытым исходным кодом: форк Chromium, созданный организацией browseros‑ai, с целью интеграции ИИ-агентов непосредственно в браузерную среду.
[ViMax](https://github.com/HKUDS/ViMax) — Agentic Video Generation (Director, Screenwriter, Producer, and Video Generator All-in-One)
[Microsoft Agent Lightning](https://github.com/microsoft/agent-lightning) — создан, чтобы **тренировать и оптимизировать существующих ИИ-агентов** — вне зависимости от того, на каком фреймворке они работают. Это значит, что ты не обязан с нуля переписывать своего агента, чтобы его улучшить.
[JSON Crack](https://github.com/AykutSarac/jsoncrack.com) — Это открытое приложение-визуализатор данных, которое позволяет превращать структуры данных (JSON, YAML, XML, CSV и др.) в интерактивные графы и деревья.
[Context7](https://github.com/upstash/context7) — Этот проект предоставляет сервер интерфейса по протоколу MCP (Model Context Protocol) — позволяет инструментам и ИИ-ассистентам получать **актуальную документацию и примеры кода** для библиотек и фреймворков.
[OpenHealth - AI Health Assistant](https://github.com/OpenHealthForAll/open-health) — Это веб-приложение с открытым исходным кодом, которое помогает пользователю централизованно собирать и анализировать личные данные о здоровье
[ART: Agent Reinforcement Trainer](https://github.com/OpenPipe/ART) — позволяет агентам на базе языковых моделей (LLM) **учиться на своём опыте** (ролл-аутах, многошаговых взаимодействиях) и становиться надёжнее и точнее.
[bitwarden/clients: Bitwarden client apps](https://github.com/bitwarden/clients) — Репозиторий **Bitwarden / clients** содержит клиентские приложения для Bitwarden Password Manager: веб-интерфейс, расширения браузеров, десктоп-приложения и CLI (мобильные приложения вынесены в отдельные репозитории).
[Step-Audio2](https://github.com/stepfun-ai/Step-Audio2) — Основная цель: объединить решение задач распознавания речи (ASR), понимания звуков/аудиоконтекста (включая паралингвистику, эмоции, стили голоса), генерации речи и диалоговых способностей агента.
[InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) — InfiniteTalk позволяет генерировать **видео с «говорящими» персонажами** на основе аудиофайла + либо статического изображения либо видео-источника.
[simstudioai/sim](https://github.com/simstudioai/sim) — Платформа визуального построения **агентных рабочих процессов** (agent workflows) — с drag-and-drop интерфейсом, узлами («blocks») и связями-потоками.
[Carbon: Carbon is a modern ERP/MES/QMS](https://github.com/crbnos/carbon) — платформа для управления производственными процессами — включает в себя ERP (Enterprise Resource Planning), MES (Manufacturing Execution System), QMS (Quality Management System).

