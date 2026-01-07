# Prior Work Analysis Report

## Target Paper
**Title:** pH3daDPj4c
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—unifying TD, PFQI, and FQI in linear off-policy evaluation as iterative solvers of the same linear system via distinct matrix splittings and preconditioners—rests on two pillars: the projected Bellman equation (PBE) formulation and classical iterative linear algebra. Tsitsiklis and Van Roy (1997), together with the broader approximate DP view in Bertsekas and Tsitsiklis (1996), establish that linear TD targets the PBE Aw = b, supplying the exact algebraic substrate for unification. Saad’s (2003) matrix-splitting and preconditioning framework then offers the language and tools—A = M − N decompositions, stationary iterations, spectral radius criteria—to recast RL updates as specific splittings and preconditioned iterations.

On the algorithmic side, Ernst et al. (2005) introduce Fitted Q-Iteration, and Antos, Szepesvári, and Munos (2008) provide convergence/error analyses for FQI that highlight behavioral differences from TD. These works define and problematize the very methods the paper unifies, motivating a principled explanation for why TD convergence need not imply FQI convergence. Sutton, Maei, and Szepesvári (2009) connect TD to preconditioned optimization of MSPBE, foreshadowing the paper’s broader preconditioning lens that encompasses FQI and PFQI. Finally, Mnih et al. (2015) popularize target networks; the new paper interprets “more updates under a fixed target” as transitioning from constant to data-feature–adaptive preconditioning, clarifying practical stabilizations used in deep RL. Together, these works enable the paper’s unifying matrix-splitting view, its spectral convergence comparisons, and its reinterpretation of target networks as preconditioner design.

---
*Generated: 2026-01-07T00:02:04.950030*
