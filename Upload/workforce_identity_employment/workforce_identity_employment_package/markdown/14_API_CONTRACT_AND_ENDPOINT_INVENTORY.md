# API Contract and Endpoint Inventory

## Objective

Define a clear API surface for the identity/employment model so backend and frontend development can proceed against stable contracts.

## Core rule

The API must reflect the separation between:

- `User` as global platform identity
- `EmployeeProfile` as business-owned workforce identity
- `UserEmployeeLink` as linkage record
- `EmployeeRoleAssignment` as RBAC assignment anchor
- resolved access context as derived state

## API design principles

- separate personal-account endpoints from employer-managed workforce endpoints
- use `/me/...` for self-service and user-visible derived context
- use `/businesses/{business_id}/...` for business-managed workforce actions
- prefer explicit action endpoints for lifecycle and access-affecting transitions

## Endpoint groups

### 1. User self-service identity
- `GET /me/profile`
- `PATCH /me/profile`
- `GET /me/settings`
- `PATCH /me/settings`

### 2. User self-view employment and access
- `GET /me/employment-links`
- `GET /me/employee-profiles/{employee_profile_id}`
- `GET /me/pending-employment-invites`
- `GET /me/access-context`

### 3. Employer-managed employee profiles
- `POST /businesses/{business_id}/employees`
- `GET /businesses/{business_id}/employees`
- `GET /businesses/{business_id}/employees/{employee_id}`
- `PATCH /businesses/{business_id}/employees/{employee_id}`

### 4. Invite / claim / link lifecycle
- `POST /businesses/{business_id}/employees/{employee_id}/invite-link`
- `POST /businesses/{business_id}/employees/{employee_id}/resend-invite`
- `POST /businesses/{business_id}/employees/{employee_id}/cancel-invite`
- `POST /employee-link-invitations/{invite_id}/claim`
- `POST /employee-links/{link_id}/activate`
- `POST /employee-links/{link_id}/suspend`
- `POST /employee-links/{link_id}/revoke`
- `POST /employee-links/{link_id}/end`

### 5. Employee lifecycle transitions
- `POST /businesses/{business_id}/employees/{employee_id}/activate-employment`
- `POST /businesses/{business_id}/employees/{employee_id}/start-leave`
- `POST /businesses/{business_id}/employees/{employee_id}/end-leave`
- `POST /businesses/{business_id}/employees/{employee_id}/suspend-employment`
- `POST /businesses/{business_id}/employees/{employee_id}/reinstate-employment`
- `POST /businesses/{business_id}/employees/{employee_id}/terminate`
- `POST /businesses/{business_id}/employees/{employee_id}/archive`
- `POST /businesses/{business_id}/employees/{employee_id}/rehire`

### 6. Employee role assignment / RBAC
- `GET /businesses/{business_id}/employees/{employee_id}/role-assignments`
- `POST /businesses/{business_id}/employees/{employee_id}/role-assignments`
- assignment deactivate/reactivate/remove endpoints

### 7. Access context and bootstrap
- `GET /me/access-context`
- optional server-side context preference endpoints
- optional admin diagnostic access-context endpoints

### 8. Audit and history
- `GET /businesses/{business_id}/employees/{employee_id}/history`
- `GET /businesses/{business_id}/employees/{employee_id}/audit-events`
- `GET /businesses/{business_id}/audit-events`

## Error contract guidance

Use structured errors for:

- invalid link state
- invalid lifecycle transition
- unauthorized field update
- cross-business mismatch
- duplicate active link conflict
- invalid scope/location combination

## Acceptance criteria

- the API is partitioned by ownership and workflow
- lifecycle and access-affecting transitions use explicit action endpoints
- validation and permission errors are predictable
- the access-context contract is stable enough for frontend bootstrap
