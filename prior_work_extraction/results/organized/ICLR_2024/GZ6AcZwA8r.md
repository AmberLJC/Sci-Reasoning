# Prior Work Analysis Report

## Target Paper

**Title:** MMD Graph Kernel: Effective Metric Learning for Graphs via Maximum Mean Discrepancy

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yan Sun, Jicong Fan

**Keywords:** graph kernel, graph metric learning, maximum mean discrepancy

**Abstract:** 
> This paper focuses on graph metric learning. First, we present a class of maximum mean discrepancy (MMD) based graph kernels, called MMD-GK. These kernels are computed by applying MMD to the node representations of two graphs with message-passing propagation. 
Secondly, we provide a class of deep MMD-GKs that are able to learn graph kernels and implicit graph features adaptively in an unsupervised manner. Thirdly, we propose a class of supervised deep MMD-GKs that are able to utilize label infor...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**A Kernel Two-Sample Test** (2012)
- *Authors:* Arthur Gretton et al.
- *Direct Connection:* This work defines Maximum Mean Discrepancy (MMD) as an RKHS-based distance between empirical distributions, which the paper directly uses to measure similarity between the node-representation distributions of two graphs and to construct a positive-definite graph kernel.

**Kernel Mean Embedding of Distributions: A Review and Beyond** (2017)
- *Authors:* Krikamol Muandet et al.
- *Direct Connection:* The kernel mean embedding framework underpins the paper’s formulation of graphs as sets of node embeddings and justifies computing a valid kernel via inner products of empirical mean embeddings (and distances via MMD) between graphs.

**Weisfeiler-Lehman Graph Kernels** (2011)
- *Authors:* Nino Shervashidze et al.
- *Direct Connection:* The WL framework of iteratively refining node labels to build graph kernels provides the propagation paradigm that the paper adopts with continuous message-passing features and compares with via an MMD-based distributional matching.

### 💡 Inspiration

**Generative Moment Matching Networks** (2015)
- *Authors:* Yujia Li et al.
- *Direct Connection:* By learning deep feature maps under which MMD is computed, this work inspires the paper’s deep MMD-based graph kernels that adaptively learn both the kernel and the graph feature extractor in unsupervised and supervised settings.

### 🔍 Gap Identification

**Optimal Assignment Kernels for Attributed Graphs** (2016)
- *Authors:* Nils M. Kriege et al.
- *Direct Connection:* This work’s assignment-based graph similarities expose issues of indefiniteness and computational cost, directly motivating the paper’s use of MMD to compare node-embedding distributions in a PSD and scalable manner.

### 📊 Baseline

**Message Passing Graph Kernels** (2020)
- *Authors:* Giannis Nikolentzos et al.
- *Direct Connection:* As a primary competitor that embeds message passing directly into a kernel, this work motivates the paper’s key step of computing a distributional set-kernel over propagated node embeddings—here realized via MMD to yield a PSD, learnable metric.

### 🔧 Extension

**Propagation Kernels: Efficient Graph Kernels from Propagated Information** (2016)
- *Authors:* Marian Neumann et al.
- *Direct Connection:* This method compares graphs by iteratively propagating node information and matching distributions across iterations, which the paper generalizes by replacing histogram-based comparisons with MMD over continuous, message-passing node representations.

---

## Synthesis: How Prior Work Led to This Paper

Maximum Mean Discrepancy (MMD) introduced an RKHS-based discrepancy for comparing empirical distributions with strong statistical guarantees, and the kernel mean embedding program established that distributions can be represented as mean elements, yielding valid kernels and distances directly from samples. In graph similarity, Weisfeiler–Lehman kernels operationalized iterative refinement of node representations to derive powerful graph features, while propagation kernels extended this paradigm by diffusing attributes and comparing the evolving node-label distributions across iterations. Message Passing Graph Kernels further integrated message passing into the kernel computation, contrasting graphs via similarities between propagated node representations. In parallel, optimal assignment kernels compared node sets via matchings but raised practical issues of indefiniteness and computational cost. Orthogonally, Generative Moment Matching Networks demonstrated that MMD can be paired with learned deep feature maps to adapt distribution comparisons by optimizing the embedding under which MMD is measured.
These strands collectively suggested a natural opportunity: treat each graph as a distribution over its message-passing node embeddings and compare graphs via an RKHS distance on these distributions. MMD offers a principled, PSD, and sample-efficient way to perform this comparison, while deep parameterizations enable learning both the kernel and the feature map, with supervision further shaping discriminative metrics. The resulting synthesis resolves limitations of histogram or assignment matching, aligns with propagation-based kernels, and delivers adaptable, theoretically grounded graph metrics.

---

*Analysis generated on: 2026-01-06T15:38:43.859338*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
