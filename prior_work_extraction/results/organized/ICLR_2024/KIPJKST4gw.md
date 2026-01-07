# Prior Work Analysis Report

## Target Paper

**Title:** At Which Training Stage Does Code Data Help LLMs Reasoning?

**Conference:** ICLR 2024 (spotlight)

**Authors:** YINGWEI MA, Yue Liu, Yue Yu, Yuanliang Zhang, Yu Jiang, Changjian Wang, Shanshan Li

**Keywords:** code data, large language models, reasoning capabilities

**Abstract:** 
> Large Language models (LLMs) have exhibited remarkable reasoning capabilities and become the foundation of language technologies. Inspired by the great success of code data in training LLMs, we naturally wonder at which training stage introducing code data can really help LLMs reasoning. To this end, this paper systematically explores the impact of code data on LLMs at different stages. Concretely, we introduce the code data at the pre-training stage, instruction-tuning stage, and both of them, ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* The study adopts the two-stage pretraining + instruction-tuning paradigm formalized by InstructGPT and explicitly manipulates whether and how code appears at each stage to isolate its effect on reasoning.

**Finetuned Language Models Are Zero-Shot Learners** (2021)
- *Authors:* Jason Wei et al.
- *Direct Connection:* This work established supervised instruction tuning as a vehicle for transferring task knowledge (including reasoning) to pretrained LMs, providing the methodological basis to test how code-focused instruction data shapes task-specific reasoning.

**Training Verifiers to Solve Math Word Problems** (2021)
- *Authors:* Karl Cobbe et al.
- *Direct Connection:* GSM8K provides a standard math reasoning benchmark used here to quantify how injecting code at pretraining versus instruction-tuning differentially affects general and task-specific reasoning.

### 💡 Inspiration

**Evaluating Large Language Models Trained on Code** (2021)
- *Authors:* Mark Chen et al.
- *Direct Connection:* By demonstrating that large-scale code pretraining (Codex) confers strong capabilities beyond pure NL modeling, it directly motivated the hypothesis that code exposure can endow or transfer general reasoning skills.

**LLaMA 2: Open Foundation and Fine-Tuned Chat Models** (2023)
- *Authors:* Hugo Touvron et al.
- *Direct Connection:* LLaMA 2 reported that mixing a nontrivial fraction of code in pretraining correlates with improved mathematical/logical evaluations, inspiring a controlled, stage-wise analysis of where code helps most.

### 🔍 Gap Identification

**Code Llama: Open Foundation Models for Code** (2023)
- *Authors:* Baptiste Rozière et al.
- *Direct Connection:* Code Llama showed continued pretraining on code boosts reasoning-leaning benchmarks but did not disentangle pretraining versus instruction-tuning effects, a gap this paper addresses via stage-specific interventions.

### 🔗 Related Problem

**WizardCoder: Empowering Large Language Models to Develop Code** (2023)
- *Authors:* Ziyang Luo et al.
- *Direct Connection:* WizardCoder demonstrated that code-centric instruction tuning substantially shifts model capabilities, motivating the paper’s examination of how code at the instruction-tuning stage imparts task-specific reasoning.

---

## Synthesis: How Prior Work Led to This Paper

Instruction tuning emerged as a distinct stage after large-scale pretraining with InstructGPT, establishing a pipeline where stage-specific data choices can steer model behavior; FLAN showed that supervised instruction tuning transfers broad task competence, including reasoning, to pretrained LMs. Codex demonstrated that pretraining on massive code corpora yields capabilities that generalize beyond code, suggesting that structural regularities in programming data can shape reasoning skills. LLaMA 2 reported performance gains on math and logic coincident with including a meaningful fraction of code during pretraining, connecting code mixture to emergent reasoning. Code Llama further showed that continued pretraining on code after text improves reasoning-leaning metrics, but without dissecting when in the training pipeline code matters most. Complementarily, WizardCoder provided evidence that code-focused instruction tuning can substantially shift capabilities, hinting that code at the instruction phase may impart task-specific reasoning patterns. GSM8K furnished a rigorous math reasoning benchmark for measuring such effects. Together, these works indicated that code benefits reasoning but left unresolved whether benefits stem primarily from pretraining, instruction tuning, or their combination. Building on the two-stage framework, the paper systematically injects code at pretraining, instruction tuning, and both, and evaluates with reasoning tasks like GSM8K to separate general from task-specific gains. This synthesis clarifies that mixing code with text during pretraining chiefly enhances general reasoning with minimal negative transfer, while code at instruction tuning confers task-specific reasoning, making the stage-aware use of code a natural next step.

---

*Analysis generated on: 2026-01-06T16:16:57.328611*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
