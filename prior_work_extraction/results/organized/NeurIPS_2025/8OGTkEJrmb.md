# Prior Work Analysis Report

## Target Paper
**Title:** 8OGTkEJrmb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution of D-Gating is a fully differentiable, multiplicative overparameterization that induces structured sparsity while remaining compatible with standard SGD. This idea is anchored in two lines of prior work. First, structured sparsity via group penalties—originating with the group lasso (Yuan & Lin, 2006) and operationalized in deep networks (Wen et al., 2016)—established the effectiveness of group-wise regularization but left a non-differentiability gap that often required specialized proximal solvers or post-hoc pruning. Network Slimming (Liu et al., 2017) advanced the notion of using simple scalar gates to prune channels with standard training, foreshadowing D-Gating’s gating design but without a formal equivalence to a target group penalty.
Second, a theoretical thread on positive homogeneity and factorization (Neyshabur et al., 2015; Haeffele & Vidal, 2015; Gunasekar et al., 2018) showed that L2 penalties on multiplicative factors implicitly induce nonconvex quasi-norms on the unfactorized parameters—specifically, a 2/D exponent in deep linear settings (Schatten 2/D). D-Gating explicitly harnesses this mechanism at the group level: splitting each group into a primary vector and D scalar gates with L2 penalties yields an induced L2,2/D group quasi-norm. This enables the authors to prove that local minima under D-Gating coincide with those of the corresponding non-smooth structured penalty and to analyze gradient-flow convergence toward the regularized objective. Compared to stochastic L0-style gating (Louizos et al., 2018), D-Gating is deterministic and fully differentiable, offering clean optimization and theory. Together, these works directly inform D-Gating’s design and its guarantees: group-sparsity goals from the structured sparsity literature, realized through the factorization-induced quasi-norm machinery from implicit-regularization theory.

---
*Generated: 2026-01-07T00:21:32.362225*
