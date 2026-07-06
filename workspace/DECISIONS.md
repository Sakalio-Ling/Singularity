# DECISIONS.md — Architecture Decision Log

> Last updated: 2026-07-07
> Format: Date | Background | Options | Decision | Reason | Risks | Rollback Condition

---

## DEC-001: Default Technical Route — Hybrid Architecture (Route F)

**Date**: 2026-07-07
**Background**: The project needs a modular, incrementally-enhanceable architecture for an LLM-powered Minecraft agent. Six routes were evaluated: (A) Mineflayer+LLM, (B) Mineflayer+Baritone+LLM, (C) Voyager-like skill library, (D) Forge/Fabric mod, (E) Visual/VLA, (F) Hybrid.
**Options**:
- Route A: Simplest, fastest to prototype. Limited pathfinding and navigation.
- Route B: Good pathfinding, but Baritone adds version coupling.
- Route C: Excellent for skill accumulation, but needs code sandbox.
- Route D: Closest to "player" behavior, but high engineering cost.
- Route E: Most "human-like", but high training cost, low real-time performance.
- Route F: Combines A/B/C with gradual E. Most flexible, best for research iteration.
**Decision**: Route F — Hybrid architecture
**Reason**: Allows fast initial prototyping with Mineflayer, incremental addition of Baritone for navigation, Voyager-style skill library for accumulation, and optional vision later. No premature commitment to any single approach.
**Risks**: More components to integrate and maintain. Need clear interface boundaries.
**Rollback Condition**: If Mineflayer integration proves too brittle, pivot to Route D (Forge mod). If vision is required earlier than M6, shift timeline.

---

## DEC-002: Minecraft Version — 1.20.4

**Date**: 2026-07-07
**Background**: Need to pin a Minecraft version for reproducible experiments. Must balance: Mineflayer support, plugin ecosystem, modern game content, community support.
**Options**: 1.19.4, 1.20.1, 1.20.4, 1.21.x
**Decision**: Minecraft 1.20.4 (Paper server)
**Reason**: 1.20.4 has stable Mineflayer support (via prismarine-world), rich plugin ecosystem, modern game mechanics (trails & tales), and broad community documentation. 1.21.x Mineflayer support is still maturing.
**Risks**: Paper server may have vanilla behavior differences. Some mods/plugins may lag behind.
**Rollback Condition**: If critical Mineflayer features break on 1.20.4, downgrade to 1.20.1.

---

## DEC-003: Bot Library — Mineflayer (Primary)

**Date**: 2026-07-07
**Background**: Need a programmatic interface to control a Minecraft player. Options: Mineflayer, Baritone, Forge mod, Fabric mod, custom proxy client.
**Options**:
- Mineflayer: Node.js, well-documented, supports 1.8-1.21, rich plugin ecosystem
- Baritone: Java, excellent pathfinding, but tightly coupled to specific Minecraft versions
- Forge/Fabric mod: Full game access, but high dev cost, version-locked
- Custom proxy: Maximum flexibility, but extreme engineering effort
**Decision**: Mineflayer as primary action interface; Baritone as optional pathfinding addon
**Reason**: Mineflayer offers the best balance of ease-of-use, documentation, community, and version flexibility. Python control via subprocess/socket bridge is well-documented.
**Risks**: Python-Node.js bridge adds latency. Complex actions may need custom Mineflayer plugins.
**Rollback Condition**: If bridge latency exceeds 200ms for simple actions, evaluate direct Java bot.

---

## DEC-004: LLM Provider — Swappable Interface

**Date**: 2026-07-07
**Background**: Need LLM for planning, reflection, skill generation, and natural language understanding. Provider landscape changes rapidly.
**Options**: Hardcode OpenAI, hardcode Anthropic, or abstract interface supporting multiple providers.
**Decision**: Abstract LLM interface with pluggable backends (OpenAI, Anthropic, DeepSeek, Qwen, Ollama local)
**Reason**: Avoids vendor lock-in, allows cost optimization, enables local model testing, future-proofs against provider changes.
**Risks**: Different providers have different APIs, token limits, and capabilities. Abstraction layer adds complexity.
**Rollback Condition**: If abstraction adds significant bugs, simplify to a single well-tested provider.

---

## DEC-005: Memory Format — Markdown + Structured JSON

**Date**: 2026-07-07
**Background**: Need a memory system that is human-readable, version-controllable, LLM-friendly, and queryable. Options: Pure Markdown, SQLite, Vector DB (Chroma/Pinecone), Knowledge Graph, or hybrid.
**Decision**: Start with Markdown + JSON files. Evaluate SQLite and vector DB after M3.
**Reason**: Markdown is human-auditable, git-tracked, and LLM-native. JSON provides structure. Can migrate to DB later without losing data.
**Risks**: File-based memory may not scale beyond a few hundred entries. Search is linear.
**Rollback Condition**: If memory search becomes a bottleneck (>1s for relevant recall), migrate to SQLite FTS or vector DB.
