# Prior Work Analysis Report

## Target Paper

**Title:** miniCTX: Neural Theorem Proving with (Long-)Contexts

**Conference:** ICLR 2025 (oral)

**Authors:** Jiewen Hu, Thomas Zhu, Sean Welleck

**Keywords:** Neural theorem proving, Formal mathematics, Benchmark dataset

**Abstract:** 
> Real-world formal theorem proving often depends on a wealth of context, including definitions, lemmas, comments, file structure, and other information. We introduce $\texttt{miniCTX}$, which tests a model's ability to prove formal mathematical theorems that depend on new context that is not seen during training. $\texttt{miniCTX}$ contains theorems sourced from real Lean projects and textbooks, each associated with a context that can span tens of thousands of tokens. Models are tasked with provi...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**miniF2F: A Cross-Domain Benchmark for Formal and Informal Mathematics** (2021)
- *Authors:* Zheng et al.
- *Direct Connection:* miniF2F established the prevailing testbed and success metrics for Lean-based neural theorem proving, whose lack of explicit long-context and repository-level conditioning is the precise gap miniCTX targets.

**HOList: An Environment for Machine Learning of Higher-Order Theorem Proving** (2019)
- *Authors:* Bansal et al.
- *Direct Connection:* HOList framed step-wise proof-state learning and large-library proving, crystallizing the state-centric setup whose limitations in leveraging external project context miniCTX addresses.

### 💡 Inspiration

**LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (2024)
- *Authors:* Zhu et al.
- *Direct Connection:* LeanDojo concretely demonstrated that retrieving code/library artifacts from Lean projects improves proof success, directly motivating miniCTX’s formulation of conditioning on repository context at scale.

### 🔍 Gap Identification

**DeepSeek-Prover: Advancing Formal Theorem Proving with Large Language Models** (2023)
- *Authors:* Zhang et al.
- *Direct Connection:* DeepSeek-Prover achieved strong results on miniF2F using state-focused generation and self-reflection, highlighting that SOTA systems excel without explicitly modeling long, repository-level context—an omission miniCTX is designed to expose.

### 📊 Baseline

**Generating Formal Proofs with GPT-f** (2020)
- *Authors:* Polu et al.
- *Direct Connection:* GPT-f popularized the state-only next-tactic paradigm for neural theorem proving, serving as the canonical baseline that miniCTX contrasts with context-conditioned proving.

### 🔗 Related Problem

**LongBench: A Bilingual, Multitask Benchmark for Long-Context Language Models** (2023)
- *Authors:* Bai et al.
- *Direct Connection:* LongBench established evaluation for long-context understanding in NLP, informing miniCTX’s emphasis on tens-of-thousands-token inputs but lacking the structured proof-state dynamics of formal theorem proving.

---

## Synthesis: How Prior Work Led to This Paper

miniF2F defined the de facto evaluation regime for Lean-based neural proving, focusing on problem statements and proof states rather than on leveraging the rich, project-level environment that real formal mathematics lives in. HOList established step-wise proof-state prediction within large theories, reinforcing the state-centric paradigm and framing success as next-tactic or next-step learning. GPT-f operationalized this paradigm with powerful language models trained to emit tactics from proof states, making “state-only” the practical default for learned theorem proving. In parallel, LeanDojo demonstrated that retrieving definitions and lemmas from Lean repositories boosts proving, foregrounding the importance of external artifacts beyond the immediate state. DeepSeek-Prover then pushed state-driven methods near the frontier on miniF2F via self-reflection and improved generation, yet still without explicit long-context conditioning. Outside formal math, LongBench clarified how long-context inputs can be systematically evaluated at scale.
Taken together, these works reveal a gap: evaluations and methods excel at state-centric proving but do not directly test or train repository- and file-structure-aware reasoning over tens of thousands of tokens. miniCTX synthesizes LeanDojo’s retrieval insight with long-context evaluation principles to build a benchmark where success requires conditioning on real project context, thereby directly challenging the state-only lineage established by HOList, GPT-f, and miniF2F—and revealing the limitations of SOTA systems like DeepSeek-Prover in this setting.

---

*Analysis generated on: 2026-01-06T15:02:12.548912*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
