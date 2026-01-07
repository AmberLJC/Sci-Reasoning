# Prior Work Analysis Report

## Target Paper

**Title:** Large Language Models Are Not Robust Multiple Choice Selectors

**Conference:** ICLR 2024 (spotlight)

**Authors:** Chujie Zheng, Hao Zhou, Fandong Meng, Jie Zhou, Minlie Huang

**Keywords:** large language model, bias, robustness, multiple choice question, evaluation

**Abstract:** 
> Multiple choice questions (MCQs) serve as a common yet important task format in the evaluation of large language models (LLMs). This work shows that modern LLMs are vulnerable to option position changes in MCQs due to their inherent “selection bias”, namely, they prefer to select specific option IDs as answers (like “Option A”). Through extensive empirical analyses with 20 LLMs on three benchmarks, we pinpoint that this behavioral bias primarily stems from LLMs’ token bias, where the model a pri...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Measuring Massive Multitask Language Understanding** (2021)
- *Authors:* Hendrycks et al.
- *Direct Connection:* This benchmark standardized MCQ evaluation with A/B/C/D options, providing the task formulation and datasets on which the selection-bias phenomenon and PriDe’s debiasing are demonstrated.

### 💡 Inspiration

**Long-Tailed Classification via Logit Adjustment** (2020)
- *Authors:* Menon et al.
- *Direct Connection:* PriDe adopts the logit-adjustment principle—subtracting log class priors from logits—to debias predictions, applying it at inference by dividing out estimated priors over option IDs.

**Self-Diagnosis and Self-Debiasing: A Proposal for Reducing Toxicity in Language Models** (2021)
- *Authors:* Schick et al.
- *Direct Connection:* PriDe echoes the self-debiasing strategy of separating a bias-only component from the model’s output and subtracting it, here instantiating the bias component as the option-ID prior rather than toxicity cues.

### 🔍 Gap Identification

**Lost in the Middle: How Language Models Use Long Context** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* Evidence of strong positional effects in long contexts motivates examining and mitigating the specific option-position sensitivity that PriDe targets in MCQs.

**Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?** (2022)
- *Authors:* Min et al.
- *Direct Connection:* Findings that label mappings and prompt formatting can dominate ICL performance directly motivate isolating and correcting the option-ID token prior that skews multiple-choice selection.

### 🔧 Extension

**Calibrate Before Use: Improving Few-Shot Performance of Language Models** (2021)
- *Authors:* Zhao et al.
- *Direct Connection:* PriDe generalizes contextual calibration’s idea of estimating and removing label-word prior bias by instead estimating option-ID token priors via option-content permutations and using this correction for MCQ selection.

### 🔗 Related Problem

**Detecting and Correcting for Label Shift with Black Box Predictors** (2018)
- *Authors:* Lipton et al.
- *Direct Connection:* PriDe parallels label-shift correction by estimating test-time label priors and adjusting predictions, but innovates by inferring option-ID priors from unlabeled test permutations without requiring labeled validation data.

---

## Synthesis: How Prior Work Led to This Paper

Contextual calibration showed that prompt-based classifiers in language models carry systematic label-word priors and that subtracting a context-induced bias improves few-shot classification. Logit adjustment from long-tailed recognition formalized a simple and effective way to correct predictions by removing the influence of class priors at logit level. Self-diagnosis and self-debiasing demonstrated that one can construct a bias-only signal from the model itself and attenuate it at inference, separating spurious cues from the desired conditional prediction. Studies of long-context processing revealed strong positional effects—models overweight earlier or later spans—highlighting that order alone can sway predictions independent of content. Work dissecting in-context learning further showed that label mappings and format choices, rather than task understanding, often drive performance, implicating superficial biases around label tokens. Finally, MMLU codified MCQ evaluation with A/B/C/D options as a standard, making option-identifier tokens central to widely used assessments, while label-shift correction established the general recipe of estimating test-time priors and reweighting posteriors. Together, these strands expose an opportunity: MCQ evaluations hinge on fixed option-ID tokens that can carry strong priors, and order-induced effects can amplify them; yet prior correction has not been tailored to this setting. The present work synthesizes these insights by explicitly estimating option-ID priors via content permutations on a small test subset and removing them through logit-level prior adjustment, yielding a label-free, inference-time debiasing method that targets selection bias in multiple-choice selection.

---

*Analysis generated on: 2026-01-07T00:17:03.500594*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
