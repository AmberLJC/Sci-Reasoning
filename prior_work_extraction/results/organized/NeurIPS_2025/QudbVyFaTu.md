# Prior Work Analysis Report

## Target Paper
**Title:** QudbVyFaTu
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—deriving minimax separation rates for univariate function selection in sparse additive models (SpAM), with guarantees under both FDR+FNR control and exact support recovery, and studying adaptation to unknown smoothness—sits at the intersection of SpAM estimation theory, nonparametric minimax testing, and sparse multiple testing. Ravikumar et al. (2010) introduced the SpAM framework and group-sparse estimation, while Raskutti, Wainwright, and Yu (2012) established minimax-optimal estimation rates over smoothness classes. These works provide the estimation benchmarks that this paper contrasts with, crystallizing the estimation–selection gap: estimation-optimal procedures need not be selection-optimal. On the selection side, Huang, Horowitz, and Wei (2010) analyzed sparsistency of penalized additive-model selectors, motivating the need for model-agnostic, information-theoretic selection boundaries.
Minimax testing theory from Ingster and Suslina (2003) supplies the backbone for separation rates and the consequences of adaptation to unknown smoothness, which the present work tailors to the per-component testing problem inherent in SpAM. Donoho and Jin (2004) contribute the sparse-signal detection paradigm and phase-diagram intuition that inform the paper’s sparse multiple-testing view. The decision-theoretic treatment of multiple testing by Sun and Cai (2007) directly underlies the paper’s FDR+FNR criterion and the design of adaptive procedures with risk control. Finally, Wainwright (2009) provides the support-recovery, error-probability framework and sharp thresholds that the paper extends to nonparametric additive settings, yielding exact support recovery separation rates. Together, these works directly shape the paper’s rate characterizations, adaptive procedure design, and the formal articulation of the estimation–selection gap in SpAM.

---
*Generated: 2026-01-07T00:21:32.270740*
