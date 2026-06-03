---
name: project-steward
description: Enforces Workforce operating procedures for progress tracking, milestone recording, and Git packaging. Use when starting a new project, updating progress, or wrapping up work.
---

# Project Steward

This skill ensures that all projects within the Workforce ecosystem follow established operating procedures for consistency, recoverability, and tracking.

## When to use
- Starting a new project.
- Updating progress on existing work.
- Recording significant completions or milestones.
- Preparing work for packaging/backing up to Git.

## Workflow

### 1. Initialize New Project
When starting a new project directory:
1. Create an `AGENTS.md` using the template below.
2. Create or copy the relevant documentation files from `workforce-backup/docs/`.
3. Set the project-specific source of truth.

### 2. Track Engineering Residue (Mandatory)
Every meaningful change MUST leave behind:
- A code diff (Git stage and commit when requested).
- An updated `TODO.md` or `PHASE_STATUS.md`.
- An updated `WORKLOG.md`.
- A decision note in `DECISIONS.md` if the direction changed.
- A changelog note in `CHANGELOG.md` if behavior changed.

### 3. Record Milestones
When a major task is complete:
1. Update `PHASE_STATUS.md`.
2. Add a comprehensive entry to `WORKLOG.md`.
3. Verify that all documentation is consistent.

### 4. Package and Backup
Before wrapping up work:
1. Review changes using `git status` and `git diff`.
2. Propose a clear, concise commit message (why, not just what).
3. Stage only relevant changes.
4. Commit changes.
5. Notify the user of the backup status.

---

## AGENTS.md Template
Use this template for new projects:

```markdown
# Project Name

## Purpose
[Concise description]

## Roles
- Primary: [Agent Name]
- Persona: [Persona Name/ID]

## Source of Truth
- [Link to project documentation]

## Workflows
- [Link to workflow docs]
```
