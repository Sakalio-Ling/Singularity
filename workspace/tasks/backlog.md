# Task Backlog

> Last updated: 2026-07-07
> Tasks are prioritized P0-P4. Move to active.md when started.

## P0 — Blockers

(none currently)

## P1 — MVP Critical

- [ ] TASK-001: Set up local Minecraft 1.20.4 Paper server
  - Acceptance: Server starts, bot can connect
  - Blocks: All M1 tasks

- [ ] TASK-002: Implement Mineflayer bot bridge (Python <-> Node.js)
  - Acceptance: Python can send commands, receive state
  - Blocks: All M1 tasks

- [ ] TASK-003: Implement observation module
  - Acceptance: Read position, health, inventory, nearby blocks/entities
  - Blocks: TASK-005

- [ ] TASK-004: Implement primitive action API
  - Acceptance: move, dig, place, craft, attack work reliably
  - Blocks: TASK-005

- [ ] TASK-005: Run M1 benchmark suite (5 basic tasks)
  - Acceptance: 5/5 tasks pass with logging
  - Blocks: M2

## P2 — Reliability

- [ ] TASK-006: Implement session logger (JSON structured logs)
  - Acceptance: Every observation/action/result is logged

- [ ] TASK-007: Implement LLM planner module
  - Acceptance: Natural language -> structured JSON plan

- [ ] TASK-008: Implement task system (hierarchical tasks with states)
  - Acceptance: Task tree with create/update/query/fail

## P3 — Enhancement

- [ ] TASK-009: Implement reflection module
  - Acceptance: Failure analysis -> re-plan trigger

- [ ] TASK-010: Implement skill library (basic version)
  - Acceptance: Store/query/execute skills

## P4 — Research

- [ ] TASK-011: Survey Mineflayer plugins for 1.20.4 compatibility
- [ ] TASK-012: Benchmark LLM planning latency and token cost
- [ ] TASK-013: Evaluate quarry library as Python-only alternative
