# Prior Work Analysis Report

## Target Paper

**Title:** Training on the Test Task Confounds Evaluation and Emergence

**Conference:** ICLR 2025 (oral)

**Authors:** Ricardo Dominguez-Olmedo, Florian E. Dorner, Moritz Hardt

**Keywords:** language models, benchmarking, emergence

**Abstract:** 
> We study a fundamental problem in the evaluation of large language models that we call training on the test task. Unlike wrongful practices like training on the test data, leakage, or data contamination, training on the test task is not a malpractice.  Rather, the term describes a growing set of techniques to include task-relevant data in the pretraining stage of a language model. We demonstrate that training on the test task confounds both relative model evaluations and claims about emergent ca...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Emergent Abilities of Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Direct Connection:* This work crystallized the notion of “emergent abilities” from scale on benchmarks, providing the specific phenomenon that the present paper re-examines and explains via the degree of training on the test task.

**Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models (BIG-bench)** (2022)
- *Authors:* Abhishek Srivastava et al.
- *Direct Connection:* BIG-bench supplied the task suite where sharp performance jumps were first documented, furnishing the concrete test tasks on which the paper studies how exposure to task-relevant data drives measured gains.

**Measuring Massive Multitask Language Understanding** (2020)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* MMLU established a central benchmark used to compare model families, which this paper analyzes under the lens of training-on-the-test-task and adjusts by equalizing task-relevant fine-tuning across models.

### 💡 Inspiration

**Don’t Stop Pretraining: Adapt Language Models to Domains and Tasks** (2020)
- *Authors:* Suchin Gururangan et al.
- *Direct Connection:* Domain- and task-adaptive pretraining showed that pretraining on task-relevant corpora boosts downstream scores, directly motivating the paper’s formalization of “training on the test task” and its controlled adjustment via shared task-relevant tuning.

**Finetuned Language Models are Zero-Shot Learners (FLAN)** (2021)
- *Authors:* Jason Wei et al.
- *Direct Connection:* Instruction tuning on mixtures of tasks demonstrated large zero-shot gains via exposure to task formulations, providing the concrete mechanism the paper identifies as training on the test task that can confound benchmark comparisons.

### 🔍 Gap Identification

**Are Emergent Abilities of Large Language Models a Mirage?** (2023)
- *Authors:* Rylan Schaeffer et al.
- *Direct Connection:* By attributing emergence to metric and scaling artifacts, this paper exposed a gap that the present work addresses by demonstrating a distinct confound—training on the test task—and providing an adjustment procedure.

**Holistic Evaluation of Language Models (HELM)** (2022)
- *Authors:* Percy Liang et al.
- *Direct Connection:* HELM highlighted confounds and comparability issues in LM evaluation, motivating the paper’s proposal to standardize evaluation by fine-tuning all compared models on the same task-relevant data.

---

## Synthesis: How Prior Work Led to This Paper

Work on large language model evaluation documented striking scale-related performance patterns on diverse, compositional tasks, with BIG-bench providing a broad suite where sharp capability jumps were observed and the Emergent Abilities paper coining the term for such discontinuities. MMLU established a widely adopted multitask benchmark for ranking models, becoming a focal point for claims about general knowledge and reasoning ability. A counterpoint argued that emergence could be a mirage induced by metric discretization and scaling choices, suggesting artifacts rather than genuine step-changes. In parallel, lines of research demonstrated that exposing models to task-relevant distributions during pretraining or fine-tuning materially boosts benchmark performance: domain- and task-adaptive pretraining showed gains from continued pretraining on task/domain text, while instruction tuning (e.g., FLAN) achieved large zero-shot improvements by training on mixtures of tasks that mirror evaluation formats. Holistic evaluation efforts emphasized comparability, surfacing confounds from differing data, prompts, and setups across model families. Together, these strands revealed a plausible mechanism behind apparent superiority and emergence: models often differ in how much they have already been trained on the very tasks or formats used for evaluation. The natural next step is to make this mechanism explicit and controlled—operationalizing fairness by equalizing task-relevant exposure across models via a shared fine-tuning phase—and to test whether emergence persists once this confound is removed, thereby reframing both model comparisons and claims of emergent capabilities.

---

*Analysis generated on: 2026-01-06T16:52:57.600025*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
