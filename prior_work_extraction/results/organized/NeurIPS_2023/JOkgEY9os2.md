# Prior Work Analysis Report

## Target Paper
**Title:** JOkgEY9os2
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MMD-Fuse’s core idea—maximizing two-sample test power by adaptively combining kernels without data splitting—sits squarely on the MMD foundation of Gretton et al. (2012), which provides the U-statistic, asymptotics, and calibration mechanisms underpinning kernel tests. Prior attempts to enhance power focused on data-dependent tuning: Sutherland et al. (2017) optimized kernel hyperparameters using a held-out split, while Jitkrittum et al. (2016) learned test features/locations to maximize a power proxy, also requiring splitting to preserve validity. These works demonstrated that adaptivity helps power but at the cost of data efficiency and potential calibration challenges.

Aggregation-based testing then provided a route to adaptation without splitting. Schrab et al. (2022) showed that aggregating MMD tests across a kernel family can maintain type-I control via permutation calibration, yet such union-type aggregation can be conservative. MMD-Fuse advances this line by introducing a weighted soft maximum (log-sum-exp) of normalized MMDs, which smoothly pools evidence across kernels and yields exponential concentration under both null and alternative, improving sensitivity while preserving calibration through permutation independence.

Supporting components come from variance/concentration analyses of MMD statistics (Zaremba et al., 2013), which motivate per-kernel normalization, and from deep-feature MMD practice (Bińkowski et al., 2018), which demonstrates the gains of neural representations—now accommodated within MMD-Fuse’s permutation-calibrated, no-split pipeline. Finally, the broader multiple-kernel learning literature (Lanckriet et al., 2004) motivates learning to combine kernels; MMD-Fuse tailors this principle to hypothesis testing by optimizing a statistic-level fusion rather than a single composite kernel.

---
*Generated: 2026-01-07T00:02:04.782654*
