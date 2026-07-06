"""Reflector — analyzes failures and triggers re-planning."""
import json
import logging
from typing import Optional

from singularity.llm.provider import LLMProvider

logger = logging.getLogger("singularity.reflector")


class Reflector:
    def __init__(self, llm: LLMProvider):
        self.llm = llm
        self.reflections: list[dict] = []

    def analyze_failure(self, task_title: str, action: dict, result: dict, world_state: dict) -> dict:
        prompt = f"""Task: {task_title}
Failed action: {json.dumps(action)}
Error: {result.get('error', 'unknown')}
World state: {json.dumps(world_state, default=str)[:1000]}

Analyze the failure:
1. What went wrong?
2. Was it a planning error, action error, environment change, or resource issue?
3. Should we retry with the same approach, try a different approach, or give up?
4. What should we do differently?

Output JSON:
{{"category": "planning|action|environment|resource|unknown", "analysis": "...", "suggestion": "...", "should_retry": true/false, "new_approach": "..."}}"""

        response = self.llm.chat([
            {"role": "system", "content": "You are a failure analysis expert for a Minecraft agent. Be concise and actionable."},
            {"role": "user", "content": prompt},
        ], response_format={"type": "json_object"})

        try:
            reflection = json.loads(response)
        except json.JSONDecodeError:
            reflection = {"category": "unknown", "analysis": "Parse error", "should_retry": True}

        self.reflections.append(reflection)
        logger.info(f"Reflection: {reflection.get('category')} - {reflection.get('analysis', '')[:100]}")
        return reflection

    def generate_summary(self, task_title: str, success: bool, reflections: list[dict]) -> str:
        if not reflections:
            return f"Task '{task_title}' {'succeeded' if success else 'failed'} with no reflections."
        prompt = f"""Summarize what happened during task '{task_title}' (success={success}):
Reflections: {json.dumps(reflections[:5], default=str)[:1000]}
Write a 2-3 sentence summary of key learnings."""
        return self.llm.chat([
            {"role": "system", "content": "Summarize task experiences concisely."},
            {"role": "user", "content": prompt},
        ])
