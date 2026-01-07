# Prior Work Analysis Report

## Target Paper

**Title:** Adaptive Chameleon  or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jian Xie, Kai Zhang, Jiangjie Chen, Renze Lou, Yu Su

**Keywords:** Large Langugage Model, Knowledge Conflict, Tool Augmentation

**Abstract:** 
> By providing external information to large language models (LLMs), tool augmentation (including retrieval augmentation) has emerged as a promising solution for addressing the limitations of LLMs' static parametric memory.
However, how receptive are LLMs to such external evidence, especially when the evidence conflicts with their parametric memory? 
We present the first comprehensive and controlled investigation into the behavior of LLMs when encountering knowledge conflicts.
We propose a systema...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** (2020)
- *Authors:* Patrick Lewis et al.
- *Direct Connection:* RAG formalized injecting retrieved evidence into generation to overcome static parametric memory, providing the core tool-augmentation setting whose conflict dynamics this paper isolates and scrutinizes.

**Improving Language Models by Retrieving from Trillions of Tokens** (2022)
- *Authors:* Sebastian Borgeaud et al.
- *Direct Connection:* RETRO explicitly frames parametric versus non-parametric memory and demonstrates large gains from retrieval, motivating this work’s controlled tests of how LLMs arbitrate between internal knowledge and external evidence when they disagree.

**Toolformer: Language Models Can Teach Themselves to Use Tools** (2023)
- *Authors:* Timo Schick et al.
- *Direct Connection:* By establishing the broader tool-augmentation paradigm where LMs condition on tool outputs as external context, Toolformer provides the operational backdrop for analyzing LMs’ receptivity to conflicting external evidence.

### 💡 Inspiration

**Locating and Editing Factual Associations in GPT** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* The construction of targeted counterfactuals (CounterFact) to probe and manipulate model beliefs directly inspires this paper’s ‘counter-memory’ design for generating controlled conflicts against elicited parametric facts.

### 🔍 Gap Identification

**Lost in the Middle: How Language Models Use Long Context** (2023)
- *Authors:* Nelson F. Liu et al.
- *Direct Connection:* Their finding that LLMs often underutilize provided context motivates this work’s controlled analysis of when coherent and convincing external evidence can override entrenched parametric memory.

### 🔧 Extension

**Language Models as Knowledge Bases?** (2019)
- *Authors:* Fabio Petroni et al.
- *Direct Connection:* Their LAMA probing paradigm for eliciting high-precision parametric facts directly underpins this paper’s systematic procedure for extracting a model’s internal (‘parametric’) memory before introducing conflicts.

---

## Synthesis: How Prior Work Led to This Paper

Retrieval-augmented generation established a practical mechanism for injecting retrieved documents into language model decoding to remedy the limits of static parametric memory, and follow-on work like RETRO sharpened the conceptual split between parametric and non-parametric memory by showing that large external corpora can be decisive for factual accuracy. Toolformer broadened this notion into a general tool-augmentation paradigm in which models consume tool outputs as context, reinforcing the idea that external evidence should guide generation. In parallel, LAMA introduced precise probing templates to extract factual associations stored inside models, demonstrating that LMs encode a rich but static reservoir of parametric knowledge. Building on this, research on model editing such as ROME created CounterFact—a methodology for crafting targeted counterfactuals to stress-test and modify internal beliefs—thereby providing a blueprint for constructing controlled, opposition-aligned facts. Meanwhile, work on long-context utilization, exemplified by Lost in the Middle, revealed that LMs may ignore or misweight provided evidence depending on how it is presented, raising doubts about unqualified trust in external context.
Together, these strands exposed a clear opportunity: despite the promise of retrieval/tool augmentation, there was no controlled, belief-aware framework to test how LLMs arbitrate conflicts between internal memory and external evidence. By combining LAMA-style belief elicitation with CounterFact-inspired counter-memory construction and situating the tests within the RAG/Toolformer paradigm, the current paper systematically probes when and why coherent, convincing external evidence can override—or fail to override—parametric memory, thereby resolving a central uncertainty in augmentation-based LLM use.

---

*Analysis generated on: 2026-01-06T18:57:23.508211*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
