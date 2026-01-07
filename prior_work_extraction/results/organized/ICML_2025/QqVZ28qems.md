# Prior Work Analysis Report

## Target Paper
**Title:** QqVZ28qems
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution is to reconcile a pervasive empirical observation—dataset-level negative log average failure decreasing as a power law with the number of attempts—with the per-problem calculation that failure should decay exponentially as attempts increase. Prior work on multi-try evaluation and sampling created the empirical puzzle. Chen et al. (2021) formalized pass@k for code generation, establishing the canonical per-instance success model (1−(1−p)^k) and aggregations across tasks. Wang et al. (2023) and Minerva (2022) documented that drawing more reasoning samples and voting improves performance on math problems, while Yao et al. (2023) showed that expanding the search tree (i.e., more attempts) similarly increases success. In safety and robustness, Zou et al. (2023) demonstrated that multiple restarts/attempts substantially raise jailbreak success rates, extending the multi-try phenomenon beyond pure reasoning to adversarial and multimodal settings.
To explain how per-problem exponential decay can coexist with aggregate power-law behavior, the paper invokes heavy-tailed heterogeneity in single-attempt success probabilities across tasks. This mechanism is rooted in classical mixture theory: as in Vaupel et al. (1979), mixing exponentials over a heavy-tailed distribution of rates produces non-exponential, regularly varying aggregate trends. Clauset et al. (2009) provides the statistical underpinning for identifying and validating such heavy tails. By integrating these strands, the paper shows that a small fraction of extremely hard tasks (with near-zero p) dominate the aggregate, bending exponential per-problem dynamics into observed power-law scaling across tasks.

---
*Generated: 2026-01-07T00:21:32.381971*
