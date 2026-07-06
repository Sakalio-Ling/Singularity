# Skill Index — Reusable Agent Skills

> Last updated: 2026-07-07
> Skill status: template (not yet implemented)

## Skill Registry

| ID | Name | Layer | Status | Success Rate | Version |
|----|------|-------|--------|-------------|---------|
| SK-001 | gather-wood | Composite | Template | N/A | 0.1 |
| SK-002 | craft-tools | Composite | Template | N/A | 0.1 |
| SK-003 | mine-stone | Composite | Template | N/A | 0.1 |
| SK-004 | mine-iron | Composite | Template | N/A | 0.1 |
| SK-005 | smelt-iron | Composite | Template | N/A | 0.1 |
| SK-006 | build-shelter | Composite | Template | N/A | 0.1 |
| SK-007 | defend-self | Composite | Template | N/A | 0.1 |
| SK-008 | navigate-to-target | Primitive | Template | N/A | 0.1 |

## Primitive Skills (Mineflayer API)

| Skill | Action |
|-------|--------|
| move_forward | bot.setControlState('forward', true) |
| move_backward | bot.setControlState('back', true) |
| strafe_left | bot.setControlState('left', true) |
| strafe_right | bot.setControlState('right', true) |
| jump | bot.setControlState('jump', true) |
| look_at | bot.lookAt(yaw, pitch) |
| dig | bot.dig(block) |
| place | bot.placeBlock(ref, face) |
| craft | bot.craft(recipe, count) |
| attack | bot.attack(entity) |
| equip | bot.equip(item, destination) |
| drop | bot.tossStack(item) |
| open_container | bot.openContainer(block) |
| chat | bot.chat(message) |
| wait | bot.waitForTicks(n) |

## Skill Composition

Skills can be composed:
- gather-wood = find_tree + navigate_to + dig_block (repeat)
- craft-tools = check_materials + open_crafting + craft_recipe
- build-shelter = select_site + gather_materials + place_blocks

## How Skills Are Created

1. **Manual**: Human writes skill definition and implementation
2. **Auto-extracted**: From successful task trace (Voyager-style)
3. **LLM-generated**: Planner proposes skill, validated by testing

## Template Format

Each skill file in skills/ follows:
- Name, description, parameters, preconditions, postconditions
- Required items, failure modes
- Implementation (code or action sequence)
- Examples, tests, version history, notes
