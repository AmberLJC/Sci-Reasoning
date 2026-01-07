# Prior Work Analysis Report

## Target Paper
**Title:** ZQMlfNijY5
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

JKO-iFlow’s core insight is to recast normalizing-flow training as a discrete-time Wasserstein gradient flow and to implement each minimizing-movement (JKO) step with an invertible residual block trained greedily. This builds directly on Jordan–Kinderlehrer–Otto’s variational time-discretization of diffusion, which provides the proximal objective per step, and on the Ambrosio–Gigli–Savaré theory that justifies working in the Wasserstein space and supports adaptive time stepping. The Benamou–Brenier dynamic formulation of optimal transport connects these gradient-flow updates to velocity fields and energy along probability paths, aligning naturally with an ODE parameterization of transport.
Neural ODEs supply the continuous change-of-variables machinery to compute likelihoods along trajectories, making it feasible to implement a normalizing flow as a neural ODE while retaining exact log-density evaluation. Residual Flows demonstrate how to realize invertible residual blocks with tractable log-determinants; JKO-iFlow leverages this architecture but departs in training: instead of end-to-end optimization of a long flow, it performs block-wise training consistent with the JKO proximal updates. The PDE/ODE perspective of Haber and Ruthotto motivates viewing residual networks as time discretizations, guiding the use of step sizes and an adaptive time reparameterization to progressively refine the probability trajectory. Finally, compared to score-based SDE approaches, which require score matching and stochastic trajectory sampling, JKO-iFlow attains high-dimensional generative performance without SDE sampling by exploiting the deterministic, likelihood-trained, JKO-unfolded ODE flow.

---
*Generated: 2026-01-06T23:42:49.053711*
