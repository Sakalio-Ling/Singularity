# Module: Perception (Observation Layer)

> Status: Design (M0)
> Owner: Core Agent

## Purpose

Collect raw game state from the Minecraft bot and produce structured observations for the World State module.

## Observations Collected

| Category | Data Points |
|----------|------------|
| Player State | position (x,y,z), yaw, pitch, health, hunger, experience, level |
| Inventory | All items with counts, equipment slots |
| Environment | Nearby blocks (6-directional + radius scan), biome, time_of_day, weather |
| Entities | Nearby mobs (type, distance, health), nearby players |
| Interaction | Chat messages, container contents, villager trades |
| Events | Damage taken, item picked up, block broken, entity killed |

## Interface

```
observe(bot) -> Observation {
  player: { position, yaw, pitch, health, hunger, xp_level },
  inventory: list[Item],
  nearby_blocks: list[BlockInfo],  // type, position, distance
  nearby_entities: list[EntityInfo],  // type, position, health, hostile
  time_of_day: int,  // 0-24000 ticks
  weather: str,  // clear, rain, thunder
  biome: str,
  chat: list[str],
  events: list[Event]
}
```

## Scan Modes

- **Fast**: Player state + inventory + immediate surroundings (1 tick)
- **Normal**: + nearby entities + 10-block radius block scan
- **Deep**: + full environment scan + container contents
- **Combat**: + hostile mob tracking + threat assessment

## Dependencies

- Mineflayer bot API (bot.entity, bot.inventory, bot.entities, bot.blockAt, etc.)

## Notes

- Observations should be token-efficient for LLM consumption (summarize, don't dump raw)
- Store raw observations for replay/debugging alongside summaries for LLM
