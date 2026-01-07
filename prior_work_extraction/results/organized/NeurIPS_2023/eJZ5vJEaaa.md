# Prior Work Analysis Report

## Target Paper
**Title:** eJZ5vJEaaa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper’s core innovation is a circuit-complexity account of when relational neural networks (GNNs and transformers) can implement goal-conditioned policies for planning via a correspondence to serialized goal regression search (S-GRS). The foundation for S-GRS is classical goal regression in STRIPS (Fikes & Nilsson), which formalizes regressing from a goal to supporting subgoals through action preconditions. Building on this, theoretical work on goal serializability and ordering (Koehler & Hoffmann) clarifies when subgoals can be pursued in sequence without destructive interactions, directly motivating the paper’s three classes of planning problems that imply different resource growth for a serialized policy circuit.

On the neural side, the focus on goal-conditioned policies follows Universal Value Function Approximators (Schaul et al.), which frame policies as feed-forward mappings from state and goal—the exact object whose width/depth complexity is analyzed. Relational neural network architectures provide the computational substrate: Transformers (Vaswani et al.) and graph networks (Battaglia et al.) supply object- and relation-centric computation with shared parameters, enabling generalization across varying numbers of objects. The paper’s constructive proofs leverage insights from GNN expressivity (Xu et al.), where required message-passing depth reflects the radius of necessary information aggregation, to tie planning horizon and interaction structure to circuit depth and width. Finally, the structural perspective on planning complexity from width-based analyses (Lipovetzky & Geffner) informs the idea that domains fall into qualitatively distinct classes, here reframed as distinct scaling regimes for relational network circuits implementing S-GRS policies.

---
*Generated: 2026-01-06T23:42:49.081341*
