# Prior Work Analysis Report

## Target Paper
**Title:** 4DA5vaPHFb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Neural optimal transport methods rely on dual Kantorovich potentials whose conjugate (the c-transform) enforces the inequality constraints and binding conditions that characterize optimal plans. Existing solvers often approximate the c-transform via inner maximization or per-sample fine-tuning, making training unstable and computationally heavy. Genevay–Peyré–Cuturi (2016) highlighted these costs in stochastic semi-dual training, while ICNN-based approaches (Amos et al., 2017; Makkuva et al., 2020) showed how to parameterize convex potentials but still required non-convex min–max or explicit conjugate computations. Cuturi’s entropic regularization (2013) established that carefully chosen surrogates for hard constraints can make OT training both smooth and efficient.
Building on this lineage, the paper reframes the c-transform approximation as a learning problem with a principled surrogate: expectile regularization. The statistical foundation of expectiles (Newey & Powell, 1987) provides an asymmetric squared loss that targets upper tails, effectively yielding an upper-bound estimator over the distribution of feasible conjugate potentials. This mirrors the Fenchel-Young perspective (Blondel et al., 2019), where convex-analytic losses provide tight upper bounds and stable optimization landscapes. Recent success of expectiles in IQL (Kostrikov et al., 2021) further demonstrates their stabilizing effect when estimating upper-tail functionals. Together, these works shape a method that enforces dual binding conditions through an expectile-based loss, removing the need for inner c-transform fine-tuning while retaining accuracy and improving training stability.

---
*Generated: 2026-01-06T23:39:42.965002*
