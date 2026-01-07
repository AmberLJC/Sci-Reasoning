# Prior Work Analysis Report

## Target Paper

**Title:** Transformers Provably Solve Parity Efficiently with Chain of Thought

**Conference:** ICLR 2025 (oral)

**Authors:** Juno Kim, Taiji Suzuki

**Keywords:** transformers, chain of thought, parity, self-consistency

**Abstract:** 
> This work provides the first theoretical analysis of training transformers to solve complex problems by recursively generating intermediate states, analogous to fine-tuning for chain-of-thought (CoT) reasoning. We consider training a one-layer transformer to solve the fundamental $k$-parity problem, extending the work on RNNs by \citet{Wies23}. We establish three key results: (1) any finite-precision gradient-based algorithm, without intermediate supervision, requires substantial iterations to s...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Direct Connection:* It introduced the central idea of supervising or eliciting intermediate reasoning chains, which this work formalizes as intermediate parities for transformers and analyzes theoretically (including under teacher forcing).

**A Learning Algorithm for Continually Running Fully Recurrent Neural Networks** (1989)
- *Authors:* Ronald J. Williams and David Zipser
- *Direct Connection:* This classic work introduced teacher forcing, the exact training regime analyzed here when ground-truth intermediate labels are fed at each generation step to yield one-step learning of parity.

### 💡 Inspiration

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2022)
- *Authors:* Xuezhi Wang et al.
- *Direct Connection:* Their insight that multiple, internally consistent chains can verify reasoning motivates this paper’s augmented-data mechanism that internally checks intermediate steps to enable efficient end-to-end learning without teacher forcing.

**STaR: Bootstrapping Reasoning With Reasoning** (2022)
- *Authors:* Eric Zelikman et al.
- *Direct Connection:* STaR’s idea of augmenting training with self-generated, correctness-verified rationales directly informs the paper’s theoretical construction where augmented data is used to verify intermediate parities and drive efficient learning.

### 🔍 Gap Identification

**Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks** (2015)
- *Authors:* Samy Bengio et al.
- *Direct Connection:* By highlighting exposure bias and the teacher-forcing vs. free-running mismatch, this work motivates the paper’s second setting—efficient end-to-end CoT learning without teacher forcing via internal verification using augmented data.

### 🔧 Extension

**RNNs Provably Solve Parity with Chain-of-Thought (CoT) Supervision** (2023)
- *Authors:* Wies et al.
- *Direct Connection:* This paper’s transformer results explicitly extend Wies (2023)’s RNN analysis on k-parity with step-by-step (CoT-like) intermediate supervision, translating their parity-learning mechanism and sample/iteration guarantees from RNNs to attention architectures.

---

## Synthesis: How Prior Work Led to This Paper

Wies (2023) analyzed how RNNs can learn k-parity efficiently when trained with chain-of-thought-style intermediate supervision, showing that supervising sub-computations circumvents difficulties faced by end-to-end training. Chain-of-Thought Prompting established that explicitly modeling intermediate reasoning steps boosts performance, crystallizing the notion of supervising a chain of partial results rather than only the final answer. Self-Consistency demonstrated that sampling multiple reasoning paths and aggregating them can serve as an internal correctness check, suggesting a route to verify intermediate steps without external labels. STaR operationalized this idea in training by augmenting data with self-generated rationales filtered by correctness, providing a concrete mechanism to improve models using verified intermediate chains. The canonical teacher forcing framework of Williams and Zipser provided the training protocol where ground-truth intermediate outputs are fed back during sequence generation, and Scheduled Sampling identified the shortcomings of teacher forcing for test-time generation, spotlighting the gap between training with supervision and end-to-end inference.

Building on these pieces, the present work generalizes Wies’s RNN parity analysis to transformers and formalizes CoT as intermediate parity supervision. It shows that teacher forcing yields one-step learning with a single gradient update, directly grounded in the teacher-forcing paradigm. Addressing the exposure-bias gap identified by Scheduled Sampling, it leverages self-consistency- and STaR-style augmentation to internally verify intermediate computations, proving efficient end-to-end learning without teacher forcing. Together, these ideas justify a provable pathway from supervised chains to self-verified chains within transformers on the k-parity problem.

---

*Analysis generated on: 2026-01-06T10:44:56.986205*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
