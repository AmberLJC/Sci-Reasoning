# Prior Work Analysis Report

## Target Paper
**Title:** Ifq8GMdqJK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The core contribution of the NeurIPS 2023 paper is to characterize how conditional independence (CI) tests that rely on supervised learning behave when their nuisance regressions are misspecified. This builds directly on regression-driven CI methodologies such as the Conditional Randomization Test (CRT) and the Generalised Covariance Measure (GCM), which established powerful, flexible CI tests but typically guaranteed Type-I control under correct specification or sufficiently accurate regression fits. The authors’ contribution is to move beyond these idealized assumptions and deliver explicit approximations and upper bounds for testing error that scale with concrete misspecification measures of the learned predictors.
Kernel-based residualization methods—including the kernel CI test (KCI) and its scalable approximations RCIT/RCoT—instantiate the same paradigm: learn E[Y|Z], E[X|Z], then test residual dependence (often via HSIC). These methods hinge critically on the inductive bias of the learner (kernel choice, regularization, feature mappings). By quantifying how imperfect nuisance fits translate to inflated Type-I error and reduced power, the paper provides robustness guarantees precisely where practitioners most need guidance.
Methodologically, the paper echoes the orthogonal/robust-inference perspective from Double/Debiased Machine Learning: it frames test error in terms of L2-type regression errors and cross-fitting-type decompositions, yielding transparent sensitivity bounds. In sum, it unifies and extends regression-based CI testing theory by replacing correctness assumptions with principled misspecification-dependent guarantees across prominent tests such as GCM, CRT-like procedures, and kernel-residual methods.

---
*Generated: 2026-01-06T23:42:49.134124*
