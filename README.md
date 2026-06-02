Merged content: (theirs first, then ours)

# nexusmud

Initial repository for the nexusmud project.


---


# NexusMUD

A persistent AI-native social network built on MUD/MMO principles.

## Core Vision

NexusMUD is a text-first civilization simulator where:
- Humans are player characters
- AI agents are NPCs, workers, moderators, merchants, historians, and guides
- Guilds operate like social communities
- Quests map to real tasks
- Reputation and economics are persistent

## Prototype Goals

### Phase 1 (Complete)
- [x] Room navigation
- [x] AI NPC interaction
- [x] Guilds/factions
- [x] Reputation system
- [x] Quest generation
- [x] Event logging
- [x] GroundTruth integration layer

### Phase 2 (Complete)
- [x] Inventory/items system
- [x] Dynamic quest generator
- [x] Guild join mechanics
- [x] Reputation engine
- [x] Memory/event tracking

### Planned Stack
- FastAPI
- PostgreSQL
- Redis
- WebSocket gateway
- Local-first AI abstraction layer
- Event sourcing
- Agent memory system

## Repository Layout

packages/
    world_engine/     -> rooms, maps, inventories, events
    agent_core/       -> AI personalities, memory, orchestration
    gateway_api/      -> websocket + REST API

docs/
    architecture.md
    roadmap.md
    gameplay_loop.md

prompts/
    copilot_world_engine.md
    gemini_agent_prompts.md
    task_runner_prompt.md
