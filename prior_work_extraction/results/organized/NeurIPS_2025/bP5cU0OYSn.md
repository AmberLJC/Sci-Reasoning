# Prior Work Analysis Report

## Target Paper
**Title:** bP5cU0OYSn
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution of Hom-PGD—achieving projection-free optimization over general compact convex sets without any optimization oracle—emerges at the intersection of conditional gradient methodology, oracle-reduction ideas, and convex-geometry-driven reparameterizations. Classical Frank–Wolfe (Frank & Wolfe) and its modern treatment (Jaggi) supply the projection-free paradigm and rate benchmarks but rely fundamentally on linear optimization oracles. Subsequent oracle-design advances (Garber & Hazan) showed that weaker, local oracles can suffice, motivating a more radical step: fully removing optimization oracles by changing the problem’s parameterization. On the rate side, Conditional Gradient Sliding (Lan & Zhou) established that projection-free methods can reach optimal first-order complexity, a target Hom-PGD retains while discarding LMOs. The mechanism enabling this departure is geometric: mirror-descent principles (Beck & Teboulle) and interior-point geometry (Nesterov & Nemirovski) advocate selecting a geometry or interior mapping that encodes feasibility and regularizes the domain. Hom-PGD concretizes this by constructing a homeomorphism from the original convex set to a unit ball, supported by convex-analytic foundations like Minkowski gauges (Rockafellar), so that each iteration becomes standard gradient descent on a ball-constrained problem. This synthesis preserves iteration-wise feasibility, avoids costly projections and LMOs, and attains optimal convergence—translating decades of insights on geometry, oracles, and rates into a new, oracle-free, projection-free first-order framework.

---
*Generated: 2026-01-07T00:21:32.294676*
