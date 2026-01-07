# Prior Work Analysis Report

## Target Paper
**Title:** 7G9YKty2UZ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CoAPT sits at the intersection of prompt-based VLM adaptation, adversarial robustness, and corruption–restoration. Its reliance on the aligned image–text latent space created by CLIP provides a high-level supervisory signal for restoring natural semantics after corruption. Building on the prompt-learning line of work—CoOp and its generalization-focused extension CoCoOp—CoAPT adopts prompt optimization as the primary adaptation mechanism, but augments it with adversarial and collaborative objectives so robustness is achieved without undermining the open-vocabulary generalization that makes VLMs useful.

On the robustness side, CoAPT draws on the adversarial training paradigm of Madry et al., translating weight-level adversarial optimization into the prompt space tailored for VLMs. To actively disrupt adversarial perturbations, it integrates a Total Variation (TV) preprocessing stage. This component is grounded in two prior strands: practical defenses via input transformations—especially TV minimization—from Guo et al., and the classical ROF model that justifies suppressing high-frequency noise while preserving edges. Finally, the overall corruption–reconstruction blueprint echoes masked image modeling (MAE): CoAPT intentionally degrades inputs to break adversarial artifacts, then leverages high-level latent guidance for semantic restoration. Together, these works motivate CoAPT’s core design: a TV-driven perturbation disruptor coupled with a latent-guided, collaboratively adversarial prompt tuning procedure that preserves the generalization of pre-trained VLMs while substantially improving adversarial robustness.

---
*Generated: 2026-01-06T23:42:48.115010*
