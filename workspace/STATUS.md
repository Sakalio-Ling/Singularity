# STATUS.md | Last updated: 2026-07-07

## Current Phase: M1 (Minimum Viable Bot) - 95%, M3 Skill Library - 65%

## Phase Progress
| Phase | Status | Progress |
|-------|--------|----------|
| M0: Research Baseline | **Complete** | 100% |
| M1: Minimum Viable Bot | **In Progress** | 95% |
| M2: LLM Task Planning | Source Complete | 70% |
| M3: Skill Library & Memory | Source Complete | 65% |
| M4-M7 | Planned | 10% |

## M0 Complete
- 17/17 paper cards, 19 implementation notes, 8 architecture modules
- 5 benchmark suites (14 tasks), research analysis RQ1-RQ10

## M1 Progress (95%)
- [x] Python agent package (22 files)
- [x] Node.js Mineflayer bot server with pathfinding
- [x] JDK 17 + MC 1.20.4 server
- [x] EXP-0001: Bot connected to MC server
- [x] EXP-0002: State reading (health, food, position)
- [x] EXP-0003: Block digging (grass_block)
- [x] EXP-0004: Observe-plan-act loop with rule planner
- [x] Observer scans 32-block radius for trees
- [x] Rule planner navigates to found trees
- [ ] BM-001 through BM-005 benchmarks

## M2 Progress (70%)
- [x] Planner with crafting recipes knowledge injection
- [x] Knowledge base loader (recipes, can_craft, chains)
- [x] Rule-based fallback planner
- [x] M2 integration test script
- [ ] End-to-end testing with LLM API

## M3 Progress (65%)
- [x] Skill library with 17 builtin skills
- [x] L0-L6 memory system
- [x] Skill extractor from session logs
- [ ] Skill extraction from successful traces
- [ ] Session persistence and recovery

## Repository
- **Commits**: 40 on master, synced to both remotes
- **Remotes**: SakalioLabs/Singularity, Sakalio-Ling/Singularity
- **Files**: 22 Python + 1 JS + setup.ps1
- **Docs**: 70+ workspace documents
