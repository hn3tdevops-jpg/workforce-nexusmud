# Frontend Bootstrap, Context Switching, and Field Ownership UX

## Objective

Make the identity/employment separation visible and usable in the frontend without confusing users or weakening ownership boundaries.

The frontend must clearly distinguish:

- the user’s personal platform account
- business-controlled employee profiles
- the active workforce/business/location context
- the permissions currently derived from active employee linkage

## UX principles

### Separate personal identity from employment identity
Do not present the user account and employee file as one merged record.

### Make active work context explicit
Users with multiple active employment links must always have a visible current context.

### Respect ownership boundaries in the interface
User-owned fields and business-owned fields must not be mixed into the same unrestricted edit form.

### Reflect derived access, not assumed access
Frontend navigation and module visibility must be driven by the resolved access context returned by the backend.

## Backend dependency

This phase assumes the backend provides:

- `GET /me/access-context`
- active user-to-employee links
- scoped permissions grouped by business/location
- linked employee profile summaries

## Bootstrap flow

1. authenticate the user
2. fetch `GET /me/access-context`
3. resolve available business/location scopes
4. determine default active context
5. render navigation and modules only for scopes supported by active permissions
6. prevent access to workforce modules when no valid active employee-linked scope exists

## Required behavior

- no active employee links -> show personal-account experience only
- one active employee link -> auto-select that context
- multiple active employee links -> require clear context selection and allow switching

## Context switcher requirements

The switcher should support:

- business
- location
- employee profile where needed

It must display:

- business name
- location name if scoped
- employment/display label
- whether scope is business-wide or location-scoped

## Navigation gating

All workforce navigation must be derived from effective permission keys, not guessed role names.

## Field ownership UX rules

### Personal account UI
Contains user-owned editable fields.

### Employment profile UI
Contains employer-managed information and only explicitly allowed self-service fields.

### Required labels
Use cues such as:

- Managed by you
- Managed by employer
- Visible to employer
- Read-only employment information
- Request change

## Build order

- add frontend access-context bootstrap integration
- create frontend state model for active context
- add default context resolution logic
- add visible context switcher
- update shell/sidebar/topbar to reflect active context
- gate module navigation using resolved permission keys
- add personal account area
- add My Employment area
- separate user-owned and business-owned profile views
- add tests for context switching and field ownership boundaries
