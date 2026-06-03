# Identity, Employee Record, and Access Linkage Model

## Purpose

The platform must treat system users and employee records as related but independent entities.

A **user account** is the person’s platform identity and is controlled by the user.

An **employee record** is a business-owned workforce record created and managed under a specific business and optionally a specific location by authorized roles.

A user may be linked to one or more employee records. When a link is active, the user receives the permissions granted through that employee record’s assigned roles and scope.

## Core principles

### Identity separation
A `user` must not be the same thing as an `employee`.

### Employee records are business-controlled
A business can create and manage employee records whether or not the person has already created a platform account.

### Linking does not merge ownership
Linking a user to an employee record does not make the employee record user-owned and does not make the user account business-owned.

### Access is derived through active linkage
Permissions are granted to the authenticated user only through active linkage to employee records that have assigned roles.

### Historical records survive employment changes
Ending employment, suspending access, or unlinking a user must revoke access without destroying business records or the user account.

## Domain separation

### User account
Represents the global person identity used for:

- authentication
- password and MFA
- personal preferences
- notification preferences
- session and device state
- personal profile settings
- account recovery

### Employee record
Represents a workforce/business identity used for:

- employment status
- hire and termination lifecycle
- business/location assignment
- role assignment context
- manager hierarchy
- department or team
- payroll-adjacent metadata hooks
- workforce scheduling eligibility
- timekeeping association
- operational permissions context
- internal notes and workforce history

## Ownership boundaries

### User-controlled
Examples:

- personal email
- password
- MFA settings
- personal preferences
- account-level profile settings

### Business-controlled
Examples:

- employment status
- department
- manager
- internal notes
- assigned location(s)
- schedule eligibility
- role assignments
- operational certifications
- work email and work phone

### Shared or synchronized fields
These must be explicitly defined field-by-field. Shared fields should never have ambiguous ownership.

## Link model

Recommended structure:

- `users`
- `employee_profiles`
- `user_employee_links`

### UserEmployeeLink responsibilities

- connects a user to an employee profile
- controls whether permissions flow
- supports invite / claim / activation / suspension / end lifecycle

## Link lifecycle states

Suggested values:

- `PENDING`
- `ACTIVE`
- `SUSPENDED`
- `REVOKED`
- `ENDED`

Permissions should flow only when `link_status = ACTIVE`.

## Supported real-world flows

### User-first
1. person creates platform account
2. employer creates employee record
3. employer links record to user
4. link becomes active
5. permissions flow

### Employer-first
1. employer creates employee record first
2. system sends invite or claim token
3. person creates or signs into user account
4. system activates link
5. permissions flow

### Employment ends
1. employee status changes to terminated or link changes to ended/revoked
2. active role resolution stops immediately
3. user account remains intact
4. employee history remains intact
