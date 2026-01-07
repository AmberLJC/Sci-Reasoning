# Prior Work Analysis Report

## Target Paper

**Title:** Test-time Adaptation for Cross-modal Retrieval with Query Shift

**Conference:** ICLR 2025 (spotlight)

**Authors:** Haobin Li, Peng Hu, Qianjun Zhang, Xi Peng, XitingLiu, Mouxing Yang

**Keywords:** Test-time adaptation, Cross-modal retrieval, Query shift

**Abstract:** 
> The success of most existing cross-modal retrieval methods heavily relies on the assumption that the given queries follow the same distribution of the source domain. 
However, such an assumption is easily violated in real-world scenarios due to the complexity and diversity of queries, thus leading to the query shift problem.
Specifically, query shift refers to the online query stream originating from the domain that follows a different distribution with the source one.
In this paper, we observe ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere** (2020)
- *Authors:* Tongzhou Wang et al.
- *Direct Connection:* TCR’s diagnosis that query shift reduces within-modality scatter and its uniformity regularization are grounded in the alignment–uniformity framework introduced by this work.

### 💡 Inspiration

**Test-Time Training with Self-Supervision for Generalization under Distribution Shift** (2020)
- *Authors:* Yu Sun et al.
- *Direct Connection:* TCR adopts the core idea of leveraging self-supervised signals at test time, replacing TTT’s rotation pretext with retrieval-derived signals from the query’s own predictions to drive on-the-fly adaptation.

**Relevance Feedback in Information Retrieval (Rocchio Algorithm)** (1971)
- *Authors:* J. J. Rocchio
- *Direct Connection:* TCR’s query prediction refinement operationalizes pseudo-relevance feedback by using top-ranked gallery items to refine the query’s effective representation and guide test-time updates.

### 🔍 Gap Identification

**CoTTA: Continual Test-Time Adaptation** (2022)
- *Authors:* Wang et al.
- *Direct Connection:* By exposing the instability and catastrophic forgetting in continual TTA, CoTTA motivates TCR’s joint objective that explicitly prevents query-shift updates from corrupting the shared cross-modal embedding space.

### 📊 Baseline

**Learning Transferable Visual Models From Natural Language Supervision (CLIP)** (2021)
- *Authors:* Alec Radford et al.
- *Direct Connection:* TCR is built on and evaluated against CLIP-style contrastive image–text retrieval encoders, serving as the primary baseline whose retrieval performance degrades under query shift.

### 🔧 Extension

**Fully Test-Time Adaptation by Entropy Minimization** (2021)
- *Authors:* Dequan Wang et al.
- *Direct Connection:* TCR extends TENT’s entropy-minimization principle to the retrieval setting by optimizing confidence over a query’s ranked matches while constraining updates so adaptation on online queries does not distort the learned cross-modal space.

**Do We Really Need Source Data? Source Hypothesis Transfer for Unsupervised Domain Adaptation (SHOT)** (2020)
- *Authors:* Jian Liang et al.
- *Direct Connection:* TCR adapts SHOT’s information maximization/diversity idea to the retrieval scenario, preserving decision structure while updating features without source data by operating directly in the cross-modal embedding space.

---

## Synthesis: How Prior Work Led to This Paper

Entropy-based test-time adaptation demonstrated that models can self-correct to distribution shift by minimizing prediction uncertainty without access to source data, while test-time training showed that auxiliary self-supervision on the test stream can serve as an adaptation signal. Continual TTA highlighted that naively adapting online induces catastrophic forgetting and feature drift, requiring mechanisms that maintain stability as inputs evolve. Source-free adaptation via information maximization preserved decision structure by increasing output confidence and diversity, providing a way to adapt features without collapsing class structure. The alignment–uniformity view of contrastive learning formalized how representations should remain well-aligned across modalities yet uniformly dispersed within each modality, offering a quantitative lens for diagnosing and regularizing scatter. CLIP established the prevailing cross-modal embedding and retrieval formulation, against which shifts in query distribution materially degrade rankings. Classic pseudo-relevance feedback introduced the idea of refining queries using their own top retrieved results, turning initial predictions into a supervisory signal. Together, these works reveal an opportunity: retrieval systems need online, source-free adaptation that leverages retrieval outputs as self-supervision, yet safeguards the shared cross-modal space from drift and preserves within-modality uniformity. Building on these insights, the present work adapts entropy/info-max style objectives to the retrieval ranking signal, uses feedback from top matches to refine query predictions, and regularizes with alignment–uniformity constraints so that adaptation from streaming, shifted queries improves recall without disturbing the common embedding space.

---

*Analysis generated on: 2026-01-06T10:10:11.975049*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
