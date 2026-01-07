# Prior Work Analysis Report

## Target Paper
**Title:** 8oSY3rA9jY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Edge Pruning’s core innovation—casting circuit discovery as an edge-level optimization problem solved with gradient-based pruning—emerges from the confluence of mechanistic interpretability’s circuit paradigm and decades of sparsification research. Foundational circuit work on induction heads formalized components (heads/MLPs) and their interactions as sparse, task-relevant subgraphs, while the IOI circuit established concrete benchmarks and causal-evaluation practices for verifying faithfulness. ACDC then demonstrated the feasibility of automated circuit discovery but relied on costly, intervention-driven combinatorial search that can mis-rank edges and struggle to scale. 

Edge Pruning imports the pruning community’s most effective ideas to overcome these limitations. SNIP’s connection-sensitivity motivated optimizing over edge masks using gradients, and L0-style hard-concrete gating provides a differentiable sparsity prior to directly minimize edge count while matching the full model’s outputs. Movement Pruning informs learning sparsity during fine-tuning, maintaining task performance as structure is removed. The older Optimal Brain Damage principle further justifies focusing on connections themselves, not just units, aligning with the interpretability goal of identifying specific inter-component pathways. 

By unifying these strands, Edge Pruning replaces discrete search with a scalable, continuous objective: preserve model predictions on circuit-finding tasks while minimizing the number of inter-component edges. The result is circuits with substantially fewer edges, comparable faithfulness, and significantly improved efficiency on large datasets.

---
*Generated: 2026-01-07T00:02:04.747806*
