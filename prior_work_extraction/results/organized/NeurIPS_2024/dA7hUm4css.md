# Prior Work Analysis Report

## Target Paper
**Title:** dA7hUm4css
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core innovation—reducing constrained RLHF to an equivalent unconstrained objective via optimal dualization—sits at the intersection of CMDP theory, practical RLHF for LLMs, preference-based optimization, and dual methods from KL-regularized policy search. Altman’s CMDP framework supplies the underlying constrained optimization and Lagrangian duality that define safety-aligned objectives. Constrained Policy Optimization operationalized these ideas in practice but exposed the computational cost and instability of iterative primal–dual policy updates, precisely the pain point this paper addresses. InstructGPT established KL-regularized RLHF with PPO as the standard alignment pipeline for LLMs, while Constitutional AI sharpened the safety motivation and constraint types relevant for modern models.
On the optimization side, MPO demonstrated that KL-constrained policy updates admit smooth convex duals whose optima yield closed-form updates, a design pattern the present work repurposes for alignment. In the preference setting, Christiano et al. introduced pairwise feedback for learning reward signals, and DPO later showed that KL-regularized RLHF with preferences collapses to a supervised objective without explicit RL. The proposed MoCAN and PeCAN unify these strands: they extend DPO-style preference optimization and MPO-style dualization to the safety-constrained regime, pre-optimizing a smooth convex dual in closed form. This eliminates unstable primal–dual loops, yielding one-shot, computationally efficient, and more stable safety alignment for LLMs.

---
*Generated: 2026-01-06T23:39:42.957682*
