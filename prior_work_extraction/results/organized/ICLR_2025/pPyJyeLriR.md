# Prior Work Analysis Report

## Target Paper
**Title:** pPyJyeLriR
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ScaleGUN’s core innovation is to make certified graph unlearning practical at billion-edge scale by replacing exact, per-request propagation with accelerated propagation whose approximation error is provably bounded at the embedding level—tight enough to preserve certificates. Two strands of prior work directly shaped this solution. On the unlearning side, Machine Unlearning (SISA) crystallized the certification paradigm—i.e., guarantees that a model with deletions is indistinguishable from a retrained counterpart—thereby setting the bar that graph unlearning must meet. On the graph learning side, a sequence of propagation-acceleration methods—APPNP’s decoupled PPR diffusion, SIGN’s precomputed multi-hop features, and PPRGo’s sparse approximate PPR—demonstrated that propagation can be modularized and scaled, but they introduce approximation error that naïvely breaks certification. ScaleGUN addresses this gap by importing error-controlled approximation techniques from spectral filtering and PageRank theory: Chebyshev polynomial filters (Defferrard et al.) provide operator-norm control over graph filter approximation, while push-based PPR (Andersen–Chung–Lang) offers explicit l1 error bounds for localized diffusion. By bridging these bounds to deviations in node embeddings and, ultimately, model outputs, ScaleGUN converts acceleration-induced errors into certification-compatible budgets. The result is a scalable, certifiable unlearning pipeline: propagation is accelerated with quantified error, and certificates remain valid without full recomputation for each unlearning request.

---
*Generated: 2026-01-06T23:42:48.093923*
