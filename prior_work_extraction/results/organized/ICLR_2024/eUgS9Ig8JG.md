# Prior Work Analysis Report

## Target Paper

**Title:** SaNN: Simple Yet Powerful Simplicial-aware Neural Networks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Sravanthi Gurugubelli, Sundeep Prabhakar Chepuri

**Keywords:** Graph Neural Networks, Higher-order Representation Learning, Simplicial Complexes, Simplicial Neural Networks, Weisfeiler-Lehman Isomorphism Test

**Abstract:** 
> Simplicial neural networks (SNNs) are deep models for higher-order graph representation learning. SNNs learn low-dimensional embeddings of simplices in a simplicial complex by aggregating features of their respective upper, lower, boundary, and coboundary adjacent simplices. The aggregation in SNNs is carried out during training. Since the number of simplices of various orders in a simplicial complex is significantly large, the memory and training-time requirement in SNNs is enormous. In this wo...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**How Powerful are Graph Neural Networks?** (2019)
- *Authors:* Keyulu Xu et al.
- *Direct Connection:* This paper established the expressivity lens connecting message-passing GNNs to the 1-WL test, a framework SaNN adopts to prove it surpasses WL while remaining as expressive as message passing on simplices under stated conditions.

### 💡 Inspiration

**Simplifying Graph Convolutional Networks** (2019)
- *Authors:* Felix Wu et al.
- *Direct Connection:* SGC’s key idea of decoupling propagation from learning by precomputing multi-hop aggregations directly inspires SaNN’s pre-aggregation of simplicial interactions before a simple neural predictor.

**SIGN: Scalable Inception Graph Neural Networks** (2020)
- *Authors:* Fabrizio Frasca et al.
- *Direct Connection:* SIGN demonstrated that multiple fixed graph diffusions can be precomputed and fed to a lightweight learner for scalability, which SaNN generalizes from graphs to simplicial complexes by precomputing boundary/coboundary and upper/lower adjacency-based features.

### 🔍 Gap Identification

**Simplicial Neural Networks** (2020)
- *Authors:* Giulia Ebli et al.
- *Direct Connection:* This work formalized aggregation on simplicial complexes via boundary/coboundary and upper/lower adjacencies but requires on-the-fly multi-adjacency message passing, whose heavy training-time memory and compute costs are exactly the scalability pain-points SaNN removes with pre-aggregated simplicial-aware features.

### 📊 Baseline

**Weisfeiler and Leman Go Topological: Message Passing Simplicial Networks** (2021)
- *Authors:* Cristian Bodnar et al.
- *Direct Connection:* MPSNs introduced WL-style message passing on simplices and established expressivity results, and SaNN is designed to match this expressivity while eliminating training-time message passing by precomputing the same simplicial interactions.

### 🔗 Related Problem

**Weisfeiler and Leman Go Cellular: CW Networks** (2021)
- *Authors:* Cristian Bodnar et al.
- *Direct Connection:* By extending WL-style expressivity analysis to cell complexes, this work provided proof techniques and topological operators that inform SaNN’s expressivity arguments and operator choices on simplicial complexes.

---

## Synthesis: How Prior Work Led to This Paper

Simplicial Neural Networks defined how to propagate information over simplicial complexes using boundary and coboundary maps together with upper and lower adjacencies, thereby operationalizing higher-order message passing but at the cost of large training-time memory and compute due to per-epoch aggregation. Weisfeiler and Leman Go Topological: Message Passing Simplicial Networks built a WL-style message passing framework on simplices, connecting topological aggregation to color-refinement expressivity and setting a high-expressivity baseline. Simplifying Graph Convolutional Networks showed that one can precompute multi-hop aggregations and train a simple classifier, decoupling propagation from learning to slash training costs. SIGN further generalized this idea by precomputing multiple diffusions and concatenating them as features to a small learner, demonstrating scalable training with constant-time epochs regardless of graph density. How Powerful are Graph Neural Networks? established the expressivity yardstick by relating MPNNs to the 1-WL test, a perspective later reused in topological settings. Weisfeiler and Leman Go Cellular: CW Networks extended WL-style reasoning from graphs to higher-order structures, offering proof strategies that translate to simplicial contexts. Together, these works expose a gap: simplicial message passing offers strong expressivity but suffers from prohibitive training-time aggregation, while precomputation on graphs yields scalability but lacks higher-order structure. SaNN synthesizes these strands by precomputing simplicial-aware features built from boundary/coboundary and upper/lower adjacencies, feeding them to a simple learner to achieve constant training-time/memory, and by leveraging WL-style analysis to show it exceeds 1-WL and matches MPSN-level power under stated conditions.

---

*Analysis generated on: 2026-01-06T05:48:09.654225*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
