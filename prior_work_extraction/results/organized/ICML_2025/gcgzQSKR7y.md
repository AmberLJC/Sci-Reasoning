# Prior Work Analysis Report

## Target Paper
**Title:** gcgzQSKR7y
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper advances adaptive experimental design by tightening Neyman regret guarantees from prior Õ(√T) to anytime Õ(log T) and by introducing contextual multigroup guarantees. Its most immediate foundation is Dai et al. (2023), which proposed ClipOGD and established the first sublinear Neyman regret for unbiased ATE estimation; the present work explicitly modifies that algorithm/analysis to achieve stronger, anytime logarithmic guarantees. These guarantees hinge on viewing the ATE variance as an online objective whose curvature can be exploited: Hazan–Agarwal–Kale (2007) showed that strongly convex online losses admit O(log T) regret, providing the key analytic paradigm applied here under natural boundedness assumptions to the variance-based design objective.
Design-based causal inference and efficiency considerations supply the problem’s statistical backbone. Neyman (1923) formalized unbiased design-based ATE estimation and variance calculations, while Neyman (1934) characterized variance-minimizing allocations (Neyman allocation), which define the hindsight-optimal nonadaptive benchmark underlying Neyman regret. To ensure unbiasedness under adaptive, unequal assignment probabilities, the paper relies on the Horvitz–Thompson (1952) estimator. For contextual extensions, classic principles on blocking/stratification and efficiency, as synthesized by Athey–Imbens (2017), clarify what the groupwise nonadaptive optima are.
Finally, the paper’s multigroup Neyman regret draws on ideas from subgroup-fairness learning (Kearns–Neel–Roth–Wu, 2018), ensuring performance guarantees that hold simultaneously across many possibly overlapping groups. Together, these works directly shape both the algorithmic design and the proof techniques enabling the paper’s stronger, anytime and multigroup Neyman regret results.

---
*Generated: 2026-01-07T00:21:32.372932*
