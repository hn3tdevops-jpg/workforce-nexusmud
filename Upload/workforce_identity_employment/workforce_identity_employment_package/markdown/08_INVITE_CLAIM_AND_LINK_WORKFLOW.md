# Invite, Claim, and Link Workflow for Employer-Created Employee Files

## Objective

Support the full lifecycle where an employer can create an employee profile before the worker has a platform account, then later connect that employee profile to a real user account through a secure invite/claim/link process.

## Core rule

An employee profile may exist without a user account.  
A user account may exist without an employee profile.  
Workforce access begins only after a valid link is established and activated.

## Primary workflow types

### Flow A - Employer-first onboarding
1. employer creates employee profile
2. employee profile exists with no linked user
3. employer sends invite or claim request
4. worker creates or signs into platform account
5. system verifies claim
6. `UserEmployeeLink` is created or activated
7. workforce permissions begin only when link becomes `ACTIVE`

### Flow B - User-first onboarding
1. person creates platform account
2. employer creates employee profile or finds matching profile
3. employer links account to employee record
4. worker confirms if policy requires confirmation
5. link becomes `ACTIVE`
6. workforce permissions begin

## Optional supporting record

Recommended optional table: `employee_link_invitations`

Suggested fields:

- `id`
- `business_id`
- `employee_profile_id`
- `target_email`
- `target_phone`
- `invite_token_hash`
- `status`
- `expires_at`
- `sent_at`
- `claimed_at`
- `created_by_user_id`
- `claimed_by_user_id`
- `completed_link_id`

## Identity matching rules

Allowed signals:

- verified email match
- verified phone match
- authenticated claim token
- admin-selected existing user
- explicit user confirmation after sign-in

Not sufficient on its own:

- matching names only
- unverified contact info
- guessed similarity

## Security rules

- claim tokens must be random, single-use, and expiring
- expired tokens must not activate links
- cancelled or revoked invites must not activate links
- successful claim must invalidate prior active token for that invite
- claims must be audited

## Duplicate prevention

- prevent multiple active links for same user + employee pair
- prevent uncontrolled duplicate claim records
- detect likely duplicate employee records in same business
- require explicit review instead of silent auto-linking

## API scope

Suggested endpoints:

- `POST /businesses/{business_id}/employees/{employee_id}/invite-link`
- `POST /businesses/{business_id}/employees/{employee_id}/resend-invite`
- `POST /businesses/{business_id}/employees/{employee_id}/cancel-invite`
- `POST /employee-link-invitations/{invite_id}/claim`
- `POST /employee-links/{link_id}/activate`

## Acceptance criteria

- employers can create employee profiles without requiring a user account
- employers can invite workers to claim those employee profiles
- users can securely claim or confirm linkage
- no workforce permissions are granted before activation
- expired or cancelled invites cannot activate links
- incorrect duplicate links are not silently created
