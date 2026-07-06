# Module: Memory System
> Status: Design (M0)
## Layers
L0 Context, L1 Working, L2 Episodic, L3 Semantic, L4 Skill, L5 Decision, L6 Research
## Write Rules
No speculation enters L3+. User temps are L0/L1 only. Every L3+ entry needs source.
## Storage
Phase 1: Markdown + JSON. Phase 2: SQLite FTS. Phase 3: Vector DB.
## Interface
write, read, search, compress, get_context_window
