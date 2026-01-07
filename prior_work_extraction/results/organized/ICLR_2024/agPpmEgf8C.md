# Prior Work Analysis Report

## Target Paper

**Title:** Predictive auxiliary objectives in deep RL mimic learning in the brain

**Conference:** ICLR 2024 (oral)

**Authors:** Ching Fang, Kim Stachenfeld

**Keywords:** hippocampus, neuroscience, cognitive science, deep reinforcement learning, representation learning, prediction

**Abstract:** 
> The ability to predict upcoming events has been hypothesized to comprise a key aspect of natural and machine cognition. This is supported by trends in deep reinforcement learning (RL), where self-supervised auxiliary objectives such as prediction are widely used to support representation learning and improve task performance. Here, we study the effects predictive auxiliary objectives have on representation learning across different modules of an RL system and how these mimic representational cha...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The hippocampus as a predictive map** (2017)
- *Authors:* M. M. Stachenfeld et al.
- *Direct Connection:* This work advanced the predictive-map view that hippocampal representations implement SR-like predictive codes, directly motivating the paper’s comparison between auxiliary predictive RL representations and hippocampal neural changes.

**Improving Generalization for Temporal-Difference Learning: The Successor Representation** (1993)
- *Authors:* Peter Dayan
- *Direct Connection:* It introduced the successor representation and its discounted predictive horizon, providing the formal mechanism the paper manipulates to study how prediction length shapes representational transfer and brain-like structure.

**Successor Features for Transfer in Reinforcement Learning** (2017)
- *Authors:* André Barreto et al.
- *Direct Connection:* It showed that predictive successor features enable transfer across tasks, which the paper builds upon by identifying when longer predictive horizons most enhance representational transfer.

### 💡 Inspiration

**Reinforcement Learning with Unsupervised Auxiliary Tasks** (2017)
- *Authors:* Max Jaderberg et al.
- *Direct Connection:* This paper established that predictive auxiliary tasks (e.g., pixel control, reward prediction) stabilize and accelerate deep RL, inspiring the paper’s systematic placement of predictive objectives across agent modules.

### 🔧 Extension

**Data-Efficient Reinforcement Learning with Self-Predictive Representations** (2021)
- *Authors:* Max Schwarzer et al.
- *Direct Connection:* By showing multi-step latent self-prediction improves RL, it directly motivates the paper’s analysis of longer predictive horizons and their effects on representation transfer.

### 🔗 Related Problem

**Dreamer: Reinforcement Learning by Latent Imagination** (2020)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* Demonstrating that learning a predictive latent dynamics model yields stable, data-efficient control supports the paper’s claim that prediction particularly benefits resource-limited architectures.

---

## Synthesis: How Prior Work Led to This Paper

A predictive account of hippocampal coding proposed that neural representations embody future-occupancy structure, formalized via the successor representation (SR) and its discount-controlled horizon. The SR framework established how predictive horizons shape representational geometry, while successor features extended this idea to practical transfer: predictive features can be reused to generalize across tasks. In deep reinforcement learning, auxiliary prediction objectives were shown to stabilize and accelerate representation learning, with UNREAL demonstrating that self-supervised predictive signals (e.g., pixel control, reward prediction) can strengthen state encodings. Moving from one-step to multi-step, self-predictive latent objectives such as SPR highlighted that explicitly predicting future embeddings over several steps further improves data efficiency and robustness. In parallel, model-based approaches like Dreamer demonstrated that learning a latent predictive world model produces more stable, compact, and useful representations for control, especially under limited data or capacity. Together, these works established that prediction—its horizon and where it is imposed in the architecture—strongly shapes learned representations. What remained unclear was how predictive objectives placed across specific agent modules alter representational structure under resource constraints, which horizons best support transfer, and whether these induced changes mirror hippocampal dynamics. By systematically varying where and how far ahead prediction is enforced, and by aligning the resulting representational signatures with hippocampal findings, the paper synthesizes SR-inspired theory with auxiliary-task practice to show that longer-horizon predictive objectives in resource-limited settings yield more transferable, brain-like representations.

---

*Analysis generated on: 2026-01-06T07:13:34.356994*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
