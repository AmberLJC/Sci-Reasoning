# Prior Work Analysis Report

## Target Paper

**Title:** Graph Neural Networks for Learning Equivariant Representations of Neural Networks

**Conference:** ICLR 2024 (oral)

**Authors:** Miltiadis Kofinas, Boris Knyazev, Yan Zhang, Yunlu Chen, Gertjan J. Burghouts, Efstratios Gavves, Cees G. M. Snoek, David W. Zhang

**Keywords:** Deep weight space, Graph neural networks, Transformers, Permutation equivariance, Implicit neural representations, Networks for networks, Neural graphs

**Abstract:** 
> Neural networks that process the parameters of other neural networks find applications in domains as diverse as classifying implicit neural representations, generating neural network weights, and predicting generalization errors. However, existing approaches either overlook the inherent permutation symmetry in the neural network or rely on intricate weight-sharing patterns to achieve equivariance, while ignoring the impact of the network architecture itself. In this work, we propose to represent...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Deep Sets** (2017)
- *Authors:* Manzil Zaheer et al.
- *Direct Connection:* Deep Sets provided the theoretical characterization of permutation-invariant/equivariant mappings over exchangeable elements, underpinning the use of GNN/Transformer architectures to respect neuron/channel permutations when operating on weight tensors.

### 💡 Inspiration

**Git Re-Basin: Merging Models modulo Permutation Symmetry** (2023)
- *Authors:* Kyle Ainsworth et al.
- *Direct Connection:* By empirically showing that neuron/channel permutations leave network functions invariant and are crucial for weight-space operations, this paper directly motivates enforcing permutation equivariance when embedding neural network parameters.

### 🔍 Gap Identification

**Learning to learn by gradient descent by gradient descent** (2016)
- *Authors:* Marcin Andrychowicz et al.
- *Direct Connection:* This seminal L2O method achieved permutation symmetry via coordinate-wise weight sharing but ignored architectural connectivity, motivating the need for an explicitly architecture-aware, equivariant model over parameter graphs as proposed here.

### 📊 Baseline

**Functa: Data as Functions in the Space of Neural Networks** (2022)
- *Authors:* Emilien Dupont et al.
- *Direct Connection:* Functa treats implicit neural representations as points in weight space for classification and editing but assumes fixed parameter orderings/architectures, providing a primary baseline that lacks the explicit permutation equivariance and architecture-aware encoding introduced here.

### 🔧 Extension

**Graph HyperNetworks** (2018)
- *Authors:* Chris Zhang et al.
- *Direct Connection:* This work introduced representing neural architectures as computational graphs and using a GNN over those graphs to generate weights, which the current paper directly extends by feeding parameter-annotated computational graphs to a GNN/Transformer to learn permutation-equivariant representations rather than generate weights.

**Parameter Prediction for Unseen Deep Architectures (GHN-2)** (2021)
- *Authors:* Boris Knyazev et al.
- *Direct Connection:* GHN-2 demonstrated that a single GNN operating on computational graphs can generalize across diverse, unseen architectures, a capability the current paper adapts to process weight graphs and maintain neuron-permutation equivariance across architectures.

---

## Synthesis: How Prior Work Led to This Paper

Graph HyperNetworks established that neural architectures can be encoded as computational graphs and that a graph neural network can operate on this structure to generate parameters, inaugurating the ‘networks-for-networks’ paradigm. GHN-2 further showed that message passing over computational graphs enables strong generalization to unseen architectures, indicating that graph-based processing can handle architectural diversity. Deep Sets provided the formal basis for designing permutation-invariant and -equivariant mappings over exchangeable elements, a property directly relevant to neurons and channels whose permutations leave function unchanged. Git Re-Basin rigorously demonstrated the practical importance of neuron/channel permutation symmetries in weight space, revealing that respecting these symmetries is essential for meaningful weight-space operations. In parallel, Learning to learn by gradient descent by gradient descent achieved symmetry via coordinate-wise parameter sharing but neglected architectural connectivity, exposing the limitations of weight-sharing heuristics. Functa treated implicit neural representations as objects in weight space for classification and editing, showing the promise of operating directly on network parameters but without explicit symmetry handling or architectural variability. Together, these works suggest the opportunity to encode neural networks as parameter-annotated computational graphs and to learn representations that are inherently equivariant to neuron permutations while remaining architecture-aware. The natural synthesis is to employ GNNs/graph Transformers that preserve permutation symmetry to process diverse architectures’ parameter graphs, yielding a unified, symmetry-respecting encoder that enables tasks such as INR classification/editing, generalization prediction, and learned optimization across heterogeneous network families.

---

*Analysis generated on: 2026-01-06T08:22:47.754135*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
