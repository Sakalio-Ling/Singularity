# RISKS.md — Risk Register

> Last updated: 2026-07-07
> Categories: Technical, Safety, Cost, Licensing, Compatibility, Operational

---

## RISK-001: Mineflayer Version Compatibility

**Category**: Technical / Compatibility
**Severity**: High
**Likelihood**: Medium
**Description**: Mineflayer may not fully support all 1.20.4 game mechanics. Some plugins (e.g., prismarine-world, mineflayer-pathfinder) may have bugs or incomplete features on this version.
**Impact**: Bot actions may fail silently or produce incorrect state.
**Mitigation**: Pin exact versions of Mineflayer + plugins. Test core actions (dig, place, craft, pathfind) on target version before building higher-level modules.
**Contingency**: Downgrade to 1.20.1 or switch to 1.19.4 if 1.20.4 proves unstable.

---

## RISK-002: LLM Hallucination in Game Actions

**Category**: Technical
**Severity**: High
**Likelihood**: High
**Description**: LLMs may generate plausible but incorrect plans, invent non-existent items, or produce invalid Minecraft actions.
**Impact**: Wasted actions, resource loss, agent death, corrupted task state.
**Mitigation**: Structured output schemas with validation. Pre-condition checks before action execution. Post-condition verification after execution. Reflection module on failure.
**Contingency**: Add a rule-based "guardian" that blocks obviously invalid actions (e.g., crafting with wrong materials).

---

## RISK-003: LLM API Cost Overruns

**Category**: Cost
**Severity**: Medium
**Likelihood**: High
**Description**: Long-horizon tasks require many LLM calls (planning, reflection, skill generation). GPT-4o / Claude costs can accumulate rapidly.
**Impact**: Research budget exhaustion, inability to run sufficient experiments.
**Mitigation**: Token budgeting per task. Use cheaper models (GPT-4o-mini, DeepSeek) for routine operations. Cache common queries. Evaluate local models (Llama, Qwen) for cost reduction.
**Contingency**: Switch to local models via Ollama for non-critical paths.

---

## RISK-004: Memory Pollution

**Category**: Technical
**Severity**: Medium
**Likelihood**: Medium
**Description**: LLM-generated or user-temporary information may contaminate long-term memory, leading to incorrect assumptions in future sessions.
**Impact**: Agent makes decisions based on false "facts", degrading performance over time.
**Mitigation**: Strict write policies: only verified, source-cited information enters L3+ memory. Regular memory audits. Separate "hypothesis" from "fact" storage.
**Contingency**: Memory reset capability. Rollback to known-good memory snapshot.

---

## RISK-005: Code-as-Skill Security Risks

**Category**: Safety
**Severity**: High
**Likelihood**: Medium
**Description**: Voyager-style code generation may produce code with side effects: file I/O, network access, infinite loops, or destructive game actions.
**Impact**: System compromise, server damage, data loss.
**Mitigation**: All generated code runs in sandboxed environment. No file/network access without explicit permission. Code review layer before execution. Action controller enforces game-level safety (no self-destructive actions).
**Contingency**: Revert to NL-only skills (no code generation) if sandboxing proves insufficient.

---

## RISK-006: Local Server Setup Complexity

**Category**: Operational
**Severity**: Low
**Likelihood**: Medium
**Description**: Setting up a local Paper/Spigot server with correct plugins, versions, and configurations may involve trial and error.
**Impact**: Delayed start on M1 implementation.
**Mitigation**: Use Docker or pre-built server images. Document exact setup steps in implementation notes.
**Contingency**: Use vanilla Minecraft server if Paper causes issues.

---

## RISK-007: Python-Node.js Bridge Latency

**Category**: Technical
**Severity**: Medium
**Likelihood**: Medium
**Description**: Communication between Python agent code and Node.js Mineflayer bot adds latency per action. Under time pressure (e.g., mob attacks), this could cause failures.
**Impact**: Slow reaction times, missed actions, combat failures.
**Mitigation**: Use persistent socket connection (not subprocess per action). Batch actions where possible. Profile latency early.
**Contingency**: Rewrite bot bridge in pure Python (using quarry library) or pure Node.js.

---

## RISK-008: Open-Source License Compatibility

**Category**: Licensing
**Severity**: Medium
**Likelihood**: Low
**Description**: Some target projects (MineDojo, Voyager) may have licenses that restrict commercial use or derivative works.
**Impact**: Cannot legally incorporate code or models from these projects.
**Mitigation**: Check licenses before reading code. Prefer MIT/Apache-2.0/BSD projects. Record license for every dependency.
**Contingency**: Reimplement inspired designs without copying code.

---

## RISK-009: Multi-Agent Coordination Complexity

**Category**: Technical
**Severity**: Medium (relevant at M7)
**Likelihood**: High
**Description**: Multi-agent coordination in open-world Minecraft is poorly explored. Existing work is limited.
**Impact**: M7 may require novel research contributions rather than simple engineering.
**Mitigation**: Start with simple shared-memory coordination. Study existing multi-agent frameworks. Build incrementally from single-agent.
**Contingency**: Limit to single-agent + human collaboration if full multi-agent proves too complex.

---

## RISK-010: Model Capability Ceiling

**Category**: Technical
**Severity**: Medium
**Likelihood**: Medium
**Description**: Current LLMs may not have sufficient spatial reasoning, planning depth, or game knowledge for higher-level tasks (M4+).
**Impact**: Agent plateaus at M2-M3 level without significant architectural innovation.
**Mitigation**: Design system to be model-upgradable. Test with frontier models. Augment with structured knowledge (crafting recipes, tech trees).
**Contingency**: Add more structured game knowledge injection (RAG over Minecraft Wiki, recipe databases).
