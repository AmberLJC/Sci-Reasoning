# Prior Work Analysis Report

## Target Paper

**Title:** Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning

**Conference:** ICLR 2025 (oral)

**Authors:** Gangwei Jiang, Caigao JIANG, Zhaoyi Li, Siqiao Xue, JUN ZHOU, Linqi Song, Defu Lian, Ying Wei

**Keywords:** Catastrophic forgetting; Large language model; Instruction tuning

**Abstract:** 
> Catastrophic forgetting (CF) poses a significant challenge in machine learning, where a model forgets previously learned information upon learning new tasks. 
Despite the advanced capabilities of Large Language Models (LLMs), they continue to face challenges with CF during continual learning. The majority of existing research focuses on analyzing forgetting patterns through a singular training sequence, thereby overlooking the intricate effects that diverse tasks have on model behavior.
Our stud...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**LAMOL: Language Modeling for Lifelong Language Learning** (2020)
- *Authors:* Fan-Keng Sun et al.
- *Direct Connection:* By formalizing continual learning for language modeling and using generative replay to combat forgetting, it establishes the continual NLP setup that this work adopts for instruction tuning and directly contrasts against with function-vector based analysis and mitigation.

### 💡 Inspiration

**Editing Models with Task Arithmetic** (2023)
- *Authors:* Gabrielle Ilharco et al.
- *Direct Connection:* The idea that behaviors/tasks can be linearly represented and composed via a vector—computed as the difference between fine-tuned and base models—directly inspires replacing weight-space “task vectors” with activation-space “function vectors” to characterize and mitigate forgetting.

**Toy Models of Superposition in Neural Networks** (2022)
- *Authors:* Nelson Elhage et al.
- *Direct Connection:* Its finding that features superpose and interfere in the residual stream underpins the hypothesis that task interference—and thus forgetting—emerges from biased activation of functions, which the function vector formalism makes measurable and correctable.

### 🔍 Gap Identification

**Overcoming catastrophic forgetting in neural networks** (2017)
- *Authors:* James Kirkpatrick et al.
- *Direct Connection:* As a canonical parameter-importance approach that assumes forgetting arises from weight overwriting, it provides the precise limitation—parameter-centric explanations and remedies—that the function-vector, activation-bias account challenges and replaces.

**Don’t Stop Pretraining: Adapt Language Models to Domains and Tasks** (2020)
- *Authors:* Suchin Gururangan et al.
- *Direct Connection:* This paper empirically shows that continued domain/task-specific training degrades out-of-domain abilities, motivating a mechanism-level account that this work provides via function-activation bias rather than parameter overwrite.

### 🔧 Extension

**Representation Engineering: A Top-Down Approach to Steering LLMs** (2024)
- *Authors:* Nora Rimsky et al.
- *Direct Connection:* This work’s method of constructing behavior-specific activation steering vectors from contrasting prompt sets is directly extended by formalizing such activation differences as function vectors that diagnose when a function’s activation is biased and then rebalancing it to mitigate CF.

---

## Synthesis: How Prior Work Led to This Paper

Weight-space task vectors showed that a task’s effect can be captured by a linear difference in parameters and composed arithmetically, revealing a compact, directional representation of behavior. Activation-based representation engineering then demonstrated that contrasting prompt sets yield steering vectors in residual space that causally modulate behaviors at inference time, grounding the idea that functions live in and can be controlled via activation subspaces. Parameter-importance methods like Elastic Weight Consolidation framed catastrophic forgetting as weight overwriting and sought to prevent specific parameter drift, while LAMOL established continual learning setups for language modeling and popularized replay as a mitigation. Empirically, domain-adaptive pretraining was shown to harm out-of-domain performance, underscoring persistent forgetting in NLP despite stronger models. Complementarily, toy models of superposition argued that features compete within limited activation subspaces, suggesting interference arises in representation space rather than solely from parameter changes.
Together these strands expose a gap: continual instruction tuning lacks a mechanism-level, model-dependent indicator of forgetting grounded in activation space and a principled way to rebalance competing functions without heavy replay or parameter freezing. By synthesizing weight-space compositionality with activation steering and superposition insights, it is natural to define function vectors that summarize a function’s activation direction, use them to detect when training biases function activation, and then directly adjust those activations to characterize and mitigate catastrophic forgetting across tasks and models.

---

*Analysis generated on: 2026-01-06T19:09:30.712134*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
