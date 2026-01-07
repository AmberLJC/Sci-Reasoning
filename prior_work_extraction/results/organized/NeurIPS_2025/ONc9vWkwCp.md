# Prior Work Analysis Report

## Target Paper
**Title:** ONc9vWkwCp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper addresses optimal online convex optimization on ℓp-balls for p > 2, identifying a fundamental regime shift between d > T and d ≤ T and showing that FTRL must adapt its regularization to be anytime optimal. Its algorithmic backbone draws on the FTRL–Mirror Descent equivalence (McMahan), which clarifies how the choice and scheduling of regularizers govern stability and regret. Geometry is central: Rakhlin–Sridharan’s Banach-space framework connects ℓp uniform convexity/smoothness to minimax regret scalings, exposing how the dimension–horizon interplay differs across regimes. Abernethy–Hazan–Rakhlin’s interior-point perspective demonstrates that carefully tailored regularizers tied to the feasible set’s geometry can achieve near-minimax bounds, motivating a regime-aware (time-varying) regularization strategy on ℓp-balls.

On the adaptivity axis, AdaGrad (Duchi–Hazan–Singer) is the archetype of separable, time-varying regularization; Orabona–Pál and Cutkosky provide parameter-free, scale-free techniques that obtain anytime guarantees via adaptive potentials. The present work sharpens these insights by proving a necessity result: for separable regularizers, any fixed choice is inherently suboptimal in one of the two dimension regimes, thereby establishing that adaptivity is not merely beneficial but required for anytime optimality on ℓp-balls.

Finally, the paper’s lower bounds for linear bandits in high dimension extend the dimension-driven hardness narrative familiar from Dani–Hayes–Kakade’s d√T barriers. It shows that when d is sufficiently large relative to T, sublinear regret is impossible across all ℓp-balls (p ≥ 1), unifying and strengthening the dimensional limitations of bandit feedback.

---
*Generated: 2026-01-07T00:21:32.232584*
