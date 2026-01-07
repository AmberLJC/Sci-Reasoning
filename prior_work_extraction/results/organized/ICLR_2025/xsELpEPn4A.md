# Prior Work Analysis Report

## Target Paper

**Title:** JudgeLM: Fine-tuned Large Language Models are Scalable Judges

**Conference:** ICLR 2025 (spotlight)

**Authors:** Lianghui Zhu, Xinggang Wang, Xinlong Wang

**Keywords:** LLM Judging

**Abstract:** 
> Evaluating Large Language Models (LLMs) in open-ended scenarios is challenging because existing benchmarks and metrics can not measure them comprehensively. To address this problem, we propose to fine-tune LLMs as scalable judges (JudgeLM) to evaluate LLMs efficiently and effectively in open-ended benchmarks. We first propose a comprehensive, large-scale, high-quality dataset containing task seeds, LLMs-generated answers, and GPT-4-generated judgments for fine-tuning high-performance judges, as ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**MT-Bench and Chatbot Arena: Evaluating Large Language Models with Pairwise Judgments** (2023)
- *Authors:* Zheng et al.
- *Direct Connection:* Established the LLM-as-a-judge paradigm with GPT-4-based pairwise judgments on open-ended tasks and highlighted order/position confounds, which JudgeLM adopts as the evaluation setting and explicitly targets with debiasing.

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Bai et al.
- *Direct Connection:* Established the viability of scaling supervision via AI-generated feedback instead of human labels, directly enabling JudgeLM’s use of GPT-4–produced judgments to supervise judge models.

**UltraFeedback: Boosting Language Models with High-quality Feedback** (2023)
- *Authors:* Cui et al.
- *Direct Connection:* Provided a large-scale, multi-dimensional GPT-4 feedback dataset with symmetric pairwise annotations and position randomization that informs JudgeLM’s data construction and swap augmentation to mitigate position bias.

### 💡 Inspiration

**Shepherd: A Critic for Language Model Generation** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* Showed that a separately fine-tuned critic model trained on AI-generated critiques can reliably score and explain LLM outputs, inspiring JudgeLM’s approach of training dedicated judge models rather than relying solely on prompted evaluators.

### 🔍 Gap Identification

**Is ChatGPT a Good MT Evaluator? A Preliminary Study** (2023)
- *Authors:* Kocmi et al.
- *Direct Connection:* Revealed strong format and reference sensitivities when using LLMs as evaluators, motivating JudgeLM’s analysis of format/knowledge bias and its reference-support and reference-drop strategies.

### 📊 Baseline

**Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models** (2023)
- *Authors:* Kim et al.
- *Direct Connection:* Demonstrated that supervised fine-tuning on GPT-4–generated judgments can turn open LLMs into general-purpose judges, providing the primary system design and training pipeline that JudgeLM scales up and aims to surpass.

### 🔧 Extension

**Prometheus 2: An Open Language Model Judge Trained with Synthetic Feedback** (2024)
- *Authors:* Kim et al.
- *Direct Connection:* Refined judgment data and protocols for training LLM judges and offered stronger baselines, which JudgeLM directly extends by training larger judges and introducing bias-mitigation techniques absent in Prometheus 2.

---

## Synthesis: How Prior Work Led to This Paper

MT-Bench and Chatbot Arena crystallized the LLM-as-a-judge paradigm by using GPT-4 to render pairwise judgments on open-ended tasks and noting the importance of order randomization to reduce position confounds. Prometheus showed that supervised fine-tuning on GPT-4 judgments can endow open LLMs with strong general-purpose evaluation capabilities, and Prometheus 2 refined this idea with better judgment data and protocols, creating widely adopted judge-model baselines. Shepherd demonstrated that training a separate critic on AI feedback can reliably score and analyze model outputs, validating the notion of a dedicated evaluator model. Constitutional AI established the practicality of AI-generated supervision at scale, showing that high-quality AI feedback can substitute for human labels. UltraFeedback scaled multi-dimensional GPT-4 feedback with symmetric pairwise annotations and side randomization, surfacing concrete data practices for more reliable preference/judgment learning. Meanwhile, work on MT evaluation found that LLM evaluators are highly sensitive to prompt format and the availability of references, underscoring vulnerabilities in reference-free judging. Together, these works reveal both the promise and pitfalls of LLM-based evaluation: fine-tuned judges can be strong and scalable, but they inherit position, knowledge, and format biases from their data and prompts. Building on the synthetic-feedback SFT pipeline and pairwise judging setup, the natural next step is to scale judge models while explicitly addressing these biases. JudgeLM synthesizes these ideas by constructing a large GPT-4–labeled judgment dataset, training judges from 7B to 33B parameters, and introducing swap augmentation for position bias and reference-support/drop to disentangle knowledge and format effects, yielding more reliable, scalable judges.

---

*Analysis generated on: 2026-01-06T06:07:58.399181*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
