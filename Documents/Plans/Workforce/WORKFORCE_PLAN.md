# Workforce — Actionable Execution Plan
*Created: 2026-04-28 from Google Drive material review*

---

## Current Status

| Area | Status | Notes |
|---|---|---|
| **Backend** | 🟢 ONLINE | Running locally at localhost:8000 |
| **Codebase** | 🟢 ACTIVE | workforce-backup used as primary backend |
| **Frontend** | 🟢 ACTIVE | workforce-showcase console artifact updated |
| **Planning docs** | ✅ READY | specs/ published for bootstrap and employee-link |
| **Source files** | ✅ READY | 12-room Silver Sands layout seeded |

---

## Phase 0 — Restore Backend + Baseline (COMPLETE)

### 0.1 — Restore Backend (COMPLETE)
Backend restored locally on Zo Computer.

### 0.2 — Get the Codebase (COMPLETE)
Workforce-backup identified as active repository.

### 0.3 — Run Migrations + Seed (COMPLETE)
Migrations applied and Silver Sands layout seeded.
Verified: /health, login, /api/v1/bootstrap, /api/v1/rooms/, /api/v1/tasks/

---

## Phase 1 — Frontend Shell + Auth

**Source:** Workforce Frontend Build Master Prompt

### Deliverables
- [ ] React + TypeScript app
- [ ] Login page → POST /api/v1/auth/login
- [ ] Auth context store (token, session hydration via GET /api/v1/auth/me)
- [ ] Protected route wrapper
- [ ] App shell: top bar + collapsible sidebar + business context
- [ ] Permission-aware navigation

### Routes
| Route | Purpose |
|---|---|
| /login | Auth page |
| /app | Protected shell |
| /app/dashboard | User context, roles, quick links |
| /app/session | Auth state inspector |
| /app/rooms | Live room list |
| /app/tasks | Live task list |
| /app/assignments | Live assignments |
| /app/shifts | Live shifts |

### Tech stack
- React + TypeScript
- Generated API client from live OpenAPI
- Dark-theme CSS tokens
- hasPermission(name), hasRole(name) helpers

---

## Phase 2 — HKOps / Silver Sands Room Board

**Source:** silver_sands_operations_blueprint.md

### Property Layout
```
Silver Sands Motel
└── Building 1 / Floor 1
    ├── North Sector: Rooms 7-12
    └── South Sector: Rooms 1-6
```

### Room Status Flow
Dirty → Cleaning → Clean → Inspected

### Features
- [ ] Room cards with status, maintenance flags, last_cleaned
- [ ] Sector-grouped view (North / South)
- [ ] Bulk status update actions
- [ ] Maintenance issue capture per room
- [ ] Asset inventory per room

---

## Phase 3 — Identity / Employment Separation

**Source:** workforce_identity_employment_package/ (19 markdown files)

### Core model
- User = global platform identity
- EmployeeProfile = business-controlled workforce identity
- UserEmployeeLink = bridge
- EmployeeRoleAssignment = employee-scoped RBAC
- Access = active link + active employee + active role assignment + tenant scope

### Execution order
1. 01_ARCHITECTURAL_RULE.md — User ≠ Employee principle
2. 03_CONCRETE_DATA_MODEL_AND_BACKEND_SCHEMA.md — schema
3. 06_DB_MIGRATION_AND_COMPATIBILITY_ROLLOUT.md — migration path
4. 09_RBAC_INTEGRATION_AND_EFFECTIVE_PERMISSION_RESOLVER.md — access
5. 08_INVITE_CLAIM_AND_LINK_WORKFLOW.md — onboarding
6. 07_FRONTEND_BOOTSTRAP_CONTEXT_SWITCHING_AND_FIELD_OWNERSHIP_UX.md — UI

---

## Phase 4 — AI Gateway Module

**Source:** AI_GATEWAY_MODULE_SPEC.md

### Tables
- ai_provider_accounts — provider config per scope
- ai_model_profiles — model_name, purpose, prompt_template_id
- ai_prompt_templates — module_key, prompt_key, version
- ai_tool_definitions — tool_key, module_key, schema_json
- ai_request_logs — trace, latency, usage

### Service methods
- generate_reply()
- extract_structured_design_items()
- run_validation_pass()
- summarize_thread()

---

## Priority Summary

| # | Task | Blocker | Status |
|---|---|---|---|
| 0 | Get backend online | NO | ✅ COMPLETE |
| 1a | Clone/rebuild workforce repo | NO | ✅ COMPLETE |
| 1b | Run migrations + seed | NO | ✅ COMPLETE |
| 2 | Frontend shell + auth | NO | 🟢 IN PROGRESS |
| 3 | HKOps room board | NO | 🟢 IN PROGRESS |
| 4 | Identity/Employment separation | NO | 3-5 days |
| 5 | AI Gateway module | NO | 2-3 days |

---

