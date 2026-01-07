# Prior Work Analysis Report

## Target Paper
**Title:** OZSXYeqpI1
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s key contribution—tight empirical auditing of mechanisms in one run using an f-DP curve—rests on two converging lines of prior work: single-run auditing and hypothesis-testing-based privacy characterizations. Steinke, Nasr, and Jagielski (2023) provided the catalyst for efficiency by showing that dataset-level randomness can be harnessed to perform a powerful audit from a single execution, avoiding multiple retrainings. This paper builds directly on that paradigm but replaces ad hoc privacy summaries with a principled hypothesis-testing lens.

The f-DP framework, introduced via Gaussian Differential Privacy by Dong, Roth, and Su (2019), reframed privacy guarantees as trade-off curves for the most powerful hypothesis tests. That perspective is exactly what this paper operationalizes: it treats the mechanism’s hypothesized f-DP curve as the null and designs a test that yields tight empirical privacy estimates. Achieving tightness further depends on modern accounting tools that produce accurate hypothesized curves for mechanisms like DP-SGD. Rényi Differential Privacy (Mironov, 2017) and its subsampled extensions and analytical accountant (Wang, Balle, Kasiviswanathan, 2019) supply precise profiles for common training pipelines, which can be converted to f-DP trade-off curves. Finally, privacy amplification by subsampling (Balle et al., 2018) justifies exploiting random inclusion of examples—the same source of randomness leveraged by one-run auditors. Together with the practical target of DP-SGD introduced by Abadi et al. (2016), these works directly enable the paper’s one-run, f-DP-based auditing method that is both efficient and empirically tight.

---
*Generated: 2026-01-07T00:21:32.374640*
