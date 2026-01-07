# Prior Work Analysis Report

## Target Paper
**Title:** Lt3jqxsbVO
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—sharp, non-asymptotic spectral rates for learning Koopman eigenvalues and eigenfunctions from data—rests on unifying three strands of prior work. First, EDMD (Williams–Kevrekidis–Rowley, 2015) provides the primary data-driven estimator of the Koopman operator, and its Galerkin/consistency foundations for stochastic systems were laid by Klus et al. (2018). These works define the estimands and algorithms whose finite-sample spectral behavior this paper rigorously characterizes. Second, the reduced-rank viewpoint, originating with Izenman (1975) and refined with finite-sample analyses by Bunea–She–Wegkamp (2011), motivates rank-constrained operator estimation (RRR) and clarifies its statistical bias–variance trade-offs. The present study leverages this framework to compare EDMD and RRR, proving that they exhibit comparable variance while elucidating when rank constraints help. Third, the transition from operator estimation to spectral accuracy exploits classical perturbation theory: Davis–Kahan (1970) turns operator-norm errors into eigenvalue/eigenfunction deviations, while concentration for dependent data (Paulin, 2015) supplies tight control of empirical covariance and cross-covariance operators under reversible dynamics, a setting that includes Langevin processes. By combining Galerkin consistency, reduced-rank regression theory, and Markov-chain concentration within a minimax analysis, the paper derives the first sharp operator-norm and spectral learning bounds for Koopman estimators and introduces a metric distortion functional to quantify eigenfunction estimation—directly extending and tightening the above foundational results.

---
*Generated: 2026-01-06T23:42:49.100277*
