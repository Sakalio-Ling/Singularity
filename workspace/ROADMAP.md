# ROADMAP.md — Phase Roadmap

> Last updated: 2026-07-07
> Current phase: M0 (Research Baseline)

## Overview

The project evolves a Minecraft LLM Agent through 8 phases (M0-M7), each building on the previous. Every phase has clear goals, acceptance criteria, key tasks, dependencies, and risks.

---

## M0: Research Baseline

**Status**: In Progress
**Goal**: Establish paper library, repo library, architecture draft, first benchmark suite, and technical stack decision.
**Acceptance Criteria**:
- At least 20 paper/project cards completed
- current-architecture.md v1 drafted
- ROADMAP.md this file finalized
- First benchmark draft with 10+ tasks
- OPEN_QUESTIONS.md populated
- Tech stack decision documented in DECISIONS.md

**Key Tasks**:
1. Survey 15+ key papers (Voyager, MineDojo, JARVIS-1, GITM, DEPS, STEVE-1, Mindcraft, etc.)
2. Survey 10+ open-source repos (Mineflayer, Baritone, Mindcraft, MineDojo, etc.)
3. Draft modular architecture (Interface, Observation, WorldState, TaskSystem, Planner, SkillLibrary, ActionController, Memory, Reflector, Evaluator, Safety)
4. Define first benchmark task suite (survival, crafting, exploration)
5. Decide Minecraft version, bot library, LLM provider
6. Document all decisions in DECISIONS.md

**Dependencies**: None (bootstrap phase)
**Risks**: Analysis paralysis, scope creep into implementation before research is solid

---

## M1: Minimum Viable Bot

**Status**: Pending
**Goal**: Connect to a local Minecraft server, read basic state, execute simple actions.
**Acceptance Criteria**:
- Bot connects to local Minecraft 1.20.x server via Mineflayer
- Bot reads: position, health, hunger, inventory, nearby blocks, nearby entities, time of day
- Bot executes: move, look, dig, place, craft, attack, open container
- 5 basic benchmark tasks pass (see benchmarks/)
- Decision/action logs are generated per session

**Key Tasks**:
1. Set up local Minecraft server (Paper/Spigot 1.20.4)
2. Implement Mineflayer bot bridge in Python (via subprocess or socket)
3. Implement observation module (read game state into structured dict)
4. Implement primitive action API (move, look, dig, place, craft, attack)
5. Build session logger (JSON log of observations, actions, outcomes)
6. Run 5 benchmark tasks and record results

**Dependencies**: M0 (tech stack decision, architecture draft)
**Risks**: Mineflayer version compatibility, Python-Node.js bridge complexity

---

## M2: LLM Task Planning

**Status**: Pending
**Goal**: Accept natural-language goals, decompose into structured plans, execute subtasks.
**Acceptance Criteria**:
- "Gather wood and craft a workbench" completes end-to-end
- "Craft a wooden pickaxe and obtain cobblestone" completes end-to-end
- At least 1 re-planning event triggered and logged on failure
- Task system tracks subtask states (proposed/active/completed/failed)

**Key Tasks**:
1. Implement Planner module (LLM-powered, outputs structured JSON plans)
2. Implement TaskSystem (hierarchical tasks with states, dependencies, priorities)
3. Implement Reflection module (failure analysis, re-plan trigger)
4. Integrate Planner -> TaskSystem -> SkillLibrary -> ActionController pipeline
5. Run M2 acceptance benchmarks

**Dependencies**: M1 (working bot with primitive actions)
**Risks**: LLM hallucination in plans, JSON parsing failures, cost overruns

---

## M3: Skill Library and Long-Term Memory

**Status**: Pending
**Goal**: Successful tasks auto-sink into reusable skills; failures become experience; long-term goals persist across sessions.
**Acceptance Criteria**:
- At least 10 reusable skills stored with success rate statistics
- Skill library supports versioning and rollback
- MEMORY.md auto-updated with validated facts
- Cross-session goal recovery works (restart server, agent resumes from memory)
- Experiment logs and failure cases are searchable

**Key Tasks**:
1. Implement Skill Library (code-based + NL-based skills, versioning, metadata)
2. Implement Memory System (L0-L6 layers, write/read/compress/evict)
3. Implement skill extraction from successful task traces
4. Implement failure case library
5. Implement session persistence and recovery
6. Run M3 acceptance benchmarks

**Dependencies**: M2 (LLM planning and task execution)
**Risks**: Skill overfitting, memory pollution, storage growth

---

## M4: Autonomous Survival Loop

**Status**: Pending
**Goal**: Agent self-directs survival goals: first-night shelter, resource gathering, tool progression, threat response.
**Acceptance Criteria**:
- Survives first night on a fixed seed (3+ repeated experiments)
- Self-proposes next survival goals without human input
- Handles nighttime threats (shelter, combat, retreat)
- Logs success rate and failure types

**Key Tasks**:
1. Implement strategic goal generation (bootstrapping -> resource chain -> tech tree)
2. Implement night cycle awareness and shelter strategy
3. Implement combat/threat response skills
4. Implement resource inventory management
5. Run 3+ repeated survival experiments on fixed seeds

**Dependencies**: M3 (skill library, memory, task system)
**Risks**: Long task chains accumulate errors, combat is hard to test

---

## M5: Open-World Exploration

**Status**: Pending
**Goal**: Agent explores unknown terrain, gathers resources, and returns to base.
**Acceptance Criteria**:
- Explore-gather-return loop completes successfully
- Handles getting lost (pathfinding recovery, compass use)
- Handles full inventory (prioritization, caching, return trip)
- Generates reusable exploration strategies

**Key Tasks**:
1. Implement exploration skill (area scanning, landmark tracking)
2. Implement navigation with pathfinding recovery
3. Implement resource prioritization and inventory management
4. Implement base return logic (coordinates, compass, path memory)
5. Run exploration benchmarks

**Dependencies**: M4 (autonomous survival)
**Risks**: Infinite exploration loops, pathfinding failures in complex terrain

---

## M6: Vision and Multimodal Enhancement

**Status**: Pending
**Goal**: Research and integrate visual input, screenshot understanding, or VLA approaches.
**Acceptance Criteria**:
- At least one vision-augmented task completed
- Decision report on whether to continue investing in VLA vs structured API
- Comparison of visual vs API-only performance on same tasks

**Key Tasks**:
1. Survey VLA approaches for Minecraft (STEVE-1, JARVIS-VLA, GROOT)
2. Implement screenshot capture and basic visual grounding
3. Run A/B comparison: API-only vs vision-augmented on same tasks
4. Write decision report

**Dependencies**: M5 (reliable autonomous exploration)
**Risks**: High latency, high cost, low accuracy of visual approaches

---

## M7: Multi-Agent Collaboration

**Status**: Pending
**Goal**: Multiple bots cooperate on shared tasks with role assignment and communication.
**Acceptance Criteria**:
- Two agents complete a resource gathering or building task together
- Communication protocol documented (shared memory, message passing, or both)
- Sync failures and conflict resolution logged
- Efficiency improvement over single-agent measured

**Key Tasks**:
1. Design multi-agent communication protocol
2. Implement task decomposition with role assignment
3. Implement shared world state and memory
4. Implement conflict resolution (resource contention, path blocking)
5. Run collaboration benchmarks

**Dependencies**: M6 (mature single-agent system)
**Risks**: Communication overhead, coordination deadlocks, shared memory corruption
