# Prior Work Analysis Report

## Target Paper
**Title:** TQNlIQIrcK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core advance—achieving a ˜O(1/N) optimality gap for degenerate homogeneous RMABs—sits at the intersection of RMAB relaxations and diffusion-based stochastic control. Whittle’s formulation of restless bandits and Lagrangian decoupling supplies the structural backbone enabling tractable per-arm analysis. Building on this, LP-based relaxations and fluid policies from Bertsimas and Niño-Mora established a powerful baseline that performs excellently under non-degeneracy, yet can stall at Θ(1/√N) gaps when degeneracies arise. The large-population, asymptotic perspective of Weber and Weiss motivates the homogeneous, many-arm setting where approximation-driven policies can be provably near-optimal.

Methodologically, the paper’s decisive step is to move beyond the fluid (LLN) approximation to a Gaussian (CLT/diffusion) approximation. Kurtz’s limit theorems justify modeling occupancy fluctuations around the fluid trajectory as Gaussian, while Harrison’s Brownian control program suggests that optimizing a diffusion surrogate can yield implementable policies with sharper performance guarantees. To operationalize this, the authors formulate and solve a stochastic program defined on the Gaussian system; Prékopa’s stochastic programming foundations—particularly for Gaussian uncertainties—inform tractable reformulations and solution strategies. Finally, mean-field control insights from Gast and Gaujal clarify when fluid solutions are unique and how variance-aware corrections can systematically repair fluid-level degeneracies. Together, these strands directly enable the paper’s SP-based Gaussian policy and its improved ˜O(1/N) gap in regimes where LP/fluid methods are insufficient.

---
*Generated: 2026-01-07T00:27:38.140423*
