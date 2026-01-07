# Prior Work Analysis Report

## Target Paper
**Title:** LzLeAscHnj
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The key contribution of HRA is to bridge low-rank and orthogonal adaptation by parameterizing trainable orthogonal transformations with chains of Householder reflections and proving their equivalence to adaptive low-rank updates. LoRA defined the modern low-rank update space for PEFT, turning weight deltas into constrained, efficient subspaces; HRA’s equivalence result directly builds on this formulation by showing that multiplying frozen weights by a product of reflections realizes a low-rank delta. The feasibility and efficiency of using reflections come from prior work on Householder parametrizations: Mhammedi et al. established that orthogonal matrices can be learned as products of Householder reflectors, and Tomczak & Welling showed that stacking such rank‑1 reflections yields expressive yet cheap transformations. Together, these works provide the mathematical and algorithmic scaffolding for HRA’s reflector-based adapters. The second pillar of HRA—regularizing the orthogonality of reflection planes to control capacity and stability—draws from the broader literature demonstrating the benefits of orthogonality in deep learning. Bansal et al. and Huang et al. showed that orthogonality constraints stabilize optimization and improve generalization, motivating HRA’s explicit regularization of reflector directions. Finally, the adapter paradigm of Houlsby et al. situates HRA within PEFT: HRA preserves frozen backbones and tunes a compact, structured parameterization, but offers a principled unification of orthogonal and low-rank routes. Collectively, these prior works shape HRA’s core insight and design: an orthogonal, Householder-based adapter that is theoretically and practically aligned with low-rank adaptation.

---
*Generated: 2026-01-06T23:33:35.565406*
