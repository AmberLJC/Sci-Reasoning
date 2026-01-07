# Prior Work Analysis Report

## Target Paper

**Title:** GeSubNet: Gene Interaction Inference for Disease Subtype Network Generation

**Conference:** ICLR 2025 (oral)

**Authors:** Ziwei Yang, Zheng Chen, Xin Liu, Rikuto Kotoge, Peng Chen, Yasuko Matsubara, Yasushi Sakurai, Jimeng Sun

**Keywords:** Gene Functional Networks, Disease Subtypes, Bioinformatics

**Abstract:** 
> Retrieving gene functional networks from knowledge databases presents a challenge due to the mismatch between disease networks and subtype-specific variations. Current solutions, including statistical and deep learning methods, often fail to effectively integrate gene interaction knowledge from databases or explicitly learn subtype-specific interactions. To address this mismatch, we propose GeSubNet, which learns a unified representation capable of predicting gene interactions while distinguishi...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The joint graphical lasso for inverse covariance estimation across multiple classes** (2014)
- *Authors:* Danaher et al.
- *Direct Connection:* GeSubNet operationalizes the joint estimation principle from the joint graphical lasso by learning a shared embedding that separates common from subtype-specific gene interactions across disease subtypes.

**Network-based stratification of tumor mutations** (2013)
- *Authors:* Hofree et al.
- *Direct Connection:* GeSubNet builds on the NBS insight that integrating patient molecular profiles with interaction networks improves disease subtyping, unifying subtype discovery with interaction-aware graph representation learning.

### 💡 Inspiration

**Variational Deep Embedding: An Unsupervised and Generative Approach to Clustering (VaDE)** (2017)
- *Authors:* Jiang et al.
- *Direct Connection:* GeSubNet adopts VaDE’s core idea of using a deep generative model with a discrete latent structure to discover disease subtypes directly from gene expression profiles.

### 📊 Baseline

**Passing messages between biological networks to refine predicted interactions (PANDA)** (2013)
- *Authors:* Glass et al.
- *Direct Connection:* GeSubNet generalizes PANDA’s knowledge-integrating strategy by encoding curated gene-interaction networks with a GNN so that physical interactions explicitly constrain subtype-specific edge prediction.

**Estimating sample-specific regulatory networks (LIONESS)** (2019)
- *Authors:* Kuijjer et al.
- *Direct Connection:* GeSubNet addresses LIONESS’s sample-specific network derivation from aggregate models by jointly learning a unified representation that yields subtype-specific networks while leveraging prior interaction knowledge.

### 🔧 Extension

**Variational Graph Auto-Encoders** (2016)
- *Authors:* Kipf et al.
- *Direct Connection:* GeSubNet extends the VGAE concept of GNN-based node embeddings for edge reconstruction by conditioning the graph encoder on curated gene-interaction priors and coupling it with subtype embeddings for interaction prediction.

---

## Synthesis: How Prior Work Led to This Paper

PANDA introduced a principled way to integrate prior biological interaction knowledge with gene expression to reconstruct regulatory networks, demonstrating that curated PPIs and motif data can anchor data-driven edge inference. LIONESS showed how to derive individualized networks from population-level reconstructions, providing a route toward context-specific interaction maps but relying on post hoc sample deconvolution rather than joint learning. The joint graphical lasso formalized simultaneous estimation of multiple related class-specific networks via shared structure, highlighting a need for representations that capture both common and condition-specific edges. VaDE established a deep generative framework in which a discrete latent variable discovers clusters directly from data, yielding robust unsupervised subtype discovery. Variational Graph Auto-Encoders demonstrated that GNN encoders can learn node embeddings whose inner products reconstruct graph edges, offering a flexible mechanism for link prediction conditioned on graph structure. Network-Based Stratification revealed that patient subtyping improves when molecular profiles are coupled to protein interaction networks, underscoring the value of network priors in stratification.
Together these works expose an opportunity: jointly discover disease subtypes while inferring subtype-specific gene interactions grounded in known physical networks. GeSubNet synthesizes VaDE-style generative subtyping with VGAE-inspired graph encoding, uses PANDA’s knowledge-integration principle to preserve physical interactions, and adopts the joint-estimation spirit of the graphical lasso to separate shared versus subtype-specific edges, thereby overcoming LIONESS’s post hoc limitation and NBS’s lack of gene-level interaction prediction.

---

*Analysis generated on: 2026-01-06T12:10:49.066256*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
