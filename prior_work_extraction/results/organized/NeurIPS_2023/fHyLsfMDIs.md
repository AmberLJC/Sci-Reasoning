# Prior Work Analysis Report

## Target Paper
**Title:** fHyLsfMDIs
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Entropic Neural Optimal Transport (ENOT) sits at the junction of entropic OT, dynamic formulations, and diffusion-based generative modeling. Cuturi’s introduction of entropic regularization established the EOT objective and the Sinkhorn algorithm, which dominates practice but struggles with quadratic cost structures and small regularization. Mikami and Thieullen’s equivalence between EOT and the Schrödinger Bridge (SB) reframed entropic OT as a stochastic control problem, opening a dynamic route to computing EOT plans. Chen, Georgiou, and Pavon’s KL-control viewpoint and dual potentials further clarified the variational and saddle-point structure of SB, directly motivating ENOT’s min–max reformulation and single-step end-to-end training.
Benamou and Brenier’s dynamic OT provided the archetypal primal–dual Lagrangian and continuity-equation framework that ENOT adapts to the entropic/SB setting. On the modeling side, score-based diffusion SDEs (Song et al.) contributed practical parameterizations and training tools for stochastic dynamics, enabling learned diffusion processes that realize transport. De Bortoli et al.’s Diffusion Schrödinger Bridge demonstrated how diffusion and score learning can solve SB, but relied on iterative IPF-like alternations; ENOT builds upon this but replaces iteration with a saddle-point learning strategy, yielding fast inference and improved behavior at small entropy. Finally, stochastic semi-dual methods for sample-based EOT (Genevay et al.) form the main static baseline that ENOT surpasses by leveraging the SB dynamic formulation. Together, these works directly shape ENOT’s core innovation: a diffusion-based, saddle-point neural algorithm for EOT that is end-to-end, scalable, and effective at low regularization.

---
*Generated: 2026-01-07T00:02:04.839145*
