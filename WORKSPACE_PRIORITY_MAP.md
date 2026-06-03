# Workspace Priority Map

This file is the short operating guide for where to look first when deciding what matters most in the Workforce workspace.

## 1) Start here first
- `file 'Workforce-Console/docs/00_START_HERE/README.md'`
- `file 'Workforce-Console/docs/00_START_HERE/CANONICAL_SOURCES.md'`
- `file 'Workforce-Console/docs/00_START_HERE/CURRENT_STATE.md'`
- `file 'Workforce-Console/docs/00_START_HERE/EXECUTION_QUEUE.md'`

These define the operating layer, the source-of-truth map, the current state, and the approved work order.

## 2) Mission and roadmap
- `file 'workforce-backup/docs/plans/HN3T_MASTER_PLAN.md'`
- `file 'workforce-backup/docs/plans/PHASE_STATUS.md'`
- `file 'workforce-backup/docs/DECISIONS.md'`

These anchor direction, phase tracking, and decision history.

## 3) Operating rules
- `file 'workforce-backup/docs/PROJECT_OPERATING_SYSTEM.md'`
- `file 'workforce-dev/AGENTS.md'`
- `file 'workforce-dev/GEMINI.md'`
- `file 'workforce-dev/README.md'`

These keep execution tight, recoverable, and aligned with the repo's procedures.

## 4) Active implementation surfaces
- `file 'workforce-backup/docs/ARCHITECTURE.md'`
- `file 'workforce-backup/docs/MIGRATION_PLAN.md'`
- `file 'workforce-backup/docs/RBAC_SUMMARY.txt'`
- `file 'workforce-dev/docs/plans/BUILD_MENU_PLANNING_QUEUE_PLAN.md'`

These are the most likely places where actual work should be aligned next.

## 5) Frontend execution evidence
- `file 'Workforce-Console/docs/ADMIN/frontend/PROGRESS_REPORT_FRONTEND.md'`
- `file 'Workforce-Console/docs/ADMIN/frontend/FRONTEND_EXECUTION_TRACKER.md'`

Use these when validating UI progress and avoiding duplicated effort.

## 6) Reference and archive material
- `file 'Workforce-Docs/00_START_HERE/README.md'`
- `file 'Workforce-Docs/00_START_HERE/CURRENT_STATE.md'`
- `file 'Workforce-Docs/00_START_HERE/OPEN_DECISIONS.md'`

Useful for reconciliation, but not the first stop unless you are resolving history or documentation drift.

## Quick rule
If a task touches planning, execution order, or project direction, check sections 1–3 before changing code. If it touches implementation, check section 4 next. If it touches UI validation, check section 5. If it is historical or editorial, check section 6.
