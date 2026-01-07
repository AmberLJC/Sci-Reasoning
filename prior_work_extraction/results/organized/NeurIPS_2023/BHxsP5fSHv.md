# Prior Work Analysis Report

## Target Paper
**Title:** BHxsP5fSHv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

OKRidge targets the longstanding challenge of certifiably optimal sparse regression central to scientific discovery of dynamical systems. The SINDy framework demonstrated the promise of sparse models for identifying governing equations but relied on heuristic thresholding, leaving a gap for exact solvers that scale. Mixed-integer approaches for best-subset selection showed that exact solutions are possible and set strong baselines, yet their reliance on commercial MIP solvers leads to high runtimes for large problems. A parallel thread on convex and dual relaxations—Boolean relaxations and perspective-based formulations—established that tight lower bounds for cardinality-constrained regression can be derived through saddle-point/Lagrangian views or conic strengthening, especially effective with ridge terms. The k-support norm clarified the convex envelope of k-sparse ridge structure, informing the geometry of relaxations and the sorted-structure computations that make such relaxations practical.
Building on these ideas, OKRidge introduces a specialized saddle-point lower bound for k-sparse ridge regression that is efficiently computable via linear systems, avoiding heavy conic or MIP machinery while still certifying optimality. For fast iterations, OKRidge employs an ADMM splitting whose proximal operators decompose into a linear solve and a projection solvable by isotonic regression—an idea popularized in SLOPE’s proximal design for sorted penalties. This synthesis of exactness-focused relaxations with lightweight linear-algebraic and isotonic subroutines yields a solver that attains provable optimality at orders-of-magnitude lower runtimes, directly addressing the scalability and certification needs raised by prior work.

---
*Generated: 2026-01-07T00:02:04.797339*
