# Prior Work Analysis Report

## Target Paper

**Title:** Learning Performance-Improving Code Edits

**Conference:** ICLR 2024 (spotlight)

**Authors:** Alexander G Shypula, Aman Madaan, Yimeng Zeng, Uri Alon, Jacob R. Gardner, Yiming Yang, Milad Hashemi, Graham Neubig, Parthasarathy Ranganathan, Osbert Bastani, Amir Yazdanbakhsh

**Keywords:** Large Language Models, Retrieval Augmented Generation, Program Synthesis, Program Optimization, Fine-Tuning, Goal-Conditioning, Data Augmentation, Self-Play, Synthetic Dataset, Performance Optimization, Machine Learning for Code Optimization, Dataset

**Abstract:** 
> With the decline of Moore's law, optimizing program performance has become a major focus of software research. However, high-level optimizations such as API and algorithm changes remain elusive due to the difficulty of understanding the semantics of code. Simultaneously, pretrained large language models (LLMs) have demonstrated strong capabilities at solving a wide range of programming tasks. To that end, we introduce a framework for adapting LLMs to high-level program optimization. First, we cu...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Competition-Level Code Generation with AlphaCode** (2022)
- *Authors:* Yujia Li et al.
- *Direct Connection:* AlphaCode established the competitive-programming setting with curated Codeforces-style problems and unit tests, providing the exact problem domain and test-driven verification substrate from which the present work mines performance-improving edit pairs.

**APPS: A Benchmark for Code Generation** (2021)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* APPS codified unit-test–based evaluation for code generation, directly underpinning this work’s requirement to verify semantic equivalence of edits while optimizing runtime.

### 💡 Inspiration

**Self-Refine: Iterative Refinement with Self-Feedback** (2023)
- *Authors:* Aman Madaan et al.
- *Direct Connection:* Self-Refine introduced an LLM self-editing loop guided by feedback, which this work adapts by substituting textual feedback with simulator-based performance signals to iteratively propose performance-improving edits.

**Reflexion: Language Agents with Verbal Reinforcement Learning** (2023)
- *Authors:* Noah Shinn et al.
- *Direct Connection:* Reflexion demonstrated that iterative reflection across attempts improves code solutions, directly informing the self-play/iterate-and-evaluate editing procedure used for performance optimization.

**Decision Transformer: Reinforcement Learning via Sequence Modeling** (2021)
- *Authors:* Lili Chen et al.
- *Direct Connection:* Decision Transformer’s return-conditioned generation inspired this work’s goal-conditioned training, where models condition on desired runtime/speedup targets when producing code edits.

### 🔍 Gap Identification

**OpenTuner: An Extensible Framework for Program Autotuning** (2014)
- *Authors:* Jason Ansel et al.
- *Direct Connection:* OpenTuner exemplifies search-based autotuning over numeric parameters, whose inability to perform semantic API/algorithm changes directly motivates learning from human performance-improving code edits.

### 🔗 Related Problem

**Discovering faster sorting algorithms using deep reinforcement learning** (2023)
- *Authors:* Daniel J. Mankowitz et al.
- *Direct Connection:* AlphaDev showed learning-based discovery of faster implementations at the assembly level, motivating a learning approach to performance but highlighting the gap in high-level, semantics-preserving code edits addressed here.

---

## Synthesis: How Prior Work Led to This Paper

Competitive-programming benchmarks such as AlphaCode established a rich, test-driven domain where solutions are validated by comprehensive unit tests, and APPS generalized this notion by framing program synthesis evaluation around unit-test correctness. These settings provided abundant, verifiable code artifacts and the methodology to assert semantic equivalence. Beyond correctness, Self-Refine introduced an LLM-centric paradigm of iterative self-editing guided by feedback, while Reflexion showed that reflective, multi-trial refinement can systematically improve code outcomes. In parallel, Decision Transformer demonstrated that conditioning sequence models on target returns can steer behavior toward desired outcomes, an idea naturally extensible to performance targets in code. Learning-driven performance optimization has also been explored at lower levels: AlphaDev revealed that RL can discover faster implementations, and OpenTuner popularized autotuning over parameter spaces—both illuminating opportunities yet remaining limited to low-level or parametric changes rather than high-level semantic edits.
Collectively, these works suggested a path: leverage unit-test–verified programming tasks to ensure semantic preservation; couple iterative self-editing with an objective signal; and condition generation on explicit performance goals. The natural next step was to mine real human optimization trajectories from competitive programming, evaluate edits deterministically, and train a goal-conditioned editor that iterates with reliable performance feedback—thereby moving beyond low-level autotuning to high-level, semantics-preserving performance improvements.

---

*Analysis generated on: 2026-01-06T16:44:36.769195*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
