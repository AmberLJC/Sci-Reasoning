# Prior Work Analysis Report

## Target Paper

**Title:** Answer, Assemble, Ace: Understanding How LMs Answer Multiple Choice Questions

**Conference:** ICLR 2025 (spotlight)

**Authors:** Sarah Wiegreffe, Oyvind Tafjord, Yonatan Belinkov, Hannaneh Hajishirzi, Ashish Sabharwal

**Keywords:** interpretability; multiple-choice question answering

**Abstract:** 
> Multiple-choice question answering (MCQA) is a key competence of performant transformer language models that is tested by mainstream benchmarks. However, recent evidence shows that models can have quite a range of performance, particularly when the task format is diversified slightly (such as by shuffling answer choice order). In this work we ask: how do successful models perform formatted MCQA? We employ vocabulary projection and activation patching methods to localize key hidden states that en...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Measuring Massive Multitask Language Understanding** (2020)
- *Authors:* Hendrycks et al.
- *Direct Connection:* This work formalized large-scale MCQA evaluation (MMLU), providing the problem setting and mainstream benchmark context that the present analysis targets and explains mechanistically.

### 💡 Inspiration

**Interpreting GPT: The Logit Lens** (2020)
- *Authors:* nostalgebraist
- *Direct Connection:* The paper’s vocabulary projection analysis directly adopts the logit-lens idea of projecting intermediate residual stream states into vocabulary space to track how specific token probabilities evolve across layers.

**Towards Automated Circuit Discovery in Language Models** (2023)
- *Authors:* Conmy et al.
- *Direct Connection:* Their methodology of head- and component-level activation patching to uncover circuits directly informs the paper’s approach to patching attention heads to reveal the causal pathway from question and choices to the answer token.

### 🔍 Gap Identification

**Calibrate Before Use: Improving Few-Shot Performance of Language Models** (2021)
- *Authors:* Zhao et al.
- *Direct Connection:* By revealing sensitivity to prompt and label format (including order effects), it motivates this paper’s investigation into how MCQA format variations, such as answer choice shuffling, affect internal mechanisms leading to the final answer.

### 🔧 Extension

**The Tuned Lens: A Tool for Interpreting and Debugging Language Models** (2023)
- *Authors:* Belrose et al.
- *Direct Connection:* They extend the logit-lens with a learned, layer-specific mapping, providing the concrete technique that this work builds on to quantify how later layers amplify the correct answer symbol in vocabulary space.

**Locating and Editing Factual Associations in GPT** (2022)
- *Authors:* Meng et al.
- *Direct Connection:* This work introduces activation patching/causal tracing to localize where specific information is represented, which the current paper adapts to MCQA to causally attribute the predicted answer symbol to particular layers and attention heads.

### 🔗 Related Problem

**In-Context Learning and Induction Heads** (2022)
- *Authors:* Olsson et al.
- *Direct Connection:* By demonstrating that specific attention heads implement distinct algorithmic roles (e.g., induction), it motivates the head-level causal analyses used here to identify sparse heads with unique roles in assembling MCQA answers.

---

## Synthesis: How Prior Work Led to This Paper

Projecting intermediate representations into vocabulary space revealed that models progressively form token-level hypotheses that sharpen across depth; the logit lens introduced this projection, and the tuned lens refined it with learned, layer-specific mappings that better track per-layer token probabilities. Parallel mechanistic work developed causal intervention techniques: activation patching and causal tracing showed that one can localize where specific content lives inside transformers, while automated circuit discovery scaled such patching to identify which layers and heads carry task-relevant signals. Complementing these tools, analyses of induction heads established that individual attention heads can implement distinct algorithmic roles, motivating head-level inspection as a meaningful granularity for causal attribution. Meanwhile, large-scale MCQA benchmarks like MMLU defined the standard evaluation setting in which model abilities are probed. Finally, studies on calibration and prompt sensitivity documented that language models are surprisingly brittle to superficial format changes, including order effects, highlighting that observed MCQA performance may hinge on formatting rather than robust reasoning. Together, these strands suggested a concrete opportunity: use causal activation patching at head and layer granularity, combined with vocabulary-space projections, to trace how MCQA answers are selected and then amplified through depth. In this view, benchmarked MCQA behavior can be decomposed into a small set of middle-layer mechanisms that select an answer symbol and later-layer processes that boost its logit, explaining sensitivity to choice formatting via the specific heads and layers that mediate these steps.

---

*Analysis generated on: 2026-01-06T07:27:25.202717*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
