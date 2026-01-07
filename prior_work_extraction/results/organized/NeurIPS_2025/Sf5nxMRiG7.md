# Prior Work Analysis Report

## Target Paper
**Title:** Sf5nxMRiG7
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—showing strongly polynomial equivalences between optimizing the average value f(S)/|S| for submodular/supermodular functions and classical submodular function minimization (SFM) via the minimum-norm-point (MNP) perspective—rests on two pillars: fractional-to-parametric reductions for ratio problems and the convex-analytic geometry of submodularity. On the ratio side, Dinkelbach’s fractional programming framework formalized the conversion of max/min of ratios to solving parametric families of difference objectives. Goldberg’s densest subgraph result embodied this idea for |E(S)|/|S| via parametric reductions, seeding the general viewpoint that optimizing f(S)/|S| can be addressed by solving instances of f(S) − λ|S|. On the submodular side, Lovász’s convexity and base polyhedron laid the geometric foundation, while Fujishige’s monograph crystallized the deep equivalence between SFM and finding the MNP over the base polyhedron and developed parametric minimization/principal partitions for f(S) − λ|S|. Wolfe’s MNP algorithm provided a concrete computational vehicle for the geometric viewpoint. Finally, the strongly polynomial algorithms of Schrijver and of Iwata–Fleischer–Fujishige established the algorithmic robustness of SFM, enabling the paper’s claim of strongly polynomial-time reductions and cross-over among USSS, UDSS, DSS, SFM, and MNP. Together, these works directly inform the paper’s unifying perspective: ratio optimization for sub/supermodular functions can be systematically and efficiently handled through the MNP/SFM machinery, even in the unrestricted (non-monotone, possibly negative) regime.

---
*Generated: 2026-01-07T00:05:12.515907*
