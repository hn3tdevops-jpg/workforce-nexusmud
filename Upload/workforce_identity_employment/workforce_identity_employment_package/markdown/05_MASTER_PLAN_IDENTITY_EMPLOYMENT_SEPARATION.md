# Identity / Employment Separation and Linked Access

## Objective

Separate global platform identity from employer-controlled workforce identity.

A **User** is the independent platform account and authentication principal.

An **EmployeeProfile** is a business-controlled workforce record under a business and optionally a location.

A **UserEmployeeLink** connects the two.

Workforce permissions are granted to the authenticated user only through:

- an active user-to-employee link
- an active employee profile
- active scoped role assignments attached to that employee profile

This model must preserve tenant isolation, RBAC correctness, historical records, and clear ownership boundaries.

## Architectural Rule

> User accounts are independent, user-controlled platform identities. Employee profiles are business-controlled workforce records. Active linkage between them is the mechanism that grants scoped workforce permissions to the authenticated user.

## Core principles

- a user can exist without any employee profile
- an employer can create an employee profile before a user account exists
- linking does not merge ownership
- businesses do not own user accounts
- users do not automatically own or control their employee files
- workforce access must be revoked immediately when the link is no longer active
- historical employee records must remain intact after unlinking or termination

## Ownership model

### User-controlled
- authentication identity
- password / auth provider
- MFA / security settings
- personal preferences
- personal notification settings
- user-owned profile settings

### Business-controlled
- employment status
- business/location assignment
- manager hierarchy
- department/team
- work email / work phone
- internal workforce metadata
- job/role assignment context
- scheduling and operational eligibility

### Shared data rule
Shared fields must be explicitly defined field-by-field. Do not use vague shared ownership.

## Permission resolution rule

A user has workforce permissions in a scope only if all of the following are true:

- the user is active
- the user has an active `UserEmployeeLink`
- the linked `EmployeeProfile` is active
- the employee profile is in an access-granting employment state
- the employee profile has active scoped role assignments
- the role assignments resolve to permissions in the requested scope

## Required security rules

- unlinking must immediately revoke derived workforce permissions
- terminating employment must not delete the user account
- deleting or disabling a user must not silently destroy employer-owned history
- being linked to an employee profile does not grant unrestricted edit rights to that employee file
- tenant isolation must remain strict across all businesses and locations
- business-controlled endpoints must never expose or overwrite unrelated user-private account data
- workforce access must not be granted directly from raw `user_id` where employment context is required

## Build order - Identity / Employment Separation

- add `EmployeeProfile` model and schema
- add `UserEmployeeLink` model and schema
- add `EmployeeRoleAssignment` model and schema
- create migrations
- add service to create employee profiles independently of user accounts
- add service to create and manage user-employee links
- add activation/suspension/revocation/end lifecycle handling for links
- add effective access resolution service
- add `GET /me/access-context`
- add employee profile CRUD endpoints
- add link lifecycle endpoints
- enforce field ownership boundaries
- add audit events
- add tests for grant/revoke and tenant isolation
