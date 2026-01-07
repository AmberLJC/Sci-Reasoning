# Prior Work Analysis Report

## Target Paper
**Title:** fqmSGK8C0B
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The key innovation of DCDC is to transform recent contractive-drift theory into a practical, sample-based calculator of convergence rates in Wasserstein distance. This rests directly on the Qu–Blanchet–Glynn (2023) framework that formulates convergence via a contractive drift certificate; DCDC introduces the Contractive Drift Equation (CDE) embodying that certificate and then solves it numerically. The theoretical lineage of this idea blends three streams: (i) Eberle’s reflection-coupling program, which shows that carefully designed distance-like functions can yield Wasserstein contraction; (ii) Harris-type results in Wasserstein metrics (Hairer–Mattingly–Scheutzow), which combine Lyapunov drift with local contractivity to obtain quantitative ergodicity; and (iii) curvature-based contraction (Ollivier) and drift-plus-contractivity analyses (Butkovsky), which formalize how an appropriate metric induces contraction of the Markov kernel. DCDC’s CDE can be viewed as a computable instantiation of these principles: learn a metric/weight function that enforces contractive drift and then translate it into explicit bounds. On the algorithmic side, path coupling provides the conceptual local-to-global contraction blueprint, while physics-informed neural networks supply a scalable methodology for solving operator equations from samples by minimizing residuals. Together, these works directly shape DCDC’s two components—its contractive-drift formulation and its neural solver—yielding the first general-purpose, sample-based tool to certify convergence of general-state-space Markov chains in Wasserstein distance.

---
*Generated: 2026-01-07T00:02:04.742166*
