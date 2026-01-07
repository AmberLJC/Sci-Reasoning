# Prior Work Analysis Report

## Target Paper
**Title:** ca2QmdOlIh
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core advance—closed-form Bayesian reconstruction formulas for extensive-rank matrix factorization under rotationally invariant priors—sits at the intersection of rotationally invariant estimation, random matrix theory, and Bayesian optimal inference. The RIE paradigm of Ledoit–Wolf and Bun–Bouchaud–Potters established that when priors/noise are rotationally invariant, optimal estimators reduce to spectral shrinkage with oracle targets determined by population spectra. Gavish–Donoho’s optimal singular-value shrinkage further refined how to design nonlinear spectral mappings for additive-noise denoising, providing a template the authors adapt to a bilinear product contaminated by noise.
Spectral behavior insights from Benaych-Georges–Nadakuditi on signal–noise interactions in spiked models motivate how oracle estimators should behave and why rotation-invariant shrinkage can be optimal in high dimensions. On the Bayesian side, BiG-AMP formulated bilinear factorization under AWGN and priors, motivating the present focus on Bayes-optimal estimators; however, those earlier methods largely target low-rank or i.i.d. settings. Lelarge–Miolane’s replica-based characterizations of Bayes-optimal limits in symmetric low-rank estimation demonstrate how Bayes-optimality can be captured via spectral quantities, a viewpoint the present work extends to extensive-rank factors. Finally, deterministic equivalents from Hachem–Loubaton–Najim supply the random matrix toolkit to express the posterior means as explicit spectral integrals under rotational invariance. Together, these lines converge to justify and derive rotation-invariant Bayesian estimators for two-factor reconstruction and to support the paper’s optimality conjecture via oracle comparisons.

---
*Generated: 2026-01-06T23:42:49.094953*
