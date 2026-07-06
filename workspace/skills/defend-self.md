# Skill: Defend Self

> SK-007 | Status: Template | Version: 0.1

## Description

Defend against hostile mob attacks. Prioritize survival over killing mobs.

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| mode | str | "evade" | "evade", "fight", "flee" |

## Preconditions

- Hostile mob(s) detected nearby or taking damage

## Postconditions

- Health stabilized (not actively taking damage)
- Mob threat neutralized or distance from threat

## Failure Modes

| Failure | Cause | Recovery |
|---------|-------|----------|
| low_health | Health below 4 hearts | Eat food immediately, flee to safety |
| no_weapon | No sword or weapon | Use fists or flee |
| overwhelmed | Too many mobs | Build emergency pillar (2 blocks up) |
| no_food | Cannot heal | Retreat to shelter, wait for regeneration |

## Implementation

```
1. Assess threat: mob type, count, distance
2. If health < 6: eat available food first
3. If mode == "evade": create distance, place blocks as barrier
4. If mode == "fight": equip best weapon, attack nearest mob
5. If mode == "flee": sprint away, place blocks behind
6. If overwhelmed: pillar up 2 blocks, wait for mobs to despawn or daylight
```

## Notes

- Zombies burn in sunlight; can wait until dawn if safe
- Spiders become neutral in daylight
- Creepers are highest priority (explosive damage)
- Skeletons are dangerous at range (close distance or use cover)
- Endermen only attack if looked at directly
