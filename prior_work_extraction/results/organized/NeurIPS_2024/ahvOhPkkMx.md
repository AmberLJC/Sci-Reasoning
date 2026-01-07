# Prior Work Analysis Report

## Target Paper
**Title:** ahvOhPkkMx
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Zipper’s core contribution—resolving the degeneracy of standardized predictiveness-difference tests in algorithm-agnostic settings—emerges at the intersection of cross-validated risk estimation and the theory of non-regular inference. Classical comparisons of predictive performance (Diebold–Mariano) motivate the loss-difference statistic, while the modern cross-fitting toolkit (Chernozhukov et al.) and cross-validated estimation frameworks (Zheng & van der Laan) provide the algorithm-agnostic and overfitting-robust machinery to estimate predictiveness with black-box learners. However, semiparametric work on variable importance (Williamson et al.) makes explicit that these risk-difference targets can be non-regular—leading to degenerate null distributions when the true difference is zero.

A traditional fix invokes higher-order influence functions (Robins et al.), which can restore valid asymptotics but at the cost of substantial technical and computational complexity. Zipper instead draws a design insight from resampling and repeated learning–testing (Burman) and recent overlapping-fold ideas with distributional guarantees (Jackknife+): by engineering dependence between two nominally separate test evaluations through a controlled overlap, the method induces a stable, nonzero variance component under the null. This ‘zippered’ overlap binds two cross-fitted predictiveness estimates, preventing the collapse of the standardized statistic and yielding a tractable, non-degenerate limit. In short, Zipper fuses the cross-fitting infrastructure with an overlapping-split construction inspired by repeated testing and jackknife-style designs, offering a simple, algorithm-agnostic solution to a degeneracy problem identified in modern variable-importance and goodness-of-fit inference.

---
*Generated: 2026-01-07T00:02:04.758571*
