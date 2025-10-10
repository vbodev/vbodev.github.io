---
title: Use case and examples
---
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

Visual scheme (3 developers)
```
main ──●────────────────────●─────────────────●───────────────►
         \