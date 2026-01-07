# Prior Work Analysis Report

## Target Paper
**Title:** zL6ljQvPzZ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core advance—adaptive, lightweight protocols for quantile estimation under local and shuffle differential privacy with improved user complexity—builds on three converging lines of prior work. First, the modeling and statistical foundations of LDP trace to Kasiviswanathan et al., which formalized local randomizers and the interactive/noninteractive landscape, and to Duchi–Jordan–Wainwright, whose minimax techniques and ε-LDP rates shape both target sample complexity (∼1/(ε^2α^2)) and the lower-bound toolkit needed to match the new upper bounds. Second, the practical nonadaptive baseline for quantiles arises from LDP histograms (Bassily–Smith), which estimate the entire distribution and then extract order statistics; this approach incurs extra log B factors, motivating a more targeted, query-efficient strategy. The paper’s key algorithmic idea—adaptive thresholding akin to a binary search over [B]—is methodologically foreshadowed by classic noisy binary search (Karp–Kleinberg), demonstrating how to navigate logarithmic-depth searches despite noise. Third, in the shuffle setting, the work leverages the privacy amplification framework inaugurated by Cheu et al. and made tight by Balle et al., enabling one-message protocols with central-like accuracy. Recent shuffle-model results on selection and median (Ghazi et al.) provide problem-specific precedents the paper sharpens by designing adaptive, single-query-per-user protocols with user complexity Õ((1/ε^2 + 1/α^2) log B). Together, these works directly inform the paper’s adaptive designs, yield principled privacy analyses in the shuffle model, and anchor the matching lower bounds that certify optimality up to logarithmic factors.

---
*Generated: 2026-01-07T00:21:32.391709*
