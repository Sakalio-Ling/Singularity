# P-015: Toolformer

**Title**: Toolformer: Language Models Can Teach Themselves to Use Tools
**Year**: 2023
**Link**: https://arxiv.org/abs/2302.04761
**Authors**: Timo Schick, et al.
**Priority**: P3

## Core Method
LLM learns to insert API calls into text autonomously. Trained on examples where tool use improved predictions.

## Key Contributions
- Self-taught tool use without explicit supervision
- Demonstrates LLMs can learn when and how to use external tools
- Minimal annotation needed

## Relevance to Singularity
- **Action space**: Mineflayer API calls are "tools" the LLM must learn to use appropriately
- **Skill library**: Skills can be viewed as tool patterns the agent has learned
- **Prompt engineering**: Toolformer-style few-shot examples in system prompt help LLM use Minecraft actions correctly
