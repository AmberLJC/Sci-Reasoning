# Prior Work Analysis Report

## Target Paper
**Title:** s6ZAT8MLKU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—proving a strict iteration-complexity advantage of alternating gradient descent–ascent (Alt-GDA) over simultaneous GDA (Sim-GDA) and introducing an alternating-extrapolation framework (Alex-GDA)—rests on two intertwined lines of prior work. First, the extrapolation paradigm for variational inequalities and saddle-point problems, pioneered by Korpelevich’s extragradient method and refined by Nemirovski’s Mirror-Prox, established that evaluating gradients at appropriately extrapolated points yields superior stability and complexity guarantees. Popov’s method, later popularized in machine learning as optimistic gradient methods, reinforced that predictive/extrapolative steps tame rotational dynamics typical of min–max games. Modern analyses unifying EG and OGDA (e.g., Mokhtari–Ozdaglar–Pattathil) provided tight rates in strongly-convex–strongly-concave and monotone regimes, forming the technical baseline for understanding how extrapolation interacts with problem structure.
Second, the scheduling perspective—whether to update variables simultaneously (Jacobi) or alternately (Gauss–Seidel)—has long been known in numerical methods to affect convergence speed. Bertsekas–Tsitsiklis codified this dichotomy, and empirical advances in adversarial learning (e.g., Daskalakis et al.’s optimism for GANs) suggested that non-simultaneous, extrapolative updates improve behavior in games. Against the broader complexity landscape charted by Lin–Jin–Jordan for SC–SC minimax optimization, the present paper isolates and quantifies the scheduling effect, deriving fine-grained global rates that strictly separate Alt-GDA from Sim-GDA. It then synthesizes the extrapolation and alternation principles into Alex-GDA, a unifying scheme that inherits the stability of extragradient-style methods while preserving the simplicity of GDA, thereby achieving provably smaller iteration complexity.

---
*Generated: 2026-01-07T00:02:04.883242*
