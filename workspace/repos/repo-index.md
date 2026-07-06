# Repo Index — Open Source Projects for Minecraft Agent

> Last updated: 2026-07-07
> Scoring: Relevance / Activity / Ease-of-Use / Reusability (1-5 each)

---

## R-001: Mineflayer

- **URL**: https://github.com/PrismarineJS/mineflayer
- **License**: MIT
- **Language**: JavaScript (Node.js)
- **MC Version**: 1.8 - 1.21
- **Activity**: Very Active (10k+ stars, regular updates)
- **Description**: Full-featured Minecraft bot framework. Create bots that can move, dig, place, craft, attack, trade, and more.
- **Dependencies**: prismarine-* ecosystem
- **Install Difficulty**: Easy (npm install)
- **Reproducibility**: High
- **Reusable Modules**: Bot API, pathfinding plugin, inventory management, entity tracking
- **Risks**: Node.js only (need Python bridge for agent logic)
- **Scores**: R=5, A=5, E=5, U=5
- **Use in Project**: Primary action interface for M1+

---

## R-002: Baritone

- **URL**: https://github.com/cabaletta/baritone
- **License**: LGPL-3.0 (careful with linking)
- **Language**: Java
- **MC Version**: 1.12 - 1.21 (various branches)
- **Activity**: Active (7k+ stars)
- **Description**: Advanced pathfinding and automated Minecraft gameplay. Used as a Minecraft mod.
- **Dependencies**: Minecraft Forge / Fabric
- **Install Difficulty**: Medium (mod installation)
- **Reproducibility**: Medium (version-specific branches)
- **Reusable Modules**: A* pathfinding, building automation, mining automation
- **Risks**: LGPL license requires careful handling. Tightly coupled to Minecraft mod loader.
- **Scores**: R=4, A=4, E=3, U=4
- **Use in Project**: Optional pathfinding addon (M2+)

---

## R-003: Mindcraft

- **URL**: https://github.com/kolbytn/mindcraft
- **License**: MIT
- **Language**: JavaScript
- **MC Version**: 1.20+
- **Activity**: Active (4k+ stars, 2024)
- **Description**: LLM-powered Minecraft agent platform. Uses Mineflayer + LLM for autonomous gameplay.
- **Dependencies**: Mineflayer, OpenAI/Anthropic API
- **Install Difficulty**: Easy
- **Reproducibility**: High
- **Reusable Modules**: Agent framework, LLM integration, skill system, conversation management
- **Risks**: Early-stage, may lack robust error handling
- **Scores**: R=5, A=4, E=5, U=5
- **Use in Project**: Direct engineering reference, possible fork/integration base

---

## R-004: Voyager (Minecraft)

- **URL**: https://github.com/MineDojo/Voyager
- **License**: Apache 2.0
- **Language**: JavaScript + Python
- **MC Version**: 1.19 (Mineflayer)
- **Activity**: Archived (research project, 4k+ stars)
- **Description**: Open-ended embodied agent using LLM. Code-as-skill library, curriculum, self-verification.
- **Dependencies**: Mineflayer, MineDojo environment, OpenAI API
- **Install Difficulty**: Medium (MineDojo dependency)
- **Reproducibility**: Medium (specific environment version)
- **Reusable Modules**: Skill library design, curriculum, verification system
- **Risks**: Archived, MineDojo dependency, not directly runnable
- **Scores**: R=5, A=2, E=3, U=4
- **Use in Project**: Architectural reference for skill library and curriculum

---

## R-005: MineDojo

- **URL**: https://github.com/MineDojo/MineDojo
- **License**: MIT
- **Language**: Python
- **MC Version**: N/A (simulation environment)
- **Activity**: Moderate (research, 2k+ stars)
- **Description**: Open-ended embodied agent benchmark with 1000+ tasks, YouTube pretraining, simulation environment.
- **Dependencies**: Minecraft, MineRL, custom environment
- **Install Difficulty**: Hard (complex environment setup)
- **Reproducibility**: Low-Medium (heavy dependencies)
- **Reusable Modules**: Benchmark suite, task taxonomy, evaluation framework
- **Risks**: Heavy setup, may be overkill for initial development
- **Scores**: R=4, A=3, E=2, U=3
- **Use in Project**: Benchmark design reference (task taxonomy)

---

## R-006: Mineflayer-Pathfinder

- **URL**: https://github.com/PrismarineJS/mineflayer-pathfinder
- **License**: MIT
- **Language**: JavaScript
- **MC Version**: Matches Mineflayer
- **Activity**: Active (part of PrismarineJS ecosystem)
- **Description**: Pathfinding plugin for Mineflayer. A* navigation, goal-based movement.
- **Dependencies**: Mineflayer, prismarine-world
- **Install Difficulty**: Easy (npm plugin)
- **Reproducibility**: High
- **Reusable Modules**: A* pathfinding, goal system, movement controls
- **Risks**: None significant
- **Scores**: R=4, A=5, E=5, U=5
- **Use in Project**: Navigation module for M1+

