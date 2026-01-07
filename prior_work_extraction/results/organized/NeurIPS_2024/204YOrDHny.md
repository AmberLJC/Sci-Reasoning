# Prior Work Analysis Report

## Target Paper
**Title:** 204YOrDHny
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—explaining and achieving reparameterization invariance in approximate Bayesian inference for neural networks—rests on three intertwined lines of prior work. First, the Laplace approximation lineage (MacKay, 1992) and its deep-learning-era refinements (Ritter et al., 2018) furnished both the method and its known deficiencies: underfitting and sensitivity to parameterization. Empirical fixes via linearized or last-layer Laplace (Kristiadi et al., 2020) demonstrated markedly improved predictive behavior, motivating a theoretical account of why linearized predictives work.
Second, the linearization perspective from the Neural Tangent Kernel (Jacot et al., 2018) established that networks locally behave like linear models with Gaussian predictive structure, offering a natural bridge from weight-space posteriors to function-space predictives. This connects directly to the observation that linearized predictives partially sidestep parameterization artifacts.
Third, information geometry supplies the invariance principle and tools: Amari (1998) argues learning rules should be invariant under reparameterization via the Fisher–Rao geometry. Building on this, Riemannian Monte Carlo and Langevin methods (Girolami & Calderhead, 2011; Patterson & Teh, 2013) show how metric-induced dynamics yield coordinate-invariant sampling on parameter manifolds. The present paper synthesizes these strands: it provides a geometric explanation for the success of linearized Laplace through reparameterization invariance and then uses Riemannian diffusion to transport these invariance properties back to the original nonlinear network’s predictive distribution, thereby aligning Bayesian uncertainty over parameters with uncertainty over functions.

---
*Generated: 2026-01-06T23:33:35.530057*
