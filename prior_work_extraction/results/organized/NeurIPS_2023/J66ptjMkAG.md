# Prior Work Analysis Report

## Target Paper
**Title:** J66ptjMkAG
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Kernel quadrature traces back to the Bayesian Monte Carlo framework of O’Hagan, which formalized integration in an RKHS and linked error to posterior uncertainty. Subsequent advances in kernel mean embeddings and maximum mean discrepancy (Gretton et al.) provided the dominant discrepancy measure and analysis toolkit for worst-case quadrature error. On the algorithmic side, greedy recombination strategies such as kernel herding (and its Frank–Wolfe interpretation by Bach, Lacoste-Julien, and Jaggi) offered deterministic node selection via iterative minimization of RKHS discrepancy, but at a computational cost that can be limiting in large-scale or complex-geometry settings.

A parallel line exploited repulsive designs: determinantal point processes and continuous volume sampling (Bardenet & Hardy; Dereziński, Liang & Mahoney) delivered near-optimal node sets with strong error guarantees, yet required solving challenging sampling problems in continuous spaces. Another influential strand—kernel thinning and recombination (Riabiz et al.)—compressed large candidate sets to high-quality quadrature rules but again incurred significant overhead.

The NeurIPS 2023 paper synthesizes these threads by importing pivoted Cholesky—classically used for fast low-rank kernel approximations (Harbrecht, Peters & Schneider)—into quadrature via a randomized pivoting rule (RPC). This sampling implicitly tracks leverage/Schur-complement mass, capturing the diversity and repulsion that make CVS/DPPs effective, while retaining the simplicity and speed of Cholesky-type updates. The result is a practical method that matches the error rates of CVS-, thinning-, and recombination-based quadrature, yet scales easily to arbitrary kernels and geometries, thereby closing the gap between theory-optimal node design and computational tractability.

---
*Generated: 2026-01-06T23:42:49.075540*
