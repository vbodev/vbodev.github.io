---
title: Use case and examples
---
[[ru/Development Tools/GIT/Use case and examples|RU]] | [[en/Development Tools/GIT/Use case and examples|EN]] | [[de/Development Tools/GIT/Use case and examples|DE]]
## Use Case Scenario
### 1. Tasks in the System
Tasks are created in Jira or GitHub Projects:
- **TASK-101**: Implement login
- **TASK-102**: Add payment
- **TASK-103**: Fix email validation
Each task has an **ID** (e.g., TASK-101), a name, a description, and acceptance criteria.
### 2. Branching for a Task
When a developer takes a task, they create a branch with that ID:
```bash
# Programmer #1 (login)
git checkout -b feature/TASK-101-login
# Programmer #2 (payment)
git checkout -b feature/TASK-102-payments
# Programmer #3 (email validation)
git checkout -b bugfix/TASK-103-email-validation
```
👉 Branch name = **work type + task ID + brief description**.
### 3. Working on a Task
The developer makes commits, indicating the task ID in the message:
```bash
git commit -m "TASK-101: added login controller"
git commit -m "TASK-101: validated user data"
```
This is convenient because:
- Git history is immediately linked to the task.
- Commits and PRs are automatically attached to the task in Jira and GitHub.
### 4. Pull Request / Merge Request
When the task is done:
```bash
git push origin feature/TASK-101-login
```
A **Pull Request** (PR) is opened in main or develop.
PR name:
```bash
[TASK-101] Implement login
```
The PR shows:
- code changes,
- a link to the task in Jira/GitHub Projects,
- team discussions and comments.
### 5. Code Review and Merge
- Other developers review the code.
- If everything is okay, they click **Approve**.
- The branch is merged into main.
### 6. Automation (CI/CD)
- Jira and GitHub automatically set the task status to **“In Review”** or **“Done”** when the PR is merged.
- CI runs tests.
- If successful, the code is deployed.

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