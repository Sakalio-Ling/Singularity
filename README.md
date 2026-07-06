# Singularity — Minecraft LLM Agent

An evolving modular agent system that drives a Minecraft Java Edition player through natural-language goals, progressing from basic connectivity to autonomous multi-agent collaboration.

## Vision

Build a long-lived, evidence-driven research system where an LLM-powered agent can:
- Understand natural-language tasks
- Decompose long-term goals into executable subtasks
- Navigate, explore, and survive in Minecraft worlds
- Learn and reuse skills across sessions
- Recover from failures and adapt to new environments
- Eventually collaborate with other agents or human players

## Capability Levels

| Level | Description |
|-------|-------------|
| 0 | Connect to Minecraft server, read basic state, execute simple commands |
| 1 | Complete short tasks from natural language: move, gather, mine, craft basics |
| 2 | Multi-step tasks: craft iron pickaxe, build a shelter, prepare night resources |
| 3 | Maintain task queue, long-term memory, skill library; retry on failure |
| 4 | Self-directed goal-setting: survival bootstrapping, resource gathering, tech tree |
| 5 | Explore unknown worlds, learn and reuse skills, adapt to new maps |
| 6 | Integrate vision / multimodal input / VLA, reduce script dependency |
| 7 | Multi-agent collaboration, division of labor, long-term human co-play |

## Tech Stack (Planned)

- **Language**: Python 3.11+
- **Minecraft Interface**: Mineflayer (via Node.js) or MineDojo / custom bot bridge
- **Pathfinding**: Baritone (optional, for navigation)
- **LLM Backend**: OpenAI GPT-4o / Claude / DeepSeek / Qwen / local models via Ollama
- **Memory**: Multi-layer (context window, working memory, episodic, semantic, skill, decision, research)
- **Task System**: Hierarchical state machine with dependency tracking
- **Skill Library**: Code-based + natural-language hybrid skills
- **Evaluation**: Structured benchmark suite across survival, crafting, exploration, building, collaboration

## Architecture Overview

```
User Goal (Natural Language)
        |
        v
  +-----------+
  |  Planner  |  (LLM-powered: strategic / tactical / action plans)
  +-----------+
        |
        v
  +-----------+
  | Task System|  (hierarchical tasks, dependencies, priorities, state machine)
  +-----------+
        |
        v
  +---------------+
  | Skill Library |  (reusable action units: code, action sequences, NL strategies)
  +---------------+
        |
        v
  +------------------+
  | Action Controller|  (pre-check, execute, post-verify, timeout, rollback)
  +------------------+
        |
        v
  +------------------+
  | Minecraft Server |  (via Mineflayer / Baritone / Mod API)
  +------------------+
        |
        v
  +---------------+
  |  Observation  |  (position, health, inventory, entities, blocks, time, weather)
  +---------------+
        |
        v
  +---------------+
  | World State   |  (structured state, LLM-readable summaries)
  +---------------+
        |
        v
  +-----------+
  | Reflector |  (failure analysis, strategy adjustment, memory updates)
  +-----------+
        |
        v
  +-----------+
  |  Memory   |  (L0-L6 layered memory system)
  +-----------+
        |
        v
  +-----------+
  | Evaluator |  (benchmark suite, task success, resource cost, safety)
  +-----------+
```

## Project Structure

```
Singularity/
├── README.md                          # This file
├── workspace/                         # Research knowledge base
│   ├── MEMORY.md                      # Long-term validated knowledge
│   ├── ROADMAP.md                     # Phase roadmap (M0-M7)
│   ├── DECISIONS.md                   # Architecture decisions log
│   ├── RISKS.md                       # Risk register
│   ├── OPEN_QUESTIONS.md             # Unresolved research questions
│   ├── STATUS.md                      # Current project status
│   ├── memory/                        # Daily research journals
│   │   └── YYYY-MM-DD.md
│   ├── papers/                        # Paper index and cards
│   │   ├── paper-index.md
│   │   └── YYYY-MM-DD-paper-title.md
│   ├── repos/                         # Open-source project cards
│   │   ├── repo-index.md
│   │   └── repo-name.md
│   ├── architecture/                  # Module design documents
│   │   ├── current-architecture.md
│   │   ├── module-planner.md
│   │   ├── module-memory.md
│   │   ├── module-task-system.md
│   │   ├── module-skill-library.md
│   │   ├── module-perception.md
│   │   ├── module-action-controller.md
│   │   ├── module-evaluator.md
│   │   └── module-safety.md
│   ├── experiments/                   # Experiment records
│   │   ├── experiment-index.md
│   │   └── EXP-NNNN-title.md
│   ├── benchmarks/                    # Benchmark task suites
│   │   ├── benchmark-index.md
│   │   ├── task-suite-survival.md
│   │   ├── task-suite-crafting.md
│   │   ├── task-suite-exploration.md
│   │   ├── task-suite-building.md
│   │   └── task-suite-collaboration.md
│   ├── implementation/                # Technical notes
│   │   ├── tech-stack.md
│   │   ├── api-notes.md
│   │   ├── minecraft-version-notes.md
│   │   ├── mineflayer-notes.md
│   │   ├── baritone-notes.md
│   │   ├── forge-fabric-notes.md
│   │   ├── model-provider-notes.md
│   │   └── local-model-notes.md
│   ├── skills/                        # Skill library
│   │   ├── skill-index.md
│   │   ├── gather-wood.md
│   │   ├── craft-tools.md
│   │   ├── mine-stone.md
│   │   ├── mine-iron.md
│   │   ├── smelt-iron.md
│   │   ├── build-shelter.md
│   │   ├── defend-self.md
│   │   └── navigate-to-target.md
│   └── tasks/                         # Task tracking
│       ├── backlog.md
│       ├── active.md
│       ├── done.md
│       └── blocked.md
├── src/                               # Agent source code (future)
├── docs/                              # Additional documentation (future)
└── .gitignore
```

## Research Methodology

Every research cycle follows an 8-step loop:
1. **Scan** — Search papers, repos, benchmarks, blogs
2. **Filter** — Score by relevance, novelty, reproducibility, engineering value
3. **Read** — Write detailed cards for high-priority sources
4. **Map** — Link findings to agent modules
5. **Experiment** — Write executable experiment tickets
6. **Implement** — Build minimum viable prototypes
7. **Evaluate** — Measure task success, cost, failure types
8. **Remember** — Update memory, decisions, roadmap, risks

## Design Constraints

1. LLM never directly executes dangerous code — all actions go through safety layer
2. All game actions are interruptible (stop / pause / resume / rollback)
3. Every task must have measurable success criteria
4. Memory must resist pollution — only verified, reusable information enters long-term memory
5. Research must track licenses — record citation, reuse boundaries
6. Model providers must be swappable — no single-provider lock-in
7. Minecraft version must be pinned per experiment
8. No capability claims without 3+ repeated experiment results

## Current Phase

**M0: Research Baseline** — Building paper library, repo library, architecture draft, and first benchmark suite.

## Getting Started

```bash
# Clone the repository
git clone https://github.com/SakalioLabs/Singularity.git
cd Singularity

# Browse the research workspace
cd workspace
cat ROADMAP.md          # Phase roadmap
cat paper-index.md      # Related papers
cat repo-index.md       # Related open-source projects
cat current-architecture.md  # Current architecture design
```

## License

TBD — Research project. Individual dependencies retain their original licenses.

## Contact

- Repository: [SakalioLabs/Singularity](https://github.com/SakalioLabs/Singularity)
- Email: sakalioling@rankchord.com
