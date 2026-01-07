# Prior Work Analysis Report

## Target Paper
**Title:** 6ZBHIEtdP4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

PiSSA’s core idea—updating the principal singular components of pretrained weights while freezing the residual—emerges at the intersection of LoRA-style PEFT and spectral views of neural weights. LoRA established the practical recipe for low-rank adapters with frozen base weights but relies on random/zero initialization, often causing slow convergence. AdaLoRA sharpened the insight that not all directions are equal, using spectral cues to allocate rank capacity adaptively; PiSSA operationalizes this by directly selecting the principal singular subspace of W as the adaptation target. DoRA further encouraged reparameterizing what we tune in a frozen model, demonstrating gains from modifying strategically chosen components rather than arbitrary deltas—PiSSA echoes this by decomposing W into principal and residual parts and focusing updates where capacity matters most.

Earlier SVD-based compression (Denton et al., 2014) provided strong empirical evidence that neural layers are approximately low-rank and dominated by a few principal components, suggesting that these directions are particularly impactful. Spectral Normalization (Miyato et al., 2018) showed the feasibility and utility of explicitly working with leading singular values/vectors during training, reinforcing that spectral control can yield stable, effective optimization dynamics. The Eckart–Young–Mirsky theorem provides the formal backbone: the top singular vectors/values capture the best low-rank approximation of W, making them a principled choice for initializing the adaptation subspace. Together, these works motivate PiSSA’s SVD-initialized adapters and frozen residual, explaining its faster convergence and stronger performance compared to conventional LoRA while preserving PEFT efficiency.

---
*Generated: 2026-01-06T23:33:36.280427*
