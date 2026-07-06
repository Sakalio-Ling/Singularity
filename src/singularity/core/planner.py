"""Planner — LLM-powered goal decomposition and action planning."""
import json
import logging
from typing import Optional

from singularity.llm.provider import LLMProvider
from singularity.core.task_system import TaskSystem, Task, TaskStatus

logger = logging.getLogger("singularity.planner")


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
        return """You are a Minecraft survival planner. Given a goal and current world state, decompose it into subtasks and immediate actions.

Output JSON:
{
  "status": "planning",
  "reasoning": "brief strategic explanation",
  "subtasks": [
    {"title": "...", "type": "...", "priority": 1-5, "success_criteria": {...}}
  ],
  "actions": [
    {"type": "action_name", "parameters": {...}}
  ]
}

Available actions: move_to, look_at, dig, place, craft, attack, equip, use_item, chat, wait.
Be practical and safe. Check inventory before crafting."""

    def _build_planning_prompt(self, goal: str, world_state: dict, memory_context: str) -> str:
        return f"""Goal: {goal}

World state:
{json.dumps(world_state, indent=2, default=str)[:2000]}

{f'Relevant memory: {memory_context}' if memory_context else ''}

Plan the steps to achieve this goal."""
