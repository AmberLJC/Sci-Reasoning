# Prior Work Analysis Report

## Target Paper

**Title:** MUSTARD: Mastering Uniform Synthesis of Theorem and Proof Data

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yinya Huang, Xiaohan Lin, Zhengying Liu, Qingxing Cao, Huajian Xin, Haiming Wang, Zhenguo Li, Linqi Song, Xiaodan Liang

**Keywords:** theorem proving, math word problem, mathematical reasoning, benchmark

**Abstract:** 
> Recent large language models (LLMs) have witnessed significant advancement in various tasks, including mathematical reasoning and theorem proving. As these two tasks require strict and formal multi-step inference, they are appealing domains for exploring the reasoning ability of LLMs but still face important challenges. Previous studies such as Chain-of-Thought (CoT) have revealed the effectiveness of intermediate steps guidance. However, such step-wise annotation requires heavy labor, leading t...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Training Verifiers to Solve Math Word Problems (GSM8K)** (2021)
- *Authors:* Cobbe et al.
- *Direct Connection:* This paper introduced a high-quality math word problem benchmark and the verifier paradigm, which MUSTARD leverages by generating math problems with solutions and filtering them via automated answer checking/verifier-style validation.

**GPT-f: Language Model Fine-Tuning for Formal Proofs** (2020)
- *Authors:* Stanislas Polu and Ilya Sutskever
- *Direct Connection:* GPT-f established the LLM + proof-checker loop for formal theorem proving, which MUSTARD generalizes by generating formal proof traces and validating them via proof assistants as a core quality-control stage.

### 💡 Inspiration

**STaR: Bootstrapping Reasoning with Reasoning** (2022)
- *Authors:* Adam Zelikman et al.
- *Direct Connection:* STaR’s generate-and-train loop using model-produced rationales inspired MUSTARD’s use of LLM-generated, step-wise solutions as supervision, extended to a uniform pipeline spanning both informal math and formal theorem proving.

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* Self-Instruct’s seed-concept/task bootstrapping directly motivates MUSTARD’s Stage-1 concept sampling and Stage-2 prompting strategy to systematically expand math categories into diverse problems with solutions.

### 🔍 Gap Identification

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Direct Connection:* By showing that step-wise rationales dramatically improve reasoning performance but require costly annotations, this work crystallized the data bottleneck that MUSTARD tackles by automatically synthesizing step-by-step proofs and solutions at scale.

**Measuring Mathematical Problem Solving With the MATH Dataset** (2021)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* MATH provided detailed step-by-step solutions but at limited scale and topic coverage, a limitation MUSTARD directly addresses through large-scale, concept-uniform synthesis of diverse math problems and proofs.

### 🔧 Extension

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2022)
- *Authors:* Xuezhi Wang et al.
- *Direct Connection:* MUSTARD adopts a multi-sample agreement/consistency-style filtering to retain only reliable synthesized problems and proofs, extending Self-Consistency from inference-time selection to dataset curation.

---

## Synthesis: How Prior Work Led to This Paper

Chain-of-Thought revealed that exposing intermediate reasoning steps markedly boosts performance, but also highlighted the scarcity and cost of step-wise annotations in math. GSM8K defined a clean math word problem benchmark and introduced verifier-based checking of solutions, while MATH supplied detailed multi-step solutions across topics yet remained limited in scale and topical uniformity. STaR demonstrated that model-generated rationales could be used as supervision to bootstrap stronger reasoners, suggesting a way to sidestep manual annotation. Self-Instruct showed how to expand task coverage by seeding with concepts and prompting a model to generate diverse, structured tasks and answers, offering a principled path to breadth and diversity. Self-Consistency established that sampling multiple chains and selecting the consistent ones increases reliability, an idea naturally repurposed for filtering synthesized data. In the formal domain, GPT-f pioneered integrating LLMs with proof assistants to produce and verify formal proof steps, proving the feasibility of generation-plus-checking loops for theorem proving.
Bringing these threads together, MUSTARD seizes the opportunity to uniformly synthesize high-quality, diverse math data by concept-seeded prompting (from Self-Instruct), generating explicit solution steps (motivated by CoT and STaR), and enforcing reliability with multi-sample agreement and formal proof checking (from Self-Consistency and GPT-f). This synthesis directly addresses the dataset bottlenecks surfaced by MATH and GSM8K, scaling step-wise supervision and bridging informal problem solving and formal theorem proving within a single, quality-controlled pipeline.

---

*Analysis generated on: 2026-01-06T18:13:48.902706*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
