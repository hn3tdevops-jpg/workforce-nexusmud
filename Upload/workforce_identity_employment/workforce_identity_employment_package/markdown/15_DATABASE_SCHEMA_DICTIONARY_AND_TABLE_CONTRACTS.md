# Database Schema Dictionary and Table-by-Table Contract

## Objective

Create a canonical schema reference for the identity/employment model so backend implementation, migrations, services, and tests all use the same entity definitions and relationship rules.

## Schema domains

1. global identity
2. workforce identity
3. linkage and onboarding
4. RBAC attachment
5. lifecycle and assignment context
6. audit/history
7. optional change-request support

## Global identity domain

### `users`
Purpose: platform-level authenticated identity.

Responsibilities:

- authentication principal
- login identity
- user preferences/settings
- personal account state
- link anchor to one or more employee profiles

Important rules:

- global, not tenant-owned
- must exist independently of employment
- must not be overloaded with business-owned employee data

## Workforce identity domain

### `employee_profiles`
Purpose: employer-owned workforce record representing a person inside a business context.

Responsibilities:

- employment identity
- lifecycle status
- org placement
- scheduling/timekeeping participation anchor
- RBAC assignment anchor
- operational/managerial identity inside a business

Important rules:

- belongs to exactly one business
- may optionally be location-scoped
- may exist without any linked user
- persists after unlinking or termination
- is not the authentication principal

## Linkage and onboarding domain

### `user_employee_links`
Purpose: relationship between platform user and employee profile.

Responsibilities:

- represent whether a user is linked
- control whether access may flow
- preserve linkage history
- support activation, suspension, revocation, and end states

Important rules:

- no workforce permissions flow unless `link_status = ACTIVE`
- primary/default link is UX metadata, not auth logic

### Optional `employee_link_invitations`
Purpose: pending invite/claim record for employer-first onboarding.

## RBAC attachment domain

### `roles`
Defines named role bundles.

### `permissions`
Defines individual permission keys.

### `role_permissions`
Joins roles to permissions.

### `employee_role_assignments`
Purpose: attach RBAC roles to employee context rather than directly to raw user.

Important rules:

- this is the primary workforce RBAC assignment table
- business and scope integrity must hold
- inactive assignments do not grant access

## Audit/history domain

### `audit_events`
Purpose: immutable or append-only historical records of important changes.

Important rules:

- preserve actor, target, scope, and change context
- remain append-only in normal practice

## Derived access model

### Effective access context
Derived from:

- `users`
- `user_employee_links`
- `employee_profiles`
- `employee_role_assignments`
- `roles`
- `role_permissions`
- `permissions`

Should be computed, not treated as unconstrained stored truth.

## Relationship summary

```text
users
  └── user_employee_links
        └── employee_profiles
              └── employee_role_assignments
                    └── roles
                          └── role_permissions
                                └── permissions
```

## Recommended enum dictionary

- `user_status`: `ACTIVE`, `SUSPENDED`, `DISABLED`
- `employee_profile_status`: `APPLICANT`, `PENDING_HIRE`, `ACTIVE`, `ON_LEAVE`, `SUSPENDED`, `TERMINATED`, `ARCHIVED`
- `employment_type`: `FULL_TIME`, `PART_TIME`, `CONTRACTOR`, `TEMP`, `SEASONAL`
- `user_employee_link_status`: `PENDING`, `ACTIVE`, `SUSPENDED`, `REVOKED`, `ENDED`
- `employee_role_scope_type`: `BUSINESS`, `LOCATION`

## Key indexing requirements

High priority indexes:

- `users.email`
- `users.phone`
- `employee_profiles.business_id`
- `employee_profiles.location_id`
- `employee_profiles.employment_status`
- `employee_profiles.employee_code`
- `user_employee_links.user_id`
- `user_employee_links.employee_profile_id`
- `user_employee_links.link_status`
- `employee_role_assignments.employee_profile_id`
- `employee_role_assignments.business_id`
- `employee_role_assignments.location_id`
- `employee_role_assignments.role_id`
- `employee_role_assignments.scope_type`
- `employee_role_assignments.active`
- audit event lookup indexes
