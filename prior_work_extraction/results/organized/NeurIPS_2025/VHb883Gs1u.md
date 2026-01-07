# Prior Work Analysis Report

## Target Paper
**Title:** VHb883Gs1u
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

RePS sits at the intersection of representation steering and preference optimization. Early controllable generation methods like PPLM and GeDi established that one can steer and suppress attributes by intervening at decoding or in intermediate activations, but their reliance on external classifiers, token-level guidance, and decoding-time gradients limited robustness and practicality. The activation-steering line, exemplified by Activation Addition, showed that linear concept directions in hidden states afford interpretable control, yet fixed or manually constructed vectors often underperform robust prompting.

RePS reframes representation control as a learning problem over preferences: inspired by DPO’s pairwise objective, it directly optimizes for generations that are preferred under a target concept while simultaneously suppressing the opposite, unifying steer-and-suppress in a single bidirectional loss. Building on ORPO’s reference-free advances, RePS removes dependence on a reference model, which reduces complexity and makes the method portable across base LMs. To keep the intervention compact and interpretable, RePS explores parameterizations in the spirit of LoRA and linear concept directions, learning small modules or vectors that adjust internal representations with minimal parameters. Finally, insights from INLP about linear subspaces for unwanted attributes inform RePS’s explicit suppression pathway, but RePS learns these subspaces from preferences rather than analytic projections.

Together, these strands yield a representation-steering method that narrows the performance gap with prompting while staying interpretable and lightweight, addressing long-standing efficacy limitations of activation- and weight-based steering.

---
*Generated: 2026-01-07T00:02:04.981098*
