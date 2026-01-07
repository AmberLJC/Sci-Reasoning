# Prior Work Analysis Report

## Target Paper
**Title:** 2uKVyGq5zK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ProtInvTree’s core idea—casting inverse folding as deliberate, reward-guided tree search—sits at the intersection of three lines of work. First, deep inverse folding models (Ingraham et al., ProteinMPNN) crystallized the structure-conditioned, autoregressive paradigm for residue assignment on protein graphs and achieved strong recovery. However, their mostly single-path decoding underplays the one-to-many mapping between structure and sequence, highlighting the need for explicit exploration that preserves structural consistency. Second, the protein design community has long optimized sequences against structural objectives: RosettaDesign established score-driven search on fixed backbones, while deep hallucination (Anishchenko et al.) showed how learned structure predictors can act as powerful oracles, turning sequence design into reward optimization. ProtInvTree leverages this tradition by using self-evaluation and oracle-like rewards to assess partial and complete designs. Third, advances in decision-time search and deliberate generation provide the algorithmic scaffold. AlphaZero’s MCTS offers lookahead, backpropagation of value estimates, and principled exploration–exploitation balancing, which ProtInvTree adapts to discrete residue assignment under structural constraints. Tree of Thoughts translates these planning ideas to generative modeling, motivating ProtInvTree’s self-evaluation, branching, and backtracking during sequence construction. Finally, the two-stage focus-and-grounding action design—separating where to act from what residue to place—draws on insertion-based decoding (Insertion Transformer), enabling flexible, non-monotonic construction and better global consistency. Together, these works directly inform ProtInvTree’s reward-guided tree search that balances diversity with structure fidelity.

---
*Generated: 2026-01-07T00:21:33.174689*
