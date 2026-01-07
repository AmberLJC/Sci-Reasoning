# Prior Work Analysis Report

## Target Paper
**Title:** 3FJaFElIVN
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

GLIME’s core contribution—a general, stable, and truly local surrogate explanation—emerges from a precise diagnosis of where LIME fails and a unification of influential strands in local explainability. Ribeiro et al. (2016) introduced LIME’s weighted local linear surrogate idea but left open problems of instability and poor locality. Follow-on variants such as DLIME and ALIME pinpointed instability due to stochastic sampling and attempted fixes via deterministic or active neighborhood selection. GLIME builds on these observations but advances them by identifying the root mechanism: LIME’s kernel often yields very small sample weights, causing regularization to dominate and optimization to converge slowly, amplifying randomness. Concurrently, theoretical critiques by Laugel et al. demonstrated that LIME’s neighborhood can be non-local and biased toward the reference, undermining local fidelity. GLIME explicitly redesigns sampling and reweighting to enforce genuine locality and reduce bias.
Insights from KernelSHAP and MAPLE further shape GLIME’s framework. KernelSHAP frames explanations as weighted linear regression with a specific kernel, motivating GLIME’s analysis of weight magnitudes and kernel choice to avoid pathological tiny weights. MAPLE underscores the value of data-driven, locally faithful neighborhoods. GLIME synthesizes these lines by proposing a generalized, principled neighborhood and weighting scheme that stabilizes the surrogate fit, improves local fidelity, and unifies LIME-style and SHAP-style explanations as special cases within one coherent methodology.

---
*Generated: 2026-01-06T23:33:35.591692*
