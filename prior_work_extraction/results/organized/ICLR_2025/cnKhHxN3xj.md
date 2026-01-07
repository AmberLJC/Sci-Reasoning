# Prior Work Analysis Report

## Target Paper

**Title:** Wasserstein Distances, Neuronal Entanglement, and Sparsity

**Conference:** ICLR 2025 (spotlight)

**Authors:** Shashata Sawmya, Linghao Kong, Ilia Markov, Dan Alistarh, Nir N Shavit

**Keywords:** Polysemanticity, Disentanglement, Wasserstein Distance, Sparsity, Large Language Models

**Abstract:** 
> Disentangling polysemantic neurons is at the core of many current approaches to interpretability of large language models. Here we attempt to study how disentanglement can be used to understand performance, particularly under weight sparsity, a leading post-training optimization technique. We suggest a novel measure for estimating neuronal entanglement: the Wasserstein distance of a neuron's output distribution to a Gaussian. Moreover, we show the existence of a small number of highly entangled ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Toy Models of Superposition** (2022)
- *Authors:* Elhage et al.
- *Direct Connection:* Formalizes how feature superposition leads to polysemantic neurons and predicts non-Gaussian activations under bottlenecks, motivating this paper’s use of a quantitative non-Gaussianity (Wasserstein-to-Gaussian) measure to identify and target entangled neurons.

**Calculation of the Wasserstein metric for probability distributions on the line** (1974)
- *Authors:* Vallender
- *Direct Connection:* Provides the one-dimensional formulation of Wasserstein distance via quantile functions, enabling the paper’s efficient computation of each neuron’s Wasserstein distance to a Gaussian as an entanglement metric.

### 💡 Inspiration

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Shazeer et al.
- *Direct Connection:* Introduces input-dependent expert routing, which directly inspires this paper’s neuron-level mixture-of-experts decomposition that replaces a highly entangled neuron with a mixture of lower-Wasserstein neurons conditioned on separated input regimes.

### 📊 Baseline

**SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot** (2023)
- *Authors:* Frantar et al.
- *Direct Connection:* Establishes one-shot LLM weight pruning as a primary post-training sparsity method, providing the baseline and motivating gap—lack of neuron-level entanglement awareness—that this paper addresses by singling out “Wasserstein neurons” crucial for accuracy under sparsity.

**Wanda: A Simple Method for Pruning LLMs** (2023)
- *Authors:* Sun et al.
- *Direct Connection:* Serves as a widely used pruning baseline whose weight/activation heuristics lack an explicit model of polysemantic entanglement, directly motivating the paper’s entanglement-aware analysis and interventions.

### 🔧 Extension

**Towards Monosemanticity: Decomposing Language Models with Dictionary Learning** (2023)
- *Authors:* Bricken et al.
- *Direct Connection:* Introduces sparse autoencoder/dictionary-learning methods to disentangle polysemantic neurons, which this paper directly extends by proposing a Wasserstein-based entanglement metric and an alternative disentangling mechanism that addresses SAEs’ failure to capture highly non-Gaussian, multi-function neurons.

---

## Synthesis: How Prior Work Led to This Paper

Sparse autoencoders for mechanistic interpretability showed that dictionary learning can decompose polysemantic neurons into more interpretable features, but they also revealed failure modes when activations are highly non-Gaussian or multi-function, leaving some features entangled (Bricken et al., 2023). Theoretical analysis of superposition argued that feature overlap under capacity constraints produces polysemantic neurons and predicts notably non-Gaussian activation patterns, identifying the need for quantitative measures of entanglement rooted in distributional shape (Elhage et al., 2022). In parallel, post-training pruning for large language models demonstrated that substantial weight sparsity is possible, yet current methods operate largely without an explicit notion of neuron-level entanglement or its effect on accuracy (Frantar et al., 2023; Sun et al., 2023). Separately, mixture-of-experts introduced input-dependent routing to multiple experts for conditional computation, offering a practical template for splitting complex behaviors across simpler components (Shazeer et al., 2017). Foundational optimal transport results provided closed-form and computationally tractable ways to compute Wasserstein distances on the real line, making it feasible to quantify departures from Gaussianity for neuron outputs at scale (Vallender, 1974). Taken together, these strands suggested a gap: interpretability techniques lacked a robust, distributional metric for entanglement closely tied to superposition theory and practically actionable for sparsity; pruning lacked neuron-level, entanglement-aware guidance; and MoE offered a natural mechanism to split polysemanticity. The present work synthesizes these insights by using Wasserstein-to-Gaussian distance to identify highly entangled neurons and by operationalizing disentanglement through neuron-level MoE decomposition, linking interpretability to performance under sparsity.

---

*Analysis generated on: 2026-01-06T07:59:36.728772*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
