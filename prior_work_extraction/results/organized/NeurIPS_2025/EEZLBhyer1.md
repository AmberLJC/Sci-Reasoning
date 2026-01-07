# Prior Work Analysis Report

## Target Paper
**Title:** EEZLBhyer1
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—a Graphon Limit Hypothesis for pruned neural networks and the derivation of a Graphon NTK—sits at the intersection of infinite-width learning theory and graph limit theory, applied to the longstanding pruning puzzle. On the learning-theoretic side, Jacot et al. (2018) introduced the Neural Tangent Kernel, and Lee et al. (2019) established that wide networks evolve as linear models under gradient descent. These works supply the analytical infrastructure for translating network training dynamics into kernel evolution in the infinite-width regime; the present paper extends this to sparsity by defining an NTK parameterized by a limiting graphon that encodes connectivity structure.

On the graph-theoretic side, Lovász and Szegedy (2006) created the graphon framework for limits of graph sequences, and Borgs et al. (2018) generalized it to sparse settings. These results justify modeling layer-wise bipartite connectivity patterns as graphons and formalize convergence of pruning-induced patterns as width increases—precisely the paper’s Graphon Limit Hypothesis.

Finally, empirical pruning literature provides both the motivation and the concrete connectivity distributions to analyze. The Lottery Ticket Hypothesis (Frankle & Carbin, 2019) crystallized the observation that some sparse subnetworks are especially trainable, while methods such as SNIP (Lee et al., 2019) and dynamic sparse training via RigL (Evci et al., 2020) demonstrably impose different structural biases on connectivity. By mapping these method-specific sparsity patterns to limiting graphons and importing NTK dynamics, the paper offers a unifying theory of how structural biases impact trainability in the infinite-width limit.

---
*Generated: 2026-01-07T00:21:32.227717*
