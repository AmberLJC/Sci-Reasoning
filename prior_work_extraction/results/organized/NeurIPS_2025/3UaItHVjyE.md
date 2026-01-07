# Prior Work Analysis Report

## Target Paper
**Title:** 3UaItHVjyE
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—a proof that the implicit bias of gradient descent in structured state space models (SSMs) can be derailed by the inclusion of a few strategically chosen, teacher-labeled examples—rests on three converging lines of prior work. First, architectural advances in SSMs, inaugurated by S4 and extended by Mamba, defined the modern, convolutional-like state-space layers whose learning dynamics and inductive priors warrant careful study. Second, the SSM-specific positive guarantee, articulated in prior work on the implicit bias of SSMs in the low-dimensional teacher setting, argued that gradient descent preferentially discovers low-order dynamics that generalize. This paper revisits that exact setting and shows the guarantee is fragile: particular clean examples can redirect the optimization trajectory to a non-generalizing solution.
Third, general implicit bias theory—Soudry et al. on maximum-margin dynamics and Gunasekar et al. linking architectural parameterizations to implicit norms—provides the analytical lens for understanding how model structure plus gradient descent select among interpolating solutions. The clean-label poisoning literature (e.g., Poison Frogs) and influence-function analyses supply the conceptual precedent that a handful of clean points can systematically steer learned models. Synthesizing these strands, the authors pinpoint and formalize a previously unobserved mechanism in SSMs: special, correctly labeled samples can corrupt the architecture-induced bias that otherwise promotes generalization, yielding rigorous theorems and empirical evidence across standalone SSMs and hybrid non-linear networks.

---
*Generated: 2026-01-07T00:21:32.283175*
