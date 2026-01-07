# Prior Work Analysis Report

## Target Paper
**Title:** pXoiIDdynI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper advances a line of work that connects multigroup calibration to omniprediction by tightening online rates under swap-style constraints. Hebert-Johnson et al. (2018) introduced multicalibration and the audit–correct paradigm, giving a reduction from fairness-style guarantees to iterative learning against an auditor. Kim et al. (2019) operationalized this through black-box multiaccuracy auditing, establishing the correction mechanics that later works adapt when moving between L2 and L1 metrics. Gopalan et al. (2021) formalized omnipredictors and proved that sufficiently strong multicalibration implies simultaneous risk minimization for broad loss classes, creating the conduit the present paper uses to transfer improved calibration error into improved omniprediction error for convex Lipschitz losses.

On the online front, Gupta et al. (2022) cast multicalibration-like guarantees as regret bounds in sequential settings, providing the predictor–auditor game template. The “swap” strengthening draws directly on swap/internal-regret theory (Blum and Mansour, 2007), replacing external-style constraints with permutation-based constraints that better capture post-hoc recoding of predictions. Achieving rates beyond √T in such adversarial games leverages optimistic online learning (Rakhlin and Sridharan, 2013), which provides faster convergence under structure/predictability; the present work deploys analogous optimistic saddle-point updates to reach Õ(T^{1/3}) L2 swap-multicalibration. Finally, Garg et al. (2024) articulated the swap framework and posed the √T open problem against bounded linear functions; this paper resolves it in a strongly affirmative fashion by surpassing √T with Õ(T^{1/3}) and then propagating the gain to Õ(T^{2/3}) bounds for L1 swap multicalibration and swap omniprediction.

---
*Generated: 2026-01-06T23:42:48.155835*
