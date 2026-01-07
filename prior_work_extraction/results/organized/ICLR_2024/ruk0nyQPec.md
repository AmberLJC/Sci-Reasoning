# Prior Work Analysis Report

## Target Paper

**Title:** SILO Language Models: Isolating Legal Risk In a Nonparametric Datastore

**Conference:** ICLR 2024 (spotlight)

**Authors:** Sewon Min, Suchin Gururangan, Eric Wallace, Weijia Shi, Hannaneh Hajishirzi, Noah A. Smith, Luke Zettlemoyer

**Keywords:** language modeling; retrieval; legality of language modeling

**Abstract:** 
> The legality of training language models (LMs) on copyrighted or otherwise restricted data is under intense debate. However, as we show, model performance significantly degrades if trained only on low-risk text (e.g., out-of-copyright books or government documents), due to its limited size and domain coverage. We present SILO, a new language model that manages this risk-performance tradeoff during inference. SILO is built by (1) training a parametric LM on the Open License Corpus (OLC), a new co...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Retrieval-Augmented Generation for Knowledge-Intensive NLP** (2020)
- *Authors:* Patrick Lewis et al.
- *Direct Connection:* By establishing the paradigm of conditioning generation on an external, updateable corpus queried at inference, RAG provides the foundational retrieval-before-generation framework that SILO repurposes for next-token LMing and legal risk separation.

**The Pile: An 800GB Dataset of Diverse Text for Language Modeling** (2021)
- *Authors:* Leo Gao et al.
- *Direct Connection:* The Pile’s curated mixture established practices for large-scale LM pretraining corpora and highlighted licensing heterogeneity, which SILO addresses by constructing the Open License Corpus as a license-clean alternative.

**Dolma: An Open Corpus of Three Trillion Tokens for Language Model Pretraining** (2023)
- *Authors:* Luca Soldaini et al.
- *Direct Connection:* Dolma’s emphasis on transparent sourcing and permissive licensing informed SILO’s OLC curation strategy and underscored the resulting coverage gaps that SILO compensates for via a high-risk nonparametric datastore.

### 💡 Inspiration

**Nearest Neighbor Machine Translation** (2021)
- *Authors:* Urvashi Khandelwal et al.
- *Direct Connection:* SILO draws on kNN-MT’s demonstration that swapping or editing an external datastore enables test-time controllability, leveraging this property to support opt-out and post-hoc removal of specific copyrighted content without retraining.

### 🔍 Gap Identification

**Extracting Training Data from Large Language Models** (2021)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* Evidence that LMs memorize and can regurgitate verbatim training text directly motivates SILO’s central design choice to avoid training on copyrighted/high-risk data and instead access it only via a queryable datastore with attribution.

### 🔧 Extension

**Generalization through Memorization: Nearest Neighbor Language Models** (2020)
- *Authors:* Urvashi Khandelwal et al.
- *Direct Connection:* SILO directly extends the kNN-LM idea by using an inference-only key–value datastore, but crucially populates it with high-risk text while training the base LM solely on open-licensed data to isolate legal risk and enable provenance.

### 🔗 Related Problem

**Improving language models by retrieving from trillions of tokens (RETRO)** (2022)
- *Authors:* Sebastian Borgeaud et al.
- *Direct Connection:* RETRO showed that much of an LM’s knowledge can be externalized in a separate retrieval database, a principle SILO adopts to keep high-risk data out of training and access it only through a modifiable nonparametric store at inference.

---

## Synthesis: How Prior Work Led to This Paper

Nearest Neighbor Language Models introduced a simple, powerful mechanism to combine a parametric LM with a nonparametric key–value datastore at inference, allowing predictions to be mixed with a kNN distribution grounded in concrete source tokens. Nearest Neighbor Machine Translation showed that such datastores can be swapped or edited at test time for domain adaptation, proving their practical controllability. RETRO demonstrated that large-scale knowledge can reside primarily in an external retrieval database while still yielding strong LM performance, suggesting that knowledge and parameters can be decoupled. Retrieval-Augmented Generation established the general recipe of querying an external, updateable corpus to condition generation, making provenance and dynamic updates natural. In parallel, work on extracting training data from LMs revealed significant memorization and verbatim regurgitation risks, surfacing concrete copyright and privacy concerns. The Pile provided a blueprint for diverse pretraining mixtures while revealing licensing heterogeneity, and Dolma advanced transparent, licensing-aware corpus construction while acknowledging remaining gaps in coverage and domain breadth. Together, these strands exposed a gap: training on license-clean data alone hurts performance, yet training on risky data creates legal exposure. SILO synthesizes the kNN-style inference-only datastore with retrieval-augmented modeling to keep high-risk data entirely outside training, querying it only at inference. This preserves performance via retrieval, enables sentence-level attribution and opt-out by editing the datastore, and grounds a practical path for legal-risk isolation while leveraging license-clean pretraining on OLC.

---

*Analysis generated on: 2026-01-06T13:57:19.389311*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
