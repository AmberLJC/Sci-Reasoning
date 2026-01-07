# Prior Work Analysis Report

## Target Paper

**Title:** Knowledge Entropy Decay during Language Model Pretraining Hinders New Knowledge Acquisition

**Conference:** ICLR 2025 (oral)

**Authors:** Jiyeon Kim, Hyunji Lee, Hyowon Cho, Joel Jang, Hyeonbin Hwang, Seungpil Won, Youbin Ahn, Dohaeng Lee, Minjoon Seo

**Keywords:** knowledge entropy, knowledge acquisition and forgetting, evolving behavior during LLM pretraining

**Abstract:** 
> In this work, we investigate how a model's tendency to broadly integrate its parametric knowledge evolves throughout pretraining, and how this behavior affects overall performance, particularly in terms of knowledge acquisition and forgetting. We introduce the concept of knowledge entropy, which quantifies the range of memory sources the model engages with; high knowledge entropy indicates that the model utilizes a wide range of memory sources, while low knowledge entropy suggests reliance on sp...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Geva et al.
- *Direct Connection:* By formalizing MLP layers as discrete key–value memory slots, this work provides the mechanistic basis for treating a language model’s internal modules as distinct “memory sources,” which the current paper aggregates into its knowledge-entropy measure.

**Language Models as Knowledge Bases?** (2019)
- *Authors:* Petroni et al.
- *Direct Connection:* This paper established factual probing as a concrete way to evaluate parametric knowledge, underpinning the current paper’s formulation of knowledge acquisition/retention metrics that are tracked as entropy evolves during pretraining.

### 💡 Inspiration

**In-Context Learning and Induction Heads** (2022)
- *Authors:* Olsson et al.
- *Direct Connection:* By revealing stagewise changes and specialization of transformer heads during training, this work directly motivates analyzing how the breadth of active mechanisms evolves, leading to the current paper’s notion and measurement of knowledge-entropy decay.

**Locating and Editing Factual Associations in GPT** (2022)
- *Authors:* Meng et al.
- *Direct Connection:* Demonstrating that specific factual knowledge localizes to narrow subcircuits (and can be edited there) directly informs the hypothesis that over time models rely on fewer, more specific memory sources—exactly what the current work quantifies as entropy decline.

### 🔍 Gap Identification

**Don't Stop Pretraining: Adapt Language Models to Domains and Tasks** (2020)
- *Authors:* Gururangan et al.
- *Direct Connection:* Observations from continued pretraining about domain adaptation and emergent forgetting highlight the stability–plasticity tension, a gap the current paper addresses by identifying knowledge-entropy decay as a mechanistic correlate of reduced plasticity.

### 🔗 Related Problem

**Generalization through Memorization: Nearest Neighbor Language Models** (2020)
- *Authors:* Khandelwal et al.
- *Direct Connection:* Showing that augmenting LMs with an external kNN datastore broadens usable memory and boosts factual recall provides a concrete mechanism the current paper cites when testing whether increasing active memory sources reverses low-entropy-induced acquisition failures.

**Retrieval-Augmented Generation for Knowledge-Intensive NLP** (2020)
- *Authors:* Lewis et al.
- *Direct Connection:* By explicitly adding a non-parametric memory to complement parametric knowledge, this work operationalizes the idea of activating more memory sources, which the current paper leverages to validate that higher knowledge entropy improves acquisition and retention.

---

## Synthesis: How Prior Work Led to This Paper

Feed-forward layers in transformers have been shown to operate as key–value memories, implying that knowledge can be viewed as distributed across discrete parametric memory slots rather than being homogeneously smeared across weights. Factual probing revealed that language models store and retrieve real-world facts directly from these parameters, establishing a concrete evaluation paradigm for knowledge access and change. Training-time analyses uncovered stagewise emergence and specialization of mechanisms such as induction heads, indicating that the set of active computational pathways evolves over training. Complementarily, causal editing of factual associations showed that specific facts often localize to narrow subcircuits, suggesting that models can come to rely on increasingly specific loci of memory. On the augmentation side, nearest-neighbor LMs demonstrated that adding an external datastore substantially expands usable memory and improves factual recall, while retrieval-augmented generation explicitly combines parametric and non-parametric sources to broaden the evidence pool for answering knowledge-intensive queries. Meanwhile, continued pretraining studies documented both gains and instances of forgetting, foregrounding a stability–plasticity trade-off without a clear mechanistic account. Taken together, these works reveal that (i) parametric knowledge resides in identifiable memory-like structures, (ii) training induces mechanism specialization, and (iii) expanding accessible memory sources improves factual performance. The natural next step is to quantify how widely a model engages its available memory sources over pretraining and to test whether that breadth governs plasticity. By defining and tracking knowledge entropy, and by experimentally increasing active memory sources via retrieval-style augmentation, the present work synthesizes these insights into a mechanistic explanation for knowledge acquisition and forgetting.

---

*Analysis generated on: 2026-01-06T06:10:19.327256*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
