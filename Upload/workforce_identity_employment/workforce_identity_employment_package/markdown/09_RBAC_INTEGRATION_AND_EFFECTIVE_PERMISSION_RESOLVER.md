# RBAC Integration and Effective Permission Resolver

## Objective

Integrate the identity/employment separation model into the RBAC system so that workforce permissions are resolved correctly, safely, and consistently across all modules.

## Core rule

A user does **not** receive workforce permissions merely because they have a platform account.

A user receives workforce permissions only when:

- the user is authenticated and active
- the user has an active link to an employee profile
- the employee profile is in an access-granting state
- the employee profile has active role assignments
- the assigned roles contain the requested permissions in the requested scope

## RBAC architecture alignment

Existing structures:

- `roles`
- `permissions`
- `role_permissions`

Required adjustment:

- workforce/business/location access should resolve primarily from **employee-linked role assignments**, not only direct assignments on raw `user_id`

## Permission resolution pipeline

1. authenticate user
2. validate user status
3. load active `UserEmployeeLink` records
4. filter active employee profiles
5. load active `EmployeeRoleAssignment` rows
6. resolve `roles -> role_permissions -> permissions`
7. build scoped access context by business and location
8. authorize the request against that resolved context

## Effective access rules

### Business-scoped role
Grants permissions within that business and not outside it.

### Location-scoped role
Grants permissions only for that location.

### No scope leakage
Permissions from one business/location must never leak into another.

### No inactive-link access
If link status is not `ACTIVE`, no employee-derived permissions may be granted.

### No inactive-employee access
If employee profile is terminated, archived, or otherwise not access-granting, no workforce permissions may be granted through it.

## Access-granting employment states

Default access-granting state:

- `ACTIVE`

Optional future policy may allow `ON_LEAVE`, but only if explicitly implemented.

## Resolver output requirements

Return a structured effective access context usable by:

- API authorization
- frontend bootstrap
- context switching
- audit logging
- troubleshooting and diagnostics

## Authorization usage rules

- endpoints must check permission keys against resolved access, not guessed titles
- services must also enforce permission checks
- frontend gating must use resolved permission keys from the backend

## Immediate revocation rule

When any of the following occurs:

- link suspended
- link revoked
- link ended
- employee terminated or moved to non-access-granting status
- employee role assignment removed/deactivated

the system must stop granting those permissions immediately or on the next authoritative access check.

## Build order

- define employee-linked workforce RBAC as canonical rule
- add effective access resolver service
- add authorization helper functions
- update protected endpoints and services to use resolved checks
- add compatibility layer for legacy direct-user workforce role logic during transition
- add cache invalidation if caching is used
- add diagnostic/explainability support
