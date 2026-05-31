
# Architecture

## Foundational Principles

1. Everything is an entity
2. Everything emits events
3. AI agents operate as autonomous services
4. Social interaction is gameplay
5. Persistent memory drives meaning

---

# Core Systems

## 1. Entity System

Entity types:
- Player
- NPC
- Guild
- Room
- Item
- Contract
- Quest
- Business
- Territory

Each entity has:
- id
- metadata
- traits
- permissions
- reputation
- memory references

---

## 2. World Engine

Responsibilities:
- room movement
- inventory
- combat/events
- interaction parsing
- persistence

Event-driven architecture:
- player_entered_room
- item_created
- quest_completed
- npc_memory_updated

---

## 3. Agent Core

AI agents contain:
- persona
- goals
- role
- memory
- faction alignment
- economic behavior

Examples:
- merchant
- recruiter
- historian
- professor
- guild master
- judge

---

## 4. GroundTruth Layer

GroundTruth acts as:
- semantic memory layer
- relationship graph
- truth consistency engine
- long-term agent memory backend

Possible uses:
- faction history
- persistent character lore
- world state reasoning
- economic relationship tracking

---

## 5. Gateway API

FastAPI + WebSockets:
- realtime room updates
- chat
- quests
- AI interactions
- inventory updates

---

# Prototype MVP

## User Flow

1. User enters world
2. Spawn in starter district
3. Meet AI guide NPC
4. Receive first quest
5. Join guild
6. Build reputation
7. Access services/economy

---

# Long-Term Vision

A programmable civilization platform where:
- AI and humans coexist
- institutions emerge
- economies persist
- governance evolves
- communities become living worlds
