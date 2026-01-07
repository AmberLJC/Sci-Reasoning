# Prior Work Analysis Report

## Target Paper
**Title:** Acvo2RGSCy
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Theory of Games and Economic Behavior** (1944)
- *Authors:* John von Neumann and Oskar Morgenstern
- *Connection:* DeLLMa explicitly instantiates the expected-utility principle from von Neumann–Morgenstern to score and select among uncertain alternatives, making this the theoretical backbone of its decision procedure.

### 💡 Inspiration

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Connection:* DeLLMa adopts chain-of-thought style stepwise rationales as the substrate for its multi-step deliberation before utility evaluation, directly leveraging CoT’s idea of eliciting intermediate reasoning.

### 🔍 Gap Identification

**Large Language Models Still Struggle with Planning** (2023)
- *Authors:* Karthik Valmeekam et al.
- *Connection:* This work’s demonstration that LLMs are unreliable at multi-step planning directly motivates DeLLMa’s structured, inference-time deliberation and verification for robust decision making under uncertainty.

### 📊 Baseline

**Large Language Models Are Zero-Shot Reasoners** (2022)
- *Authors:* Takeshi Kojima et al.
- *Connection:* Zero-shot CoT prompting serves as a primary baseline that DeLLMa shows degrades on complex decision-under-uncertainty tasks, motivating its structured, utility-aware inference-time reasoning.

### 🔧 Extension

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2023)
- *Authors:* Xuezhi Wang et al.
- *Connection:* DeLLMa generalizes self-consistency from majority voting over sampled rationales to aggregating multiple sampled reasoning traces via expected-utility scoring over uncertain outcomes.

**Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Connection:* DeLLMa extends ToT-style structured exploration by guiding branch expansion and pruning with decision-theoretic expected-utility estimates, yielding an auditable decision path.

### 🔗 Related Problem

**ReAct: Synergizing Reasoning and Acting in Language Models** (2022)
- *Authors:* Shunyu Yao et al.
- *Connection:* ReAct’s interleaving of reasoning with evidence-gathering inspired DeLLMa’s use of intermediate computations/queries to estimate outcome probabilities that feed into utility calculations.

---

## Synthesis

DeLLMa’s core innovation is to fuse inference-time reasoning with classical decision theory so that LLMs make auditable, utility-maximizing choices under uncertainty. The theoretical foundation comes from von Neumann–Morgenstern’s expected-utility framework, which DeLLMa operationalizes to score candidate actions based on uncertain outcomes and user- or task-specific utilities. To generate and refine candidate decisions, DeLLMa builds directly on the inference-time reasoning paradigm inaugurated by chain-of-thought prompting, using stepwise rationales as a scaffold for decomposing complex decision problems. Recognizing that single trajectories are brittle, it extends self-consistency by moving from majority voting over answers to an expected-utility aggregation over multiple sampled reasoning traces. To further scale deliberation, DeLLMa adapts Tree-of-Thoughts, employing utility-guided expansion and pruning so the search over thoughts aligns with decision-theoretic optimality and remains human-auditable. Inspired by ReAct, DeLLMa interleaves reasoning with intermediate queries or computations to estimate outcome likelihoods, feeding these into its utility calculations. The overall framework is explicitly motivated by evidence that LLMs struggle with planning and reliability on complex tasks, as shown by Valmeekam et al., and by the empirical shortcomings of zero-shot CoT baselines on decision-under-uncertainty problems. The result is a principled, inference-time scalable procedure that transforms LLM deliberation into sound decision making grounded in expected-utility theory.

---
*Generated: 2026-01-06T23:09:26.588885*