---

## R-007: prismarine-viewer

- **URL**: https://github.com/PrismarineJS/prismarine-viewer
- **License**: MIT
- **Language**: JavaScript
- **MC Version**: 1.8 - 1.20
- **Activity**: Active
- **Description**: Web-based 3D viewer for Minecraft bot state. Useful for debugging and monitoring.
- **Dependencies**: Mineflayer
- **Install Difficulty**: Easy
- **Reproducibility**: High
- **Reusable Modules**: Web viewer, block visualization, entity rendering
- **Risks**: Performance on large worlds
- **Scores**: R=3, A=4, E=5, U=4
- **Use in Project**: Debugging tool, agent state visualization

---

## R-008: Quarry (Python Minecraft Protocol)

- **URL**: https://github.com/barneygale/quarry
- **License**: MIT/GPL-3.0
- **Language**: Python
- **MC Version**: 1.7 - 1.20
- **Activity**: Low-Moderate
- **Description**: Pure Python implementation of Minecraft protocol. Alternative to Mineflayer.
- **Dependencies**: twisted (Python networking)
- **Install Difficulty**: Medium
- **Reproducibility**: Medium
- **Reusable Modules**: Protocol implementation, packet handling
- **Risks**: Less feature-complete than Mineflayer. Limited community.
- **Scores**: R=3, A=2, E=3, U=3
- **Use in Project**: Alternative if Python-only stack needed (eliminates Node.js bridge)

---

## R-009: GROOT / Mars (ByteDance Minecraft Agent)

- **URL**: https://github.com/minecraft-analysis (various repos)
- **License**: TBD (check per repo)
- **Language**: Python + C++
- **MC Version**: Various
- **Activity**: Low-Moderate
- **Description**: Research group projects on Minecraft agents, visual understanding, and VLA.
- **Dependencies**: Various
- **Install Difficulty**: Hard
- **Reproducibility**: Low
- **Reusable Modules**: Visual understanding components
- **Risks**: Sparse documentation, may not be maintained
- **Scores**: R=3, A=2, E=1, U=2
- **Use in Project**: VLA research reference (M6)

---

## R-010: MineRL

- **URL**: https://github.com/minerllabs/minerl
- **License**: MIT
- **Language**: Python
- **MC Version**: 1.16 (Minecraft jar included)
- **Activity**: Moderate (research, 2k+ stars)
- **Description**: Research environment for RL in Minecraft. Includes pre-collected datasets and Gym-like interface.
- **Dependencies**: Minecraft, Java, custom Malmo/MineRL backend
- **Install Difficulty**: Hard
- **Reproducibility**: Low-Medium
- **Reusable Modules**: Gym interface, dataset, evaluation tools
- **Risks**: Heavy dependency, version-locked, complex setup
- **Scores**: R=3, A=3, E=2, U=2
- **Use in Project**: Alternative environment for RL experiments (future)

---

## R-011: OpenAI Gym Minecraft (Malmo / Project Malmo successor)

- **URL**: https://github.com/microsoft/malmo (archived)
- **License**: MIT
- **Language**: Python / Java
- **MC Version**: 1.11 (archived)
- **Activity**: Archived (no updates)
- **Description**: Microsoft research platform for AI in Minecraft.
- **Dependencies**: Minecraft, Java, custom server mod
- **Install Difficulty**: Hard
- **Reproducibility**: Low (archived, old version)
- **Reusable Modules**: Mission XML format, Gym-like interface concept
- **Risks**: Dead project, incompatible with modern Minecraft
- **Scores**: R=2, A=1, E=2, U=2
- **Use in Project**: Historical reference only

---

## Summary Table

| ID | Project | License | Language | Scores | Priority |
|----|---------|---------|----------|--------|----------|
| R-001 | Mineflayer | MIT | JS | R5/A5/E5/U5 | P1 |
| R-002 | Baritone | LGPL-3.0 | Java | R4/A4/E3/U4 | P2 |
| R-003 | Mindcraft | MIT | JS | R5/A4/E5/U5 | P1 |
| R-004 | Voyager | Apache 2.0 | JS+Py | R5/A2/E3/U4 | P1 |
| R-005 | MineDojo | MIT | Py | R4/A3/E2/U3 | P2 |
| R-006 | mineflayer-pathfinder | MIT | JS | R4/A5/E5/U5 | P1 |
| R-007 | prismarine-viewer | MIT | JS | R3/A4/E5/U4 | P3 |
| R-008 | Quarry | MIT/GPL | Py | R3/A2/E3/U3 | P3 |
| R-009 | GROOT | TBD | Py/C++ | R3/A2/E1/U2 | P4 |
| R-010 | MineRL | MIT | Py | R3/A3/E2/U2 | P3 |
| R-011 | Malmo | MIT | Py/Java | R2/A1/E2/U2 | P5 |
