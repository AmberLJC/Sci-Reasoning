# Prior Work Analysis Report

## Target Paper

**Title:** Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach

**Conference:** ICLR 2025 (spotlight)

**Authors:** Qi Liu, Xinhao Zheng, Xudong Lu, Qinxiang Cao, Junchi Yan

**Keywords:** Large Language Model, Formal Verification, Autoformalization

**Abstract:** 
> As a central component in formal verification, statement autoformalization has been widely studied including the recent efforts from machine learning community, but still remains a widely-recognized difficult and open problem. In this paper, we delve into two critical yet under-explored gaps: 1) absence of faithful and universal automated evaluation for autoformalization results; 2) agnosia of contextual information, inducing severe hallucination of formal definitions and theorems. To address th...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**DeepMath: Deep Sequence Models for Premise Selection** (2016)
- *Authors:* Alexander A. Alemi et al.
- *Direct Connection:* DeepMath established learned premise selection as a crucial step for reusing formal libraries, and this paper extends that idea to statement autoformalization by retrieving dependent objects to condition generation on the right context.

**The Lean 4 Theorem Prover and Programming Language** (2021)
- *Authors:* Leonardo de Moura et al.
- *Direct Connection:* Lean 4 formalizes definitional equality and reduction rules; BEq directly builds on and extends these definitional-equivalence mechanisms to check bidirectional, definition-unfolding equivalence between formal statements.

### 💡 Inspiration

**LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (2023)
- *Authors:* First author et al.
- *Direct Connection:* LeanDojo operationalized retrieval-augmented modeling over Lean’s library by fetching prerequisite definitions/lemmas, directly inspiring this paper’s Dependency Retrieval to ground autoformalization and curb hallucinated symbols.

### 🔍 Gap Identification

**Generative Language Modeling for Automated Theorem Proving** (2020)
- *Authors:* Karlis Polu et al.
- *Direct Connection:* Polu et al. evaluated generative models mainly via proof success or surface-level matches, highlighting the lack of a faithful automated equivalence metric for generated statements that this paper addresses with BEq.

**MiniF2F: A Cross-System Benchmark for Formal Reasoning** (2021)
- *Authors:* First author et al.
- *Direct Connection:* MiniF2F highlighted the mismatch between human-perceived equivalence and surface-form comparisons across systems, motivating a faithful, system-grounded equivalence metric like BEq for autoformalized statements.

### 🔗 Related Problem

**Hammering Towards QED** (2016)
- *Authors:* Jasmin C. Blanchette et al.
- *Direct Connection:* Hammering Towards QED systematized premise selection and dependency tracking in large formal libraries, providing the concrete notion of dependency graphs that this work leverages for retrieval during autoformalization.

---

## Synthesis: How Prior Work Led to This Paper

Learned premise selection demonstrated that retrieving the right library facts is pivotal for effective reuse of formal knowledge: DeepMath showed deep models can select relevant premises from large corpora, while Hammering Towards QED integrated dependency tracking and premise selection into mainstream hammering pipelines, making dependency graphs a practical interface to large formal libraries. LeanDojo then operationalized retrieval augmentation specifically in Lean, showing that fetching precise formal dependencies (definitions and lemmas) stabilizes language-model behavior in proof tasks. In parallel, generative ATP systems such as Polu et al. primarily assessed models via proof success or surface-form agreement, exposing how fragile and indirect these proxies are for judging statement correctness. Lean 4 clarified the formal bedrock—definitional equality, reductions, and unfolding—on which equivalence inside the proof assistant truly rests, and cross-system efforts like MiniF2F underscored that syntactic similarity often misaligns with mathematical equivalence.
Collectively, these lines reveal two complementary opportunities: first, evaluation should be grounded in the proof assistant’s own equivalence notions rather than surface forms; second, generation should be conditioned on the exact formal context to avoid inventing symbols or misusing definitions. This paper synthesizes those insights by proposing a neuro-symbolic equivalence checker, BEq, that extends definitional equivalence with bidirectional unfolding and alignment, and by adapting retrieval—rooted in premise/dependency selection—to autoformalization via targeted Dependency Retrieval that injects the precise objects needed to faithfully formalize a statement.

---

*Analysis generated on: 2026-01-06T17:43:51.467392*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
