# Prior Work Analysis Report

## Target Paper
**Title:** dpllevHMbc
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—a Functional Scaling Law (FSL) describing the entire loss trajectory and isolating the effect of arbitrary learning-rate schedules via an intrinsic-time reparameterization—emerges by fusing three strands of prior work. First, the NTK framework (Jacot et al.) establishes that wide-network training follows linear kernel dynamics with mode-wise contraction rates set by kernel eigenvalues. Building on this, spectral analyses in kernel regression (Bordelon, Canatar, Pehlevan) show that power-law eigenvalue decay produces predictable convergence profiles across modes, furnishing the spectral backbone and scaling exponents that the present paper aggregates into a functional law. Second, SGD-in-RKHS theory (Dieuleveut & Bach) explicitly characterizes how step-size sequences enter convergence through cumulative sums and related functionals, directly inspiring the paper’s intrinsic-time variable that collapses disparate schedules into a unified progress measure and enables a schedule-separable representation of the loss. Complementary continuous-time viewpoints of SGD (Mandt, Hoffman, Blei) reinforce this time-reparameterization perspective by linking learning rate to effective temperature and temporal scaling. Third, practical scheduling advances—large-batch training with warmup (Goyal et al.) and LR–batch-size equivalences (Smith & Le)—motivate analyzing realistic piecewise schedules such as warmup–stable–decay within the same functional framework. Finally, empirical scaling laws for final losses in language models (Kaplan et al.) supply the impetus to move beyond endpoints to a trajectory-level law, with the new FSL unifying spectral structure and schedule design into a single predictive description of loss dynamics.

---
*Generated: 2026-01-07T00:29:42.052668*
