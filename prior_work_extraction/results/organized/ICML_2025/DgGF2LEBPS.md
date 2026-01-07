# Prior Work Analysis Report

## Target Paper
**Title:** DgGF2LEBPS
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EmbodiedBench’s core contribution—a comprehensive, capability-driven benchmark for vision-based MLLM embodied agents—builds on three converging lines of prior work. First, embodied instruction-following benchmarks such as ALFRED and VLN (R2R) established how to rigorously evaluate agents that ground natural language in visual perception and spatial action. Their task schemas and metrics (e.g., success rates, subgoal completion, SPL) directly inform EmbodiedBench’s high-level semantic tasks and its spatial-awareness and complex instruction-understanding subsets.
Second, simulation platforms and task taxonomies typified by Habitat standardized navigation/manipulation settings and measurement practices. This provides the methodological backbone for EmbodiedBench’s multi-environment coverage and its inclusion of low-level, atomic action tasks for navigation and manipulation.
Third, the emergence of language- and multimodal-model-driven agents has revealed new evaluation needs. TEACh highlighted multi-turn, compositional instruction challenges; CALVIN crystallized language-conditioned, long-horizon manipulation with fine-grained action sequences; SayCan demonstrated that LLM planners require grounding via affordances to exhibit commonsense and long-term planning; and MineDojo broadened the scope to open-ended, vision-language tasks for foundation-model agents. These works collectively motivate EmbodiedBench’s six capability-focused subsets—commonsense reasoning, complex instruction understanding, spatial awareness, visual perception, and long-term planning—explicitly targeted at MLLMs. By unifying these strands, EmbodiedBench advances from single-domain or single-capability tests to a unified, diverse, and scalable evaluation suite purpose-built for modern MLLM embodied agents.

---
*Generated: 2026-01-07T00:21:32.373504*
