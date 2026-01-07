# Prior Work Analysis Report

## Target Paper
**Title:** bOYVESX7PK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—identifying when distinct training procedures have equivalent dynamics via topological conjugacy—rests on two pillars: a precise notion of dynamical equivalence and a computable, data-driven test. Koopman’s original operator-theoretic formulation provided the lens to encode nonlinear dynamics linearly in function space, while Mezić’s development of Koopman spectral analysis established that spectral objects (eigenvalues/eigenfunctions) are invariants under conjugacy, making them suitable markers of equivalence. Applied Koopmanism further connected these invariants to practical computation and clarified their behavior under coordinate changes, directly shaping the paper’s choice of spectral criteria. The computational backbone comes from EDMD, which enables robust estimation of Koopman spectra from sampled training trajectories, allowing the proposed equivalence test to be executed on real optimization dynamics.
On the validation side, the optimization literature supplies canonical equivalences the method should recover. Beck and Teboulle’s mirror descent framework and its dual-coordinate interpretation, together with Kivinen and Warmuth’s exponentiated-gradient-as-gradient-descent-in-log-space result, offer concrete instances of algorithmic conjugacy. Shalev-Shwartz’s synthesis of online gradient descent and online mirror descent situates these relationships in the online learning setting used by the paper’s experiments. Together, these works directly enable the paper’s key idea: use Koopman spectral invariants, estimated from data, to detect when different training algorithms or parameterizations are topologically conjugate—and thus dynamically equivalent.

---
*Generated: 2026-01-06T23:39:42.962759*
