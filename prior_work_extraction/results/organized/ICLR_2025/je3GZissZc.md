# Prior Work Analysis Report

## Target Paper

**Title:** Instant Policy: In-Context Imitation Learning via Graph Diffusion

**Conference:** ICLR 2025 (oral)

**Authors:** Vitalis Vosylius, Edward Johns

**Keywords:** In-context Imitation Learning, Robotic Manipulation, Graph Neural Networks, Diffusion Models

**Abstract:** 
> Following the impressive capabilities of in-context learning with large transformers, In-Context Imitation Learning (ICIL) is a promising opportunity for robotics. We introduce Instant Policy, which learns new tasks instantly from just one or two demonstrations, achieving ICIL through two key components. First, we introduce inductive biases through a graph representation and model ICIL as a graph generation problem using a learned diffusion process, enabling structured reasoning over demonstrati...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**One-Shot Imitation Learning** (2017)
- *Authors:* Yan Duan et al.
- *Direct Connection:* It formalized the problem of learning new tasks from a single demonstration in robotics, providing the problem setup and evaluation paradigm that this paper targets but achieves via pure in-context conditioning instead of meta-updates.

### 💡 Inspiration

**Language Models are Few-Shot Learners** (2020)
- *Authors:* Tom B. Brown et al.
- *Direct Connection:* This work popularized in-context learning by conditioning on a handful of prompt examples, directly inspiring the test-time, no-gradient-update ICIL setting adopted and operationalized in this paper.

**Diffuser: Diffusion Models for Planning** (2022)
- *Authors:* Michael Janner et al.
- *Direct Connection:* This work reframed control as conditional denoising diffusion over trajectories, providing the key generative-control insight that is extended here to graph-structured diffusion conditioned on demonstration graphs.

### 🔍 Gap Identification

**Learning Latent Plans from Play** (2019)
- *Authors:* Corey Lynch et al.
- *Direct Connection:* It demonstrated that large, task-agnostic play can train generalist policies but relies on human collection, motivating this paper’s use of virtually unlimited simulation pseudo-demonstrations to remove expert data dependency.

### 🔧 Extension

**DiGress: Discrete Denoising Diffusion for Graph Generation** (2023)
- *Authors:* Thibaut Vignac et al.
- *Direct Connection:* The paper adapts DiGress-style permutation-equivariant diffusion over node/edge types to generate policy outputs on a structured demonstration–observation–action graph, enabling the core graph-diffusion formulation of ICIL.

### 🔗 Related Problem

**Trajectory Transformer: Off-Policy Reinforcement Learning via Sequence Modeling** (2021)
- *Authors:* Michael Janner et al.
- *Direct Connection:* By casting control as sequence modeling over trajectories, it established the idea of conditioning policy behavior on context trajectories, a principle this paper retains while changing the representation to structured graphs and the generator to diffusion.

**Decision Transformer: Reinforcement Learning via Sequence Modeling** (2021)
- *Authors:* Lili Chen et al.
- *Direct Connection:* It showed that transformers can exploit trajectory context for in-context policy adaptation, motivating the paper’s pursuit of ICIL but with a graph-based diffusion model instead of an autoregressive sequence model.

---

## Synthesis: How Prior Work Led to This Paper

Few-shot conditioning without parameter updates was crystallized by the discovery that large sequence models can perform in-context learning when given example prompts; Brown et al. showed that behavior can be steered by a handful of demonstrations in-context. In robotics, Duan et al. defined the one-shot imitation problem—execute a new task from a single demonstration—typically solved through meta-learning, while Janner et al.’s Trajectory Transformer and Chen et al.’s Decision Transformer recast control as sequence modeling, indicating that trajectories themselves can serve as powerful contextual prompts for adaptation. Complementing these sequence models, Diffuser established that denoising diffusion can generate feasible, multi-modal control trajectories under rich conditioning, suggesting a robust generative mechanism for policies. In parallel, DiGress introduced discrete, permutation-equivariant diffusion over graphs, enabling generation over structured node/edge types and relations rather than flat sequences. Finally, Lynch et al. showed that broad, unlabeled play data can substitute for curated demonstrations to build generalist manipulation behaviors, albeit with costly human collection.
Together, these works expose an opportunity: use in-context demonstrations to specify a task at test time, but process them with an object- and relation-centric representation and a powerful generative engine, and train not from scarce expert demos but from abundant synthetic trajectories. The present paper synthesizes these ideas by representing demonstrations, observations, and actions as a graph and learning a diffusion process over that graph, while scaling training via simulation-generated pseudo-demonstrations—an immediate next step given the convergence of in-context conditioning, diffusion-based control, and graph generative modeling.

---

*Analysis generated on: 2026-01-06T10:12:38.372271*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
