# Prior Work Analysis Report

## Target Paper

**Title:** Evaluating the Zero-shot Robustness of Instruction-tuned Language Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jiuding Sun, Chantal Shaib, Byron C Wallace

**Keywords:** Instruction Tuning, Robustness, Large Language Models

**Abstract:** 
> Instruction fine-tuning has recently emerged as a promising approach for improving the zero-shot capabilities of Large Language Models (LLMs) on new tasks. This technique has shown particular strength in improving the performance of modestly sized LLMs, sometimes inducing performance competitive with much larger model variants. In this paper, we ask two questions: (1) How sensitive are instruction-tuned models to the particular phrasings of instructions, and, (2) How can we make them more robust...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Multitask Prompted Training Enables Zero-Shot Generalization** (2022)
- *Authors:* Victor Sanh et al.
- *Direct Connection:* This work established the instruction-tuned, zero-shot evaluation paradigm using multiple prompt templates per task and documented difficulties generalizing to unseen templates, which this paper directly measures and seeks to mitigate for instruction-tuned LMs.

**Super-Natural Instructions: Generalization via Declarative Instructions** (2022)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* Its curated instruction–task collection and multiple human-written templates define the ‘observed’ phrasing distribution used in instruction tuning, against which this paper contrasts newly collected practitioner-written phrasings to quantify robustness gaps.

### 💡 Inspiration

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* Demonstrating that increasing instruction diversity via synthetic instruction generation boosts zero-shot performance directly motivates this paper’s robustness-oriented use of diverse paraphrastic instructions to improve invariance to wording.

### 🔍 Gap Identification

**Prompting Is Not Enough: Investigating Zero-Shot Performance of Large Language Models** (2022)
- *Authors:* Alicia Parrish Webson and Ellie Pavlick
- *Direct Connection:* This study’s evidence that zero-shot performance varies drastically with prompt wording identifies the fragility that this paper tests in instruction-tuned LMs and explicitly targets with robustness interventions.

### 📊 Baseline

**Scaling Instruction-Finetuned Language Models** (2022)
- *Authors:* Hyung Won Chung et al.
- *Direct Connection:* The FLAN family of instruction-tuned models constitutes a primary baseline whose claimed benefits from instruction diversity are directly probed here by testing sensitivity to unseen but appropriate instruction paraphrases.

### 🔧 Extension

**PromptSource: An Integrated Development Environment and Repository for Prompt Engineering** (2022)
- *Authors:* Stephen Bach et al.
- *Direct Connection:* By providing the P3 pool of standardized prompt templates used to train/evaluate T0-style models, it furnishes the canonical template set that this paper explicitly extends with additional human-authored instructions to stress-test cross-prompt robustness.

---

## Synthesis: How Prior Work Led to This Paper

Multitask prompted training (T0) formalized instruction-tuned zero-shot evaluation by training on many prompt templates per task and revealed that models still struggle with unseen templates. Super-NaturalInstructions operationalized task descriptions as explicit instructions and supplied multiple human-written templates per task, creating a concrete distribution of ‘observed’ phrasings that instruction-tuned models learn from. PromptSource/P3 standardized and centralized these templates, providing a canonical pool that most instruction-tuning pipelines rely on for both training and evaluation. Building on this, FLAN scaled instruction tuning to far larger model and instruction mixtures and argued that diversity of tasks and prompts is a key driver of zero-shot gains. Self-Instruct showed that automatically generated, diverse instructions can further enhance zero-shot capabilities, underscoring the role of instruction variety in shaping model behavior. Complementing these advances, work on zero-shot prompting fragility demonstrated that performance can swing widely with benign wording variations, highlighting a core vulnerability in prompt-based use of LMs. Taken together, these strands suggest that while instruction tuning improves zero-shot generalization, models may remain brittle to naturally occurring instruction paraphrases. This paper synthesizes these insights by explicitly contrasting performance on ‘observed’ instruction phrasings from Super-NaturalInstructions/PromptSource-style sources with newly collected practitioner-written paraphrases, quantifying the robustness gap in state-of-the-art instruction-tuned baselines like FLAN. Motivated by evidence that instruction diversity helps, it then leverages diverse paraphrastic instructions to improve invariance to wording, providing a targeted, natural next step toward robust zero-shot instruction following.

---

*Analysis generated on: 2026-01-06T14:37:42.664559*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
