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

Visual diagram (3 developers)
```
main ──●────────────────────●────────────────────●────────────────────────►
        \                    \                    \
 feature/TASK-101-login       \                    \
                               \                    \
                      feature/TASK-102-payments      \
                                                      \
                                            bugfix/TASK-103-email-validation
```
Each task → its own branch → its own PR → merge into main.
### 📌Result:

- Each task lives in its own branch.
- Branch and commit names are linked to the task ID.
- Jira/GitHub Projects automatically connect tasks ↔ branches ↔ commits ↔ PRs.
- The history is clean and transparent: you can see who completed which task and when.
## Examples

### Example 1: One task per developer in Jira.

**TASK-101**: Implement login  
**Description:** The user must enter an email and password; the system validates the data and grants access.

#### 1. Task in Jira

The task is created in Jira and assigned to the developer. Status: **To Do** → **In Progress**.
#### 2. Creating a branch in Git

The developer starts working on the task:
##### Update the local main branch to the latest version
```bash
git checkout main
git fetch origin
git rebase origin/main
```
##### Create a branch for the task
```
git checkout -b feature/TASK-101-login
```
Теперь у разработчика своя изолированная ветка.
#### 3. Working on the task
The developer writes code and records changes with commits:
```bash
git add src/login_controller.java
git commit -m "TASK-101: login controller added"
git add src/login_service.java
git commit -m "TASK-101: email and password validation implemented"
git add src/tests/login_test.java
git commit -m "TASK-101: unit-tests for login added"
```
> [!Note]
> 👉 Note: each commit message includes **TASK-101** so that Jira and GitHub can link the commit to the task.
#### 4. Publishing the branch
When the task is ready:
```bash
git push origin feature/TASK-101-login
```
Now the branch has appeared on GitHub/GitLab.
#### 5. Creating a Pull Request
A **Pull Request** is created on GitHub:
- Branch: feature/TASK-101-login → main
- Title: [TASK-101] Implement login
- Description: link to the Jira task ([https://jira.company.com/browse/TASK-101](https://jira.company.com/browse/TASK-101))  
    The PR is automatically linked to the task in Jira.
#### 6. Code Review
- The other two developers review the changes.
- They leave comments (for example, “move the method to a separate service”).
- The author refines the code → pushes new commits:
```bash
git add src/login_service.java
git commit -m "TASK-101: рефакторинг сервиса логина"
git push origin feature/TASK-101-login
```
The PR updates automatically.
#### 7. Merge
After approval (Approve):
- The PR is merged into main (using **Squash** or **Rebase and merge** to keep the history clean).
- CI runs tests, build, and deployment.
#### 8. Task completion
- Jira automatically moves the task to **Done** (via a GitHub webhook).
- The history shows commits, the PR, who reviewed, and who merged.

**Visual diagram**
```
main ────●───────────────●─────────────────●───────────────►
          \                                      /
           \                                    /
 feature/TASK-101-login ──●──●──●──●───────────● (merge)
                          (code, test, fix)
```
📌 **Result**:
- Jira → stores the task (ID, description, status).
- Git → stores the branch and commits.
- GitHub/GitLab → links the PR to the task.
- CI/CD → tests and deploys the code.  
    Each step is transparent: it’s immediately clear which code belongs to which task.
### Example 2:

Tasks in Jira:

- **TASK-101** — login (Developer #1)
- **TASK-102** — payment (Developer #2)
- **TASK-103** — email bug (Developer #3)
#### 1. Each developer creates a branch for their task.
```bash
# Developer №1
git checkout -b feature/TASK-101-login
# Developer №2
git checkout -b feature/TASK-102-payments
# Developer №3
git checkout -b bugfix/TASK-103-email-validation
```
#### 2. Each developer makes commits locally.
```bash
Developer №1 (login):
git commit -m "TASK-101: login controller"
Developer №2 (payment):
git commit -m "TASK-102: payment service"
Developer №3 (valiidation email):
git commit -m "TASK-103: validation email fixed"
```
#### 3. Each developer pushes their own branch.
```bash
git push origin feature/TASK-101-login
git push origin feature/TASK-102-payments
git push origin bugfix/TASK-103-email-validation
```
Now there are three new branches in origin.
#### 4. PR (Pull Request)
- #1 opens PR **[TASK-101] Implement login**
- #2 opens PR **[TASK-102] Add payment**
- #3 opens PR **[TASK-103] Fix email**  
    All PRs are targeted at the main branch.
#### 5. Code Review и Merge
Let’s assume the PRs are processed sequentially.

**First merge** **(TASK****-101):**
```graph
main ───A──B──C─────────●──────●──────●──────────────►
         \
          feature/TASK-101-login (merge → ●)
```

**Second merge (TASK-102):**
```graph
main ───A──B──C─────────●──────●──────●──────────────►
          \                      /
           feature/TASK-101-login
                          \
                           feature/TASK-102-payments (merge → ●)
```

**Third merge (TASK-103):**

```graph
main ───A──B──C─────────●──────●──────●──────────────►
          \                /              /
           feature/TASK-101-login        /
                          \             /
                           feature/TASK-102-payments
                                         \
                             bugfix/TASK-103-email-validation (merge → ●)
```
#### 6. What the team gets

- The main branch now contains the code for all three tasks.
- Each task went through a separate PR and code review.
- Jira automatically closed the tasks with the status **Done**.

**Important point — conflicts**

If two developers edit the same file (for example, `UserService.java`):
- The second one to merge will get a **merge conflict**.
- It’s resolved as follows:

```bash
git fetch origin
git rebase origin/main   # или git merge origin/main
```

**Resolving conflicts**
```bash
git add .
git rebase --continue
git push origin feature/TASK-102-payments
```
After that, the PR is ready to be merged again.

#### 7. Summary:
- Each task = separate branch = separate PR.
- Branches live briefly (1–5 days).
- Only reviewed code gets into main.
- Conflicts are resolved before merging.