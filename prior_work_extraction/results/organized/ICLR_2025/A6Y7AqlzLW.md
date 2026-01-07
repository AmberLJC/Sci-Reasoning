# Prior Work Analysis Report

## Target Paper

**Title:** Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, Aviral Kumar

**Keywords:** LLM, Math Reasoning, Process Supervision, Reward Models, RL, Search

**Abstract:** 
> A promising approach for improving reasoning in large language models is to use process reward models (PRMs). PRMs provide feedback at each step of a multi-step reasoning trace, improving credit assignment over outcome reward models (ORMs) that only provide feedback at the final step. However, collecting dense, per-step human labels is not scalable, and training PRMs from automatically-labeled data has thus far led to limited gains. With the goal of using PRMs to improve a *base* policy via test...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Policy Invariance under Reward Transformations: Theory and Application to Reward Shaping** (1999)
- *Authors:* Ng et al.
- *Direct Connection:* The paper’s progress reward instantiates potential-based shaping by using a value-like potential—the prover’s success probability—and rewarding the difference across consecutive steps for better credit assignment.

### 💡 Inspiration

**Let’s Verify Step by Step** (2023)
- *Authors:* Wang et al.
- *Direct Connection:* By framing intermediate-step verification and using verifiers to score partial reasoning, this paper directly motivates defining a step reward from changes in a verifier’s predicted likelihood of eventual correctness.

**STaR: Bootstrapping Reasoning With Reasoning** (2022)
- *Authors:* Zelikman et al.
- *Direct Connection:* STaR demonstrates that conditioning on improved intermediate rationales raises the chance of a correct final answer, motivating the paper’s explicit measurement of progress as the change in success probability after each step.

### 📊 Baseline

**Process Supervision Improves Mathematical Reasoning in Large Language Models (PRM800K)** (2023)
- *Authors:* Lightman et al.
- *Direct Connection:* This work established process reward models trained from human step labels to guide search and RL, which the current paper replaces with an automated, progress-based reward to overcome the scalability and limited generalization of human-annotated PRMs.

### 🔧 Extension

**Verifier-of-Thought: Generalist Verifiers for Step-by-Step Reasoning** (2023)
- *Authors:* Zhou et al.
- *Direct Connection:* Building on verifier models that assess intermediate steps, the current work extends the idea by calibrating the verifier as a probabilistic ‘prover’ and using deltas in its predicted success as the reward signal.

### 🔗 Related Problem

**Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (2023)
- *Authors:* Yao et al.
- *Direct Connection:* Tree of Thoughts evaluates partial thoughts to steer search, and the present paper formalizes this evaluation as a calibrated prover’s success probability and uses its before/after change as a principled progress signal.

---

## Synthesis: How Prior Work Led to This Paper

Process supervision for reasoning introduced training and deployment of process reward models that score intermediate steps, exemplified by PRM800K, which showed that step-wise feedback improves credit assignment but at the cost of expensive human annotations and limited generalization beyond curated labels. Let’s Verify Step by Step further crystallized the notion of intermediate-step verification, training models to judge partial chains-of-thought and use those judgments to guide solution search. Tree of Thoughts operationalized partial-state evaluation for test-time search, proposing that a value or heuristic score over partial thoughts can steer exploration effectively. In parallel, Verifier-of-Thought demonstrated generalist verifiers capable of assessing step-wise reasoning across tasks, highlighting that verifier predictions over partial trajectories can be broadly applied. From the reinforcement learning side, potential-based reward shaping established that rewards defined as differences in a potential (value) across consecutive states produce effective, policy-invariant shaping. Finally, STaR revealed that improved intermediate rationales causally increase the probability of final correctness, underscoring the importance of quantifying incremental progress along a trajectory.

Together, these works exposed a gap: verifiers scored steps, and search used heuristic partial-state evaluations, but there was no principled, scalable reward that directly measured incremental movement toward correctness. The current paper synthesizes these insights by calibrating a distinct prover to estimate the probability of eventual success given a partial trace and defining the process reward as the before/after change in that estimate. This turns verifier-style evaluation into a potential-based progress signal that scales without human step labels and plugs naturally into both test-time search and RL for stronger credit assignment.

---

*Analysis generated on: 2026-01-06T06:22:49.133999*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
