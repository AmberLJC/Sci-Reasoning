# Prior Work Analysis Report

## Target Paper
**Title:** vIGNYQ4Alv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Jiang and Mokhtari’s core contribution—an accelerated quasi-Newton proximal extragradient method that matches NAG’s O(1/k^2) and surpasses it to O(√(d log k)/k^{2.5}) in high-iteration regimes—rests on combining acceleration via proximal extragradient with gradient-only curvature learning. Nesterov’s accelerated gradient (2004) supplies both the optimal first-order benchmark and the potential/estimate-sequence mindset the authors must match or exceed. The acceleration scaffold comes from the Monteiro–Svaiter hybrid proximal extragradient framework (2013), whose residual-based, inexact proximal conditions the paper leverages in a recent variant to retain acceleration while altering the metric. Catalyst (2015) contributes the broader inexact proximal-point wrapper viewpoint and complexity transfer, guiding how a quasi-Newton preconditioned inner step can be embedded without losing accelerated rates.
On the curvature side, the quasi-Newton lineage is essential: BFGS (Broyden–Fletcher–Goldfarb–Shanno, 1970) provides the gradient-only, positive-definite inverse-Hessian updates, and limited-memory BFGS (Nocedal, 1980) furnishes a scalable mechanism with spectral bounds that naturally introduce the dimension dependence appearing in the refined rate. Scheinberg and Tang (2016) demonstrate how quasi-Newton metrics define variable-metric proximal subproblems with only gradients and tolerable inexactness—an interface the present work adapts to an accelerated extragradient context. Finally, Nemirovski’s Mirror-Prox (2004) underpins the stability and error-robustness of the extragradient correction in variable metrics. Integrating these strands yields a gradient-only, variable-metric proximal extragradient whose analysis extends MS-style acceleration to quasi-Newton metrics, producing the first provable convex-case gain of a quasi-Newton-type method over NAG.

---
*Generated: 2026-01-07T00:02:04.823144*
