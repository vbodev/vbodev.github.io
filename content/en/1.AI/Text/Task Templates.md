---
title: "Task Templates"
tags: [ai, text, prompt, templates]
---
[[ru/1.AI/Text/Task Templates|RU]] | [[en/1.AI/Text/Task Templates|EN]] | [[de/1.AI/Text/Task Templates|DE]]

## 1. Example: Writing a Blog Article 

```markdown
# Task: Writing a Blog Article

## Topic
How to use ChatGPT to automate developer tasks

## Audience
Junior and Middle-level developers

## Volume
1000–1200 words

## Structure
1. Introduction
2. Examples of using ChatGPT in daily development
3. Integration with VS Code / Postman / n8n
4. Potential errors and limitations
5. Conclusion and tips

## Style
Semi-formal, with code examples, humor, and friendly tone

## Additional
Mention ChatGPT-4 capabilities and ChatGPT in the desktop application

```
## 2. Example: Generating Python Code

```Markdown
# Task: Generating Python Code for Data Analysis

## Goal
Create a Python script that reads a CSV file, analyzes data (mean, median, standard deviation), and builds a distribution plot.

## Input Data
- CSV file with one column of numeric values.
- Filename: `data.csv`
- Column name: `value`

## Output
- Statistical metrics: mean, median, standard deviation
- Saved plot: `histogram.png`

## Requirements
- Use libraries: pandas, matplotlib
- Code should be clear and contain comments

## Additional
- Build a histogram with 20 bins

```
## 3. Example: Generate an Image

```markdown
# Task: Generate an Image

## Image Type
Fantasy portrait of a girl in cyberpunk style

## Description
- Young girl with purple hair
- Neon lights, night city in the background
- Cyber glasses and metallic collar
- Emotion: confidence and independence

## Size
1024x1024 pixels

## Style
Realistic + some anime

## Additional
Background should be slightly blurred, main focus – on the face

```
## 4. Example: Specification: Landing Page for IT Company

```markdown
# Specification: Landing Page for IT Company

## Company Name
NextGenSoft

## Goal
Attract clients for software development services

## Website Blocks
- Header with logo and navigation
- Main banner (with slogan and button)
- Services (3 cards)
- About company (text + photo)
- Contact form
- Footer with contacts

## Design
- Colors: blue, white, gray
- Style: minimalism, sans-serif fonts

## Responsiveness
Yes (mobile and desktop versions)

## Technologies
HTML, CSS (Tailwind or Bootstrap), JS (Vanilla)

## Deadline
1 week
```
## 5. Task Template
````markdown
# 📌 Task Name
[INSERT_SHORT_TASK_DESCRIPTION]

---

## 🎯 Goal
[DESCRIBE_WHY_THIS_TASK_IS_NEEDED_AND_EXPECTED_RESULT]

---

## 🧱 Project Context
- Language: [Delphi / Python / Java / other]
- IDE / Framework: [RAD Studio / PyCharm / n8n / other]
- Main technologies: [Virtual TreeView, SQLLite, REST API, JSON, etc.]
- Module name (if any): [FILENAME.pas]

---

## 📂 Structure/Files to work in
- `PATH_TO_FILE_1`
- `PATH_TO_FILE_2`

---

## 🛠️ What should be implemented
1. [WHAT_TO_DO_1]
2. [WHAT_TO_DO_2]
3. [WHAT_TO_DO_3]

---

## ✅ Requirements
- [REQUIREMENT_1]
- [REQUIREMENT_2]
- [REQUIREMENT_3]

---

## 📈 Expected Result
- [EXPECTED_RESULT_1]
- [EXPECTED_RESULT_2]

---

## 🧪 Test Data (if any)
```pascal
// Example in Delphi
Task := TTaskNode.Create;
Task.Typ := 'Document';
Task.Status := 'In Progress';
```

---

## ✨ Additional
- Suggest alternative: [Yes / No]
- Code documentation needed: [Yes / No]
- Usage example: [Yes / No]

---

## 💬 Response Format from ChatGPT
- Complete source code
- Description of steps and logic
- Additionally: generated usage example (if needed)
````

## 6. Python Task Template

````markdown
# 🐍 Python Task

## 📌 Task Name
[EXAMPLE: CSV Analysis and Data Visualization]

## 🎯 Goal
[Describe why the script is written and how the result will be used]

## 📚 Context
- Language: Python
- Version: [3.10+]
- Used libraries: [pandas, matplotlib, requests, etc.]
- Where it will run: [locally / server / Jupyter Notebook]

## 🛠 What should be implemented
1. [Read CSV file]
2. [Build distribution plot]
3. [Save result to file]

## ✅ Requirements
- [Code with comments]
- [Error handling]
- [Input/output format must be specified]

## 🔍 Example Input Data
```csv
value
12
34
23
...
```

## 📤 Example Output Data
- Mean: 23.1
- Plot: `histogram.png`

## 💬 Response Format from ChatGPT
- Complete code
- Explanation of logic
````

## 7. Java Task Template

````markdown
# ☕ Java Task

## 📌 Task Name
[EXAMPLE: Processing JSON from REST API]

## 🎯 Goal
[Describe why the program is written and how it will be used]

## 📚 Context
- Language: Java
- Version: [Java 11+]
- Used libraries: [Jackson, HttpClient, Spring, etc.]
- IDE: [IntelliJ IDEA / Eclipse / VS Code]

## 🛠 What should be implemented
1. [Make HTTP GET request to API]
2. [Parse JSON]
3. [Output data to console or GUI]

## ✅ Requirements
- [Error handling]
- [Code should be readable and structured]
- [Maven/Gradle support (if required)]

## 🔍 Example API Response
```json
{
  "user": "Vitaliy",
  "active": true
}
```

## 📤 Example Expected Output
```
User: Vitaliy
Status: active
```

## 💬 Response Format from ChatGPT
- Complete source code
- Step-by-step explanation
````

