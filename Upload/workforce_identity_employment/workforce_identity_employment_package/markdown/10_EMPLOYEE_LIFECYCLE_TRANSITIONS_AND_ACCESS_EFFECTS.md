# Employee Lifecycle Transitions and Access Effects

## Objective

Define a consistent workforce lifecycle model for employee records and ensure each lifecycle transition has clear effects on:

- access
- history
- audit logging
- scheduling/timekeeping eligibility
- manager and operational workflows
- rehire and relink handling

## Core rule

An employee’s lifecycle state is not just descriptive metadata.  
It directly affects whether the linked user can receive workforce access and participate in workforce operations.

## Primary employee lifecycle states

### `APPLICANT`
Pre-hire consideration. No workforce permissions.

### `PENDING_HIRE`
Onboarding / pre-active. No workforce permissions by default.

### `ACTIVE`
Currently employed and eligible for workforce participation.

### `ON_LEAVE`
Still employed but temporarily not in normal active duty. Default policy should be no workforce access unless explicitly configured otherwise.

### `SUSPENDED`
Employment continuity preserved, but operational participation/access is blocked.

### `TERMINATED`
Employment relationship ended. No workforce permissions, but history must remain.

### `ARCHIVED`
Historical inactive workforce record retained for reference and reporting.

## Access-granting rule by status

Default access-granting state:

- `ACTIVE`

Default non-access-granting states:

- `APPLICANT`
- `PENDING_HIRE`
- `ON_LEAVE`
- `SUSPENDED`
- `TERMINATED`
- `ARCHIVED`

## Distinguish employment state from link state

Examples:

- employee `ACTIVE`, link `PENDING` -> no access
- employee `ACTIVE`, link `ACTIVE` -> access may flow
- employee `SUSPENDED`, link `ACTIVE` -> no access
- employee `TERMINATED`, link `ACTIVE` -> no access

## Required lifecycle transitions

- applicant -> pending hire
- pending hire -> active
- active -> on leave
- on leave -> active
- active -> suspended
- suspended -> active
- active/on leave/suspended -> terminated
- terminated -> archived
- terminated/archived -> active only through controlled rehire workflow

## Transition semantics

### Hire activation
`PENDING_HIRE -> ACTIVE`  
Employee becomes workforce-eligible. Access may flow if link and roles are active.

### Leave start
`ACTIVE -> ON_LEAVE`  
Default: remove workforce access.

### Leave return
`ON_LEAVE -> ACTIVE`  
Access returns only if link and roles are still active.

### Suspension
`ACTIVE or ON_LEAVE -> SUSPENDED`  
Immediately remove workforce access.

### Suspension reinstatement
`SUSPENDED -> ACTIVE`  
Access eligibility restored if link and roles are active.

### Termination
`ACTIVE/ON_LEAVE/SUSPENDED -> TERMINATED`  
Immediately remove workforce access, preserve history.

### Archive
`TERMINATED -> ARCHIVED`  
Move out of normal operational views, preserve reporting and audit.

### Rehire / Reactivation
`TERMINATED or ARCHIVED -> ACTIVE` through controlled workflow.

## Transfer workflows

Transfers must be structured:

- location transfer
- department transfer
- manager reassignment
- role change

Location transfer must not leave stale location-scoped permissions behind.

## Acceptance criteria

- lifecycle states are canonical and enforced
- access changes follow lifecycle transitions
- lifecycle changes use explicit services, not loose field edits
- termination preserves history while removing access
- rehire is controlled
- transfers reevaluate scoped permissions correctly
