"""Memory system — multi-layered memory for the Singularity agent."""
import json
import time
import os
import logging
from typing import Optional

logger = logging.getLogger("singularity.memory")


class MemorySystem:
    """Multi-layer memory: L0 Context, L1 Working, L2 Episodic, L3 Semantic, L4 Skill, L5 Decision, L6 Research."""

    def __init__(self, memory_dir: str = "workspace/memory", max_context_tokens: int = 4000):
        self.memory_dir = memory_dir
        self.max_context_tokens = max_context_tokens
        os.makedirs(memory_dir, exist_ok=True)
        # In-memory layers
        self.l0_context: list[dict] = []     # Current cycle context
        self.l1_working: dict = {}           # Session working memory
        self.l2_episodic: list[dict] = []    # Episode log
        self.l3_semantic: dict = {}          # Verified facts
        self.l4_skill: dict = {}             # Skill metadata
        self.l5_decision: list[dict] = []    # Architecture decisions
        self.l6_research: list[dict] = []    # Paper/repo cards

    def write_context(self, entry: dict):
        """L0: Write to current context window."""
        entry["timestamp"] = time.time()
        self.l0_context.append(entry)
        if len(self.l0_context) > 50:
            self.l0_context = self.l0_context[-30:]

    def write_working(self, key: str, value):
        """L1: Write to working memory."""
        self.l1_working[key] = value

    def write_episode(self, event_type: str, data: dict):
        """L2: Write episodic memory entry."""
        entry = {"timestamp": time.time(), "type": event_type, "data": data}
        self.l2_episodic.append(entry)

    def write_fact(self, key: str, value: str, source: str = ""):
        """L3: Write verified semantic fact. Only use for confirmed information."""
        self.l3_semantic[key] = {"value": value, "source": source, "verified": True, "timestamp": time.time()}

    def get_context_window(self) -> str:
        """Get L0+L1 combined context for LLM, token-bounded."""
        parts = []
        for entry in self.l0_context[-10:]:
            parts.append(json.dumps(entry, default=str)[:200])
        for k, v in list(self.l1_working.items())[:5]:
            parts.append(f"{k}: {json.dumps(v, default=str)[:100]}")
        return "\n".join(parts)[:self.max_context_tokens]

    def get_relevant_memory(self, query: str) -> str:
        """Search L2+L3 for information relevant to query."""
        parts = []
        for key, fact in self.l3_semantic.items():
            if any(word in key.lower() or word in fact["value"].lower() for word in query.lower().split()[:3]):
                parts.append(f"Fact: {key} = {fact['value']}")
        for ep in self.l2_episodic[-20:]:
            if any(word in json.dumps(ep, default=str).lower() for word in query.lower().split()[:3]):
                parts.append(f"Experience: {ep['type']} - {json.dumps(ep['data'], default=str)[:100]}")
        return "\n".join(parts[:10])

    def save_session(self, session_id: str):
        """Save episodic memory to daily journal file."""
        date_str = time.strftime("%Y-%m-%d")
        filepath = os.path.join(self.memory_dir, f"{date_str}.md")
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"\n## Session {session_id}\n")
            for entry in self.l2_episodic:
                f.write(f"- [{entry['type']}] {json.dumps(entry['data'], default=str)[:200]}\n")
        logger.info(f"Session saved to {filepath}")

    def clear_session(self):
        """Clear L0 and L1 (session-specific). Keep L2+ for long-term."""
        self.l0_context.clear()
        self.l1_working.clear()
