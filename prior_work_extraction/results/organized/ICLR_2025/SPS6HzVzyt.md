# Prior Work Analysis Report

## Target Paper

**Title:** Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance

**Conference:** ICLR 2025 (oral)

**Authors:** Sachin Goyal, Christina Baek, J Zico Kolter, Aditi Raghunathan

**Keywords:** Instruction finetuning, context-vs-parametric reliance

**Abstract:** 
> Large Language Model's are instruction-finetuned to enhance their ability to follow user instructions and better comprehend input context. Still, they often struggle to follow the input context, especially when it contradicts model's parametric knowledge. This manifests as various failures, such as hallucinations where a model inserts outdated or unwarranted facts into its response. In this work, we observe an intriguing phenomenon: the context reliance of the model decreases as instruction fine...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Finetuned Language Models Are Zero-Shot Learners** (2021)
- *Authors:* Jason Wei et al.
- *Direct Connection:* This work established instruction finetuning as the core paradigm for improving instruction-following, providing the problem formulation whose effect on context usage the current paper systematically interrogates across training.

**UltraChat: A Large-scale Automatic Multi-turn Chat Dataset for Instruction Tuning** (2023)
- *Authors:* Shuyue Stella Ding et al.
- *Direct Connection:* UltraChat supplies multi-turn conversational instruction data, enabling the paper’s cross-dataset tests that show the inversion phenomenon persists beyond single-turn instruction formats.

### 💡 Inspiration

**Lost in the Middle: How Language Models Use Long Context** (2023)
- *Authors:* Nelson F. Liu et al.
- *Direct Connection:* By isolating and measuring systematic underuse of long-context information, this work informs the paper’s measurement lens for quantifying context reliance as finetuning progresses.

### 🔍 Gap Identification

**Discovering Language Model Behaviors with Model-Written Evaluations** (2022)
- *Authors:* Ethan Perez et al.
- *Direct Connection:* This work documents undesirable alignment side effects like sycophancy, directly motivating the paper’s investigation into another alignment-tuning failure mode: reduced grounding in provided context over finetuning.

### 📊 Baseline

**Stanford Alpaca: An Instruction-Following LLaMA Model** (2023)
- *Authors:* Rohan Taori et al.
- *Direct Connection:* Alpaca provides a canonical general-purpose instruction-tuning dataset and setup that the paper uses as a primary baseline to reveal the context–parametric inversion during finetuning.

### 🔧 Extension

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2022)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* Self-Instruct’s concrete data-generation recipe underlies modern instruction-tuning pipelines, and the present paper directly extends this setting by tracking how reliance on provided context evolves as more Self-Instruct–style data is used.

### 🔗 Related Problem

**Improving language models by retrieving from trillions of tokens (RETRO)** (2022)
- *Authors:* Sebastian Borgeaud et al.
- *Direct Connection:* RETRO shows that explicitly training models to use retrieved evidence can shift reliance toward context, motivating the paper’s contrast that generic instruction finetuning alone can instead drift toward parametric knowledge.

---

## Synthesis: How Prior Work Led to This Paper

Instruction tuning was crystallized by Finetuned Language Models Are Zero-Shot Learners, which showed that supervised finetuning on diverse instructions reliably improves instruction following and generalization. Self-Instruct operationalized a scalable data-creation recipe—models generating and filtering their own instructions and responses—setting the template for most modern general-purpose tuning corpora. Stanford Alpaca demonstrated that modest, general-purpose instruction datasets can yield strong instruction-following behavior with lightweight finetuning, establishing a widely adopted baseline recipe. UltraChat extended this paradigm to large, multi-turn conversational traces, reflecting real dialog structure while retaining the instruction-following objective. In parallel, Lost in the Middle revealed that language models systematically underutilize provided evidence, especially in long contexts, and offered concrete evaluation setups for measuring context reliance. On the other hand, RETRO showed that when training explicitly rewards use of retrieved evidence, models shift reliance toward context over parametric memory. Complementing these perspectives, Discovering Language Model Behaviors with Model-Written Evaluations documented alignment-tuning side effects such as sycophancy, suggesting that naively optimizing for instruction adherence can induce unintended behaviors. Together, these works highlight a tension: instruction tuning promises better instruction adherence, yet models often underuse provided context unless training explicitly incentivizes evidence use, and alignment-style finetuning can introduce new failure modes. Building on the standard Alpaca- and UltraChat-style finetuning setups derived from Self-Instruct and FLAN, and using Lost in the Middle’s lens to quantify context use, the paper synthesizes these insights to probe the dynamics of context reliance during instruction finetuning—showing a counterintuitive inversion where reliance initially improves but then degrades—thereby explaining why generic instruction finetuning can drift toward parametric knowledge unless evidence use is explicitly trained, as in retrieval-augmented approaches.

---

*Analysis generated on: 2026-01-06T07:33:27.423152*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
