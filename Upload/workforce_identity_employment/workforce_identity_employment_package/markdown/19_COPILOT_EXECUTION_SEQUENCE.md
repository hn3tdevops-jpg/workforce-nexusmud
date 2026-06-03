# Copilot Execution Sequence

Use these as atomic build slices.

## Slice 1
Schema enums + tables + indexes

## Slice 2
ORM models + relationships

## Slice 3
Service scaffolding + domain errors + audit helper skeleton

## Slice 4
Employee profile CRUD services + endpoints + tests

## Slice 5
Link lifecycle services + endpoints + tests

## Slice 6
Employee role assignment services + endpoints + tests

## Slice 7
Effective access resolver + permission helpers + tests

## Slice 8
`GET /me/access-context` + tests

## Slice 9
Lifecycle transition services + endpoints + tests

## Slice 10
Self-service/profile visibility endpoints + tests

## Slice 11
Audit/history query APIs + tests

## Slice 12
Frontend bootstrap/context switching integration

## Slice 13
Compatibility cleanup + final regression suite

## Review gate after each slice

Verify:

- migrations apply cleanly
- tests pass for touched scope
- tenant isolation is unchanged or stronger
- no endpoint bypasses service-layer rules
- audit writes exist for access-affecting changes
- access revocation works correctly where relevant
- new code uses employee-linked concepts consistently
