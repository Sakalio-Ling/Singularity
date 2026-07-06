"""Skill library — stores, versions, and retrieves reusable action skills."""
import json
import time
import logging
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger("singularity.skills")


@dataclass
class Skill:
    name: str
    description: str = ""
    parameters: dict = field(default_factory=dict)
    preconditions: dict = field(default_factory=dict)
    postconditions: dict = field(default_factory=dict)
    required_items: list = field(default_factory=list)
    failure_modes: list = field(default_factory=list)
    implementation: str = ""  # code or action sequence
    examples: list = field(default_factory=list)
    version: str = "1.0"
    success_rate: float = 0.0
    total_uses: int = 0
    successful_uses: int = 0
    last_used: Optional[str] = None
    layer: str = "composite"  # primitive, composite, strategic, social, meta
    notes: str = ""


class SkillLibrary:
    def __init__(self, storage_path: str = "workspace/skills"):
        self.storage_path = storage_path
        self.skills: dict[str, Skill] = {}
        self._load_builtin_skills()

    def _load_builtin_skills(self):
        """Load pre-defined skill templates."""
        builtins = [
            Skill("move_to", "Navigate to target coordinates", {"x": "float", "z": "float"}, layer="primitive"),
            Skill("look_at", "Look at target position", {"x": "float", "y": "float", "z": "float"}, layer="primitive"),
            Skill("dig_block", "Dig block at position", {"x": "int", "y": "int", "z": "int"}, layer="primitive"),
            Skill("place_block", "Place block at position", {"x": "int", "y": "int", "z": "int", "item": "str"}, layer="primitive"),
            Skill("craft_item", "Craft item from recipe", {"item": "str", "count": "int"}, layer="primitive"),
            Skill("attack_entity", "Attack nearest hostile entity", {}, layer="primitive"),
            Skill("eat_food", "Eat best available food", {}, layer="primitive"),
            Skill("gather_wood", "Find and chop trees for logs", {"wood_type": "str", "quantity": "int"}, layer="composite",
                  success_rate=0.0, notes="Works best with axe. Hand gathering is slow."),
            Skill("craft_tools", "Craft tools from available materials", {"tool_type": "str", "material": "str"}, layer="composite"),
            Skill("mine_stone", "Mine cobblestone underground", {"quantity": "int"}, layer="composite"),
            Skill("mine_iron", "Find and mine iron ore", {"quantity": "int"}, layer="composite"),
            Skill("smelt_iron", "Smelt raw iron into ingots", {"quantity": "int"}, layer="composite"),
            Skill("build_shelter", "Build a simple shelter", {"size": "str"}, layer="composite"),
            Skill("defend_self", "Defend against hostile mobs", {"mode": "str"}, layer="composite"),
            Skill("navigate_to_target", "Pathfind to coordinates", {"x": "float", "z": "float"}, layer="composite"),
            Skill("survive_first_night", "Complete first night survival", {}, layer="strategic"),
            Skill("prepare_for_mining", "Gather tools and torches for mining", {}, layer="strategic"),
        ]
        for skill in builtins:
            self.skills[skill.name] = skill

    def get_skill(self, name: str) -> Optional[Skill]:
        return self.skills.get(name)

    def list_skills(self, layer: Optional[str] = None) -> list[Skill]:
        if layer:
            return [s for s in self.skills.values() if s.layer == layer]
        return list(self.skills.values())

    def create_skill(self, name: str, description: str, implementation: str, **kwargs) -> Skill:
        skill = Skill(name=name, description=description, implementation=implementation, **kwargs)
        self.skills[name] = skill
        return skill

    def record_use(self, name: str, success: bool):
        skill = self.skills.get(name)
        if skill:
            skill.total_uses += 1
            if success:
                skill.successful_uses += 1
            skill.success_rate = skill.successful_uses / skill.total_uses if skill.total_uses > 0 else 0
            skill.last_used = time.strftime("%Y-%m-%d")

    def get_recommended_skills(self, goal: str, world_state: dict) -> list[Skill]:
        """Return skills that match the current context, sorted by success rate."""
        candidates = [s for s in self.skills.values() if s.total_uses > 0]
        candidates.sort(key=lambda s: s.success_rate, reverse=True)
        return candidates[:5]
