# Module: Task System
> Status: Design (M0)
## Purpose
Manage hierarchical tasks with states, dependencies, priorities, failure recovery.
## Task Schema
id, title, type, parent, status, priority, preconditions, success_criteria, failure_criteria, assigned_skill, created_at, updated_at, attempts, observations, blockers, result
## States
proposed -> accepted -> active -> waiting | blocked | failed | completed | cancelled
## Interface
create_task, update_task, get_next_task, fail_task, get_task_tree
