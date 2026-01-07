# Prior Work Analysis Report

## Target Paper
**Title:** MI1uT5rReV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Connection:* The FAST-GRPO difficulty-aware KL regularization is an explicit adaptation of the KL-control in RLHF introduced by Ouyang et al., changing the static KL penalty into one that depends on estimated question difficulty.

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Connection:* The paper’s fast–slow thinking paradigm builds on Chain-of-Thought’s core finding that longer, stepwise reasoning improves accuracy, while motivating the need to selectively invoke such slow reasoning rather than applying it uniformly.

**Visual Instruction Tuning (LLaVA)** (2023)
- *Authors:* Haotian Liu et al.
- *Connection:* FAST-GRPO operates in the LVLM setting and inherits the visual-instruction tuning problem formulation and benchmarks from LLaVA-style models, targeting the specific gap of inefficient, overly long reasoning in LVLMs.

### 💡 Inspiration

**Complexity-Based Prompting for Multi-Step Reasoning** (2023)
- *Authors:* Yao Fu et al.
- *Connection:* FAST-GRPO’s two difficulty estimators and policy to choose fast vs slow reasoning are directly inspired by complexity-based prompting, which predicts problem difficulty to decide when to elicit CoT.

**Adaptive Computation Time for Recurrent Neural Networks** (2016)
- *Authors:* Alex Graves
- *Connection:* The core idea of allocating variable computation per input underpins FAST-GRPO’s adaptive reasoning depth, transposed from ACT’s dynamic halting to dynamic reasoning-length control in LVLMs with RL.

### 📊 Baseline

**DeepSeek-R1: Incentivizing LLMs to Reason via Reinforcement Learning** (2024)
- *Authors:* DeepSeek-AI et al.
- *Connection:* FAST-GRPO directly modifies the GRPO-based reinforcement learning setup popularized in DeepSeek-R1 by adding difficulty-aware KL and adaptive length rewards to avoid the universal, often verbose slow-thinking behavior induced by plain GRPO.

### 🔧 Extension

**Learning to Summarize with Human Feedback** (2020)
- *Authors:* Nisan Stiennon et al.
- *Connection:* FAST-GRPO generalizes the length/verbosity-aware reward shaping used in RLHF summarization by making the length-based reward adaptive to item difficulty, directly tackling verbosity-vs-accuracy trade-offs observed by Stiennon et al.

---

## Synthesis

FAST-GRPO’s core contribution—adapting reasoning depth to problem difficulty within a GRPO-based RL framework for LVLMs—stands on three intertwined lineages. First, reinforcement-learning-from-feedback with KL control (Stiennon et al.; Ouyang et al.) established the PPO-style/KL-regularized paradigm and exposed verbosity–quality trade-offs. FAST-GRPO directly extends this by making the KL coefficient difficulty-aware and by shaping rewards with an adaptive length term, rather than a one-size-fits-all penalty. Second, the reasoning literature (Wei et al.) showed that chain-of-thought improves accuracy but often at the cost of longer outputs; subsequent complexity-based prompting (Fu et al.) demonstrated that predicting difficulty to selectively trigger CoT can preserve accuracy while saving compute. FAST-GRPO internalizes this selectivity during RL, using learned difficulty metrics to decide when to encourage fast or slow thinking. Third, the algorithmic principle of input-conditional compute (Graves) provides the conceptual backbone for dynamic reasoning length, now instantiated for LVLMs trained with GRPO. Practically, the work targets the LVLM regime popularized by LLaVA, and its baseline is the GRPO-style reasoning RL exemplified by DeepSeek-R1; FAST-GRPO modifies that baseline to avoid universal slow thinking, yielding difficulty-aware, compute-efficient reasoning that scales accuracy without unnecessary verbosity.

---
*Generated: 2026-01-06T23:08:23.971940*
