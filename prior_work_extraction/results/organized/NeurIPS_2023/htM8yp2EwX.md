# Prior Work Analysis Report

## Target Paper
**Title:** htM8yp2EwX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

AMDP’s core innovation—an optimal ranking coupled with a data-driven selection rule that controls FDR for high-dimensional mediation under a composite null—stands at the intersection of three lines of prior work. First, the selection step is grounded in the BH paradigm for FDR control, with Storey’s adaptive approach motivating the estimation of null proportions; AMDP generalizes this adaptivity by modeling the distinct components of the mediation composite null (a = 0, b = 0, or both). Second, the ranking step draws from optimality principles developed for large-scale testing: Storey–Taylor–Siegmund’s Optimal Discovery Procedure and the Sun–Cai local-fdr framework show that likelihood-based or lfdr-based orderings maximize true discoveries under FDR constraints. AMDP translates these ideas to the mediation setting by constructing an optimal ordering that leverages the composite-null mixture and test-statistic distributions across mediators, thereby using joint information across hypotheses rather than treating them independently. Third, mediation-specific testing tradition (Baron–Kenny) and modern combination strategies (e.g., Cauchy combination) highlight the challenges of p-value calibration under composite nulls; AMDP replaces ad hoc combination with principled estimation of null-type proportions and distributional components to both rank and threshold. Finally, the adaptivity of AdaPT informs AMDP’s data-driven thresholding, ensuring asymptotic FDR control while maximizing power. Together, these works directly shape AMDP’s design: optimal (lfdr/likelihood) ranking adapted to composite nulls, and adaptive, estimation-driven thresholds for scalable, powerful FDR control in high-dimensional mediation.

---
*Generated: 2026-01-06T23:42:49.055071*
