# Prior Work Analysis Report

## Target Paper
**Title:** YlmYm7sHDE
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Minimum Entropy Coupling with Bottleneck (MEC-B) fuses two threads: extremal couplings with fixed marginals and bottleneck-based representation learning. On the coupling side, the decoder subproblem is a classical Minimum Entropy Coupling: among all joint distributions with given marginals, select the one that maximizes dependence (equivalently, minimizes joint entropy). The structural intuition for this problem traces to Rüschendorf’s extremal couplings and Fréchet–Hoeffding bounds, which explain why comonotone, monotone-mass matchings are optimal and motivate efficient greedy constructions. On the representation side, MEC-B’s encoder is governed by an explicit bottleneck that constrains stochasticity. This is directly inspired by the Information Bottleneck framework, with the Deterministic Information Bottleneck clarifying when optimal encoders become nearly functional—precisely the regime MEC-B analyzes. Algorithmically, the proposed greedy EBIM procedure parallels the Agglomerative Information Bottleneck’s monotonic improvement guarantees and is conceptually akin to deterministic annealing’s entropy-constrained progression from stochastic to deterministic assignments. The choice of logarithmic loss ties the two halves together: as established in the log-loss literature, optimal reconstructions are posterior distributions and the expected distortion equals conditional entropy, legitimizing MEC-B’s decomposition into an encoder-side information maximization under an entropy budget and a decoder-side MEC. Finally, the paper’s characterization near functional mappings resonates with Gács–Körner’s common information, which delineates when a deterministic common part suffices—providing a principled boundary case for MEC-B’s controlled stochasticity.

---
*Generated: 2026-01-06T23:33:35.569183*
