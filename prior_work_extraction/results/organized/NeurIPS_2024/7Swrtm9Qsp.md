# Prior Work Analysis Report

## Target Paper
**Title:** 7Swrtm9Qsp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core innovation is a function-space characterization of the local minima that constant–step-size gradient descent can stably reach in univariate two-layer ReLU regression with noise, showing these minima necessarily implement smooth, low-variation functions and thus cannot overfit. This advances beyond the NTK/lazy-training view (Jacot et al.; Chizat & Bach), which linearizes dynamics and is known to be suboptimal in this setting. Instead, the authors analyze the feature-learning regime under finite learning rates, connecting optimization stability to a bound on a weighted first-order total variation of the learned function.

This total-variation perspective is rooted in the convex neural networks framework (Bach), where two-layer ReLU models admit a variation/path-norm controlling function complexity. In 1D, such networks correspond to adaptive piecewise-linear splines whose smoothness can be described by TV of derivatives—a connection long exploited by locally adaptive regression splines (Mammen & van de Geer) and trend filtering (Tibshirani) to achieve near-minimax n^{-4/5} error rates. The paper leverages precisely this structure to show that stable GD minima have TV bounded in terms of the step size (∝ 1/η), implying a near-optimal MSE rate ~n^{-4/5} under mild conditions.

Conceptually, the work extends the implicit bias program (Soudry et al.) from classification/max-margin to noisy regression: algorithmic details—here, constant step size and dynamical stability—impose an implicit TV regularizer on the realized function. In a regime where benign overfitting does not occur (Bartlett et al.), this implicit regularization precludes interpolation of noise and yields provable generalization.

---
*Generated: 2026-01-06T23:42:49.024828*
