# Prior Work Analysis Report

## Target Paper

**Title:** From Bricks to Bridges: Product of Invariances to Enhance Latent Space Communication

**Conference:** ICLR 2024 (spotlight)

**Authors:** Irene Cannistraci, Luca Moschella, Marco Fumero, Valentino Maiorca, Emanuele Rodolà

**Keywords:** invariance, latent space, latent comunication, zero-shot stitching, representation learning, relative representation

**Abstract:** 
> It has been observed that representations learned by distinct neural networks conceal structural similarities when the models are trained under similar inductive biases. From a geometric perspective, identifying the classes of transformations and the related invariances that connect these representations is fundamental to unlocking applications, such as merging, stitching, and reusing different neural modules. However, estimating task-specific transformations a priori can be challenging and expe...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Understanding image representations by measuring their equivariance and equivalence** (2015)
- *Authors:* Karel Lenc et al.
- *Direct Connection:* This work introduced the idea of ‘stitching’ layers from different networks via a learned linear connector to test representation equivalence, defining the core problem of cross-model latent communication that is generalized here without training.

### 💡 Inspiration

**Similarity of Neural Network Representations Revisited** (2019)
- *Authors:* Simon Kornblith et al.
- *Direct Connection:* By proposing CKA and analyzing its invariance to orthogonal transformations and isotropic scaling, this work supplies the key insight that invariant components (e.g., Gram-based signals) can robustly capture cross-model representational commonality.

**Prevalence of Neural Collapse during the terminal phase of deep learning** (2020)
- *Authors:* Vardan Papyan et al.
- *Direct Connection:* Neural Collapse shows penultimate features converge to a simplex ETF up to rotation and scaling, pinpointing specific invariances that different networks share and should be encoded to enable cross-model stitching.

### 🔍 Gap Identification

**Git Re-Basin: Merging Models Modulo Permutation Symmetries** (2023)
- *Authors:* Evan L. Ainsworth et al.
- *Direct Connection:* By addressing permutation symmetries to merge models in weight space, this work exposes the limitation of handling a single invariance class and motivates a latent-space approach that composes broader invariances without explicit alignment.

### 📊 Baseline

**Revisiting Model Stitching to Compare Generalization across Neural Networks** (2021)
- *Authors:* Bansal et al.
- *Direct Connection:* This paper established model stitching with trainable linear adapters as a practical mechanism to assess and enable interchangeability of layers, providing the primary baseline whose data- and training-dependent connectors are replaced by zero-shot invariance-based components.

### 🔧 Extension

**SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability** (2017)
- *Authors:* Maithra Raghu et al.
- *Direct Connection:* SVCCA aligns representations up to subspace transformations, directly inspiring the idea of explicitly factoring out classes of transformations—here extended by composing multiple invariances into a single latent product space.

### 🔗 Related Problem

**Relational Knowledge Distillation** (2019)
- *Authors:* Wonpyo Park et al.
- *Direct Connection:* This paper operationalizes pairwise relational signals (distances/angles) as architecture-agnostic targets, directly informing the use of relational, transformation-invariant components within a composite latent representation.

---

## Synthesis: How Prior Work Led to This Paper

Lenc and Vedaldi established that modules from different networks can be interchanged by inserting a learned linear connector, concretely framing representation equivalence and the practical act of ‘stitching’ between latent spaces. Bansal and colleagues advanced this by systematically using trainable linear adapters to measure interchangeability across independently trained models, showing that a learned connector can make disparate features compatible but at the cost of data and optimization. Raghu’s SVCCA demonstrated that representations can be compared after factoring out subspace transformations, while Kornblith’s CKA highlighted that robust similarity arises from invariance to orthogonal transformations and isotropic scaling, suggesting Gram/relational components as stable cross-model signals. Papyan’s Neural Collapse revealed that class features tend toward a simplex ETF geometry up to rotation and scaling, pinpointing concrete invariances prevalent in well-trained networks. In weight space, Ainsworth’s Git Re-Basin targeted permutation symmetries to merge models, underscoring the importance—but also the narrowness—of handling only one invariance class. Park’s Relational KD showed that pairwise relational structure in features provides architecture-agnostic targets, reinforcing the utility of relative, transformation-invariant signals.
Together these works expose a gap: stitching typically requires training connectors or assumes a single known symmetry, while multiple latent invariances jointly govern cross-model compatibility. The natural next step is to explicitly encode a product of invariant components—combining relational and norm/angle/scale factors—directly in the latent space so that independently trained networks become interoperable without learning task-specific transformations, enabling consistent similarity and zero-shot stitching across models and tasks.

---

*Analysis generated on: 2026-01-06T07:18:15.672633*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
