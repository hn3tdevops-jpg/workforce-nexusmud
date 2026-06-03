# Multi-Employment, Multi-Business, and Transfer Edge-Case Rules

## Objective

Define how the system handles users who may be linked to:

- multiple employee profiles
- multiple locations
- multiple businesses
- sequential or overlapping employment relationships
- transfers, rehiring, and mixed-scope role assignments

## Core rule

A single user account may be linked to zero, one, or many employee profiles over time.

Each employee profile remains a separate business-controlled workforce record.

Access is always resolved from:

- the authenticated user
- active user-to-employee links
- active employee profiles
- active scoped role assignments
- the currently selected business/location context where applicable

## Supported patterns

### One user, one employee profile
Common case.

### One user, multiple employee profiles in the same business
Allow only if business policy supports it; do not assume it as default.

### One user, multiple employee profiles across different businesses
Must be supported with strict tenant isolation.

### One user, multiple active scopes within one business
May hold business-wide and multiple location-scoped permissions simultaneously.

### Historical employment records
Terminated, archived, or ended-link records must not grant current access.

## Multi-business rules

- tenant isolation is absolute
- each business sees only its own employee records
- permissions resolve independently per business
- context switching must be explicit

## Multi-location rules

Location permissions must be evaluated separately.

Example:

- `schedule.read` at Location A
- `timeclock.manage` at Location B

The effective access context must preserve exactly that split.

## Multiple active employee profiles in same business

Preferred default:

- one active employee profile per user per business unless there is a strong reason not to

If multiple are allowed, the resolver must:

- combine valid permissions from each active linked employee profile
- preserve explainability of which profile granted which access
- avoid silent merging

## Transfer rules

### Location transfer
Must update assignments and remove invalid old location-scoped permissions.

### Department or manager transfer
Must preserve history and reevaluate manager/organizational workflows.

### Business transfer
Should create a **new** employee profile in the destination business. Do not move the same employee profile across businesses.

## Duplicate and merge rules

Duplicate employee profiles must not be silently merged. Use review or reconciliation workflows later if needed.

## Acceptance criteria

- one user can safely exist across multiple businesses without tenant leakage
- multiple scopes within a business are resolved accurately
- transfers preserve history and reevaluate access correctly
- historical or duplicate records do not silently grant access
- primary/default context remains a UX preference, not an authorization shortcut
