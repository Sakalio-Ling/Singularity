# Skill: Mine Iron

> SK-004 | Status: Template | Version: 0.1

## Description

Find and mine iron ore blocks, then smelt them into iron ingots.

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| quantity | int | 8 | Number of iron ingots needed |

## Preconditions

- Has at least a stone pickaxe
- Access to underground (y-level -64 to 64 where iron spawns)

## Postconditions

- At least `quantity` iron ingots in inventory (after smelting)

## Failure Modes

| Failure | Cause | Recovery |
|---------|-------|----------|
| no_stone_pickaxe | Need stone+ pickaxe for iron ore | Craft stone pickaxe first |
| no_iron_found | Bad luck with ore distribution | Mine at y=16 for best rates |
| lava_encounter | Underground lava pools | Retreat, mine around lava |
| no_fuel_for_smelting | Need coal/charcoal | Find coal or make charcoal |

## Implementation

```
1. Ensure stone pickaxe or better is equipped
2. Mine down to y=16 (optimal iron level)
3. Strip mine or explore caves for iron ore blocks
4. Mine iron ore (drops raw iron)
5. Return to surface or find furnace
6. Smelt raw iron with fuel (coal, charcoal, wood)
7. Collect iron ingots
```

## Notes

- Iron ore is most common at y=16 (0.5% of blocks)
- Each ore drops 1 raw iron (with silk touch, drops ore block)
- Smelting takes 10 seconds per item
- Fortune enchantment increases drop rate
