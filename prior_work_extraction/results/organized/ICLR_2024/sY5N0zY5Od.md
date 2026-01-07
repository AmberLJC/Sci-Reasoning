# Prior Work Analysis Report

## Target Paper

**Title:** DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines

**Conference:** ICLR 2024 (spotlight)

**Authors:** Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan A, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, Christopher Potts

**Keywords:** programming models, prompting techniques, in-context learning, few-shot learning, chain of thought, multi-hop reasoning, language agents

**Abstract:** 
> The ML community is rapidly exploring techniques for prompting language models (LMs) and for stacking them into pipelines that solve complex tasks. Unfortunately, existing LM pipelines are typically implemented using hard-coded “prompt templates”, i.e. lengthy strings discovered via trial and error. Toward a more systematic approach for developing and optimizing LM pipelines, we introduce DSPy, a programming model that abstracts LM pipelines as text transformation graphs, or imperative computati...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Direct Connection:* DSPy’s teleprompters explicitly generate and leverage intermediate rationales as learnable module parameters, directly building on the CoT insight that exposing step-by-step reasoning improves multi-step tasks.

**Self-Ask: A Simple Approach to Multi-Hop Reasoning** (2022)
- *Authors:* Press et al.
- *Direct Connection:* DSPy uses Self-Ask’s question-decomposition with search as a pipeline template and compiles it by learning prompts, selectors, and demonstrations that are tuned jointly to a task metric.

**Retrieval-Augmented Generation for Knowledge-Intensive NLP** (2020)
- *Authors:* Patrick Lewis et al.
- *Direct Connection:* DSPy formalizes RAG’s retriever–generator pattern as declarative modules whose prompts and retrieval selectors become learnable parameters optimized by the compiler.

### 💡 Inspiration

**Large Language Models are Human-Level Prompt Engineers** (2022)
- *Authors:* Zhou et al.
- *Direct Connection:* DSPy adopts APE’s core idea of treating prompts as objects to be optimized via sampling and evaluation, elevating it into a compiler that searches module parameters to maximize an external metric over a pipeline.

**Decomposed Prompting: A Modular Approach for Solving Complex Tasks** (2022)
- *Authors:* Tushar Khot et al.
- *Direct Connection:* DSPy systematizes decomposed prompting by representing each subtask as a declarative LM module with learnable prompting parameters and compiling the whole graph jointly rather than hand-crafting prompts.

### 📊 Baseline

**ReAct: Synergizing Reasoning and Acting in Language Models** (2022)
- *Authors:* Yao et al.
- *Direct Connection:* DSPy re-implements the ReAct reasoning-and-acting pattern as a composable pipeline and shows that compiling and optimizing its modules yields stronger performance, effectively subsuming ReAct as the primary baseline.

### 🔧 Extension

**Automatic Chain of Thought Prompting in Large Language Models** (2022)
- *Authors:* Zhang et al.
- *Direct Connection:* DSPy generalizes Auto-CoT’s automatic construction and selection of rationale-augmented demonstrations from single prompts to entire pipelines by compiling and optimizing example sets across modules using task metrics.

---

## Synthesis: How Prior Work Led to This Paper

Chain-of-thought prompting revealed that explicitly eliciting intermediate rationales can unlock stronger multi-step reasoning in large language models, providing a concrete handle—the rationale—to optimize. Auto-CoT showed that these rationales and demonstrations need not be hand-written: they can be automatically generated and selected to improve performance. In parallel, APE framed prompting itself as an optimization problem, iteratively proposing and scoring candidate prompts against an objective. For complex tasks requiring tools or multiple steps, ReAct established a reasoning-and-acting template, while Self-Ask demonstrated that decomposing a question into sub-questions with retrieval markedly improves multi-hop QA. RAG formalized the retriever–generator interface, making retrieval a first-class, composable component. Decomposed Prompting generalized the notion of breaking problems into modular subtasks, each guided by targeted prompts rather than a single monolithic instruction.
Taken together, these works suggested that (1) prompts, demonstrations, and rationales are trainable objects, (2) multi-step pipelines with retrieval and decomposition are powerful but brittle when hand-crafted, and (3) automatic construction and selection of demonstrations can outperform manual prompt engineering. The natural next step was to unify these insights into a programming model where each pipeline component exposes learnable prompt parameters and a compiler optimizes them end-to-end against a metric—automating demonstration creation, rationale generation, and example selection across modules to transform brittle prompt templates into state-of-the-art, trainable pipelines.

---

*Analysis generated on: 2026-01-06T11:29:38.083460*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
