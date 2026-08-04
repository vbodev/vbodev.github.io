---
title: Use case and examples
---
[[ru/Dev Tools/GIT/Use case and examples|RU]] | [[en/Dev Tools/GIT/Use case and examples|EN]] | [[de/Dev Tools/GIT/Use case and examples|DE]]
## Szenario der Nutzung
### 1. Aufgaben im System
In Jira oder GitHub Projects werden Aufgaben erstellt:
- **TASK-101**: Login implementieren
- **TASK-102**: Zahlung hinzufügen
- **TASK-103**: E-Mail-Validierung beheben
Jede Aufgabe hat eine **ID** (z.B. TASK-101), einen Namen, eine Beschreibung und Akzeptanzkriterien.
### 2. Erstellung eines Branches für eine Aufgabe
Wenn ein Entwickler eine Aufgabe übernimmt, erstellt er einen Branch mit dieser ID:
```bash
# Programmierer Nr. 1 (Login)
git checkout -b feature/TASK-101-login
# Programmierer Nr. 2 (Zahlung)
git checkout -b feature/TASK-102-payments
# Programmierer Nr. 3 (E-Mail-Validierung)
git checkout -b bugfix/TASK-103-email-validation
```
👉 Branchname = **Aufgabetyp + Aufgabennummer + kurze Beschreibung**.
### 3. Arbeit an der Aufgabe
Der Entwickler erstellt Commits, in denen die Aufgabennummer in der Nachricht angegeben wird:
```bash
git commit -m "TASK-101: Login-Controller hinzugefügt"
git commit -m "TASK-101: E-Mail- und Passwortvalidierung implementiert"
```
Dies ist praktisch, weil:
- Die Git-Historie sofort mit der Aufgabe verknüpft ist.
- Commits und Pull Requests in Jira und GitHub automatisch mit der Aufgabe verknüpft werden.
### 4. Pull Request / Merge Request
Wenn die Aufgabe erledigt ist:
```bash
git push origin feature/TASK-101-login
```
Es wird ein **Pull Request** (PR) in main oder develop geöffnet.
Name des PR:
```bash
[TASK-101] Login implementieren
```
Im PR sind sichtbar:
- Änderungen im Code,
- ein Link zur Aufgabe in Jira/GitHub Projects,
- Diskussionen und Kommentare des Teams.
### 5. Code Review und Merge
- Andere Entwickler überprüfen den Code.
- Wenn alles in Ordnung ist, klicken sie auf **Approve**.
- Der Branch wird in main integriert.
### 6. Automatisierung (CI/CD)
- Jira und GitHub setzen automatisch den Status der Aufgabe auf **“In Review”** oder **“Done”**, wenn der PR gemerged wurde.
- CI startet Tests.
- Bei Erfolg wird der Code deployed.

Визуальная схема (3 разработчика)
```
main ──●────────────────────●────────────────────●────────────────────────►
        \                    \                    \
 feature/TASK-101-login       \                    \
                               \                    \
                      feature/TASK-102-payments      \
                                                      \
                                            bugfix/TASK-103-email-validation
```
Каждая задача → своя ветка → свой PR → merge в main.
### 📌Итог:
- Каждая задача живёт в своей ветке.
- Названия веток и коммитов связаны с ID задачи.
- Jira/GitHub Projects автоматически связывают задачи ↔ ветки ↔ коммиты ↔ PR.
- История чистая и прозрачная: видно, кто сделал какую задачу и когда.
## Примеры

### Пример 1: Одна задача одного разработчика в Jira

