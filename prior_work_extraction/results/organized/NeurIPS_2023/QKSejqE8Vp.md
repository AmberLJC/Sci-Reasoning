# Prior Work Analysis Report

## Target Paper
**Title:** QKSejqE8Vp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

ResidualPlanner sits firmly in the lineage of the matrix mechanism, which recasts answering linear queries under differential privacy as choosing a strategy matrix and reconstructing workload answers. The matrix mechanism (Li, Hay, Miklau) provides the core linear-algebraic identity for error—covariances derived from the inverse information matrix—that ResidualPlanner exploits. Hay et al.’s consistency work complements this by formalizing least-squares reconstruction, yielding unbiased estimates with explicit covariance formulas; ResidualPlanner leverages this structure to compute both variances and covariances for many marginals efficiently. Hardt and Talwar’s geometric view of DP connects query error to convex, norm-based objectives, supporting ResidualPlanner’s convex optimization framing for Gaussian matrix mechanisms.

Within the specific domain of marginals, HDMM established an influential planner that combined structured strategies and heuristic search to lower error in high dimensions, but at significant memory cost and with a fixed objective (largely total MSE). ResidualPlanner advances this line by retaining workload awareness while scaling to hundreds of attributes and extending optimization beyond a single criterion to any convex function of marginal variances. This generality is conceptually aligned with optimal experimental design (Kiefer), where A-, E-, and related criteria are convex in variances; ResidualPlanner effectively instantiates these design principles in the DP matrix-mechanism setting. Finally, precise calibration of Gaussian noise (Balle and Wang) ensures accurate privacy loss accounting, enabling ResidualPlanner’s optimality claims under (epsilon, delta)-DP across diverse convex loss objectives.

---
*Generated: 2026-01-06T23:42:49.091111*
