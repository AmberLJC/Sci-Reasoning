# Prior Work Analysis Report

## Target Paper
**Title:** o7Z8TClGjp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

Two largely separate lines of work crystallized proportional fairness in clustering: centroid-based models (k-median–like), where each point is assigned to a representative and pays its distance, and non-centroid models (k-center/diameter–like), where a point’s loss is its distance to the farthest point in its cluster. Chen et al. (ICML 2019) formalized proportional fairness for the centroid paradigm via core and FJR-style guarantees, while Caragiannis et al. (NeurIPS 2024) established analogous notions and algorithms for the non-centroid, diameter-based paradigm. The present paper’s key contribution is to unify these by introducing semi-centroid clustering, in which each point’s loss blends centroid and diameter components, and by delivering a polynomial-time constant-factor approximation to the core across this spectrum.
Conceptually, the centroid side inherits the assignment-to-representatives perspective from Monroe’s fully proportional representation, and its fairness relaxations build on JR/EJR principles from approval-based committee voting (Aziz et al. 2017), which motivate the FJR relaxation used in clustering. Technically, controlling a mixed loss calls for interpolation ideas reminiscent of ordered k-median (Chakrabarty–Swamy 2018), which bridges k-median and k-center. Classical k-center guarantees (Gonzalez 1985) support the diameter component of the analysis. By marrying the centroid and non-centroid traditions within one model and proof framework, the paper recovers prior guarantees at both extremes and extends proportional fairness—via core and FJR—to intermediate regimes and even heterogeneous metrics.

---
*Generated: 2026-01-07T00:02:04.952634*
