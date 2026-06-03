# Self-Service vs Employer-Managed Field Permissions

## Objective

Define clear ownership, edit rights, visibility rules, and workflow boundaries for profile-related data so the system never confuses:

- user-owned personal account data
- business-owned employee record data
- shared/reference data visible to both sides
- self-service edits allowed by policy

## Core rule

A linked employee is **not** automatically the owner of their employee file.

The platform must distinguish:

- what the user controls
- what the business controls
- what the user may request to change
- what the user may edit directly through approved self-service workflows
- what is view-only
- what is hidden

## Ownership domains

### User-owned domain
Examples:

- login email for platform identity
- password / auth provider settings
- MFA settings
- session/security settings
- personal preferences
- personal notification settings
- user-level avatar
- privacy settings

### Business-owned employee domain
Examples:

- employment status
- business/location assignment
- department
- manager
- internal notes
- work email
- work phone / extension
- role assignments
- schedule eligibility
- certifications and compliance flags
- internal identifiers such as employee code

### Shared / dual-visibility domain
Examples:

- legal name
- preferred display name
- personal phone visible to employer
- emergency contact
- address

Each field must have an owner, visibility policy, edit policy, and sync policy.

## Field permission categories

### Category A - User-editable
User may edit directly.

### Category B - User-editable with employer visibility
User may edit directly and employer can view.

### Category C - User-requested, employer-approved
User may request change, but approval is required.

### Category D - Employer-editable, user-viewable
Business controls field, user can see it.

### Category E - Employer-editable, user-hidden or restricted
Business controls field, linked user does not automatically see it.

## Required policy matrix

Each field should define:

- `field_key`
- `record_owner`
- `source_of_truth`
- `user_visibility`
- `employer_visibility`
- `user_edit_mode`
- `employer_edit_mode`
- `sync_direction`
- `approval_required`
- `audit_required`

## Source-of-truth rules

Supported patterns:

- pure user-owned
- pure employer-owned
- user-owned with employer-visible copy
- employer-owned with user-visible display

Prohibited pattern:

- ambiguous shared ownership with no defined source of truth

## Backend enforcement

The backend must enforce ownership at:

- schema validation where useful
- service layer
- authorization checks
- serializer/response shaping
- audit logging

## Endpoint guidance

### User-owned self-service endpoints
- `GET /me/profile`
- `PATCH /me/profile`
- `GET /me/settings`
- `PATCH /me/settings`

### Employment self-view endpoints
- `GET /me/employment-links`
- `GET /me/employee-profiles/{employee_profile_id}`

### Employer-managed endpoints
- `PATCH /businesses/{business_id}/employees/{employee_id}`

### Optional request workflow
- `POST /me/employee-change-requests`

## Acceptance criteria

- user-owned and employer-owned fields are clearly separated
- linked employees do not automatically gain edit rights over employee records
- self-service editing is limited to explicitly approved fields
- employer-managed edits remain permissioned and auditable
- sensitive/private employer fields are not exposed to linked employees
