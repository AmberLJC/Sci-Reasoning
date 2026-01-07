# Prior Work Analysis Report

## Target Paper
**Title:** XUL75cvHL5
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core advance—establishing weak convergence of the joint process (x_k, θ_k) for constant-stepsize nonlinear stochastic approximation with Markovian data and precisely decomposing the asymptotic bias—builds on two intertwined traditions. From classical SA with Markovian noise, Kushner–Yin and Borkar–Meyn provide the weak-convergence/ODE and Poisson-equation frameworks for converting dependent noise into tractable martingale terms. Meyn–Tweedie anchors the required recurrence and ergodicity conditions and guarantees existence and properties of Poisson solutions, which the authors leverage to rigorously manage iterate–data correlations. Benveniste–Métivier–Priouret contributes smoothness-based expansions and martingale decompositions that the paper adapts to quantify higher-order bias in a nonlinear regime.

On the constant-stepsize front, linear SA and TD analyses under Markovian sampling (Bhandari–Russo–Singal; Srikant–Ying) revealed an O(α) steady-state bias but were confined to linear updates; the present work both recovers those linear effects and shows an additional cross-term created by the interaction of Markovian memory with nonlinearity. Complementing these, Mandt–Hoffman–Blei’s stationary OU approximation for i.i.d. SGD motivates a stationary-distribution viewpoint; the paper extends that intuition to Markovian data and develops a fine-grained control of the θ_k–x_k correlation. Together, these prior works directly enable the new joint-process weak convergence result and the first precise decomposition of constant-stepsize bias into memory, nonlinearity, and their interaction.

---
*Generated: 2026-01-06T23:33:36.264726*
