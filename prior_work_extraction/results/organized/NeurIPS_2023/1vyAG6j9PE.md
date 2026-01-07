# Prior Work Analysis Report

## Target Paper
**Title:** 1vyAG6j9PE
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core innovation of “Unexpected Improvements to Expected Improvement for Bayesian Optimization” is to recast improvement-based acquisition functions in log-space (LogEI and its variants) so that they retain the same maximizers but avoid numerical underflow and vanishing gradients that hamper acquisition optimization in practice. This contribution sits squarely on the lineage of improvement-based Bayesian optimization. The original EI of Jones, Schonlau, and Welch (1998) defined the improvement objective that LogEI transforms while preserving argmax equivalence. As practical BO evolved to batch settings, Chevalier and Ginsbourger (2013) established multi-point EI (qEI), where the numerical difficulties compound with batch size—precisely the regime LogEI targets. In multi-objective BO, EHVI became the canonical improvement criterion; Couckuyt, Deschrijver, and Dhaene (2014) provided analytic computation that is widely used yet prone to underflow away from the Pareto frontier, motivating the LogEHVI reformulation. Modern scalable, differentiable MOBO—exemplified by Daulton, Balandat, and Bakshy’s qEHVI (2020)—relies on gradient-based optimization of Monte Carlo objectives; the LogEI paper directly augments these formulations with log-space, numerically stable evaluations. Constraints and noise exacerbate vanishing-acquisition issues: Gardner et al. (2014) introduced constrained EI (EIC), and Daulton et al. (2021) extended to noisy, constrained MOBO (qNEHVI), both of which benefit from LogEI’s stabilization. Finally, BoTorch (Balandat et al., 2020) provided the MC-differentiable infrastructure that makes the numerical pathologies salient in practice and serves as the platform where LogEI demonstrably improves acquisition optimization.

---
*Generated: 2026-01-06T23:42:49.090196*
