# Prior Work Analysis Report

## Target Paper
**Title:** S2P6KPLtm8
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—necessary and sufficient identification conditions for bidirectional MR with some invalid instruments, alongside a cluster fusion-like estimator—builds on three intertwined strands of prior work. First, robustness to invalid instruments in MR was crystallized by MR-Egger (Bowden et al., 2015), the weighted median (Bowden et al., 2016), and the mode-based estimator (Hartwig et al., 2017), which collectively demonstrated that consistent causal estimation is possible when only a subset of instruments is valid. Among these, the mode-based rationale—leveraging clustering of ratio estimates around the true effect—directly informs the new paper’s clustering-and-fusion strategy for isolating valid IV sets.
Second, explicit strategies for identifying valid subsets under partial invalidity were advanced by Kang et al. (2016) via SisVIVE, formalizing the idea that one can recover causal effects if a sufficiently large and coherent valid subset exists; this perspective is extended here to bidirectional models with theoretical guarantees. Complementarily, practical outlier detection and filtering in summary-data MR (Zhu et al., 2018, GSMR) highlighted the utility of variant-level diagnostics to excise pleiotropic instruments, a theme operationalized in the paper’s valid-IV discovery algorithm.
Third, the paper’s identification theory echoes structural equation model results on instrumental sets and graphical identifiability (Brito and Pearl, 2002), bringing rigorous necessary-and-sufficient conditions to the MR context. Finally, for orienting causality between two phenotypes, the MR Steiger test (Hemani et al., 2017) is the nearest antecedent; the paper generalizes direction identification by supplying full identification conditions that remain valid even with unmeasured confounding and some invalid instruments.

---
*Generated: 2026-01-06T23:33:35.543436*
