# Prior Work Analysis Report

## Target Paper

**Title:** Learning Dynamics of LLM Finetuning

**Conference:** ICLR 2025 (oral)

**Authors:** Yi Ren, Danica J. Sutherland

**Keywords:** Learning dynamics, LLM, finetuning, DPO

**Abstract:** 
> Learning dynamics, which describes how the learning of specific training examples influences the model's predictions on other examples, 
gives us a powerful tool for understanding the behavior of deep learning systems. We study the learning dynamics of large language models during different types of finetuning, by analyzing the step-wise decomposition of how influence accumulates among different potential responses. Our framework allows a uniform interpretation of many interesting observations a...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* This work established the pairwise preference-learning formulation and datasets underpinning modern preference tuning, which the paper’s dynamics framework targets to explain cross-example influence among candidate responses.

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* The instruction-tuning and SFT+RLHF protocols formalized here define the finetuning regimes whose example-to-example influence and post-finetuning behaviors the paper analyzes under a unified dynamics framework.

### 💡 Inspiration

**Estimating Training Data Influence by Tracing Gradient Descent** (2020)
- *Authors:* Pruthi et al.
- *Direct Connection:* The idea of decomposing influence along the optimization trajectory directly motivates the paper’s step-wise accumulation analysis of how each gradient step redistributes probability mass across potential responses.

**The Implicit Bias of Gradient Descent on Separable Data** (2018)
- *Authors:* Daniel Soudry et al.
- *Direct Connection:* Results showing cross-entropy gradient descent drives margins to grow inform the paper’s ‘squeezing effect’ explanation by extending margin-growth intuitions to token-level logit dynamics in LLM finetuning.

### 🔍 Gap Identification

**The Curious Case of Neural Text Degeneration** (2020)
- *Authors:* Ari Holtzman et al.
- *Direct Connection:* This work’s identification of repetition and degeneration under likelihood-based generation motivates the paper’s analysis of how finetuning dynamics amplify phrase repetition via cross-example influence.

### 📊 Baseline

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023)
- *Authors:* Alexander N. Rafailov et al.
- *Direct Connection:* The paper’s step-wise influence decomposition explicitly analyzes how updates change the chosen–rejected log-odds margin that DPO directly optimizes, providing a unified interpretation of DPO’s learning behavior during finetuning.

---

## Synthesis: How Prior Work Led to This Paper

Direct Preference Optimization formalizes preference learning as maximizing the log-odds margin between chosen and rejected responses, making the update direction and its effect on response probabilities explicit. RLHF for helpful and harmless assistants established pairwise preference datasets and the Bradley–Terry–style modeling that now anchor preference tuning objectives. Instruction-tuned systems via SFT and RLHF defined the dominant finetuning regimes and surfaced practical alignment–factuality tradeoffs, seeding observations about post-finetuning behaviors. TracIn showed that training influence can be decomposed step-by-step along the optimization trajectory, providing a concrete way to attribute how gradients from specific examples accumulate over time. Implicit bias results for cross-entropy gradient descent demonstrated that margins grow even without explicit regularization, suggesting systematic probability reallocation as training proceeds. Finally, neural text degeneration work highlighted that likelihood-driven models tend toward repetitive, high-probability phrases, a phenomenon plausibly affected by how finetuning reshapes logits across alternatives.

Taken together, these works exposed a gap: we lacked a principled, step-wise account of how finetuning objectives—spanning SFT and preference optimization—redistribute probability mass among competing responses and thereby induce repetition or hallucination. By marrying trajectory-based influence decomposition with the explicit log-odds structure of preference objectives and the margin-growth implicit bias of cross-entropy, the paper synthesizes a unified dynamics view. This perspective naturally yields the ‘squeezing effect,’ where growing margins compress probability for neutral alternatives, explaining strengthened hallucinations and phrase repetition after finetuning across both instruction and preference-tuning algorithms.

---

*Analysis generated on: 2026-01-06T20:01:32.934580*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
