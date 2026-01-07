# Prior Work Analysis Report

## Target Paper
**Title:** Vhc0KrcqWu
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution of Feynman-Kac Correctors (FKC) is a principled, efficient way to sample from annealed, geometric-averaged, and product-of-experts targets derived from pretrained score-based models by correctly simulating the associated PDEs. This builds directly on the SDE/PDE formulation and predictor–corrector sampling of score-based generative modeling (Song et al., 2021), but replaces heuristic guidance with corrections derived from the Feynman–Kac (FK) formula. The need for principled guidance stems from the success and limitations of classifier and classifier-free guidance (Dhariwal & Nichol, 2021; Ho & Salimans, 2022), which mix scores but do not preserve the correct intermediate distributions, necessitating ad hoc correctors. FKC instead leverages the FK path-measure theory (Del Moral, 2004) to derive continuous-time weights that exactly account for potential terms induced by annealing, geometric averaging, or PoE compositions. The notion of geometric bridges and annealed paths is inherited from Annealed Importance Sampling (Neal, 2001), which FKC generalizes to diffusion trajectories via FK weights. Product-of-experts composition (Hinton, 2002) provides the statistical semantics for combining multiple pretrained models; FKC supplies the missing sampling mechanism that targets the resulting product distribution faithfully over time. Finally, to make these FK-weighted simulations practical, FKC employs Sequential Monte Carlo resampling (Del Moral, Doucet & Jasra, 2006) to control weight degeneracy, yielding a scalable algorithm that unifies guidance, annealing, and composition under a single PDE-consistent framework.

---
*Generated: 2026-01-07T00:21:32.386566*
