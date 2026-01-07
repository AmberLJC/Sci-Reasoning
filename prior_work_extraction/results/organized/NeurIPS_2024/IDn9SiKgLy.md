# Prior Work Analysis Report

## Target Paper
**Title:** IDn9SiKgLy
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—principled Bayesian optimization that consults human experts via binary accept/reject signals while providing (i) a handover guarantee on label usage and (ii) a no-harm guarantee via adaptive trust—builds on three converging threads. First, the regret-theoretic backbone of GP-BO (Srinivas et al., 2010) supplies the confidence-based sampling and the baseline to which performance is compared; the proposed method must preserve this regret to satisfy no-harm. Second, prior work on human feedback within BO (González et al., 2017) demonstrates how binary human signals can be integrated into GP inference, a modeling idea the authors repurpose from pairwise preferences to single-point accept/reject labels. Third, the multi-source/multi-fidelity literature (Kandasamy et al., 2016; Poloczek et al., 2017) provides the abstraction of humans as a biased, noisy, and costly auxiliary source whose utility is greatest early; this directly influences the handover design and its sublinear label-complexity bound, mirroring how low-fidelity queries fade as learning proceeds. To ensure collaboration never degrades BO, the method adopts a meta-level perspective akin to corralling (Agarwal et al., 2017), adaptively tuning trust so the combined policy tracks the best single strategy (pure BO) up to sublinear terms. Finally, the selective consultation and deferral perspective from human–AI collaboration (Madras et al., 2018) informs the data-driven gating of expert input, yielding principled trust calibration and an asymptotically vanishing reliance on labels without sacrificing BO regret.

---
*Generated: 2026-01-06T23:33:35.582955*
