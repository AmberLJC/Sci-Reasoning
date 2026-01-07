# Prior Work Analysis Report

## Target Paper
**Title:** fGfl6dqQVf
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—proving that averaged projected SGD estimates the semi-discrete OT map at the minimax O(1/√n) rate and identifying a projection set that contains an optimizer even with non-compact source support—rests on two pillars: the semi-discrete OT geometry and modern stochastic approximation theory. Mérigot (2011) supplied the essential semi-discrete dual formulation, expressing the objective in terms of Kantorovich potentials and Laguerre (power) diagrams; this precise structure makes unbiased stochastic gradients from samples readily available. Building on that foundation, Kitagawa–Mérigot–Thibert (2019) analyzed differentiability, convexity, and stability of the semi-discrete dual and its cells, providing the regularity needed to assert existence/uniqueness of minimizers and to motivate boundedness properties that justify projection even when the source measure is not compact.
On the algorithmic side, Genevay–Peyré–Cuturi (2016) demonstrated that stochastic gradients on OT duals are effective at scale (albeit in the entropically regularized setting), directly inspiring the unregularized semi-discrete SGD considered here. The convergence and statistical guarantees of the present work lean on Polyak–Juditsky (1992) for averaging to attain optimal variance and Nemirovski–Juditsky–Lan–Shapiro (2009) for projected stochastic approximation with finite-sample O(1/√n) rates under convexity and Lipschitz conditions. Finally, recent statistical studies of OT map estimation, exemplified by Manole–Niles-Weed–Rigollet (2021), shaped the risk formulation and lower-bound methodology; by exploiting the finite-dimensional semi-discrete parameterization of the potentials, the current paper translates those ideas to establish a sharp, parametric minimax rate for map recovery via SGD.

---
*Generated: 2026-01-07T00:21:32.257101*
