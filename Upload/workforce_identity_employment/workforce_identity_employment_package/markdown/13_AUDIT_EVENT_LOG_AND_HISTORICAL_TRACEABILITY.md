# Audit, Event Log, and Historical Traceability

## Objective

Create a consistent audit and event history foundation so the system can answer:

- who did what
- to which record
- in which business/location scope
- when it happened
- what changed
- why it changed if a reason was provided
- what access or workflow consequences followed

## Core rule

Any change that affects:

- workforce access
- employment state
- role assignment
- business/location scope
- sensitive employee data
- identity linkage
- operational accountability

must generate an auditable historical record.

## Audit vs event log distinction

### Audit log
Compliance/accountability record of important changes.

### Event log
Broader operational history of meaningful system events.

Critical security and employment-state changes must be audit events.

## Required audit coverage areas

### Identity and linkage
- invite create/resend/cancel/claim
- user_employee_link create/activate/suspend/revoke/end

### Employee lifecycle
- create
- hire activation
- leave start/end
- suspension
- reinstatement
- termination
- archive
- rehire

### Assignment and scope
- department change
- manager reassignment
- location transfer
- role assignment add/remove/deactivate/reactivate

### Sensitive field changes
- employment status
- work email/work phone
- schedule eligibility
- compliance flags
- self-service updates
- restricted private field changes

### Access-impacting system events
- access context invalidation
- authorization denied events where policy supports logging

## Suggested data model

### `audit_events`
Suggested fields:

- `id`
- `event_key`
- `actor_type`
- `actor_user_id`
- `actor_employee_profile_id`
- `target_type`
- `target_id`
- `business_id`
- `location_id`
- `related_user_id`
- `related_employee_profile_id`
- `request_id`
- `source`
- `reason`
- `before_json`
- `after_json`
- `metadata_json`
- `created_at`

## Event key taxonomy

Examples:

- `user_employee_link.activate`
- `employee_profile.terminate`
- `employee_role_assignment.add`
- `employee_profile.transfer.location`
- `employee_profile.private_field.update`
- `authorization.denied`

## Actor attribution rules

Actors should be one of:

- `USER`
- `EMPLOYEE`
- `SYSTEM`
- `JOB`
- `API_CLIENT`
- `SYNC_PROCESS`
- `ADMIN_TOOL`

## Immutability rules

Audit history should be append-only in normal operation. Corrections should be new events, not silent edits to prior audit rows.

## Visibility rules

Audit history is sensitive and must be permissioned.

- limited self-history for users
- business-scoped authorized admin history
- restricted/private audit streams where needed for sensitive events

## Acceptance criteria

- all critical identity, linkage, lifecycle, RBAC, and sensitive-field changes produce auditable history
- audit records include actor, scope, target, and change context
- business/location attribution is preserved
- historical access-affecting transitions can be reconstructed later
