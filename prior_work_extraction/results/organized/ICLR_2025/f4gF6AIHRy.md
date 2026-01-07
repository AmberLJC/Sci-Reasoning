# Prior Work Analysis Report

## Target Paper

**Title:** Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection

**Conference:** ICLR 2025 (oral)

**Authors:** Ziqing Fan, Siyuan Du, Shengchao Hu, Pingjie Wang, Li Shen, Ya Zhang, Dacheng Tao, Yanfeng Wang

**Keywords:** file selection, large language model, pre-training, submodular optimization

**Abstract:** 
> Selecting high-quality pre-training data for large language models (LLMs) is crucial for enhancing their overall performance under limited computation budget, improving both training and sample efficiency. Recent advancements in file selection primarily rely on using an existing or trained proxy model to assess the similarity of samples to a target domain, such as high quality sources BookCorpus and Wikipedia. However, upon revisiting these methods, the domain-similarity selection criteria demon...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Intelligent Selection of Language Model Training Data** (2010)
- *Authors:* Robert C. Moore et al.
- *Direct Connection:* This work introduced domain-similarity data selection via cross-entropy difference, the canonical paradigm DiSF explicitly replaces to avoid the diversity collapse induced by selecting data too close to a target domain.

### 💡 Inspiration

**Submodular Optimization for Data Subset Selection in Machine Learning** (2015)
- *Authors:* Kai Wei et al.
- *Direct Connection:* This line of work demonstrates that greedy submodular objectives (e.g., facility location, log-det) produce diverse, representative data subsets in NLP and vision, directly informing DiSF’s use of submodular selection for diversity.

**VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning** (2021)
- *Authors:* Adrien Bardes et al.
- *Direct Connection:* VICReg’s anti-collapse principle of enforcing per-dimension variance and decorrelated features motivates DiSF’s objective of achieving more uniform eigenvalues in the selected data’s feature covariance.

### 🔍 Gap Identification

**Don’t Stop Pretraining: Adapt Language Models to Domains and Tasks** (2020)
- *Authors:* Suchin Gururangan et al.
- *Direct Connection:* By showing domain-adaptive pretraining boosts in-domain performance while harming general capabilities, this paper surfaces the exact trade-off (domain gains vs. broad generalization) that DiSF’s diversity-preserving selection is designed to fix.

**Deduplicating Training Data Makes Language Models Better** (2021)
- *Authors:* Katherine Lee et al.
- *Direct Connection:* By showing that redundancy and near-duplicates in pretraining corpora degrade performance, this work highlights the need for diversity-aware selection that DiSF achieves via decorrelation in feature space.

### 📊 Baseline

**DoReMi: Optimizing Data Mixtures for Language Model Pretraining** (2023)
- *Authors:* Xie et al.
- *Direct Connection:* DoReMi reweights sources using a proxy to match a target distribution (e.g., Wikipedia/Books), providing the primary similarity-driven baseline whose tendency to narrow the representation space DiSF counters with decorrelation-based submodular selection.

### 🔧 Extension

**Near-Optimal Sensor Placements in Gaussian Processes: Theory, Efficient Algorithms and Empirical Studies** (2008)
- *Authors:* Andreas Krause et al.
- *Direct Connection:* DiSF adapts the log-determinant information gain submodular objective (and its greedy 1−1/e maximization) from this work to select text files that maximize the volume of feature covariance, yielding decorrelated, diverse subsets.

---

## Synthesis: How Prior Work Led to This Paper

Early data selection for language modeling centered on domain similarity: Moore and Lewis proposed choosing sentences that minimize cross-entropy difference to a target domain, a strategy that later became ubiquitous. Gururangan and colleagues then showed that continued pretraining on in-domain data improves domain tasks but can erode broad generalization, exposing a central tension in domain-focused selection. DoReMi operationalized this paradigm at pretraining scale by learning mixture weights that align sources (e.g., Wikipedia/Books) to a target distribution using a proxy model, but its similarity-driven emphasis risks narrowing the representation space. In parallel, the submodular optimization literature established that greedy maximization of objectives like log-determinant yields diverse, representative subsets; Krause et al. provided the log-det information gain objective with strong guarantees, and Wei et al. demonstrated practical, scalable submodular subset selection for text. From representation learning, VICReg formalized anti-collapse via enforcing variance and decorrelation, while Lee et al. showed that redundancy in LM corpora harms performance, underscoring the value of diversity.
Taken together, these works reveal both the effectiveness and the pitfalls of similarity-driven selection and point to a remedy: explicitly manage representation diversity. The submodular toolbox offers a principled, efficient way to choose diverse sets, and anti-collapse objectives suggest what kind of diversity matters—uniform, decorrelated features. Building on these insights, the current paper replaces target-similarity scoring with a submodular, log-det-style decorrelation criterion over file features, using greedy maximization to equalize covariance eigenvalues and thereby prevent dimensional collapse while preserving broad capability.

---

*Analysis generated on: 2026-01-06T17:52:39.209294*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
