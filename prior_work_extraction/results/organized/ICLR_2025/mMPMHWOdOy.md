# Prior Work Analysis Report

## Target Paper

**Title:** WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct

**Conference:** ICLR 2025 (oral)

**Authors:** Haipeng Luo, Qingfeng Sun, Can Xu, Pu Zhao, Jian-Guang Lou, Chongyang Tao, Xiubo Geng, Qingwei Lin, Shifeng Chen, Yansong Tang, Dongmei Zhang

**Keywords:** Mathematical Reasoning, Evol-Instruct, Reinforcement Learning

**Abstract:** 
> Large language models (LLMs), such as GPT-4, have shown remarkable performance in natural language processing (NLP) tasks, including challenging mathematical reasoning. However, most existing open-source models are only pre-trained on large-scale internet data and without math-related optimization. In this paper, we present WizardMath, which enhances the mathematical reasoning abilities of LLMs, by applying our proposed Reinforcement Learning from Evol-Instruct Feedback (RLEIF) method to the dom...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* WizardMath adopts the RLHF recipe (SFT → reward modeling → PPO) established by InstructGPT, but replaces human preferences with Evol-Instruct-derived feedback tailored for mathematics.

**Training Verifiers to Solve Math Word Problems (GSM8K)** (2021)
- *Authors:* Karl Cobbe et al.
- *Direct Connection:* GSM8K defines the grade-school math reasoning task and answer-checking protocol that WizardMath uses to evolve instructions and to generate outcome/process feedback for RLEIF.

**Measuring Mathematical Problem Solving With the MATH Dataset** (2021)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* MATH provides competition-level problems and verifiable solutions that WizardMath leverages both to create challenging evolved instructions and to supervise process- and outcome-level rewards.

### 💡 Inspiration

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* The shift from human labels to AI feedback in Constitutional AI directly motivates WizardMath’s RL from Evol-Instruct Feedback, where automatically generated judgments supervise policy optimization.

**Self-Consistent Reasoners: STaR—Bootstrapping Reasoning with Reasoning** (2022)
- *Authors:* Ethan Zelikman et al.
- *Direct Connection:* STaR’s core insight that supervising intermediate rationales improves reasoning underpins WizardMath’s use of process supervision and step-level signals within its RL pipeline.

### 🔧 Extension

**WizardLM: Empowering Large Language Models to Follow Complex Instructions** (2023)
- *Authors:* Can Xu et al.
- *Direct Connection:* WizardMath directly extends WizardLM’s Evol-Instruct paradigm by evolving math-specific instructions and reusing the evolution signals as feedback to drive its RLEIF training.

---

## Synthesis: How Prior Work Led to This Paper

Evol-Instruct introduced by WizardLM demonstrated that instructions can be automatically evolved to become more compositional and challenging, yielding higher-quality supervision signals for instruction-following models. InstructGPT established the practical pipeline for reinforcement learning from human feedback—supervised fine-tuning followed by reward modeling and PPO—that operationalized preference-based alignment at scale. Constitutional AI generalized RLHF by replacing costly human labels with AI feedback, showing that preference signals derived from model-based judges can effectively guide policy improvement. STaR revealed that supervising intermediate reasoning steps and bootstrapping from rationales substantially improves a model’s ability to perform multi-step reasoning. GSM8K defined a clean, verifiable benchmark for grade-school math word problems with robust answer checking, while the MATH dataset supplied a harder, competition-level setting with formal solutions suitable for verifying both final answers and intermediate reasoning.
Collectively, these works suggested a pathway to scalable math specialization: use automated instruction evolution to generate harder math tasks and accompanying feedback; exploit verifiable datasets to check both outcomes and steps; and drive learning via an RLHF-style loop but with AI-generated, process-aware feedback rather than human labels. WizardMath synthesizes these pieces by turning instruction evolution into a source of structured preference/process signals and embedding them in an RL framework (RLEIF), thereby unifying automatic data evolution, AI feedback, and process supervision to markedly strengthen mathematical reasoning.

---

*Analysis generated on: 2026-01-06T19:50:09.348470*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
