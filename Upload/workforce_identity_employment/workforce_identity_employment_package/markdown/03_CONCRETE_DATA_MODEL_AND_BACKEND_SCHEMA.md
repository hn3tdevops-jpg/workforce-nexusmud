# Concrete Data Model and Backend Schema

## Goal

Implement a model where:

- `User` remains the independent platform account and authentication principal
- `EmployeeProfile` becomes the business-owned workforce record
- `UserEmployeeLink` bridges a `User` to an `EmployeeProfile`
- `EmployeeRoleAssignment` anchors workforce RBAC
- workforce permissions are granted to the authenticated `User` only through:
  - an active `UserEmployeeLink`
  - an active `EmployeeProfile`
  - active scoped role assignments attached to the employee profile

## Core tables

### `users`
Global platform identity.

Suggested fields:

- `id`
- `email`
- `phone`
- `password_hash` or auth-provider references
- `first_name`
- `last_name`
- `preferred_name`
- `avatar_url`
- `status`
- `last_login_at`
- `created_at`
- `updated_at`

Rules:

- not tenant-owned
- can exist without any business relationship
- should not hold employer-owned workforce fields

### `employee_profiles`
Business-owned workforce record.

Suggested fields:

- `id`
- `business_id`
- `location_id` nullable
- `employee_code`
- `legal_first_name`
- `legal_last_name`
- `display_name`
- `work_email`
- `work_phone`
- `employment_status`
- `employment_type`
- `hire_date`
- `termination_date`
- `department_id`
- `manager_employee_profile_id`
- `created_by_user_id`
- `updated_by_user_id`
- `is_active`
- `created_at`
- `updated_at`

Rules:

- belongs to exactly one business
- may exist without a linked user
- persists after unlinking or termination

### `user_employee_links`
Bridge between platform identity and workforce identity.

Suggested fields:

- `id`
- `user_id`
- `employee_profile_id`
- `link_status`
- `invited_by_user_id`
- `activated_by_user_id`
- `ended_by_user_id`
- `linked_at`
- `unlinked_at`
- `ended_reason`
- `is_primary`
- `created_at`
- `updated_at`

Rules:

- no workforce permissions flow unless `link_status = ACTIVE`
- preserve historical ended/revoked rows if desired
- primary/default flag is UX metadata, not authorization logic

### `employee_role_assignments`
RBAC assignments attached to the employee context.

Suggested fields:

- `id`
- `employee_profile_id`
- `business_id`
- `scope_type` (`BUSINESS` or `LOCATION`)
- `location_id` nullable
- `role_id`
- `assigned_by_user_id`
- `active`
- `created_at`
- `updated_at`

Rules:

- `scope_type = BUSINESS` => `location_id IS NULL`
- `scope_type = LOCATION` => `location_id IS NOT NULL`
- assignment business must match employee profile business
- role must belong to same business and valid scope

## Permission resolution model

The permission resolver should:

1. authenticate the user
2. load active links
3. filter linked employees to access-granting states
4. load active employee role assignments
5. join to roles, role_permissions, and permissions
6. group effective permission keys by business and location

Formal rule:

> A user has a permission in a scope only if the user is actively linked to an employee profile that has an active role assignment granting that permission in that same scope.

## Service-layer invariants

- link activation requires valid user and valid employee profile
- access flows only when user, link, employee, and assignment are all active/valid
- unlinking or revoking access must invalidate derived access immediately
- business and location mismatches must be blocked
- manager chain should remain within the same business

## API guidance

Examples:

- `POST /businesses/{business_id}/employees`
- `PATCH /businesses/{business_id}/employees/{employee_id}`
- `POST /employee-links/{link_id}/activate`
- `GET /me/access-context`

## Migration direction

If roles are currently assigned directly to `user_id`, transition toward employee-linked workforce RBAC while preserving any truly global platform roles on the user if they are actually needed.
