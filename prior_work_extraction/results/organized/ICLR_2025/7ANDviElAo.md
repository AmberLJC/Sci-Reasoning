# Prior Work Analysis Report

## Target Paper

**Title:** Graph Sparsification via Mixture of Graphs

**Conference:** ICLR 2025 (spotlight)

**Authors:** Guibin Zhang, Xiangguo Sun, Yanwei Yue, Chonghe Jiang, Kun Wang, Tianlong Chen, Shirui Pan

**Keywords:** Graph Sparsification, Mixture-of-Experts

**Abstract:** 
> Graph Neural Networks (GNNs) have demonstrated superior performance across various graph learning tasks but face significant computational challenges when applied to large-scale graphs. One effective approach to mitigate these challenges is graph sparsification, which involves removing non-essential edges to reduce computational overhead. However, previous graph sparsification methods often rely on a single global sparsity setting and uniform pruning criteria, failing to provide customized spars...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Predict then Propagate: Graph Neural Networks meet Personalized PageRank (APPNP)** (2019)
- *Authors:* Johannes Klicpera et al.
- *Direct Connection:* MoG uses PPR-based pruning as a sparsifier expert and generalizes APPNP’s globally fixed teleport/threshold into a node-conditioned choice among different PPR sparsity regimes.

**Graph Sparsification by Effective Resistances** (2011)
- *Authors:* Daniel A. Spielman et al.
- *Direct Connection:* MoG leverages the core idea of criterion-driven edge selection from spectral sparsification and relaxes its single global sparsity budget by routing nodes to experts with different sparsity levels.

### 💡 Inspiration

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Direct Connection:* MoG ports the sparsely-gated MoE idea by treating diverse sparsifiers as experts and learning a node-wise gating function that selects which sparsification rule to apply for each node.

### 🔍 Gap Identification

**DropEdge: Towards Deep Graph Convolutional Networks on Node Classification** (2020)
- *Authors:* Yu Rong et al.
- *Direct Connection:* MoG explicitly addresses DropEdge’s limitation of a global, uniform edge-drop rate by learning per-node selections over multiple pruning schemes rather than applying a single stochastic rule across the graph.

**Learning Discrete Structures for Graph Neural Networks** (2019)
- *Authors:* Luca Franceschi et al.
- *Direct Connection:* MoG departs from LDS’s single, globally learned discrete adjacency by learning to combine several sparsification principles via node-wise routing, addressing LDS’s monolithic structure and scalability limits.

### 📊 Baseline

**Diffusion Improves Graph Learning (GDC)** (2019)
- *Authors:* Johannes Klicpera et al.
- *Direct Connection:* MoG incorporates diffusion/top-k-based sparsification as an expert and extends GDC by mixing diffusion-sparsified graphs with other criteria under a learned gate instead of fixing one diffusion recipe globally.

### 🔧 Extension

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Direct Connection:* MoG adopts Switch-style simple top-1 routing and a load-balancing auxiliary loss to prevent expert collapse when assigning nodes to sparsifier experts.

---

## Synthesis: How Prior Work Led to This Paper

Sparsely-gated mixture-of-experts established that inputs can be routed to specialized experts via a learned gate, yielding conditional computation and diversity in processing; later, Switch Transformers simplified this idea with top-1 routing and load-balancing losses that stabilize expert usage at scale. On the graph side, DropEdge showed that removing edges reduces computation and can even help generalization, but it did so with a global, uniform drop rate that ignores local structural needs. APPNP grounded a principled, PPR-based propagation that effectively acts as a PPR-driven sparsification of neighborhoods using globally fixed parameters, while GDC implemented diffusion-based reweighting with top‑k sparsification—still governed by uniform, graph-wide settings. Learning Discrete Structures (LDS) demonstrated that one can learn a task-specific sparse adjacency end-to-end, yet produced a single global structure with heavy bilevel optimization, limiting scalability and per-node adaptivity. Classical spectral sparsification by effective resistances provided a criterion-based lens on which edges to keep, but again under a single global budget. Taken together, these works revealed a tension: edge sparsification is powerful but typically applied uniformly or as a single global structure, whereas gating can tailor computation per input. The natural next step is to treat different sparsification criteria and sparsity levels as experts and learn a node-wise routing policy that selects and mixes them. By importing stabilized MoE routing into graph sparsification, the current work enables locally customized, computationally efficient sparsity that flexibly combines diffusion/PPR/criterion-driven graphs without committing to one global recipe.

---

*Analysis generated on: 2026-01-06T18:35:07.761299*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
