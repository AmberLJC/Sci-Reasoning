# Prior Work Analysis Report

## Target Paper

**Title:** SD-LoRA: Scalable Decoupled Low-Rank Adaptation for Class Incremental Learning

**Conference:** ICLR 2025 (oral)

**Authors:** Yichen Wu, Hongming Piao, Long-Kai Huang, Renzhen Wang, Wanhua Li, Hanspeter Pfister, Deyu Meng, Kede Ma, Ying Wei

**Keywords:** Continual learning; Low-rank adaptation

**Abstract:** 
> Continual Learning (CL) with foundation models has recently emerged as a promising paradigm to exploit abundant knowledge acquired during pre-training for tackling sequential tasks. However, existing prompt-based and Low-Rank Adaptation-based (LoRA-based) methods often require expanding a prompt/LoRA pool or retaining samples of previous tasks, which poses significant scalability challenges as the number of tasks grows. 
To address these limitations, we propose Scalable Decoupled LoRA (SD-LoRA) ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**LoRA: Low-Rank Adaptation of Large Language Models** (2022)
- *Authors:* Edward J. Hu et al.
- *Direct Connection:* LoRA provides the core low-rank adapter parameterization (W + BA) that SD-LoRA directly builds upon and re-parameterizes by separating update magnitude and direction across tasks.

### 💡 Inspiration

**Weight Normalization: A Simple Reparameterization to Accelerate Training of Deep Neural Networks** (2016)
- *Authors:* Tim Salimans et al.
- *Direct Connection:* Weight Normalization’s decoupling of weight magnitude and direction motivates SD-LoRA’s explicit separation of LoRA update magnitude and direction to stabilize optimization across sequential tasks.

**Continual Learning of Context-Dependent Processing in Neural Networks** (2019)
- *Authors:* Guangshe Zeng et al.
- *Direct Connection:* The OWM approach’s idea of protecting prior knowledge by constraining update directions inspires SD-LoRA’s focus on controlling the directional component of LoRA updates to reduce interference across tasks.

### 🔍 Gap Identification

**DualPrompt: Complementary Prompting for Rehearsal-Free Continual Learning** (2022)
- *Authors:* Zhou et al.
- *Direct Connection:* DualPrompt’s complementary prompt pools improved rehearsal-free CIL but still required expanding and managing multiple prompts per task, a scalability gap SD-LoRA addresses by eliminating pool expansion through decoupled LoRA updates.

### 📊 Baseline

**Learning to Prompt for Continual Learning** (2022)
- *Authors:* Wang et al.
- *Direct Connection:* L2P established rehearsal-free class-incremental learning with prompt pools that grow with tasks, a primary baseline whose pool-expansion scalability limitation SD-LoRA explicitly avoids by a single decoupled LoRA path.

### 🔧 Extension

**DoRA: Weight-Decomposed Low-Rank Adaptation** (2024)
- *Authors:* Liu et al.
- *Direct Connection:* DoRA introduced decomposing weights into magnitude and direction within a LoRA-style update, and SD-LoRA extends this idea to the continual learning regime by continually decoupling and updating the LoRA components’ magnitude and direction to achieve stability-plasticity without rehearsal.

### 🔗 Related Problem

**Mode Connectivity in Loss Landscapes of Neural Networks** (2018)
- *Authors:* Timur Garipov et al.
- *Direct Connection:* The demonstration of low-loss trajectories and overlapping basins between solutions informs SD-LoRA’s theoretical and empirical claim that decoupled LoRA updates can follow low-loss paths that intersect across tasks.

---

## Synthesis: How Prior Work Led to This Paper

Low-rank adaptation introduced a compact update parameterization by injecting trainable rank-constrained matrices into pretrained weights, enabling effective fine-tuning with very few parameters. Weight-decomposed adaptations advanced this by explicitly factorizing weight updates into magnitude and direction, revealing that decoupling these components can yield more stable and efficient optimization. Classical reparameterization via weight normalization showed that separating scale from direction simplifies optimization geometry and improves convergence behavior. In continual learning, Learning to Prompt demonstrated that rehearsal-free class-incremental learning is achievable by selecting task-appropriate prompts from a growing pool, while DualPrompt further improved accuracy via complementary prompt sets but retained the intrinsic pool expansion and management overhead. Orthogonal Weight Modification highlighted that preserving past knowledge can be achieved by controlling update directions, reducing interference across tasks without storing data. Concurrently, mode connectivity revealed that seemingly different solutions can be connected by low-loss paths and even share overlapping low-loss regions, suggesting that updates guided along appropriate directions can remain within shared basins. Together, these works suggested an opportunity: combine the parameter efficiency of low-rank adapters with an explicit magnitude–direction decomposition to control interference, while avoiding the scalability issues of prompt or adapter pools. By continually decoupling and steering the directional component of low-rank updates along low-loss trajectories and managing magnitude separately, it becomes possible to achieve rehearsal-free, scalable class-incremental learning that preserves prior tasks and maintains parameter efficiency.

---

*Analysis generated on: 2026-01-06T16:29:51.118552*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
