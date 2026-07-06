# M6: Vision and Multimodal Enhancement
## Goal
Research and integrate visual input, screenshot understanding, or VLA approaches.
## Key Tasks
1. Survey VLA approaches (STEVE-1, JARVIS-VLA, GROOT, OmniJARVIS)
2. Implement screenshot capture and basic visual grounding
3. A/B comparison: API-only vs vision-augmented on same tasks
4. Decision report on whether to continue investing in VLA
## Acceptance Criteria
- At least one vision-augmented task completed
- Decision report: VLA vs structured API tradeoff
- Performance comparison data
## Key Research
- STEVE-1: Text-conditioned behavior via latent action pretraining (most practical)
- JARVIS-1: Multimodal memory with visual backbone (expensive but powerful)
- OmniJARVIS: VLA world model (state-of-art but complex)
## Recommendation
Start with screenshot-based visual grounding for error detection, not full VLA. Structured API is faster and more reliable for most tasks. Visual input adds value for ambiguous situations.
