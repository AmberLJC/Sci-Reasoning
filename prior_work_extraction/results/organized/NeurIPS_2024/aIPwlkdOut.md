# Prior Work Analysis Report

## Target Paper
**Title:** aIPwlkdOut
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper fuses two lines of work: cognitive models of decision making that jointly explain choices and response times, and preference-based linear bandits for pure exploration. The diffusion decision model (Ratcliff & McKoon, 2008) establishes that faster responses typically arise from stronger latent evidence, implying an inverse relationship between response time and preference ambiguity. The EZ-diffusion estimator (Wagenmakers et al., 2007) operationalizes this insight, providing a computationally efficient way to recover drift-rate–like signals from observed accuracies and response times. On the bandit side, the dueling bandits formulation (Yue et al., 2009) defined the interactive preference-learning setting with pairwise comparisons, while RUCB-style methods (Zoghi et al., 2014) codified confidence-based exploration for noisy comparative feedback. Linear dueling bandits (Saha & Gopalan, 2018) demonstrated how to exploit linear utility structure in preference feedback, and linear best-arm identification results (Soare et al., 2014; Jedra & Proutiere, 2020) provided fixed-budget and information-theoretic design principles for efficient pure exploration. Building directly on these, the present work injects RT-derived strength information—grounded in EZ-diffusion—into the preference-based linear BAI pipeline. The key advance is showing theoretically and empirically that response times complement binary choices, especially for queries with strong preferences, yielding more informative feedback and faster convergence in linear BAI.

---
*Generated: 2026-01-06T23:33:35.544789*
