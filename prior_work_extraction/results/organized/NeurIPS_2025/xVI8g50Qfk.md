# Prior Work Analysis Report

## Target Paper
**Title:** xVI8g50Qfk
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution of Error Forcing (EF) is a principled way to use feedback to adjust recurrent neural activities during learning: guide the state orthogonally toward the zero-error manifold, providing temporal credit assignment while minimally perturbing intrinsic dynamics. This idea arises at the intersection of three strands of prior work. First, foundational RNN learning methods—BPTT (Werbos, 1990) and RTRL/teacher forcing (Williams & Zipser, 1989)—established how gradients flow through time and how clamping to targets can simplify training, but they also revealed computational, biological, and distribution-shift drawbacks. Subsequent critiques like Scheduled Sampling (Bengio et al., 2015) formalized exposure bias from teacher forcing, motivating learning rules that better align training and test-time dynamics.
Second, control-inspired training of RNNs, especially FORCE (Sussillo & Abbott, 2009) and full-FORCE (DePasquale et al., 2018), demonstrated that injecting error feedback can stabilize and shape recurrent dynamics. EF inherits the power of feedback-based control but replaces target clamping with a geometric rule: push only along the error-orthogonal direction, reducing dynamical distortion while still conveying error information.
Third, theories casting learning as inference—predictive coding (Whittington & Bogacz, 2017) and nudging-based energy methods like equilibrium propagation (Scellier & Bengio, 2017)—show how small feedback signals can perform approximate inference and credit assignment. EF’s Bayesian framing as approximate dynamic inference resonates with these, while its orthogonality constraint specifies how feedback should couple to the dynamics. Together, these works directly scaffold EF’s design and its empirical advantages under biological constraints.

---
*Generated: 2026-01-06T23:42:48.125363*
