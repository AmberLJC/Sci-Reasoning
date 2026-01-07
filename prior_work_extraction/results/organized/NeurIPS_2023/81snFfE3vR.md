# Prior Work Analysis Report

## Target Paper
**Title:** 81snFfE3vR
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper positions one-step differentiation at the intersection of three established lines: unrolling-based AD, implicit differentiation of solution mappings, and truncated/Neumann approximations for hypergradients. Domke (2012) first articulated hypergradients via fixed-point/implicit differentiation and proposed truncated, Jacobian-free estimators—conceptually the progenitors of a one-step surrogate. Pedregosa (2016) and OptNet (Amos & Kolter, 2017) then consolidated the implicit-function approach for differentiating through optimization, defining the exact target Jacobian that one-step aims to approximate. In parallel, Maclaurin et al. (2015) exposed the prohibitive memory and compute of reverse-mode through long optimization trajectories, motivating alternatives that avoid full unrolling.

Subsequent work in bilevel learning (Franceschi et al., 2018) established the dominant application context, while Lorraine et al. (2020) demonstrated scalable implicit gradients using Neumann-series and linear solves, making explicit the trade-off between solver iterations and gradient accuracy. Deep Equilibrium Models (Bai et al., 2019) further popularized Jacobian-free backpropagation for fixed-point systems using only JVP/VJP oracles.

Building on these threads, the paper crystallizes “one-step differentiation” as an extreme truncation—essentially the first Neumann term or a single adjoint iterate—and delivers new approximation guarantees showing it is asymptotically as accurate as full implicit differentiation for fast (e.g., superlinear) algorithms like Newton’s method. The resulting estimator matches the usability of AD while achieving the efficiency of implicit differentiation in regimes that matter for bilevel optimization, thus unifying prior ideas under a precise theory and practical recipe.

---
*Generated: 2026-01-07T00:02:04.852450*
