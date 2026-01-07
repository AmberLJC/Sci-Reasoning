# Prior Work Analysis Report

## Target Paper
**Title:** qOgKMqv9T7
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

TIMING’s core contribution is twofold: it repositions Integrated Gradients (IG) as a strong time-series explainer when directional effects are properly evaluated, and it introduces a temporality-aware path for IG tailored to sequential data. Sundararajan et al. (2017) provide the mathematical backbone—signed, path-integral attributions—on which TIMING operates; the paper retains IG’s axiomatic strengths while modifying the interpolation path to encode temporal dynamics. DeepLIFT and Layer-wise Relevance Propagation contributed the emphasis on signed attributions and relevance conservation, highlighting that explanations must distinguish positive from negative effects—an idea TIMING elevates into its evaluation design.

The second thrust builds on a decade of scrutiny around evaluation. Adebayo et al. exposed how common tests can be misleading, prompting TIMING to propose CPD/CPP as behavior-grounded metrics that explicitly track cumulative prediction changes without canceling opposing contributions. Likewise, ROAR’s remove-and-retrain and RISE’s deletion/insertion paradigms shaped TIMING’s cumulative, perturbation-based assessment tailored to time-series structure. Finally, Expected Gradients underscored how reference distributions and paths materially affect attributions; TIMING translates this principle into a temporality-aware IG path that avoids the pitfalls of straight-line interpolation across time steps. Together, these works directly inform TIMING’s redesign of both the explainer (path choice for IG in sequences) and its validation (direction-aware, cumulative metrics), enabling a more faithful identification of significant positive and negative time points.

---
*Generated: 2026-01-07T00:05:12.561770*
