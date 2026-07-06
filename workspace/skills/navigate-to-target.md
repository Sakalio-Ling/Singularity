# Skill: Navigate to Target

> SK-008 | Status: Template | Version: 0.1

## Description

Navigate from current position to a target location using pathfinding.

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| target_x | float | required | Target X coordinate |
| target_z | float | required | Target Z coordinate |
| target_y | float | auto | Target Y (auto-find surface if not given) |
| max_distance | int | 200 | Max pathfinding distance |

## Preconditions

- Target coordinates known or estimable
- No immediate threats blocking path (handle separately)

## Postconditions

- Agent position within 2 blocks of target

## Failure Modes

| Failure | Cause | Recovery |
|---------|-------|----------|
| no_path | Unreachable target (lava, void, wall) | Find alternative route or abort |
| stuck | Pathfinder stuck on terrain | Manual movement to unstuck |
| too_far | Target beyond max_distance | Intermediate waypoint navigation |
| fell_in_hole | Path led to drop | Pillar up, re-navigate |

## Implementation

```
1. Calculate distance to target
2. If within 2 blocks: done
3. Set pathfinder goal to target coordinates
4. Monitor movement progress every 5 seconds
5. If no progress for 15 seconds: stuck handler
6. If arrived: verify position
7. If path fails: try direct movement or find intermediate point
```

## Notes

- mineflayer-pathfinder uses A* algorithm
- Can set goal as GoalBlock(x,y,z) or GoalNear(x,y,z,range)
- Pathfinder handles basic terrain but struggles with water, lava, and vertical drops
- For long distances, consider chunked navigation with waypoints
