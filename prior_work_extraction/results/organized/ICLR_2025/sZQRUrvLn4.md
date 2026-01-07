# Prior Work Analysis Report

## Target Paper

**Title:** Graph Neural Networks Can (Often) Count Substructures

**Conference:** ICLR 2025 (spotlight)

**Authors:** Paolo Pellizzoni, Till Hendrik Schulz, Karsten Borgwardt

**Keywords:** graph neural networks, subgraphs, expressivity

**Abstract:** 
> Message passing graph neural networks (GNNs) are known to have limited expressive power in their ability to distinguish some non-isomorphic graphs.
Because of this, it is well known that they are unable to detect or count arbitrary graph substructures (i.e., solving the subgraph isomorphism problem), a task that is of great importance for several types of graph-structured data. 
However, we observe that GNNs are in fact able to count graph patterns quite accurately across several real-world grap...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**How Powerful are Graph Neural Networks?** (2019)
- *Authors:* Keyulu Xu et al.
- *Direct Connection:* This paper formalized message-passing GNNs’ equivalence to 1-WL and highlighted their inability to count many substructures in the worst case, providing the formal expressivity framework and motivating gap that the present work addresses with beyond–worst-case conditions.

**Weisfeiler and Leman Go Neural: Higher-Order Graph Neural Networks** (2019)
- *Authors:* Christopher Morris et al.
- *Direct Connection:* By tying GNN expressivity to the WL hierarchy and introducing higher-order variants, this work supplies the theoretical lens (1-WL vs k-WL) that the present analysis leverages to characterize when standard message passing can (and cannot) count subgraphs.

**Color-Coding** (1995)
- *Authors:* Noga Alon et al.
- *Direct Connection:* Color-coding’s dynamic programming framework for detecting/counting bounded-treewidth patterns underpins the subgraph isomorphism DPs that this work designs and shows can be efficiently implemented by message-passing GNNs.

### 💡 Inspiration

**Homomorphisms are a good basis for counting small subgraphs** (2017)
- *Authors:* Radu Curticapean et al.
- *Direct Connection:* The homomorphism-count decomposition insight directly motivates linking message-passing aggregates to subgraph counts, enabling the paper’s sufficient conditions and sample-efficient learnability results for counting.

**Neural Algorithmic Reasoning** (2021)
- *Authors:* Petar Veličković et al.
- *Direct Connection:* This work’s thesis that GNNs can emulate classical dynamic programs informs the construction and proofs showing message-passing GNNs can implement the proposed subgraph-isomorphism DPs efficiently.

### 🔍 Gap Identification

**Improving Graph Neural Network Expressivity via Subgraph Isomorphisms (Graph Substructure Networks)** (2020)
- *Authors:* Andreas Bouritsas et al.
- *Direct Connection:* GSN augments GNNs with explicit subgraph features to overcome MPNN limitations, a design that the present work challenges by proving conditions under which plain MPNNs can learn to count subgraphs without such augmentations.

### 📊 Baseline

**Provably Powerful Graph Networks** (2019)
- *Authors:* Haggai Maron et al.
- *Direct Connection:* This paper provides higher-order architectures that can provably count motifs, serving as the chief comparator and efficiency foil against which the current work shows when vanilla message passing can achieve subgraph counting without higher-order tensors.

---

## Synthesis: How Prior Work Led to This Paper

Message-passing GNNs were rigorously positioned by Xu et al. as no more expressive than the 1-WL color refinement, cementing their worst‑case inability to distinguish certain non‑isomorphic graphs and, by extension, to count many substructures. Morris et al. connected GNN expressivity to the full WL hierarchy and introduced higher‑order models, providing the formal ladder against which counting capabilities are assessed. Maron et al. then delivered higher‑order architectures that can provably count motifs, albeit at higher computational cost, demonstrating that counting is achievable with more expressive (but expensive) tensorized networks. In contrast, Bouritsas et al. proposed augmenting MPNNs with explicit subgraph features (GSN) to overcome counting limits, implying that plain message passing is insufficient in practice. On the algorithmic side, Alon, Yuster, and Zwick’s color‑coding established dynamic programming schemes to detect/count bounded‑treewidth patterns, while Curticapean, Dell, and Marx showed subgraph counts can be expressed as linear combinations of homomorphism counts. Finally, Veličković et al. argued GNNs can learn to execute classical dynamic programs, suggesting a route to algorithmically grounded GNN behaviors.
Taken together, these works expose a tension: worst‑case limits versus practical algorithmic structure. The combination of WL‑based limits, homomorphism‑count decompositions, and DP schemes for restricted patterns suggests that counting may be tractable when graphs satisfy structural conditions. Building on this, the present paper crystallizes sufficient conditions under which message passing can both compute and learn subgraph counts, and designs dynamic programs whose operations align with MPNN updates—showing that, beyond worst case, standard GNNs can often count substructures efficiently and sample‑efficiently.

---

*Analysis generated on: 2026-01-06T14:12:27.054315*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
