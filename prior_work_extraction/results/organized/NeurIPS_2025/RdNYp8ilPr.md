# Prior Work Analysis Report

## Target Paper
**Title:** RdNYp8ilPr
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core innovation of this paper is to solve private set union when each user may contribute up to k items, and to evaluate algorithms via a dataset-normalized utility ratio with matching upper and lower bounds. This builds on three pillars. First, foundational DP principles—sensitivity, composition, and group privacy—codified by Dwork–Roth and Dwork–McSherry–Nissim–Smith, underwrite the per-user accounting needed when multiple items come from the same individual. They also justify thresholding and noise calibration for histogram-style queries that power subset-of-union reporting. Second, classical DP selection tools, especially the exponential mechanism, map naturally onto deciding which items to include under a dataset-specific utility, shaping mechanisms that favor reliably present items while controlling privacy loss. Third, lower-bound methodology from fingerprinting-code–based arguments (Bun–Ullman–Vadhan) provides the template to prove that no algorithm can privately recover too many low-frequency items, enabling tight utility-ratio impossibility results.
On the applied/algorithmic side, prior art on discovering strings and heavy hitters under privacy—RAPPOR and minimax analyses for locally private frequency estimation—clarified the operational tradeoffs between suppressing rare items and maximizing discovery, directly motivating the paper’s normalized utility criterion. Finally, work on the shuffle model for multi-message contributions (e.g., Cheu–Smith–Ullman–Zeber) established how aggregating multiple user reports affects privacy/accuracy, a perspective this paper adapts to the central model to design and analyze algorithms with worst-case utility-ratio guarantees across datasets.

---
*Generated: 2026-01-07T00:21:32.226304*
