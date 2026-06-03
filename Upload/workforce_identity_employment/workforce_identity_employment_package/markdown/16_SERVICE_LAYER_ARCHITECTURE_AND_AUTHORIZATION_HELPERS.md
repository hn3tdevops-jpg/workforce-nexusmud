# Service-Layer Architecture and Authorization Helper Contract

## Objective

Define a concrete backend implementation pattern for the identity/employment model so business logic stays consistent, secure, testable, and reusable across modules.

## Core rule

Authorization, linkage, lifecycle, and ownership rules must be enforced in the **service layer**, not only in routers, frontend code, ORM hooks, or one-off helpers.

## Recommended service domains

### 1. Identity services
User-owned account/profile operations.

### 2. Employee profile services
Employer-managed workforce record creation, update, lookup, and lifecycle actions.

### 3. Link services
Invite, claim, activate, suspend, revoke, and end workflows.

### 4. Role assignment services
Employee-linked RBAC assignment management.

### 5. Access resolution services
Effective permission and context resolver for authenticated users.

### 6. Field ownership / visibility services
Validation and shaping of self-service vs employer-managed fields.

### 7. Audit/event services
Consistent writing of audit and domain events.

### 8. Context/bootstrap services
Support `GET /me/access-context` and related bootstrap behavior.

## Suggested service functions

### Identity
- `get_user_profile(user_id)`
- `update_user_profile(user_id, payload)`

### Employee profile
- `create_employee_profile(actor, business_id, payload)`
- `get_employee_profile(actor, business_id, employee_id)`
- `list_employee_profiles(actor, business_id, filters)`
- `update_employee_profile(actor, business_id, employee_id, payload)`

### Link lifecycle
- `create_pending_employee_link(...)`
- `create_employee_link_invite(...)`
- `claim_employee_link_invite(...)`
- `activate_employee_link(...)`
- `suspend_employee_link(...)`
- `revoke_employee_link(...)`
- `end_employee_link(...)`

### Lifecycle transitions
- `activate_employment(...)`
- `start_employee_leave(...)`
- `end_employee_leave(...)`
- `suspend_employment(...)`
- `reinstate_employment(...)`
- `terminate_employment(...)`
- `archive_employee_profile(...)`
- `rehire_employee(...)`

### Transfer and assignment
- `transfer_employee_location(...)`
- `change_employee_manager(...)`
- `change_employee_department(...)`

### Role assignment
- `add_employee_role_assignment(...)`
- `list_employee_role_assignments(...)`
- `deactivate_employee_role_assignment(...)`
- `reactivate_employee_role_assignment(...)`
- `remove_employee_role_assignment(...)`

### Effective access resolver
- `resolve_effective_access_for_user(user_id)`
- `get_current_access_context(user_id, preferred_scope=None)`

### Authorization helpers
- `require_permission(actor_context, permission_key, business_id, location_id=None)`
- `has_permission(actor_context, permission_key, business_id, location_id=None)`

## Actor context object

Suggested contents:

- `actor.user_id`
- `actor.access_context`
- `actor.current_business_id`
- `actor.current_location_id`
- `actor.request_id`

## Transaction boundary rules

For access-affecting changes, authoritative services should:

1. validate actor authorization
2. load and validate current state
3. validate transition or ownership rules
4. apply state mutation
5. write audit event
6. invalidate affected access context/cache
7. return resulting state

## Domain error guidance

Use structured service errors for:

- authorization denied
- invalid state transition
- ownership violation
- cross-business mismatch
- scope mismatch
- duplicate conflict
- not found in scope
- invalid invitation/token state

## Acceptance criteria

- the repo has clear service boundaries for identity/employment workflows
- authorization logic is reusable and consistent
- audit and access invalidation happen in the same authoritative workflow
- routers stay thin and predictable
