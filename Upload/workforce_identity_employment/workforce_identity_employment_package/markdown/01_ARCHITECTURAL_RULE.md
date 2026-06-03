# Architectural Rule

> User accounts are independent, user-controlled platform identities. Employee profiles are business-controlled workforce records. Active linkage between them is the mechanism that grants scoped workforce permissions to the authenticated user.

## What this means

- a person can have a platform account without being employed
- an employer can create an employee file before the user account exists
- linking does not merge ownership
- users do not automatically own their employee file
- businesses do not automatically control the person’s full platform account
- workforce access is derived, not assumed

## The four core entities

### 1. User
The authentication principal and personal account.

### 2. EmployeeProfile
The employer-owned workforce record scoped to a business and optionally a location.

### 3. UserEmployeeLink
The relationship record that determines whether the user is actively linked to the employee profile.

### 4. EmployeeRoleAssignment
The RBAC attachment that gives the employee profile business- or location-scoped permissions.

## Access rule

A user gets workforce access only if all of the following are true:

- the user is active
- the user has an active link to an employee profile
- the employee profile is in an access-granting status
- the employee profile has active scoped role assignments
- those roles grant the requested permission in the requested scope

## Safety consequences

- unlinking must revoke derived access immediately
- termination must not delete the user account
- deleting or disabling a user must not silently destroy employer-owned history
- tenant isolation must remain strict across businesses and locations
