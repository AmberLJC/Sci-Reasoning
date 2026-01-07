# Prior Work Analysis Report

## Target Paper

**Title:** Learning to Act without Actions

**Conference:** ICLR 2024 (spotlight)

**Authors:** Dominik Schmidt, Minqi Jiang

**Keywords:** reinforcement learning, world models, inverse dynamics models, imitation learning, representation learning

**Abstract:** 
> Pre-training large models on vast amounts of web data has proven to be an effective approach for obtaining powerful, general models in domains such as language and vision. However, this paradigm has not yet taken hold in reinforcement learning. This is because videos, the most abundant form of embodied behavioral data on the web, lack the action labels required by existing methods for imitating behavior from demonstrations. We introduce **Latent Action Policies** (LAPO), a method for recovering ...

---

## Key Prior Works (6 papers with direct influence)

### 💡 Inspiration

**Diversity is All You Need: Learning Diverse Skills without a Reward Function (DIAYN)** (2018)
- *Authors:* Benjamin Eysenbach et al.
- *Direct Connection:* DIAYN’s mutual-information-driven discovery of discrete latent codes that control state transitions inspired LAPO’s use of latent variables tied to one-step dynamics to uncover action-equivalent factors from video.

### 🔍 Gap Identification

**Behavior Cloning from Observation** (2018)
- *Authors:* Faraz Torabi et al.
- *Direct Connection:* BCO formalized learning from state-only demonstrations by training an inverse dynamics model on agent-collected action-labeled experience, and LAPO directly addresses BCO’s core limitation by recovering action structure without any action-labeled interactions.

**Video PreTraining (VPT): Learning to Act by Watching Internet Videos** (2022)
- *Authors:* Bowen Baker et al.
- *Direct Connection:* VPT showed large-scale video pretraining for control by training an inverse dynamics model using a small action-labeled seed set, and LAPO removes this labeled dependency by first recovering latent action structure from unlabeled videos then fine-tuning with minimal labels.

### 📊 Baseline

**Generative Adversarial Imitation from Observation (GAIfO)** (2019)
- *Authors:* Faraz Torabi et al.
- *Direct Connection:* GAIfO learns policies from state-only trajectories via occupancy matching but does not infer action semantics, providing a primary baseline that LAPO surpasses by explicitly recovering a discrete action space from dynamics.

### 🔧 Extension

**ILPO: Imitation Learning from Observation by Inferring Latent Actions** (2019)
- *Authors:* Andrew Liu et al.
- *Direct Connection:* ILPO clusters state transitions into discrete latent actions and later maps them to real actions with limited interaction, a mechanism LAPO generalizes to high-dimensional video domains by learning latent actions and associated world/inverse-dynamics models purely from videos.

### 🔗 Related Problem

**Actionable Representations for Control** (2019)
- *Authors:* Benjamin Eysenbach et al.
- *Direct Connection:* By emphasizing representations that reflect the agent’s controllable aspects of dynamics, this work informed LAPO’s design of latent variables whose identities are determined by how they transform state transitions, i.e., action structure.

---

## Synthesis: How Prior Work Led to This Paper

Behavior Cloning from Observation (BCO) established a practical recipe for learning from state-only trajectories by first training an inverse dynamics model on a small set of action-labeled interactions and then inferring missing actions on demonstrations, crystallizing the central obstacle: dependence on action labels. Generative Adversarial Imitation from Observation (GAIfO) bypassed actions via occupancy matching between expert and learner state sequences, but left action semantics implicit and brittle in generalization. ILPO advanced a concrete mechanism for inferring discrete latent actions from state transitions and then mapping them to real actions with minimal environment interaction, demonstrating that latent action discovery can bridge state-only demos and executable policies. Video PreTraining (VPT) validated internet-scale video as a powerful pretraining source but relied on an action-labeled seed set to train an inverse dynamics model, tying scalability to labeled actions. In parallel, DIAYN showed that discrete latent variables aligned with changes in future states can be discovered by maximizing mutual information, while Actionable Representations for Control argued representations should encode the agent’s controllable aspects of dynamics. Together these works reveal both a path and a gap: latent variables that explain one-step dynamics can encode action-like factors, but prior pipelines still hinge on action labels or do not recover explicit action structure. The natural next step is to recover the true action space structure directly from unlabeled videos by learning latent variables whose identities are determined by how they transform states, yielding latent-action policies and dynamics models that can be minimally fine-tuned to real actions, thus marrying VPT-style scale with ILPO’s latent-action bridge and DIAYN’s dynamics-aligned latents.

---

*Analysis generated on: 2026-01-06T10:03:49.538567*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
