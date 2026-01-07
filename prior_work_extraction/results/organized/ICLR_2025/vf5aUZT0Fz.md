# Prior Work Analysis Report

## Target Paper

**Title:** DEPT: Decoupled Embeddings for Pre-training Language Models

**Conference:** ICLR 2025 (oral)

**Authors:** Alex Iacob, Lorenzo Sani, Meghdad Kurmanji, William F. Shen, Xinchi Qiu, Dongqi Cai, Yan Gao, Nicholas Donald Lane

**Keywords:** Decentralized Training, Federated Learning, Multi-domain Training, Multilingual Training

**Abstract:** 
> Language Model pre-training uses broad data mixtures to enhance performance across domains and languages. However, training on such heterogeneous text corpora requires extensive and expensive efforts. Since these data sources vary significantly in lexical, syntactic, and semantic aspects, they cause negative interference or the ``curse of multilinguality''. To address these challenges we propose a communication-efficient pre-training framework, DEPT. Our method decouples embeddings from the tran...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Communication-Efficient Learning of Deep Networks from Decentralized Data (FedAvg)** (2017)
- *Authors:* Brendan McMahan et al.
- *Direct Connection:* FedAvg formalizes the round-based communication model that DEPT exploits by keeping large per-source embedding parameters local and only communicating the shared body, reducing communication in proportion to embedding size.

### 💡 Inspiration

**ALBERT: A Lite BERT for Self-supervised Learning of Language Representations** (2019)
- *Authors:* Zhenzhong Lan et al.
- *Direct Connection:* ALBERT’s factorized embedding parameterization showed that input embeddings can be decoupled from the transformer hidden size, inspiring DEPT’s further decoupling of token embeddings as modular, source-specific components.

**MAD-X: An Adapter-based Framework for Multilingual Transfer** (2020)
- *Authors:* Jonas Pfeiffer et al.
- *Direct Connection:* MAD-X shows that small language-specific modules attached to a shared transformer can mitigate interference across languages, informing DEPT’s choice to modularize token embeddings while sharing the transformer body.

### 🔍 Gap Identification

**The Curse of Multilinguality in Multilingual Neural Machine Translation** (2019)
- *Authors:* Naveen Arivazhagan et al.
- *Direct Connection:* This work documents performance degradation when scaling to many languages with a single shared vocabulary/model, directly motivating DEPT’s design to avoid a shared vocabulary and mitigate cross-source interference.

**ByT5: Towards a token-free future for text** (2022)
- *Authors:* Linting Xue et al.
- *Direct Connection:* ByT5 demonstrates that dropping a shared subword vocabulary can help multilingual robustness but incurs significant computational cost, highlighting the need for a more efficient alternative that DEPT achieves via decoupled subword embeddings.

### 📊 Baseline

**Unsupervised Cross-lingual Representation Learning at Scale** (2020)
- *Authors:* Alexis Conneau et al.
- *Direct Connection:* XLM-R establishes the shared-vocabulary, fully shared-parameter multilingual pre-training paradigm that DEPT replaces by keeping a shared transformer body while decoupling per-source token embeddings.

### 🔧 Extension

**Exploiting Shared Representations for Personalized Federated Learning (FedRep)** (2021)
- *Authors:* Collins et al.
- *Direct Connection:* FedRep’s split of a globally shared representation with small personalized modules is directly generalized in DEPT by treating token embeddings as per-source modules while synchronizing only the shared transformer body.

---

## Synthesis: How Prior Work Led to This Paper

XLM-R established the dominant approach to multilingual pre-training by sharing both a subword vocabulary and all model parameters across languages, achieving strong cross-lingual transfer but locking languages into one lexical space. Arivazhagan et al. showed that such sharing can degrade performance as the number of languages grows, highlighting a "curse of multilinguality" rooted in interference. ALBERT demonstrated that input embeddings need not be tightly coupled to the transformer hidden size by factorizing and projecting embeddings, revealing embeddings as a separable, parameter-dominant component. In federated settings, FedAvg defined round-based synchronization where communication scales with model size, while FedRep showed that sharing a global representation and keeping small personalized modules local improves robustness under heterogeneity and reduces communication. ByT5 removed shared vocabularies entirely via byte-level modeling, proving robustness without a shared lexicon but at notable computational cost. MAD-X further evidenced that small, language-specific modules added to a shared transformer can curb cross-language interference without full parameter duplication.
Taken together, these works imply that the primary locus of heterogeneity lies in the lexical interface and that embeddings are both separable and communication-heavy. The natural next step is to share only the transformer body for generalization while keeping per-source lexical modules local, avoiding a shared vocabulary and reducing communication by not syncing large embedding tables. Building on ALBERT’s decoupling insight, FedRep’s split-sharing strategy, and multilingual findings on interference and vocabulary design, the current work operationalizes a decoupled-embedding framework that robustly trains across heterogeneous domains and languages with communication savings aligned to embedding size.

---

*Analysis generated on: 2026-01-06T09:37:03.362726*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
