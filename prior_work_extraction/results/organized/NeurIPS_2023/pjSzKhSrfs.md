# Prior Work Analysis Report

## Target Paper
**Title:** pjSzKhSrfs
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Wasserstein Quantum Monte Carlo pivots from optimizing wavefunction parameters to directly optimizing the Born probability distribution, recasting QVMC within a geometric view of optimization on the space of measures. The classical QVMC optimization backbone is Sorella’s stochastic reconfiguration, which operationalizes natural-gradient descent for variational wavefunctions; this is grounded in Amari’s Fisher–Rao information geometry. Neural quantum states made this setting both powerful and challenging: Carleo and Troyer showed that neural parametrizations dramatically expand expressivity but exacerbate optimization stiffness, while subsequent state-of-the-art electronic-structure ansätze such as FermiNet emphasized symmetry and nodal-structure constraints that intensify the need for robust optimization beyond standard QVMC.

The paper’s key step is to interpret QVMC as a Fisher–Rao gradient flow over Born distributions and then replace this geometry with Wasserstein gradient flow, aiming for more favorable optimization dynamics. This substitution relies directly on the JKO theory of Wasserstein gradient flows and the AGS calculus on probability measures, which provide the variational and metric foundations to define, analyze, and discretize energy-descent dynamics in Wasserstein space. Finally, turning these geometric ideas into practical algorithms draws on particle-based functional gradient methods exemplified by SVGD, informing how to transport particle ensembles to follow the targeted gradient flow in distribution space. Together, these works supply the information-geometric starting point (SR/natural gradient), the neural-QMC motivation and constraints (NQS/FermiNet), and the optimal-transport geometry and particle-transport machinery (JKO/AGS/SVGD) that directly enable the Wasserstein QMC formulation and algorithm.

---
*Generated: 2026-01-06T23:42:49.052290*
