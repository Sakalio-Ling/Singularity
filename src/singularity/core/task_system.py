"""Task system — hierarchical task management with states, dependencies, and priorities."""
import time
import uuid
import logging
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger("singularity.task")


class TaskStatus(Enum):
    PROPOSED = "proposed"
    ACCEPTED = "accepted"
    ACTIVE = "active"
    WAITING = "waiting"
    BLOCKED = "blocked"
    FAILED = "failed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    title: str = ""
    type: str = "general"
    parent_id: Optional[str] = None
    status: TaskStatus = TaskStatus.PROPOSED
    priority: int = 3  # 0=highest
    preconditions: dict = field(default_factory=dict)
    success_criteria: dict = field(default_factory=dict)
    failure_criteria: dict = field(default_factory=dict)
    assigned_skill: Optional[str] = None
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)
    attempts: int = 0
    observations: list = field(default_factory=list)
    blockers: list = field(default_factory=list)
    result: Optional[dict] = None
    children: list = field(default_factory=list)


class TaskSystem:
    def __init__(self):
        self.tasks: dict[str, Task] = {}
        self.root_tasks: list[str] = []

    def create_task(self, title: str, task_type: str = "general", parent_id: Optional[str] = None, **kwargs) -> Task:
        task = Task(title=title, type=task_type, parent_id=parent_id, **kwargs)
        self.tasks[task.id] = task
        if parent_id and parent_id in self.tasks:
            self.tasks[parent_id].children.append(task.id)
        else:
            self.root_tasks.append(task.id)
        return task

    def update_task(self, task_id: str, status: Optional[TaskStatus] = None, observations: Optional[list] = None, result: Optional[dict] = None):
        task = self.tasks.get(task_id)
        if not task:
            return
        if status:
            task.status = status
        if observations:
            task.observations.extend(observations)
        if result:
            task.result = result
        task.updated_at = time.time()
        if status == TaskStatus.FAILED:
            task.attempts += 1

    def get_next_task(self) -> Optional[Task]:
        candidates = [t for t in self.tasks.values() if t.status in (TaskStatus.ACCEPTED, TaskStatus.ACTIVE)]
        candidates.sort(key=lambda t: t.priority)
        return candidates[0] if candidates else None

    def get_task_tree(self) -> dict:
        def build_tree(task_id):
            task = self.tasks.get(task_id)
            if not task:
                return None
            return {"task": task, "children": [build_tree(cid) for cid in task.children if cid in self.tasks]}
        return {tid: build_tree(tid) for tid in self.root_tasks if tid in self.tasks}

    def fail_task(self, task_id: str, reason: str):
        self.update_task(task_id, status=TaskStatus.FAILED, observations=[f"FAILURE: {reason}"])

    def complete_task(self, task_id: str, result: dict = None):
        self.update_task(task_id, status=TaskStatus.COMPLETED, result=result or {})
