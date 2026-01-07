# Prior Work Analysis Report

## Target Paper
**Title:** Bk13Qfu8Ru
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—severing spurious correlations by pruning a small set of harmful training examples—emerges at the intersection of robustness-under-shift and per-example attribution. IRM formalized the goal of learning invariances to avoid shortcut features, while Group DRO operationalized worst-group robustness, revealing practical gaps when group labels are unavailable. EIIL advanced this by inferring environments from model behavior, demonstrating that one can recover structure related to spuriousness without annotations. Parallel to these robustness threads, influence functions and data valuation (Data Shapley) established that individual training points can be quantified for their impact on model predictions, offering mechanisms to identify samples that disproportionately induce undesirable behavior. Complementing these, example forgetting studies showed that a small subset of examples critically shapes generalization, suggesting that strategic removal can alter what models learn. Finally, results on last-layer retraining indicate that learned representations often contain both core and spurious signals and that decision boundaries can be corrected with minimal interventions—implying that pruning targeted examples could similarly reorient the boundary toward invariant features. Building on these insights, the present work addresses a less-explored regime where spurious signals are weaker and harder to detect per-example, showing that even then, a handful of samples can trigger catastrophic reliance on spurious cues and that carefully identifying and pruning them provides a simple, annotation-free route to robust generalization.

---
*Generated: 2026-01-06T23:42:48.088588*
