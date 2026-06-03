# Workforce Identity / Employment Architecture Package

This package compiles the identity, employee-record, linkage, RBAC, lifecycle, API, and implementation planning work for the Workforce platform.

## Package purpose

This bundle is designed to give you a clean handoff set that can be used for:

- master-plan integration
- Copilot / coding-agent execution
- backend schema and service implementation
- frontend access-context integration
- audit and history design
- phased rollout planning

## Package contents

- `markdown/00_PACKAGE_INDEX.md` - file guide and recommended read order
- `markdown/01_ARCHITECTURAL_RULE.md` - one-page core rule
- `markdown/02_IDENTITY_EMPLOYEE_ACCESS_MODEL.md` - foundational conceptual model
- `markdown/03_CONCRETE_DATA_MODEL_AND_BACKEND_SCHEMA.md` - backend-ready schema section
- `markdown/04_COPILOT_IMPLEMENTATION_PROMPT.md` - repo execution prompt for Copilot
- `markdown/05_MASTER_PLAN_IDENTITY_EMPLOYMENT_SEPARATION.md` - master-plan section
- `markdown/06_DB_MIGRATION_AND_COMPATIBILITY_ROLLOUT.md`
- `markdown/07_FRONTEND_BOOTSTRAP_CONTEXT_SWITCHING_AND_FIELD_OWNERSHIP_UX.md`
- `markdown/08_INVITE_CLAIM_AND_LINK_WORKFLOW.md`
- `markdown/09_RBAC_INTEGRATION_AND_EFFECTIVE_PERMISSION_RESOLVER.md`
- `markdown/10_EMPLOYEE_LIFECYCLE_TRANSITIONS_AND_ACCESS_EFFECTS.md`
- `markdown/11_SELF_SERVICE_VS_EMPLOYER_MANAGED_FIELD_PERMISSIONS.md`
- `markdown/12_MULTI_EMPLOYMENT_MULTI_BUSINESS_AND_TRANSFER_EDGE_CASES.md`
- `markdown/13_AUDIT_EVENT_LOG_AND_HISTORICAL_TRACEABILITY.md`
- `markdown/14_API_CONTRACT_AND_ENDPOINT_INVENTORY.md`
- `markdown/15_DATABASE_SCHEMA_DICTIONARY_AND_TABLE_CONTRACTS.md`
- `markdown/16_SERVICE_LAYER_ARCHITECTURE_AND_AUTHORIZATION_HELPERS.md`
- `markdown/17_CONCRETE_IMPLEMENTATION_ROADMAP.md`
- `markdown/18_CONSOLIDATED_MASTER_SPEC.md` - full combined reference
- `markdown/19_COPILOT_EXECUTION_SEQUENCE.md` - slice-by-slice build order
- `REFERENCE_CATALOGUE.pdf` - PDF catalogue explaining purpose and correct usage of each file

## Recommended read order

1. `01_ARCHITECTURAL_RULE.md`
2. `02_IDENTITY_EMPLOYEE_ACCESS_MODEL.md`
3. `03_CONCRETE_DATA_MODEL_AND_BACKEND_SCHEMA.md`
4. `09_RBAC_INTEGRATION_AND_EFFECTIVE_PERMISSION_RESOLVER.md`
5. `10_EMPLOYEE_LIFECYCLE_TRANSITIONS_AND_ACCESS_EFFECTS.md`
6. `11_SELF_SERVICE_VS_EMPLOYER_MANAGED_FIELD_PERMISSIONS.md`
7. `14_API_CONTRACT_AND_ENDPOINT_INVENTORY.md`
8. `15_DATABASE_SCHEMA_DICTIONARY_AND_TABLE_CONTRACTS.md`
9. `16_SERVICE_LAYER_ARCHITECTURE_AND_AUTHORIZATION_HELPERS.md`
10. `17_CONCRETE_IMPLEMENTATION_ROADMAP.md`
11. `04_COPILOT_IMPLEMENTATION_PROMPT.md`

## Suggested repo usage

- Use the master-plan sections to update `HN3T_MASTER_PLAN.md`
- Use the Copilot prompt and execution sequence for small reviewable patches
- Use the schema, API, service, and RBAC sections as implementation references
- Use the PDF as a human-readable navigation guide and reference catalogue
