# Copilot Prompt - Implement User / Employee Separation with Linked Permission Resolution

You are working in the Workforce backend repository.

Your task is to implement a new identity and workforce access model where:

- `User` remains the independent platform account and authentication principal
- `EmployeeProfile` becomes the business-owned workforce record
- `UserEmployeeLink` bridges a `User` to an `EmployeeProfile`
- workforce permissions are granted to the authenticated `User` only through:
  - an **ACTIVE** `UserEmployeeLink`
  - an **ACTIVE** `EmployeeProfile`
  - active scoped role assignments attached to the employee profile

This must preserve tenant isolation, RBAC correctness, and auditability.

## Required architecture rules

1. Do **not** merge `User` and employee data into one model.
2. Do **not** make employee records the authentication principal.
3. Do **not** grant workforce access directly from raw `user_id` if it should come from employment context.
4. Business-controlled employee records must remain separate from user-controlled account data.
5. Access must be revoked immediately when a link is suspended, revoked, or ended.
6. Never weaken tenant isolation or RBAC scope rules.

## Target data model

Implement:

- `EmployeeProfile`
- `UserEmployeeLink`
- `EmployeeRoleAssignment`

Use the fields, states, scope rules, and constraints described in this package.

## Permission resolution requirement

A user has workforce permissions in a scope only if all of the following are true:

- `User` is active
- `UserEmployeeLink.link_status == ACTIVE`
- `EmployeeProfile.is_active == True`
- `EmployeeProfile.employment_status == ACTIVE`
- `EmployeeRoleAssignment.active == True`

Return a structured access context for frontend bootstrap and service authorization.

## API requirements

Add minimal endpoints in existing repo style:

### Employee profile endpoints
- `POST /businesses/{business_id}/employees`
- `GET /businesses/{business_id}/employees`
- `GET /businesses/{business_id}/employees/{employee_id}`
- `PATCH /businesses/{business_id}/employees/{employee_id}`

### Link lifecycle endpoints
- `POST /businesses/{business_id}/employees/{employee_id}/invite-link`
- `POST /employee-links/{link_id}/activate`
- `POST /employee-links/{link_id}/suspend`
- `POST /employee-links/{link_id}/revoke`
- `POST /employee-links/{link_id}/end`

### Current access endpoint
- `GET /me/access-context`

## Field ownership rules

### User-owned
Keep on `User`:
- login identity
- password/auth provider
- MFA/security settings
- personal preferences
- personal notification settings
- account-level profile settings

### Business-owned
Keep on `EmployeeProfile`:
- employment status
- department
- manager
- internal notes
- work email / work phone
- location assignment
- schedule eligibility
- workforce metadata
- job title / organizational display values if business-controlled

### Important rule
Do not let linked users arbitrarily edit their whole employee record just because they are linked to it.

## Audit events

Write audit events for:

- employee profile create/update/status change
- user_employee_link create/activate/suspend/revoke/end
- employee role assignment add/remove/deactivate

## Migration strategy

1. add schema
2. add service layer logic
3. add access resolver
4. add `GET /me/access-context`
5. transition workforce access away from direct raw user-based role assumptions where appropriate

## Tests

Add tests for:

- user exists without employee profile
- employee profile exists without user
- active link grants derived permissions
- suspended/revoked/ended links remove permissions
- terminated employee profile prevents permission flow
- location and business isolation
- linked user cannot arbitrarily edit employer-owned fields
- audit rows are written for access-affecting transitions

## Implementation rules

- reuse repository patterns
- prefer small, reviewable changes
- avoid unrelated refactors
- do not weaken RBAC or tenant safety checks

## Deliverables

Produce:

1. models
2. migrations
3. schemas
4. services
5. API routes
6. audit integration
7. tests
