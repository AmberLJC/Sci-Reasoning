# Prior Work Analysis Report

## Target Paper
**Title:** Zn44XGFGam
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper fuses two threads: convex formulations of shallow ReLU models and provable optimization dynamics under random data. The convex-function-space lineage (Barron; Bach) formalized two-layer networks as convex objects via variation/Barron norms, clarifying how explicit regularization (such as weight decay) can induce tractable convex surrogates. In parallel, the verification community (Wong–Kolter; Raghunathan et al.) developed LP/SDP relaxations that upper-bound ReLU nonconvexity in polynomial time, demonstrating that tight convex outer approximations can yield certified bounds. Kim and Pilanci build on these insights but pivot the target: instead of worst-case verification, they analyze the training objective with L2 weight decay on random data, proving that a principled convex relaxation approximates the nonconvex optimum within an O(sqrt(log n)) relative gap—an exponential improvement over prior guarantees.

The second pillar is optimization theory for over-parameterized networks on random designs (Du et al.; Allen-Zhu–Li–Song), which established that gradient descent achieves small training error with high probability. Together with implicit-bias results for homogeneous networks (Lyu–Li), these works explain why local methods tend toward norm-regularized solutions aligned with convex surrogates. The present paper synthesizes these lines: it crafts a polynomial-time convex relaxation inspired by prior convex bounds for ReLUs, then uses random-data geometry and insights from GD analyses to prove near-optimality and to show that standard gradient methods reach comparably low loss. The result provides a unified, average-case explanation for the empirical success of local training and a concrete algorithmic relaxation with provable approximation guarantees.

---
*Generated: 2026-01-07T00:02:04.888168*
