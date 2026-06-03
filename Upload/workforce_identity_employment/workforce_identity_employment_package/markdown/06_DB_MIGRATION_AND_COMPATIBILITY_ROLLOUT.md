# Database Migration and Compatibility Rollout

## Objective

Introduce the new identity/employment model safely without breaking existing authentication, tenancy, RBAC, or active development flows.

## Migration strategy

### Stage 1 - Additive schema only
Add:

- `employee_profiles`
- `user_employee_links`
- `employee_role_assignments`

Do not remove current direct user role logic yet.

### Stage 2 - Dual-path resolution
Add new permission resolution services that can read employee-linked access while preserving existing user-based access where necessary for compatibility.

### Stage 3 - Workforce access transition
Move workforce/business/location permission derivation to employee-linked role assignments.

### Stage 4 - Cleanup and hardening
After validation, reduce or remove direct-user workforce role dependency where appropriate.

## Required migration artifacts

### New enums
- `employee_profile_status`
- `employment_type` if used
- `user_employee_link_status`
- `employee_role_scope_type`

### New tables
- `employee_profiles`
- `user_employee_links`
- `employee_role_assignments`

### New indexes
Add indexes for business, location, status, employee code, link lookup, and assignment resolver paths.

## Required constraints

### `employee_profiles`
- unique `employee_code` within a business if present
- `business_id` required

### `user_employee_links`
- FK to `users`
- FK to `employee_profiles`
- prevent duplicate active links for the same pair

### `employee_role_assignments`
- business scope requires null location
- location scope requires non-null location

### Service-enforced invariants
- assignment business must match employee profile business
- location must belong to same business
- manager must belong to same business
- no permission flow unless link is active

## Compatibility rules during rollout

- existing direct user-based role logic may remain temporarily
- new employee-linked logic must be isolated and testable
- current login/auth flows must not break
- no existing tenant data should be mutated automatically unless a backfill plan is explicitly defined

## Acceptance criteria

- new schema objects exist
- migrations apply cleanly
- no current auth flow is broken
- no current RBAC path is accidentally removed
- new tables are ready for service-layer adoption
