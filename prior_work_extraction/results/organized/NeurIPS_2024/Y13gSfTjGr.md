# Prior Work Analysis Report

## Target Paper
**Title:** Y13gSfTjGr
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

This paper’s core contribution—replacing cosine annealing with a constant learning rate plus cooldown to enable reusable runs across training lengths, while maintaining predictable scaling and boosting trajectory performance via SWA—draws directly from several strands of prior work. SGDR (Loshchilov & Hutter, 2017) established cosine annealing as a default, but its dependence on a predefined total duration makes it awkward for varying-length experiments. By explicitly critiquing this coupling, the authors motivate a schedule that retains performance without binding training to fixed horizons.

The overarching aim is grounded in the scaling-law literature: Kaplan et al. (2020) and Hoffmann et al. (2022) demonstrated predictable loss–compute–size trade-offs and compute-optimality, but typically under fixed-duration assumptions that require many bespoke runs. The proposed constant-LR plateau with a late cooldown decouples schedule from horizon, allowing a single run to serve multiple effective training lengths—substantially reducing compute for scaling studies while preserving the predictability those laws rely on.

Two optimization lines make this feasible. First, SWA (Izmailov et al., 2018) provides a no-cost mechanism to improve checkpoints along the trajectory, making intermediate-length evaluations stronger and more comparable. Second, practical evidence that constant-LR phases train stably comes from large-batch ImageNet training (Goyal et al., 2017) and the demonstrated interchangeability of LR decay and batch-size adjustments (Smith et al., 2018), which together justify long constant-LR regimes and brief cooldowns. Integrating these ideas yields a schedule and evaluation protocol tailored to compute-efficient, predictable scaling beyond fixed training durations.

---
*Generated: 2026-01-06T23:33:36.259580*
