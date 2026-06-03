# Consolidated Master Spec - Workforce Identity / Employment Architecture

This document consolidates the package into one long-form reference.

## 1. Architectural foundation

The Workforce platform must separate:

- global platform identity
- business-controlled workforce identity
- the active link between them
- employee-scoped RBAC assignment
- derived effective access context

### Core rule

> User accounts are independent, user-controlled platform identities. Employee profiles are business-controlled workforce records. Active linkage between them is the mechanism that grants scoped workforce permissions to the authenticated user.

## 2. Entity model

### User
Global authentication principal.

### EmployeeProfile
Business-owned workforce record.

### UserEmployeeLink
Relationship record that determines whether access may flow.

### EmployeeRoleAssignment
RBAC attachment for workforce access in business or location scope.

## 3. Access resolution

A user has workforce access only when:

- user is active
- link is active
- employee status is access-granting
- employee role assignment is active
- permission exists in requested business/location scope

## 4. Core implementation themes

### Identity / employment separation
Do not merge user and employee records.

### Field ownership
Do not blur self-service and employer-managed fields.

### Employee-linked RBAC
Do not use raw `user_id` as the only workforce permission anchor.

### Lifecycle-aware access
Employment state changes must affect access.

### Auditability
All critical linkage, lifecycle, RBAC, and sensitive-field changes must be historically traceable.

## 5. Key domains covered in this package

- conceptual model
- concrete schema
- Copilot implementation prompt
- master-plan sections
- migration strategy
- frontend bootstrap
- invite/claim workflow
- RBAC resolver
- lifecycle transitions
- self-service boundaries
- multi-business edge cases
- audit and historical traceability
- API contract
- schema dictionary
- service-layer architecture
- concrete implementation roadmap

## 6. Recommended implementation sequence

1. add schema
2. add models
3. add service scaffolding
4. add employee CRUD
5. add link workflows
6. add employee role assignment workflows
7. add effective access resolver
8. add `/me/access-context`
9. add lifecycle transitions
10. add self-service boundaries
11. add audit/history APIs
12. integrate frontend context switching
13. clean up legacy direct-user workforce auth shortcuts

## 7. Final intent

This model should become the Workforce foundation for:

- scheduling
- timekeeping
- shift swap / marketplace
- housekeeping operations
- inspections
- communications
- CRM assignment contexts
- timeline/activity feeds
- future workforce modules that require accurate scoped access
