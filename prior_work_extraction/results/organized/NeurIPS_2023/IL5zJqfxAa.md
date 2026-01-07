# Prior Work Analysis Report

## Target Paper
**Title:** IL5zJqfxAa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EmbodiedGPT’s core innovation—vision-language pre-training for embodied planning via an embodied Chain-of-Thought—sits at the intersection of CoT reasoning, egocentric video corpora, parameter-efficient LLM tuning, and vision-language-action (VLA) robotics. Chain-of-Thought prompting (Wei et al., 2022) provides the central idea of explicit step decomposition, which EmbodiedGPT instantiates as sub-goal plans in EgoCOT. Constructing EgoCOT hinges on Ego4D (Grauman et al., 2022), whose large, diverse first-person videos allow grounding plans in realistic visual contexts. To scale training without full finetuning, EmbodiedGPT adopts prefix-tuning (Li & Liang, 2021), aligning a 7B LLM to the embodied planning distribution efficiently.

Prior robotics work showed how language models can structure actions. SayCan (Ahn et al., 2022) demonstrated LLM-based high-level planning constrained by affordances, directly informing EmbodiedGPT’s use of LLM-generated plans as actionable scaffolds. RT-2 (Brohan et al., 2023) established the effectiveness of VLA models in mapping web-scale semantics to robot control, paralleling EmbodiedGPT’s extraction of task-relevant features from plans to drive execution. On the multimodal alignment front, BLIP-2 (Li et al., 2023) showed that frozen LLMs can be effectively paired with visual encoders via lightweight adaptation, a blueprint echoed in EmbodiedGPT’s training recipe. Finally, ALFRED (Shridhar et al., 2020) crystallized the importance of subgoal decomposition for long-horizon household tasks, reinforcing EmbodiedGPT’s stepwise planning paradigm and evaluation focus. Together, these works directly shaped EmbodiedGPT’s dataset design, training strategy, and plan-to-action pipeline.

---
*Generated: 2026-01-07T00:02:04.865806*
