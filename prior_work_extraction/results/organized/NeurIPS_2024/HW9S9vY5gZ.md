# Prior Work Analysis Report

## Target Paper
**Title:** HW9S9vY5gZ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—characterizing the (non-)convergence of no-regret/FTRL learning in generalized harmonic games and showing how extrapolation alters these outcomes—rests on two intertwined lines of prior work. Structurally, the Hodge decomposition of games by Candogan et al. defined harmonic games as the orthogonal complement of potential games, giving a canonical space of conflicting-interest interactions to analyze. Dynamically, the continuous-time viewpoint on regularized learning (Mertikopoulos–Sandholm) and the classical Hamiltonian perspective on adversarial dynamics (Hofbauer) established that, in zero-sum games, regularized/replicator flows are volume-preserving and Poincaré recurrent—precluding convergence in last iterates. Building directly on this, Mertikopoulos, Papadimitriou, and Piliouras showed FTRL’s Hamiltonian cycling in 2-player zero-sum games, introducing invariants and tools that the present paper extends to the full harmonic class, proving recurrence in continuous time and diagnosing discrete-time pathologies (e.g., trapping) for vanilla FTRL. To remedy such issues, the paper turns to extrapolation. The optimism paradigm (Rakhlin–Sridharan) and its instantiation in adversarial/saddle-point settings (Daskalakis et al.) demonstrated that predict-then-correct steps tame rotational dynamics and yield last-iterate convergence in zero-sum models—ideas ultimately rooted in Korpelevich’s extragradient method for monotone variational inequalities. Together, these works provide the structural definition, dynamical invariants, and algorithmic mechanisms that enable this paper’s generalization from zero-sum to harmonic games and its analysis of extrapolated FTRL.

---
*Generated: 2026-01-06T23:39:42.944400*
