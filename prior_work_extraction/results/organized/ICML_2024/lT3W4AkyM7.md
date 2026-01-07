# Prior Work Analysis Report

## Target Paper
**Title:** lT3W4AkyM7
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

PLOT’s core contribution—achieving O(√(T V_T)) dynamic regret for online tracking of unknown, non-stationary targets by combining prediction with receding-horizon control—sits at the intersection of dynamic-regret OCO, adaptive control, and learning-based MPC. The dynamic-regret lens originates in online convex optimization: Hall and Willett’s formulation of tracking regret against time-varying comparators motivates PLOT’s benchmark of a moving target and its use of predictive models to stabilize regret. Besbes, Gur, and Zeevi’s variation-budget framework provides the precise non-stationarity metric V_T that PLOT adopts to quantify target drift and to express performance. The OCO-with-memory perspective of Anava et al. connects control problems to online learning with temporal coupling, shaping PLOT’s analytical approach to receding-horizon policies. On the control side, Mania, Tu, and Recht established regret guarantees for adaptive LQR, providing techniques and baselines that PLOT extends to a different axis of uncertainty: known plant but unknown, time-varying target dynamics. The algorithmic spine of PLOT—the use of recursive least squares with exponential forgetting—draws directly from Ljung’s system identification treatment, enabling consistent tracking of evolving target models. Finally, the control synthesis leverages the model predictive control foundation of Mayne et al., while Aswani et al.’s learning-based MPC shows how learned models can be embedded within MPC with guarantees. PLOT unifies these strands by learning a time-varying target model with RLS-forgetting, deploying it in MPC, and analyzing performance through the variation-budget dynamic-regret lens.

---
*Generated: 2026-01-07T00:02:04.903529*
