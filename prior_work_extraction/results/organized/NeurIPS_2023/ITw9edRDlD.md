# Prior Work Analysis Report

## Target Paper
**Title:** ITw9edRDlD
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The Mirage paper’s central claim—that apparent emergent abilities arise from evaluation choices rather than abrupt capability phase transitions—builds directly on two strands of prior work. First, emergent-ability narratives from Wei et al. (2022) and the BIG-bench report documented sharp, seemingly unpredictable jumps in accuracy on select tasks. These studies popularized exact-match and other thresholded or aggregated metrics that readily transform gradual improvements in token-level probabilities into step-like gains in reported performance. Methods like chain-of-thought prompting and self-consistency (Wei et al., 2022; Wang et al., 2022) further entrenched nonlinear aggregation—e.g., majority voting over samples—intensifying the appearance of sudden breakthroughs.

Second, the scaling-law literature (Kaplan et al., 2020; Hoffmann et al., 2022) established that pretraining loss follows smooth, predictable trends with model scale and data. Mirage hinges on this smoothness: if underlying log-likelihood improves continuously, then discontinuities in reported performance must originate from the evaluation mapping. Code-evaluation practice (Chen et al., 2021) exemplifies this, with pass@k introducing a pronounced nonlinear relationship between token probabilities and task success rates.

Synthesizing these threads, Mirage provides a simple mathematical model and empirical remeasurements showing that replacing discontinuous metrics (exact match, pass@k, majority-vote accuracy) with linear or continuous metrics yields smooth, predictable curves, dissolving purported ‘emergence.’ Thus, the paper reframes the discourse: the surprise lies not in model behavior but in the metrics that compress gradual probability improvements into threshold crossings.

---
*Generated: 2026-01-06T23:42:49.073335*
