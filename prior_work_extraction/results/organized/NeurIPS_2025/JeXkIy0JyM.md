# Prior Work Analysis Report

## Target Paper
**Title:** JeXkIy0JyM
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Ctrl-DNA’s core contribution—controllable, cell-type-specific regulatory DNA design via constrained reinforcement learning—emerges at the intersection of three lines of work. First, predictive sequence-to-expression models such as Enformer made it feasible to define precise, cell-type-specific reward signals and off-target penalties directly from DNA, providing the oracle necessary for optimization. Second, genomic language models like DNABERT established that Transformers can capture the regulatory grammar of DNA, motivating Ctrl-DNA’s use of an autoregressive genomic LM as a policy prior to keep designs realistic and diverse. Third, the methodology of optimizing discrete sequences with feedback from learned property predictors was pioneered in molecular and biological design: REINVENT introduced policy-gradient RL over token sequences guided by oracle rewards, while CbAS formalized oracle-in-the-loop optimization with distributional regularization to prevent unrealistic over-optimization. Ctrl-DNA synthesizes these ideas within a principled constrained RL framework, drawing on Constrained Policy Optimization to encode cell-type specificity as maximizing target rewards under explicit off-target constraints. Compared to earlier deep generative approaches for regulatory DNA (e.g., Killoran et al.), Ctrl-DNA replaces gradient-based or GAN methods with an RL formulation that naturally supports multi-objective trade-offs. Relative to general controllable generation methods (e.g., PPLM), Ctrl-DNA contributes domain-specific constraints and reward shaping aligned with cell-type-specific regulatory biology, yielding more reliable, controllable sequence design.

---
*Generated: 2026-01-07T00:02:04.974161*
