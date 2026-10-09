# Loan Eligibility System — Developer Guide

This README explains how team members should work with the **Loan Eligibility System** repository.

This repository follows a **branch-based development workflow**.

---

## 1. Repository Structure

The repository uses the following branches:

```text
main
develop

feature/developer-1
feature/developer-2
feature/developer-3
feature/developer-4
feature/developer-5
```

### Branch Responsibilities

| Branch | Assigned Developer |
|---|---|
| `feature/developer-1` | Developer 1 |
| `feature/developer-2` | Developer 2 |
| `feature/developer-3` | Developer 3 |
| `feature/developer-4` | Developer 4 |
| `feature/developer-5` | Developer 5 |

Each developer should work primarily on their assigned feature branch.

---

## 2. Branch Workflow

The project follows this workflow:

```text
Developer Feature Branch
          |
          | Pull Request
          v
       develop
          |
          | Pull Request
          v
         main
```

### Important

Developers should **NOT directly push** to:

```text
develop
main
```

Developers should push their work to their assigned feature branch and create a Pull Request when their work is ready.

---

## 3. First-Time Setup

Clone the repository:

```bash
git clone https://github.com/swejangit/loan-eligibility-system.git
```

Enter the project:

```bash
cd loan-eligibility-system
```

Check the available branches:

```bash
git branch -a
```

Switch to your assigned branch.

Example for Developer 1:

```bash
git switch feature/developer-1
```

For Developer 2:

```bash
git switch feature/developer-2
```

---

## 4. Before Starting Work

Always check your current branch:

```bash
git branch
```

The branch with `*` is your current branch.

Example:

```text
* feature/developer-1
  develop
  main
```

Make sure you are working on your assigned feature branch.

Get the latest changes:

```bash
git pull
```

---

## 5. Daily Development Workflow

The normal development cycle is:

```text
Write Code
    ↓
Test Code
    ↓
git status
    ↓
git add
    ↓
git commit
    ↓
git push
```

### Check changes

```bash
git status
```

### Stage changes

```bash
git add .
```

### Commit changes

Use a meaningful commit message:

```bash
git commit -m "Add loan application validation"
```

### Push your branch

Example:

```bash
git push origin feature/developer-1
```

If your branch is already connected to the remote:

```bash
git push
```

---

## 6. Commits

Commits should represent meaningful units of work.

Examples:

```bash
git commit -m "Add user authentication"
git commit -m "Implement loan application API"
git commit -m "Add loan eligibility prediction"
git commit -m "Add admin loan management"
git commit -m "Fix loan validation"
```

Avoid unclear commit messages such as:

```bash
git commit -m "changes"
git commit -m "update"
git commit -m "done"
```

---

## 7. Pull Requests

When your assigned task is ready for integration:

```text
feature/developer-X
        |
        | Pull Request
        v
      develop
```

Create a Pull Request on GitHub.

For example:

```text
base:    develop
compare: feature/developer-1
```

The Pull Request should contain:

- What was implemented
- Important changes
- APIs added or modified
- Testing performed
- Any known issues
- Any dependencies on another developer's work

Do not merge your feature directly into `develop` without following the team's review process.

---

## 8. Develop Branch

`develop` is the **integration branch**.

It contains the combined development work after feature branches are reviewed and merged.

Example:

```text
feature/developer-1 ──┐
feature/developer-2 ──┤
feature/developer-3 ──┼──> develop
feature/developer-4 ──┤
feature/developer-5 ──┘
```

Do not use `develop` as your normal development branch.

---

## 9. Main Branch

`main` represents the stable project version.

The intended workflow is:

```text
Feature Branches
       ↓
    develop
       ↓
Testing / Integration
       ↓
      main
```

The Lead/Repository Owner handles promotion from `develop` to `main`.

Developers should not directly push to `main`.

---

## 10. Important Django Rules

### Migrations

Migration files are part of the project code and **MUST be committed**.

After changing Django models:

```bash
python manage.py makemigrations
python manage.py migrate
```

Commit the generated migration files:

```bash
git add .
git commit -m "Add loan application model migration"
git push
```

Do **NOT** add migration files to `.gitignore`.

---

## 11. Environment Variables

Never commit secrets or local environment files.

Do NOT push:

```text
.env
```

The `.env` file should remain local.

Never commit:

- Database passwords
- API keys
- Django secret keys
- ML service credentials
- Access tokens
- Personal credentials

For example:

```env
SECRET_KEY=your-secret-key
GEMINI_API_KEY=your-api-key
```

These values should remain in the local environment.

---

## 12. Files That Should Not Be Committed

Do not commit local development files such as:

```text
venv/
.venv/
__pycache__/
*.pyc
.env
db.sqlite3
.idea/
```

These should be covered by `.gitignore`.

---

## 13. Avoid Unnecessary Conflicts

Before starting work:

```bash
git pull
```

Work primarily inside your assigned module.

Avoid making unrelated changes to other developers' files.

For example, if you are working on:

```text
authentication/
```

do not unnecessarily modify:

```text
loan/
prediction/
admin/
```

unless the task requires it.

This helps reduce merge conflicts.

---

## 14. Useful Git Commands

### Check status

```bash
git status
```

### See branches

```bash
git branch
```

### See all remote branches

```bash
git branch -a
```

### Switch branch

```bash
git switch feature/developer-1
```

### Create a branch

```bash
git switch -c feature/my-feature
```

### Stage changes

```bash
git add .
```

### Commit

```bash
git commit -m "Your message"
```

### Push

```bash
git push
```

### Pull latest changes

```bash
git pull
```

### View commit history

```bash
git log --oneline
```

### See uncommitted changes

```bash
git diff
```

### See configured remote

```bash
git remote -v
```

---

## 15. Recommended Daily Workflow

Use this simple workflow:

```bash
git switch feature/developer-X
git pull

# Work on your code

git status
git add .
git commit -m "Describe your change"
git push
```

Repeat this process as you complete meaningful pieces of work.

When your task is complete:

```text
Push Branch
     ↓
Create Pull Request
     ↓
feature/developer-X → develop
     ↓
Code Review
     ↓
Approval
     ↓
Merge into develop
     ↓
Testing / Integration
     ↓
develop → main
```

---

## 16. Before Creating a Pull Request

Check the following:

- [ ] Code works locally
- [ ] Tests pass
- [ ] No `.env` or secrets are committed
- [ ] No unnecessary files are included
- [ ] Required migration files are included
- [ ] Changes are limited to the assigned task
- [ ] Commit messages are meaningful
- [ ] Branch is pushed to GitHub
- [ ] Pull Request targets `develop`
- [ ] Pull Request description explains the changes

---

## 17. Quick Workflow

```text
1. Clone repository
       ↓
2. Switch to assigned feature branch
       ↓
3. Pull latest changes
       ↓
4. Write code
       ↓
5. Test
       ↓
6. git add .
       ↓
7. git commit -m "message"
       ↓
8. git push
       ↓
9. Create Pull Request
       ↓
10. Code Review
       ↓
11. Approval
       ↓
12. Merge into develop
       ↓
13. Test integrated application
       ↓
14. Promote develop to main
```

---

## Remember

Your **feature branch** is where you develop.

`develop` is where the team's feature branches are integrated and tested.

`main` is the stable/release branch.

```text
Feature Branch
      ↓
Pull Request
      ↓
   develop
      ↓
Testing / Integration
      ↓
     main
```
