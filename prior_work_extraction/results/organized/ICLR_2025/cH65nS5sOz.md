# Prior Work Analysis Report

## Target Paper

**Title:** Subgraph Federated Learning for Local Generalization

**Conference:** ICLR 2025 (oral)

**Authors:** Sungwon Kim, Yoonho Lee, Yunhak Oh, Namkyeong Lee, Sukwon Yun, Junseok Lee, Sein Kim, Carl Yang, Chanyoung Park

**Keywords:** Graph Neural Networks, Graph Federated Learning

**Abstract:** 
> Federated Learning (FL) on graphs enables collaborative model training to enhance performance without compromising the privacy of each client. However, existing methods often overlook the mutable nature of graph data, which frequently introduces new nodes and leads to shifts in label distribution. Since they focus solely on performing well on each client's local data, they are prone to overfitting to their local distributions (i.e., local overfitting), which hinders their ability to generalize t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**FedGraphNN: A Federated Learning System and Benchmark for Graph Neural Networks** (2021)
- *Authors:* He et al.
- *Direct Connection:* FedLoG adopts the standard federated graph learning formulation and evaluation setups systematized by FedGraphNN while modifying the training data via global synthetic subgraphs.

### 💡 Inspiration

**Dataset Condensation with Gradient Matching** (2021)
- *Authors:* Bo Zhao et al.
- *Direct Connection:* FedLoG adopts the core idea of distilling class information into a compact synthetic dataset via gradient/feature matching, adapting it from images to synthesize class-consistent subgraphs for federated training.

**FedProto: Federated Prototype Learning across Heterogeneous Clients** (2022)
- *Authors:* Tan et al.
- *Direct Connection:* FedLoG builds on the idea of sharing class-wise prototypes, using reliable per-class client representations as inputs to construct structure-aware synthetic subgraphs that convey missing classes.

### 📊 Baseline

**FedSage+: Scalable Federated Graph Learning with Subgraph Sampling** (2021)
- *Authors:* Zhang et al.
- *Direct Connection:* FedLoG targets the key limitation of FedSage+—training solely on locally observed subgraphs—by injecting globally synthesized subgraphs to prevent local overfitting under label-shifted, mutable graphs.

### 🔧 Extension

**GCond: Efficient Graph Condensation** (2022)
- *Authors:* Jin et al.
- *Direct Connection:* FedLoG directly extends graph condensation by incorporating structural priors and class-level signals across clients to generate global synthetic subgraphs rather than a single-graph setting.

### 🔗 Related Problem

**FedGen: Data-Free Knowledge Distillation for Heterogeneous Federated Learning** (2021)
- *Authors:* Zhu et al.
- *Direct Connection:* FedLoG adopts the principle that server-generated, class-conditioned synthetic data can mitigate non-IID label shift, but instantiates it for graphs by synthesizing subgraphs with explicit structural information.

---

## Synthesis: How Prior Work Led to This Paper

Dataset condensation showed that a small synthetic dataset can be optimized to match the training dynamics of real data via gradient or feature matching, providing a template for compact, class-aware data surrogates. Graph condensation then adapted this principle to graphs, explicitly encoding structural priors to produce synthetic graphs that preserve task-relevant topology and features. In federated learning with heterogeneous clients, prototype-based methods demonstrated that sharing class-wise representations can be both communication-efficient and privacy-preserving, enabling global aggregation of label-conditioned knowledge without raw data exchange. Complementarily, data-free distillation methods for federated learning established that server-side, class-conditioned synthetic data can mitigate non-IID label shift by supplying clients with absent labels. Within graph federated learning, scalable subgraph-centric training such as FedSage+ illustrated the practicality of local subgraph training while exposing its susceptibility to local overfitting under distributional drift. The FedGraphNN benchmark formalized common tasks and protocols for federated GNNs, solidifying the problem setting these techniques target. Together, these works revealed an opportunity to combine class-wise prototypical knowledge sharing with structure-aware dataset condensation, suggesting a server synthesis mechanism that constructs global, class-conditioned subgraphs; such synthetic subgraphs can be broadcast to clients to counteract label imbalance and mutable graph dynamics, naturally addressing local overfitting while remaining communication- and privacy-conscious.

---

*Analysis generated on: 2026-01-06T17:02:39.673456*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
