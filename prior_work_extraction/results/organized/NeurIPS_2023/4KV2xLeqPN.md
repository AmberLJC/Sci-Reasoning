# Prior Work Analysis Report

## Target Paper
**Title:** 4KV2xLeqPN
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The NeurIPS paper tackles a long-standing puzzle: ERM is known to be minimax suboptimal in mean squared error in several settings, yet it often performs competitively. Birgé and Massart’s foundational examples and the aggregation literature (e.g., Rigollet–Tsybakov) crystallized this suboptimality, but did not isolate whether variance or bias is to blame. The authors’ key advance is to show that, under mild assumptions, ERM’s variance term actually attains the minimax rate; suboptimality comes from bias.
Two strands of prior work directly shape their argument. First, Chatterjee’s admissibility theorem for least squares under fixed design established that ERM cannot be uniformly dominated; the present paper supplies a simple proof and extends admissibility to random design, reinforcing ERM’s fundamental optimality properties. Second, stability theory—initiated by Bousquet–Elisseeff and extended by Caponnetto–Rakhlin to non-Donsker classes—provides the lens through which their new variance bounds translate into algorithmic stability, thereby complementing and broadening earlier stability guarantees.
Technically, local complexity methods (Bartlett–Bousquet–Mendelson) and sharp analyses of constrained least squares via Gaussian width (Bellec) underpin the decomposition that disentangles variance from bias and delivers minimax-rate variance control in both fixed and random design. Together, these works inform the paper’s unifying explanation: ERM’s deficiencies in MSE trace to bias, while its variance is inherently optimal, reconciling suboptimality results with admissibility and stability insights.

---
*Generated: 2026-01-06T23:33:36.296504*
