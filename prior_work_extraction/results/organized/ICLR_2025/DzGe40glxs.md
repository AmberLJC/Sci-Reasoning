# Prior Work Analysis Report

## Target Paper

**Title:** Interpreting Emergent Planning in Model-Free Reinforcement Learning

**Conference:** ICLR 2025 (oral)

**Authors:** Thomas Bush, Stephen Chung, Usman Anwar, Adrià Garriga-Alonso, David Krueger

**Keywords:** reinforcement learning, interpretability, planning, probes, model-free, mechanistic interpretability, sokoban

**Abstract:** 
> We present the first mechanistic evidence that model-free reinforcement learning agents can learn to plan. This is achieved by applying a methodology based on concept-based interpretability to a model-free agent in Sokoban -- a commonly used benchmark for studying planning. Specifically, we demonstrate that DRC, a generic model-free agent introduced by [Guez et al. (2019)](https://arxiv.org/abs/1901.03559), uses learned concept representations to internally formulate plans that both predict the ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Value Iteration Networks** (2016)
- *Authors:* Aviv Tamar et al.
- *Direct Connection:* VIN formalizes differentiable planning computations on grid worlds, shaping the notion of planning signals (e.g., propagating future consequences via value maps) that the paper probes for inside a model-free agent.

### 💡 Inspiration

**GAN Dissection: Visualizing and Understanding Generative Adversarial Networks** (2019)
- *Authors:* David Bau et al.
- *Direct Connection:* The intervention methodology of manipulating internal units to induce targeted output changes directly inspires the paper’s causal tests that activating or ablating plan features alters action selection.

**Concept Bottleneck Models** (2020)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* This work motivates treating concepts as causal variables; the paper borrows the paradigm of intervening on concept representations to establish that inferred plan concepts causally mediate policy behavior.

### 📊 Baseline

**Investigating Model-Free Reinforcement Learning for Planning** (2019)
- *Authors:* Arthur Guez et al.
- *Direct Connection:* This work introduces the DRC agent on Sokoban and hypothesizes that a purely model-free system may exhibit planning-like behavior, providing both the architecture and central open claim that this paper probes mechanistically.

### 🔧 Extension

**Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)** (2018)
- *Authors:* Been Kim et al.
- *Direct Connection:* The paper adapts TCAV-style concept probes to identify planning-relevant concepts in the agent’s internal representations and quantify their influence on decisions.

### 🔗 Related Problem

**Imagination-Augmented Agents for Deep Reinforcement Learning** (2017)
- *Authors:* Théophane Weber et al.
- *Direct Connection:* By establishing Sokoban as a planning benchmark and showing performance gains with extra test-time imagination, this work motivates the paper’s analysis of whether a model-free agent exhibits analogous planning-like benefits and internal plan formation.

---

## Synthesis: How Prior Work Led to This Paper

Guez et al. introduced the DRC agent and showed that a nominally model-free architecture can excel on Sokoban, raising the explicit possibility that such an agent might internally plan. Tamar et al. formalized differentiable planning via Value Iteration Networks, providing concrete computational primitives—like value propagation and rollout-like backups—against which internal signals can be conceptualized as planning computations in grid-based domains. Weber et al. demonstrated that explicit imagination modules improve performance on Sokoban and that more test-time computation can yield better behavior, connoting a planning-like scaling property for agents that simulate futures. Kim et al. developed TCAV, establishing concept-based linear probes that quantify whether human-interpretable concepts are present and influential in internal activations. Koh et al. introduced concept bottleneck models and emphasized interventions on concept variables to test causal mediation, framing concepts as manipulable causal factors. Bau et al. showed that targeted unit-level interventions can causally edit model behavior, validating intervention-based evidence of internal feature causality.

Together, these works expose a gap: strong external evidence of planning in model-free agents without mechanistic verification, interpretability methods for concept probing without causal confirmation in RL, and planning benchmarks that suggest test-time compute benefits. The paper synthesizes these strands by probing DRC’s representations for planning concepts, tracing plan formation consistent with value-propagation style computations, and applying causal interventions on the discovered plan features to demonstrate direct control over action choices. It further links the emergence of these internal plans to a planning-like benefit from added test-time computation, providing the mechanistic bridge between behavioral planning signatures and internal representations in a model-free agent.

---

*Analysis generated on: 2026-01-06T09:25:35.522335*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
