# Concrete Implementation Roadmap

## Objective

Turn the identity/employment architecture into an execution-ready build sequence that can be implemented in small, testable, low-risk increments.

## Core rule

Do **not** attempt to build the full identity/employment system in one large patch.

Implementation should proceed in layers so each step can be migrated safely, tested independently, reviewed clearly, and integrated without breaking existing auth flows.

## Rollout strategy

Build from the bottom up in this order:

1. schema and enums
2. ORM models and relationships
3. service-layer foundations
4. access resolver
5. employer-managed CRUD
6. link lifecycle workflows
7. lifecycle transition workflows
8. RBAC assignment APIs
9. access-context bootstrap API
10. audit/history views
11. frontend context integration
12. compatibility cleanup and hardening

## Phase 1 - Schema foundations
Deliverables:

- enums
- tables
- constraints
- indexes
- reversible migrations where policy allows

## Phase 2 - ORM models and canonical relationships
Deliverables:

- ORM models
- relationship mappings
- enum bindings
- repository import integration

## Phase 3 - Service-layer foundation and domain errors
Deliverables:

- actor context object
- service modules
- shared validation helpers
- domain error types

## Phase 4 - Employee profile core services and CRUD APIs
Deliverables:

- employee profile service methods
- employer CRUD endpoints
- field ownership enforcement
- audit integration

## Phase 5 - Link lifecycle services and invite/claim foundations
Deliverables:

- pending link creation
- activation/suspension/revocation/end workflows
- optional invite workflow
- audit and duplicate protection

## Phase 6 - Employee-linked RBAC assignment services
Deliverables:

- role assignment services
- role assignment endpoints
- scope checks
- audit integration

## Phase 7 - Effective access resolver and authorization helpers
Deliverables:

- effective access resolver
- permission helper functions
- compatibility-aware integration with current auth
- tests for grant/revoke correctness

## Phase 8 - Access context bootstrap API
Deliverables:

- `/me/access-context`
- access-context schema
- stable bootstrap contract

## Phase 9 - Employee lifecycle transition services and endpoints
Deliverables:

- lifecycle service methods
- action endpoints
- audit writes
- access consequence handling

## Phase 10 - Transfer and edge-case workflows
Deliverables:

- transfer services
- transfer endpoints
- stale-scope cleanup
- tests for multi-business/multi-location correctness

## Phase 11 - Self-service and field ownership endpoints
Deliverables:

- `/me/profile`
- `/me/settings`
- self-view employment endpoints
- filtered employee self-view
- restricted self-service write support

## Phase 12 - Audit and history query APIs
Deliverables:

- employee history endpoints
- business audit query endpoints
- permissioned history access

## Phase 13 - Frontend bootstrap and context switching integration
Deliverables:

- frontend bootstrap against `/me/access-context`
- default context logic
- business/location switcher
- permission-based navigation gating

## Phase 14 - Compatibility hardening and legacy cleanup
Deliverables:

- compatibility review
- migration path documentation
- cleanup of duplicated auth logic
- final hardening tests

## Definition of done

The rollout is complete when:

- users and employee profiles are separate authoritative entities
- employers can create employee profiles without user accounts
- users can exist without employment
- active user-employee links control whether workforce access may flow
- employee-linked RBAC drives workforce permissions
- lifecycle and transfer workflows affect access correctly
- self-service and employer-managed field ownership are enforced
- frontend bootstrap consumes resolved access context
- audit/history exists for all critical transitions
- tenant isolation remains strict
- tests protect grant/revoke behavior and scope correctness
