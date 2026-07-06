# OPEN_QUESTIONS.md — Unresolved Research Questions

> Last updated: 2026-07-07
> Review and update after each research cycle.

---

## OQ-001: Action Space Design

**Question**: What is the optimal action space for the Minecraft agent?
**Candidates**:
- Natural language actions (LLM outputs text, mapped to game commands)
- Mineflayer API calls (structured function calls)
- Baritone pathfinding commands (high-level navigation)
- Code-as-skill (Voyager-style generated JavaScript)
- Behavior tokens (discrete action vocabulary)
- Keyboard/mouse control (raw input signals)
- VLA (visual-language-action end-to-end)
- Hybrid (LLM chooses from action vocabulary, some actions are code, some are API calls)
**Status**: Open. Route F (hybrid) chosen as default, but specific action vocabulary TBD.
**Impact**: Affects planner design, skill library format, evaluation metrics, and error modes.

---

## OQ-002: Task System Granularity

**Question**: How should the task system handle long-term goals, concurrent tasks, failure recovery, and priority changes?
**Candidates**:
- Flat task queue (simple but no hierarchy)
- Hierarchical task tree (HTN-like, supports decomposition)
- Goal-task-skill DAG (directed acyclic graph with dependencies)
- Reactive behavior trees (with fallback nodes)
**Status**: Open. Hierarchical task tree is the current default.
**Impact**: Affects planner output format, state tracking, memory writes, and evaluation granularity.

---

## OQ-003: Memory Technology Stack

**Question**: What storage and retrieval technology should power the memory system?
**Candidates**:
- Markdown files (human-readable, git-tracked, linear search)
- SQLite with FTS (structured, queryable, local)
- Vector database (Chroma, Qdrant, Pinecone — semantic search)
- Knowledge graph (Neo4j-style — relational reasoning)
- Hybrid (Markdown for facts, SQLite for logs, vector DB for semantic recall)
**Status**: Open. Starting with Markdown + JSON per DEC-005. Evaluate SQLite/vector after M3.
**Impact**: Affects recall quality, write latency, storage cost, and auditability.

---

## OQ-004: Skill Representation

**Question**: Should skills be code, behavior sequences, natural language strategies, or multi-layer?
**Candidates**:
- Code skills (Voyager-style JavaScript functions)
- Action sequence skills (ordered Mineflayer API call lists)
- Natural language skills (strategy descriptions for LLM to interpret)
- Multi-layer (NL for strategy, action sequence for tactic, code for primitive)
**Status**: Open. Multi-layer is the current default.
**Impact**: Affects skill library format, skill generation method, composability, and debugging.

---

## OQ-005: Minecraft Knowledge Injection

**Question**: How should domain knowledge (crafting recipes, mob behavior, biomes, tech trees) be provided to the agent?
**Candidates**:
- Minecraft Wiki RAG (retrieve relevant wiki pages at query time)
- Structured recipe database (JSON/SQLite of all crafting recipes)
- Tech tree graph (dependency graph of item progression)
- Experience traces (learned from past successful/failed sessions)
- Human-written SOPs (standard operating procedures for common tasks)
**Status**: Open. Likely hybrid: structured recipe DB + tech tree graph + RAG for edge cases.
**Impact**: Affects planner accuracy, reduces hallucination, enables better pre-condition checking.

---

## OQ-006: Reducing LLM Hallucination in Execution

**Question**: How to minimize the impact of LLM errors on actual game execution?
**Candidates**:
- Structured output with JSON schema validation
- Action schema enforcement (pre-condition checks)
- Post-condition verification (did the expected result happen?)
- Reflection and re-planning on failure
- Simulation/dry-run before execution
- Rule-based safety controller (guardian layer)
**Status**: Open. All candidates should be tested. Structured output + pre/post checks are the minimum.
**Impact**: Directly affects task success rate and reliability.

---

## OQ-007: Evaluation Methodology

**Question**: How to reliably evaluate "autonomous working" rather than demo-level success?
**Candidates**:
- Fixed-seed deterministic benchmarks (reproducible)
- Random-seed aggregate benchmarks (statistical significance)
- Long-horizon survival metrics (hours survived, resources accumulated)
- Skill acquisition rate (new skills per session)
- Human evaluation (does it "feel" like a competent player?)
- Automated scoring (task completion, resource efficiency, death count)
**Status**: Open. Fixed-seed benchmarks for M1-M3, aggregate metrics for M4+.
**Impact**: Affects how we measure progress and make routing decisions.

---

## OQ-008: API Bot to Human-Like Agent Transition

**Question**: When and how should the system transition from API-based control to more human-like behavior?
**Candidates**:
- Stay with API bot (structured, reliable, fast)
- Add visual input alongside API (multimodal grounding)
- Keyboard/mouse control via screen reading (most human-like but hardest)
- VLA models (end-to-end visual-language-action)
- Hybrid (API for structured tasks, vision for ambiguous situations)
**Status**: Open. Deferred to M6. API bot is sufficient for M0-M5.
**Impact**: Affects long-term architecture evolution and research investment.

---

## OQ-009: Multi-Agent Communication Protocol

**Question**: How should multiple agents communicate, coordinate, and resolve conflicts?
**Candidates**:
- Shared memory (read/write common state file)
- Message passing (structured messages between agents)
- Blackboard system (shared workspace with read/write locks)
- LLM-mediated negotiation (agents "talk" via natural language)
**Status**: Open. Deferred to M7.
**Impact**: Affects multi-agent architecture, scalability, and conflict resolution.

---

## OQ-010: Long-Term System Evolution Without Loss of Control

**Question**: How to keep the system maintainable as it grows in complexity?
**Candidates**:
- Strict module boundaries with interface contracts
- Comprehensive logging and audit trails
- Memory compression (summarize old entries)
- Version management for skills, memory, and configuration
- Experiment rollback capability (git-based)
- Safety boundaries (permission system for dangerous actions)
**Status**: Open. Modular architecture + logging + versioning are the minimum. Others TBD.
**Impact**: Affects long-term research velocity and system reliability.
