"""Planner - LLM-powered goal decomposition and action planning with Minecraft knowledge injection."""
import json
import os
import logging
from typing import Optional

from singularity.llm.provider import LLMProvider
from singularity.core.task_system import TaskSystem, Task, TaskStatus

logger = logging.getLogger("singularity.planner")

# Load crafting recipes at module level
_RECIPES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'crafting_recipes.json')
_CRAFTING_KNOWLEDGE = ""
try:
    with open(_RECIPES_PATH, 'r', encoding='utf-8') as f:
        _data = json.load(f)
        _CRAFTING_KNOWLEDGE = json.dumps(_data, indent=1)
except Exception:
    _CRAFTING_KNOWLEDGE = "{}"


class Planner:
    def __init__(self, llm: LLMProvider, task_system: TaskSystem):
        self.llm = llm
        self.task_system = task_system

    def plan_from_goal(self, goal: str, world_state: dict, memory_context: str = "") -> dict:
        prompt = self._build_planning_prompt(goal, world_state, memory_context)
        response = self.llm.chat([
            {"role": "system", "content": self._planner_system_prompt()},
            {"role": "user", "content": prompt},
        ], response_format={"type": "json_object"})
        try:
            plan = json.loads(response)
        except json.JSONDecodeError:
            plan = {"status": "error", "subtasks": [], "actions": [], "reasoning": "Failed to parse LLM output"}
        subtasks = plan.get("subtasks", [])
        for st in subtasks:
            self.task_system.create_task(
                title=st.get("title", "unnamed"),
                task_type=st.get("type", "general"),
                success_criteria=st.get("success_criteria", {}),
                priority=st.get("priority", 3),
            )
        return plan

    def replan(self, failed_task: Task, world_state: dict, failure_reason: str) -> dict:
        prompt = f"""Task '{failed_task.title}' failed: {failure_reason}
Attempts so far: {failed_task.attempts}
Current state: {json.dumps(world_state, default=str)[:1000]}
Suggest a new plan. Output JSON: {{"status":"replan","subtasks":[...],"actions":[...],"reasoning":"..."}}"""
        response = self.llm.chat([
            {"role": "system", "content": "You are a replanning system. Analyze failures and propose alternative approaches."},
            {"role": "user", "content": prompt},
        ], response_format={"type": "json_object"})
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"status": "error", "subtasks": [], "actions": [], "reasoning": "Parse error"}

    def _planner_system_prompt(self) -> str:
        return f"""You are a Minecraft survival planner. Given a goal and current world state, decompose it into subtasks and immediate actions.

Available actions: move_to, look_at, dig, place, craft, attack, equip, use_item, chat, wait.

MINECRAFT CRAFTING RECIPES:
{_CRAFTING_KNOWLEDGE}

TOOL PROGRESSION: hand -> wooden -> stone -> iron -> diamond
To mine stone/cobblestone you need at least a wooden pickaxe.
To mine iron_ore you need at least a stone pickaxe.
To get oak_planks, craft them from oak_log (1 log = 4 planks).
To get sticks, craft from 2 planks (2 planks = 4 sticks).
You can punch trees to get oak_log without any tools.

Output JSON:
{{
  "status": "planning" or "complete" or "blocked",
  "reasoning": "brief strategic explanation",
  "subtasks": [
    {{"title": "...", "type": "...", "priority": 1-5, "success_criteria": {{...}}}}
  ],
  "actions": [
    {{"type": "action_name", "parameters": {{...}}}}
  ]
}}

Be practical and safe. Check inventory before crafting. Follow tool progression."""

    def _build_planning_prompt(self, goal: str, world_state: dict, memory_context: str) -> str:
        return f"""Goal: {goal}

World state:
{json.dumps(world_state, indent=2, default=str)[:2000]}

{f'Relevant memory: {memory_context}' if memory_context else ''}

Plan the steps to achieve this goal."""
