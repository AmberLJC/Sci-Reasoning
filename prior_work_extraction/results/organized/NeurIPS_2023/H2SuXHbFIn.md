# Prior Work Analysis Report

## Target Paper
**Title:** H2SuXHbFIn
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

TreeDSB sits at the intersection of entropic multi-marginal optimal transport (mOT), Schrödinger bridges (SB), and score-based diffusion modeling. The theoretical foundation that entropic OT admits a dynamic SB formulation originates from the stochastic-control and large-deviation perspectives of Mikami–Thieullen and Léonard, which justify casting regularized transport as a controlled diffusion with marginal constraints. On the computational OT side, Cuturi and Doucet introduced efficient entropic barycenters via Sinkhorn, and Benamou–Carlier–Cuturi–Nenna–Peyré generalized this to multi-marginal problems through iterative Bregman projections (generalized Sinkhorn), with structure that naturally accommodates tree factorizations; the star-shaped case corresponds to Wasserstein barycenters. Diffusion Schrödinger Bridge (De Bortoli et al.) then brought these ideas to continuous-time dynamics with learned score functions, enabling high-dimensional applications by alternating forward/backward diffusions and marginal projections. Song et al.’s score-SDE framework provides the practical machinery to learn time-reversed drifts required by DSB-style algorithms.

TreeDSB’s key contribution is to merge these threads: it extends DSB from two marginals to a tree of marginals, designing a message-passing, alternating-projection procedure over edges that is the dynamic continuous-state analogue of generalized Sinkhorn on trees. This yields a principled and scalable method for multi-marginal entropic OT, with Wasserstein barycenters emerging as the star-tree special case. The result is a high-dimensional, diffusion-based algorithm that inherits both the theoretical guarantees of SB/entropic OT equivalence and the computational efficiency of Sinkhorn-style factorizations.

---
*Generated: 2026-01-06T23:42:49.102724*
