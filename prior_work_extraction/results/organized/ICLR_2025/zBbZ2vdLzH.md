# Prior Work Analysis Report

## Target Paper

**Title:** Joint Graph Rewiring and Feature Denoising via Spectral Resonance

**Conference:** ICLR 2025 (oral)

**Authors:** Jonas Linkerhägner, Cheng Shi, Ivan Dokmanić

**Keywords:** GNNs, Rewiring, Denoising, Spectral Resonance, cSBM

**Abstract:** 
> When learning from graph data, the graph and the node features both give noisy information about the node labels. In this paper we propose an algorithm to **j**ointly **d**enoise the features and **r**ewire the graph (JDR), which improves the performance of downstream node classification graph neural nets (GNNs). JDR works by aligning the leading spectral spaces of graph and feature matrices. It approximately solves the associated non-convex optimization problem in a way that handles graphs with...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**How to Learn a Graph from Smooth Signals** (2016)
- *Authors:* V. Kalofolias
- *Direct Connection:* By formulating topology learning as choosing a graph whose Laplacian makes observed node features smooth, this work provides the optimization lens that JDR extends from smoothness to explicit spectral-space alignment for joint graph rewiring and feature denoising.

### 💡 Inspiration

**Covariate-Assisted Spectral Clustering** (2017)
- *Authors:* M. Binkiewicz et al.
- *Direct Connection:* CASC showed that combining adjacency and covariate similarity in a joint spectral objective improves community recovery under contextual SBMs, directly inspiring JDR’s explicit alignment of leading eigenspaces of graph and feature matrices to guide rewiring and denoising.

**Simplifying Graph Convolutional Networks** (2019)
- *Authors:* F. Wu et al.
- *Direct Connection:* The Jaccard-based preprocessing heuristic prunes edges between nodes with dissimilar features, suggesting that structure–feature agreement should guide rewiring—a principle JDR formalizes by aligning leading spectral spaces rather than local pairwise similarities.

### 🔍 Gap Identification

**Learning Discrete Structures for Graph Neural Networks** (2019)
- *Authors:* A. Franceschi et al.
- *Direct Connection:* LDS demonstrated that bilevel optimization can learn task-specific graph structure but is label-dependent and computationally heavy, motivating JDR’s unsupervised, closed-form spectral alignment as a scalable alternative for structure refinement.

**Beyond Homophily in Graph Neural Networks: Current Limitations and Effective Designs** (2020)
- *Authors:* Z. Zhu et al.
- *Direct Connection:* By pinpointing failures of smoothing-based GNNs and many rewiring techniques on heterophilous graphs and advocating frequency-aware designs, this work motivates JDR’s spectrum-alignment approach that remains effective across homophily and heterophily regimes.

### 📊 Baseline

**Diffusion Improves Graph Learning** (2019)
- *Authors:* J. Klicpera et al.
- *Direct Connection:* GDC is a primary rewiring baseline that reweights edges via PPR/heat diffusion without using node attributes, a limitation JDR overcomes by steering rewiring through graph–feature spectral alignment.

**Graph Structure Learning for Robust Graph Neural Networks (Pro-GNN)** (2020)
- *Authors:* W. Jin et al.
- *Direct Connection:* Pro-GNN jointly infers a clean graph using low-rank and sparsity with feature-smoothness regularization, whose homophily bias JDR addresses by aligning spectral subspaces to accommodate multi-class settings and heterophily while denoising features.

---

## Synthesis: How Prior Work Led to This Paper

Covariate-Assisted Spectral Clustering established that incorporating node attributes by mixing covariate similarity with adjacency in a spectral objective can significantly improve community detection under contextual SBMs, highlighting the value of matching structural and attribute spectra. Complementing this, Kalofolias framed graph topology learning as finding a graph on which observed features are smooth, providing an optimization perspective for turning noisy attributes into graph-aware signals. Diffusion-based rewiring via personalized PageRank or heat kernels emerged as a strong, practical way to refine topology, albeit without leveraging node features. Bilevel graph structure learning further showed that task-driven topology inference is powerful but computationally demanding and dependent on labels. Robust GSL methods like Pro-GNN pursued joint graph recovery using low-rank and sparsity with feature smoothness priors, implicitly assuming homophily. Simple Jaccard pruning revealed that even heuristic, feature-guided edge edits can enhance learning by enforcing agreement between structure and attributes. Finally, the heterophily literature documented how smoothing-centric GNNs and many rewiring strategies falter when signal resides in higher frequencies, calling for frequency-aware alignment between features and graph. Against this backdrop, it was natural to synthesize a feature-aware, unsupervised alternative to diffusion and heavy bilevel GSL: align the leading spectral spaces of graph and feature matrices to guide both edge rewiring and feature denoising. This unifies CASC’s spectral fusion with signal-driven topology ideas, while addressing heterophily by aligning spectra rather than enforcing smoothness, and yields a scalable pre-processing that subsumes heuristic pruning and improves over feature-agnostic diffusion.

---

*Analysis generated on: 2026-01-06T08:34:05.406774*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
