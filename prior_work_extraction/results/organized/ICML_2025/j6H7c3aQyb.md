# Prior Work Analysis Report

## Target Paper
**Title:** j6H7c3aQyb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Temporal Difference Flows (TD-Flow) sits at the intersection of generative modeling, RL theory, and world-model learning. Geometric Horizon Models (GHMs) introduced the central idea of predicting future states directly under a geometric horizon, but inherited the instability of bootstrapped TD-style training. TD-VAE had earlier demonstrated the appeal of temporal-difference bootstrapping for generative latent models and simultaneously exposed its variance and bias trade-offs, foreshadowing the need for a lower-variance alternative.
Distributional RL reframed Bellman updates as operators over distributions, and DualDICE extended Bellman-style constraints to discounted state distributions (occupancies). TD-Flow synthesizes these ideas by posing a novel Bellman equation on probability paths, providing a principled fixed-point structure for the evolution of future-state distributions under discounting.
On the generative side, flow-matching offered a direct way to learn probability paths by supervising the vector field (path velocities) rather than relying on noisy bootstrapped targets, while score-based generative modeling formalized probability flow ODE/SDE views that make such pathwise training natural. This substitution of bootstrapping with flow-matching is the crux behind TD-Flow’s reduced gradient variance and improved long-horizon fidelity.
Finally, modern world-model approaches like Dreamer highlight how iterative unrolling compounds small errors, motivating GHMs and, in turn, TD-Flow’s path-based approach. Collectively, these works directly shaped TD-Flow’s core contribution: a Bellman-consistent, flow-matched training paradigm for GHMs that scales to substantially longer horizons with theoretical convergence guarantees.

---
*Generated: 2026-01-07T00:21:33.183832*
