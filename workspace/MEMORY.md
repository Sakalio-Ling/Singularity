# MEMORY.md — Long-Term Knowledge Base

> Last updated: 2026-07-07
> Only store verified, reusable, high-value information here. No raw speculation.

## Current Technical Route

- **Default route**: Hybrid architecture (Route F)
  - High-level: LLM planner (natural language -> structured JSON plans)
  - Mid-level: Task system + Skill library
  - Low-level: Mineflayer + Baritone for actions and pathfinding
  - Future: Gradually add vision/VLA capabilities
- **Minecraft version**: 1.20.4 (Paper server, TBD after M0 research)
- **Bot library**: Mineflayer (Node.js) with Python bridge (primary candidate)
- **LLM backend**: Swappable — OpenAI GPT-4o / Claude / DeepSeek / Qwen / local via Ollama
- **Memory format**: Markdown files + structured JSON (evaluate SQLite/vector DB later)

## Key Design Decisions

1. **Modular architecture** — Every component (perception, planning, memory, action, evaluation) is a separate module with defined interfaces. This allows incremental replacement.
2. **Evidence-first research** — No capability claims without 3+ repeated experiments. All findings must cite sources.
3. **Safety layer** — LLM never executes code or game actions directly. All outputs go through validation and action controller.
4. **Model-agnostic** — Core logic must not depend on any single LLM provider. Abstract the LLM interface.
5. **Skill library is code + NL hybrid** — Skills can be code snippets, action sequences, or natural language strategies. Version-tracked.

## Proven Approaches (from literature)

- Voyager (2023): Code-as-skill library + LLM curriculum works well for open-ended exploration
- MineDojo (2022): Large-scale benchmark with 1000+ tasks provides evaluation foundation
- JARVIS-1 (2023): Multimodal memory with pre-trained visual backbone improves grounding
- GITM (2023): Text-only LLM + structured actions can beat RL baselines on specific tasks
- Mindcraft (2024): Mineflayer + LLM is a viable fast-iteration development path

## Known Limitations

- Mineflayer supports up to 1.21.x but plugin compatibility varies by version
- LLM cost can escalate quickly with long-horizon tasks; token budgeting is essential
- Code-as-skill (Voyager-style) needs sandboxing to prevent dangerous code execution
- Visual approaches (VLA) are high latency and may not be cost-effective for structured tasks
- Multi-agent coordination is poorly explored in open-world Minecraft settings
