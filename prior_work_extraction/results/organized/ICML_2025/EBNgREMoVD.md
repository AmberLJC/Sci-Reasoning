# Prior Work Analysis Report

## Target Paper
**Title:** EBNgREMoVD
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

HiRef’s central idea—recovering a bijective Monge map at large scale by orchestrating low-rank OT subproblems within a multiscale refinement scheme—sits at the intersection of three lines of prior work. First, Cuturi’s entropic OT made OT practical but retained quadratic memory/time; subsequent advances such as Altschuler et al. and Genevay et al. improved scalability yet still inherit the dense coupling or stochastic approximation limitations, which complicate exact bijection recovery. Second, Scetbon–Peyré–Cuturi’s low-rank Sinkhorn factorization established that OT couplings can be represented with linear complexity, but the factorized plan itself is not one-to-one. HiRef’s key conceptual leap is to interpret the low-rank factors as co-clusters that tend to group points with their Monge images, and to turn this observation into an iterative partition-refinement mechanism. Third, Schmitzer’s multiscale OT demonstrated that hierarchical, coarse-to-fine strategies can drastically cut computational cost. HiRef fuses this hierarchical paradigm with low-rank OT: it constructs data-driven multiscale partitions induced by factorized couplings and progressively refines them until the residual subproblems reduce to bijective assignments. The theoretical north star for this design is the Monge-map framework (Brenier), and, in the discrete limit, classical assignment (Kuhn), which together justify aiming for a permutation as the terminal object. In sum, HiRef synthesizes low-rank factorization, multiscale refinement, and Monge-map/assignment theory to achieve linear-scale computation that still yields an exact bijective correspondence.

---
*Generated: 2026-01-07T00:21:32.367222*
