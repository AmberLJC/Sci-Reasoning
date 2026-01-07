# Prior Work Analysis Report

## Target Paper

**Title:** Efficient Episodic Memory Utilization of Cooperative Multi-Agent Reinforcement Learning

**Conference:** ICLR 2024 (oral)

**Authors:** Hyungho Na, Yunkyeong Seo, Il-chul Moon

**Keywords:** Multi-agent reinforcement learning, episodic control, episodic incentive, state embedding

**Abstract:** 
> In cooperative multi-agent reinforcement learning (MARL), agents aim to achieve a common goal, such as defeating enemies or scoring a goal. Existing MARL algorithms are effective but still require significant learning time and often get trapped in local optima by complex tasks, subsequently failing to discover a goal-reaching policy. To address this, we introduce Efficient episodic Memory Utilization (EMU) for MARL, with two primary objectives: (a) accelerating reinforcement learning by leveragi...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Model-Free Episodic Control** (2016)
- *Authors:* Charles Blundell et al.
- *Direct Connection:* EMU builds on the core idea from MFEC of storing and recalling high-return state–action experiences from an episodic buffer to accelerate learning, repurposing this principle for cooperative MARL.

### 💡 Inspiration

**Episodic Curiosity through Reachability** (2018)
- *Authors:* Nikolay Savinov et al.
- *Direct Connection:* EMU adapts the concept of using a learned embedding and episodic memory to compute auxiliary rewards, shifting from reachability/novelty bonuses to desirability-based incentives for promoting beneficial states.

**Never Give Up: Learning Directed Exploration Strategies** (2020)
- *Authors:* Adrià Puigdomènech Badia et al.
- *Direct Connection:* EMU draws on NGU’s episodic-memory-driven intrinsic reward mechanism, replacing novelty scoring with a desirability metric that augments the TD target and biases exploration away from local optima.

### 🔍 Gap Identification

**Go-Explore: a New Approach for Hard-Exploration Problems** (2019)
- *Authors:* Adrien Ecoffet et al.
- *Direct Connection:* EMU directly addresses the detachment/derailment failures identified by Go-Explore by explicitly incentivizing returns to promising states via an episodic archive and desirability-weighted promotion of transitions.

### 📊 Baseline

**QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning** (2018)
- *Authors:* Tabish Rashid et al.
- *Direct Connection:* EMU integrates with and improves upon QMIX’s value-decomposition Q-learning by modifying its TD targets with episodic incentives and memory-guided sampling to accelerate cooperative policy discovery.

### 🔧 Extension

**Neural Episodic Control** (2017)
- *Authors:* Alexander Pritzel et al.
- *Direct Connection:* EMU extends NEC’s embedding-based episodic lookup by learning a task-specific encoder–decoder that produces semantically coherent memory embeddings to guide exploratory recall in multi-agent settings.

---

## Synthesis: How Prior Work Led to This Paper

Model-Free Episodic Control showed that storing high-return state–action experiences and retrieving them via nearest neighbors can dramatically speed learning by exploiting episodic memory. Neural Episodic Control refined this idea with a learned embedding and a differentiable memory, enabling semantically meaningful retrieval that aligns recall with task structure. Episodic Curiosity through Reachability introduced a learned reachability embedding coupled with an episodic memory to compute intrinsic rewards, using distances in representation space to motivate exploration toward novel but reachable states. Never Give Up broadened this line by maintaining a per-episode memory to compute episodic novelty bonuses that complement life-long exploration, demonstrating how episodic signals can shape behavior and accelerate credit propagation. Meanwhile, Go-Explore highlighted the failure modes of standard exploration—detachment and derailment—and argued for archiving and revisiting promising states as a path to overcoming local optima. In cooperative settings, QMIX formalized a practical Q-learning backbone through monotonic value decomposition under centralized training and decentralized execution, providing the prevailing target and training pipeline for many MARL systems.
Together these works suggest that episodic memory can both recall semantically useful experiences and produce auxiliary signals that guide exploration, yet they lack a mechanism tailored to cooperative MARL that explicitly promotes desirable joint states and integrates with value decomposition. The synthesis is to learn a representation that makes episodic memories semantically coherent for multi-agent recall and to transform episodic assessments into a desirability-based incentive that directly augments the TD targets within a QMIX-style learner, thereby accelerating learning and escaping local optima in cooperative tasks.

---

*Analysis generated on: 2026-01-06T08:41:14.921072*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