**TASK-101**: Реализовать логин 
**Описание:** пользователь должен вводить email + пароль, система проверяет данные и пускает в систему.
#### 1. Задача в Jira
В Jira задача создана и назначена на разработчика.Статус: **To Do** → **In Progress**.
#### 2. Создание ветки в Git**
Разработчик берёт задачу в работу:
##### Обновляем локальную main до актуальной версии
```bash
git checkout main
git fetch origin
git rebase origin/main
```
##### Создаём ветку под задачу
```
git checkout -b feature/TASK-101-login
```
Теперь у разработчика своя изолированная ветка.
#### 3. Работа над задачей
Программист пишет код и фиксирует изменения коммитами:
```bash
git add src/login_controller.java
git commit -m "TASK-101: добавлен контроллер логина"
git add src/login_service.java
git commit -m "TASK-101: реализована проверка email и пароля"
git add src/tests/login_test.java
git commit -m "TASK-101: добавлены unit-тесты для логина"
```
👉 Обрати внимание: в каждом сообщении указан **TASK****-101**, чтобы Jira и GitHub могли связать коммит с задачей.
#### 4. Публикация ветки
Когда задача готова:
```bash
git push origin feature/TASK-101-login
```
Теперь ветка появилась на GitHub/GitLab.
#### 5. Создание Pull Request
На GitHub создаётся **Pull Request**:
- Ветка: feature/TASK-101-login → в main
- Заголовок: [TASK-101] Реализовать логин
- Описание: ссылка на задачу в Jira (https://jira.company.com/browse/TASK-101)
PR автоматически привязывается к задаче в Jira.
#### 6. Code Review
- Другие 2 разработчика смотрят изменения.
- Оставляют комментарии (например, «вынести метод в отдельный сервис»).
- Автор дорабатывает код → пушит новые коммиты:

```bash
git add src/login_service.java
git commit -m "TASK-101: рефакторинг сервиса логина"
git push origin feature/TASK-101-login
```
PR обновляется автоматически.
#### 7. Merge
После одобрения (Approve):
- PR вливается в main (через **Squash** или **Rebase** **and** **merge**, чтобы история была чистой).
- CI запускает тесты, билд и деплой.
#### 8. Завершение задачи
- Jira переводит задачу в статус **Done** автоматически (по хуку из GitHub).
- В истории видно: коммиты, PR, кто ревьюил, кто мерджил.

**Визуальная схема**
```
main ────●───────────────●─────────────────●───────────────►
          \                                      /
           \                                    /
 feature/TASK-101-login ──●──●──●──●───────────● (merge)
                          (код, тесты, фиксы)
```
📌 **Итог**:
- Jira → хранит задачу (ID, описание, статус).
- Git → хранит ветку и коммиты.
- GitHub/GitLab → связывает PR с задачей.
- CI/CD → проверяет и деплоит код.
Каждый шаг прозрачен: сразу видно, какой код относится к какой задаче.

### Пример 2:

Задачи в Jira:
- **TASK-101** — логин (Программист №1)
- **TASK-102** — оплата (Программист №2)
- **TASK-103** — баг в email (Программист №3)
#### 1. Каждый создаёт ветку под задачу
```bash
# Программист №1
git checkout -b feature/TASK-101-login
# Программист №2
git checkout -b feature/TASK-102-payments
# Программист №3
git checkout -b bugfix/TASK-103-email-validation
```
#### 2. Каждый делает коммиты локально
```bash
Программист №1 (логин):
git commit -m "TASK-101: контроллер логина"
Программист №2 (оплата):
git commit -m "TASK-102: сервис оплаты"
Программист №3 (валидация email):
git commit -m "TASK-103: исправлена валидация email"
```
#### 3. Каждый пушит свою ветку
```bash
git push origin feature/TASK-101-login
git push origin feature/TASK-102-payments
git push origin bugfix/TASK-103-email-validation
```
Теперь в origin есть три новые ветки.
#### 4. PR (Pull Request)
- №1 открывает PR [TASK-101] Реализовать логин
- №2 открывает PR [TASK-102] Добавить оплату
- №3 открывает PR [TASK-103] Фикс email
Все PR направлены в main.
#### 5. Code Review и Merge
Представим, что PR идут последовательно.

**Первый merge** **(TASK****-101):**
```graph
main ───A──B──C─────────●──────●──────●──────────────►
         \
          feature/TASK-101-login (merge → ●)
```

**Второй merge (TASK-102):**
```graph
main ───A──B──C─────────●──────●──────●──────────────►
          \                      /
           feature/TASK-101-login
                          \
                           feature/TASK-102-payments (merge → ●)
```

**Третий merge (TASK-103):**

```graph
main ───A──B──C─────────●──────●──────●──────────────►
          \                /              /
           feature/TASK-101-login        /
                          \             /
                           feature/TASK-102-payments
                                         \
                             bugfix/TASK-103-email-validation (merge → ●)
```
**6. Что получает команда**

- В main теперь лежит код всех трёх задач.
- Каждая задача прошла через отдельный PR и code review.
- Jira автоматически закрыла задачи в статус **Done**.

**Важный момент — конфликты**

Если два программиста правят один и тот же файл (например, UserService.java):

- Второй, кто делает merge, получит **merge** **conflict**.
- Решается так:
```bash
git fetch origin
git rebase origin/main   # или git merge origin/main
```
## Решаем конфликты

```bash
git add .
git rebase --continue
git push origin feature/TASK-102-payments
```
После этого PR снова готов к слиянию.

📌 **Итого:**
- Каждая задача = отдельная ветка = отдельный PR.
- Ветки живут недолго (1–5 дней).
- В main попадает только проверенный код.
- Конфликты решаются до merge.