# Prior Work Analysis Report

## Target Paper
**Title:** 9XieH21Tlf
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

Prompt-based continual learning (CL) emerged with L2P, which established a now-standard recipe: learn a pool of prompts, retrieve them per input via keys derived from frozen features, and make predictions with minimal backbone updates. DualPrompt refined this by splitting knowledge into general and expert prompts, implicitly hinting that different functional roles coexist in prompt-based CL. CODA-Prompt took this further by decomposing and composing prompts to isolate knowledge components across tasks. In parallel, Visual Prompt Tuning and Prefix-Tuning provided the core mechanism and conceptual framing: small learned prompts can steer large pretrained models without altering backbone weights.

This paper identifies a critical failure mode of those designs when the backbone is self-supervised (e.g., MAE-pretrained): task-specific knowledge must be injected via prompts (instruction), yet prompt retrieval at test time relies on uninstructed representations. This mismatch obscures sub-optimality. Building on the above lineage, the authors formalize a hierarchical decomposition of the CL objective into within-task prediction, task-identity inference, and task-adaptive prediction, clarifying which components current methods entangle and why that hurts under self-supervised pretraining. Their method operationalizes this separation, improving retrieval (task-ID inference) and adaptation without conflating them with within-task predictors. Thus, the contribution synthesizes prompt-tuning mechanisms (Prefix/VPT), prompt-based CL architectures (L2P, DualPrompt, CODA-Prompt), and the SSL pretraining regime (MAE) into a principled framework that resolves the instructed–uninstructed representation gap.

---
*Generated: 2026-01-07T00:02:04.849594*
