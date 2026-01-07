# Prior Work Analysis Report

## Target Paper

**Title:** LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization

**Conference:** ICLR 2025 (oral)

**Authors:** Jui-Nan Yen, Si Si, Zhao Meng, Felix Yu, Sai Surya Duvvuri, Inderjit S Dhillon, Cho-Jui Hsieh, Sanjiv Kumar

**Keywords:** optimization, LoRA

**Abstract:** 
> Low-rank adaption (LoRA) is a widely used parameter-efficient finetuning method for LLM that reduces memory requirements. However, current LoRA optimizers lack transformation invariance, meaning the updates depending on how the two LoRA factors are scaled or rotated. This deficiency leads to inefficient learning and sub-optimal solutions in practice. This paper introduces LoRA-RITE, a novel adaptive matrix preconditioning method for LoRA optimization, which can achieve transformation invariance ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**LoRA: Low-Rank Adaptation of Large Language Models** (2021)
- *Authors:* Edward J. Hu et al.
- *Direct Connection:* Introduced the low-rank factorization parameterization (W + A B^T) for PEFT, defining the exact optimization setting and equivalence class (A→AS, B→B S^{-T}) that LoRA-RITE targets with an invariant preconditioner.

**Natural Gradient Works Efficiently in Learning** (1998)
- *Authors:* Shun-ichi Amari
- *Direct Connection:* Establishes parameterization-invariant optimization via the Fisher metric, which directly motivates LoRA-RITE’s design of an efficient, approximate natural-gradient-style preconditioner confined to the LoRA subspace.

### 💡 Inspiration

**Optimizing Neural Networks with Kronecker-factored Approximate Curvature** (2015)
- *Authors:* James Martens and Roger Grosse
- *Direct Connection:* Shows how Kronecker-structured preconditioning approximates natural-gradient invariances to linear reparameterizations, a principle LoRA-RITE adapts to the coupled A/B LoRA factors to achieve invariance under their joint transformations.

### 🔍 Gap Identification

**Adam: A Method for Stochastic Optimization** (2015)
- *Authors:* Diederik P. Kingma and Jimmy Ba
- *Direct Connection:* Serves as the dominant LoRA optimizer whose coordinate-wise updates depend on the arbitrary scaling/rotation of LoRA factors, a deficiency LoRA-RITE explicitly corrects with transformation-invariant preconditioning.

### 📊 Baseline

**Adafactor: Adaptive Learning Rates with Sublinear Memory** (2018)
- *Authors:* Noam Shazeer and Mitchell Stern
- *Direct Connection:* Provides the memory-efficient factored preconditioner widely used for LLM fine-tuning but remains non-invariant to basis changes in the low-rank subspace, motivating LoRA-RITE’s invariant matrix preconditioning tailored to LoRA factors.

### 🔗 Related Problem

**Low-Rank Matrix Completion by Riemannian Optimization** (2013)
- *Authors:* Bart Vandereycken
- *Direct Connection:* Formulates optimization on the quotient manifold of fixed-rank matrices to handle non-uniqueness under factor transformations (A→AS, B→B S^{-T}), the exact invariance that LoRA-RITE enforces via matrix preconditioning rather than manifold machinery.

---

## Synthesis: How Prior Work Led to This Paper

Low-rank adaptation (LoRA) introduced an explicit parameterization W + A B^T for PEFT in large models, making updates operate on two coupled factors whose product defines the actual parameter change, and implicitly defining an equivalence class under A→AS, B→B S^{-T}. Adam’s coordinate-wise moment adaptation became the default optimizer for LoRA but its updates depend on the scale and basis of A and B, producing different learning trajectories for equivalent factorizations; Adafactor brought memory-efficient factored second moments yet still lacks invariance to rotations in the low-rank subspace. Natural gradient theory established that optimization should be invariant to reparameterization when measured in the appropriate metric, a property later approximated efficiently in deep networks by K-FAC through Kronecker-structured preconditioning that preserves certain linear reparameterization invariances. In low-rank problems, Riemannian/quotient-manifold methods formalized the gauge symmetry of matrix factorizations and optimized directly over equivalence classes, guaranteeing invariance to transformations of the latent rank space.
Together these works revealed a gap: LoRA training uses factorized parameters with inherent gauge freedom, but common adaptive optimizers ignore this structure, while existing invariant methods (natural gradient, manifold optimization) are too costly for LLM-scale PEFT. LoRA-RITE naturally arises by blending natural-gradient invariance with efficient left-right matrix preconditioning: it designs a preconditioner over the coupled LoRA factors that is invariant to their scaling/rotation and computationally tractable, thereby rectifying Adam/Adafactor’s dependence on arbitrary factor parameterizations while preserving the efficiency demanded by LoRA fine-tuning.

---

*Analysis generated on: 2026-01-06T12:53:27.514065*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
