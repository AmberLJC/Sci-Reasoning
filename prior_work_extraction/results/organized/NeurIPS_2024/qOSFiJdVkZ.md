# Prior Work Analysis Report

## Target Paper
**Title:** qOSFiJdVkZ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core idea—interpreting a neural network as an ensemble of neural tangent experts and deriving Bayesian updates that coincide with scaled, projected SGD—rests on three converging lines of prior work. First, NTK theory (Jacot et al., 2018) and linearized training dynamics (Lee et al., 2019) formalize the lazy regime in which a network’s tangent features are fixed, making it natural to treat parameters as weights over a basis of fixed functions. This fixed-feature perspective echoes the random features program (Rahimi & Recht, 2008), where prediction arises from linearly weighting immutable basis functions, anticipating the paper’s “expert” viewpoint.
Second, continual learning through Bayesian updating (Nguyen et al., 2018; Ritter et al., 2018) established Bayes’ rule as a principled antidote to forgetting, with practical approximations via variational or Laplace methods. These works motivate the paper’s strategy: if a single network can be recast as a Bayesian ensemble of fixed experts, then continual learning reduces to sequential posterior updates over those experts. EWC (Kirkpatrick et al., 2017) further highlighted the importance of curvature-weighted constraints, foreshadowing the curvature-scaled projections that emerge in the authors’ analysis.
Third, the equivalence between SGD and Bayesian inference (Mandt et al., 2017) provides the crucial bridge to show that expert posterior updates map to a particular scaled/projected SGD on network weights. Together, these threads directly enable the paper’s main contribution: a theoretically grounded ensemble interpretation of neural networks that yields practical, forgetting-resistant continual learning algorithms.

---
*Generated: 2026-01-06T23:33:35.522438*
