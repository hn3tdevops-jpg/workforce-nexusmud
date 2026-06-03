# Package Index

## What this package covers

This package defines the Workforce architecture rule that **User accounts are independent from Employee files**, with access flowing through an active linkage model.

## Core concepts

- `User` = global platform identity
- `EmployeeProfile` = business-controlled workforce identity
- `UserEmployeeLink` = bridge between the two
- `EmployeeRoleAssignment` = employee-scoped RBAC grants
- effective access = derived from active link + active employee + active role assignment + tenant scope

## File map

### Foundation
- `01_ARCHITECTURAL_RULE.md`
- `02_IDENTITY_EMPLOYEE_ACCESS_MODEL.md`
- `03_CONCRETE_DATA_MODEL_AND_BACKEND_SCHEMA.md`

### Repo execution
- `04_COPILOT_IMPLEMENTATION_PROMPT.md`
- `17_CONCRETE_IMPLEMENTATION_ROADMAP.md`
- `19_COPILOT_EXECUTION_SEQUENCE.md`

### Master-plan drops
- `05_MASTER_PLAN_IDENTITY_EMPLOYMENT_SEPARATION.md`
- `06_DB_MIGRATION_AND_COMPATIBILITY_ROLLOUT.md`
- `07_FRONTEND_BOOTSTRAP_CONTEXT_SWITCHING_AND_FIELD_OWNERSHIP_UX.md`
- `08_INVITE_CLAIM_AND_LINK_WORKFLOW.md`
- `09_RBAC_INTEGRATION_AND_EFFECTIVE_PERMISSION_RESOLVER.md`
- `10_EMPLOYEE_LIFECYCLE_TRANSITIONS_AND_ACCESS_EFFECTS.md`
- `11_SELF_SERVICE_VS_EMPLOYER_MANAGED_FIELD_PERMISSIONS.md`
- `12_MULTI_EMPLOYMENT_MULTI_BUSINESS_AND_TRANSFER_EDGE_CASES.md`
- `13_AUDIT_EVENT_LOG_AND_HISTORICAL_TRACEABILITY.md`
- `14_API_CONTRACT_AND_ENDPOINT_INVENTORY.md`
- `15_DATABASE_SCHEMA_DICTIONARY_AND_TABLE_CONTRACTS.md`
- `16_SERVICE_LAYER_ARCHITECTURE_AND_AUTHORIZATION_HELPERS.md`

### Consolidated reference
- `18_CONSOLIDATED_MASTER_SPEC.md`
- `REFERENCE_CATALOGUE.pdf`

## Best use pattern

- read the architectural rule first
- align schema and service implementation second
- wire RBAC and access resolution next
- integrate frontend bootstrap after the resolver is stable
- use the execution sequence for small, reviewable build slices
