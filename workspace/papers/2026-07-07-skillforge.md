# P-016: SkillForge

**Title**: SkillForge - Toward Generalist Embodied Agents via Skill Mining and Composition
**Year**: 2024
**Priority**: P3

## Core Method
Automated skill mining from successful trajectories. Skills are extracted, versioned, and composed for reuse.

## Key Contributions
- Automated skill extraction from task traces
- Skill composition for complex behaviors
- Version-tracked skill library with success rates

## Relevance to Singularity
- **Skill library**: SkillForge directly informs our SkillLibrary design (M3)
- **Skill extraction**: When a task succeeds, extract the action sequence as a reusable skill
- **Version tracking**: Our SkillLibrary already supports versioning and success rate tracking
- **Composition**: Complex skills (survive_first_night) can be composed from primitives (gather_wood, craft_tools, build_shelter)
