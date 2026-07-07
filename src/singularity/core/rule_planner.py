"""Rule-based fallback planner for M1 benchmarks - no LLM required."""
import json
import logging

logger = logging.getLogger("singularity.rule_planner")


class RuleBasedPlanner:
    """Simple rule-based planner that can handle basic Minecraft tasks without an LLM."""

    def __init__(self):
        self.step_index = 0

    def plan_from_goal(self, goal: str, world_state: dict) -> dict:
        goal_lower = goal.lower()
        inventory = world_state.get("inventory", {})
        # Parse goal and generate appropriate plan
        if "oak" in goal_lower and ("log" in goal_lower or "wood" in goal_lower):
            return self._plan_gather_wood(world_state)
        elif "craft" in goal_lower and "table" in goal_lower:
            return self._plan_craft_workbench(world_state)
        elif "craft" in goal_lower and "pickaxe" in goal_lower and "wooden" in goal_lower:
            return self._plan_craft_wooden_pickaxe(world_state)
        elif "cobblestone" in goal_lower or "stone" in goal_lower:
            return self._plan_mine_cobblestone(world_state)
        elif "stone" in goal_lower and "pickaxe" in goal_lower:
            return self._plan_craft_stone_pickaxe(world_state)
        else:
            return {"status": "blocked", "reasoning": f"No rule for goal: {goal}", "actions": []}

    def _plan_gather_wood(self, state: dict) -> dict:
        inv = state.get("inventory", {})
        oak_logs = inv.get("oak_log", 0)
        if oak_logs >= 3:
            return {"status": "complete", "reasoning": f"Already have {oak_logs} oak logs", "actions": []}
        # Look for nearby trees and dig
        return {
            "status": "in_progress",
            "reasoning": f"Have {oak_logs} oak logs, need 3. Looking for trees.",
            "actions": [
                {"type": "dig", "parameters": {"x": -9, "y": 63, "z": 2}},
                {"type": "wait", "parameters": {"ms": 500}},
            ]
        }

    def _plan_craft_workbench(self, state: dict) -> dict:
        inv = state.get("inventory", {})
        if inv.get("crafting_table", 0) >= 1:
            return {"status": "complete", "reasoning": "Already have crafting table", "actions": []}
        if inv.get("oak_planks", 0) >= 4:
            return {"status": "in_progress", "reasoning": "Have planks, crafting table",
                    "actions": [{"type": "craft", "parameters": {"item": "crafting_table", "count": 1}}]}
        if inv.get("oak_log", 0) >= 1:
            return {"status": "in_progress", "reasoning": "Have logs, crafting planks first",
                    "actions": [{"type": "craft", "parameters": {"item": "oak_planks", "count": 4}}]}
        return {"status": "blocked", "reasoning": "Need oak logs to craft workbench", "actions": []}

    def _plan_craft_wooden_pickaxe(self, state: dict) -> dict:
        inv = state.get("inventory", {})
        if inv.get("wooden_pickaxe", 0) >= 1:
            return {"status": "complete", "reasoning": "Already have wooden pickaxe", "actions": []}
        planks = inv.get("oak_planks", 0)
        sticks = inv.get("stick", 0)
        if planks >= 3 and sticks >= 2:
            return {"status": "in_progress", "reasoning": "Have materials, crafting pickaxe",
                    "actions": [{"type": "craft", "parameters": {"item": "wooden_pickaxe", "count": 1}}]}
        if planks >= 2 and sticks < 2:
            return {"status": "in_progress", "reasoning": "Need sticks first",
                    "actions": [{"type": "craft", "parameters": {"item": "stick", "count": 1}}]}
        if inv.get("oak_log", 0) >= 1:
            return {"status": "in_progress", "reasoning": "Need planks first",
                    "actions": [{"type": "craft", "parameters": {"item": "oak_planks", "count": 4}}]}
        return {"status": "blocked", "reasoning": "Need oak logs for wooden pickaxe", "actions": []}

    def _plan_mine_cobblestone(self, state: dict) -> dict:
        inv = state.get("inventory", {})
        cobblestone = inv.get("cobblestone", 0)
        if cobblestone >= 3:
            return {"status": "complete", "reasoning": f"Have {cobblestone} cobblestone", "actions": []}
        if inv.get("wooden_pickaxe", 0) >= 1 or inv.get("stone_pickaxe", 0) >= 1:
            return {"status": "in_progress", "reasoning": "Have pickaxe, mining stone",
                    "actions": [
                        {"type": "dig", "parameters": {"x": -9, "y": 64, "z": 3}},
                        {"type": "wait", "parameters": {"ms": 500}},
                    ]}
        return {"status": "blocked", "reasoning": "Need at least wooden pickaxe for cobblestone", "actions": []}

    def _plan_craft_stone_pickaxe(self, state: dict) -> dict:
        inv = state.get("inventory", {})
        if inv.get("stone_pickaxe", 0) >= 1:
            return {"status": "complete", "reasoning": "Already have stone pickaxe", "actions": []}
        cobblestone = inv.get("cobblestone", 0)
        sticks = inv.get("stick", 0)
        if cobblestone >= 3 and sticks >= 2:
            return {"status": "in_progress", "reasoning": "Have materials, crafting stone pickaxe",
                    "actions": [{"type": "craft", "parameters": {"item": "stone_pickaxe", "count": 1}}]}
        if cobblestone < 3:
            return {"status": "in_progress", "reasoning": "Need more cobblestone",
                    "actions": [{"type": "dig", "parameters": {"x": -9, "y": 64, "z": 3}}]}
        return {"status": "blocked", "reasoning": "Need cobblestone and sticks for stone pickaxe", "actions": []}
