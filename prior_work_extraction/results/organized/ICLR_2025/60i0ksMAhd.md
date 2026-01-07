# Prior Work Analysis Report

## Target Paper

**Title:** BlendRL: A Framework for Merging Symbolic and Neural Policy Learning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Hikaru Shindo, Quentin Delfosse, Devendra Singh Dhami, Kristian Kersting

**Keywords:** Neuro-Symbolic AI, Differentiable Reasoning, Reinforcement Learning, Interpretable AI, First-order logic

**Abstract:** 
> Humans can leverage both symbolic reasoning and intuitive responses. In contrast, reinforcement learning policies are typically encoded in either opaque systems like neural networks or symbolic systems that rely on predefined symbols and rules. This disjointed approach severely limits the agents’ capabilities, as they often lack either the flexible low-level reaction characteristic of neural agents or the interpretable reasoning of symbolic agents. 

To overcome this challenge, we introduce *Ble...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Relational Reinforcement Learning** (2001)
- *Authors:* Sašo Džeroski et al.
- *Direct Connection:* It established first-order logic policy representations for RL, providing the symbolic policy formalism that BlendRL retains while making it differentiable and co-trainable with neural networks.

### 💡 Inspiration

**DeepProbLog: Neural Probabilistic Logic Programming** (2018)
- *Authors:* Robin Manhaeve et al.
- *Direct Connection:* Its end-to-end coupling of neural perception with a differentiable logic program directly inspired BlendRL’s joint optimization of neural and logical policy components.

### 🔍 Gap Identification

**Towards Deep Symbolic Reinforcement Learning** (2016)
- *Authors:* Marta Garnelo et al.
- *Direct Connection:* By separating neural perception from symbolic planning with hand-crafted predicates on Atari, it exposed the brittleness of disjoint pipelines that BlendRL replaces with a unified hybrid policy.

**Verifiable Reinforcement Learning via Policy Extraction (VIPER)** (2018)
- *Authors:* Osbert Bastani et al.
- *Direct Connection:* VIPER’s post-hoc decision-tree extraction from deep RL highlighted the lack of jointly learned, interpretable policies—a gap BlendRL fills by learning neural and symbolic policies together.

### 🔧 Extension

**Logic Tensor Networks: Deep Learning and Logical Reasoning** (2016)
- *Authors:* Luciano Serafini et al.
- *Direct Connection:* BlendRL adopts LTN-style t-norm–based differentiable first-order logic to parameterize its symbolic policy head and backpropagate through logical rules during joint training.

### 🔗 Related Problem

**Neural Logic Machines** (2019)
- *Authors:* Honghua Dong et al.
- *Direct Connection:* NLM demonstrated that differentiable multi-step relational inference can improve control, informing BlendRL’s design of an embedded reasoning module inside the policy.

**Reward Machines: Exploiting Reward Function Structure in Reinforcement Learning** (2019)
- *Authors:* Fernando F. Icarte et al.
- *Direct Connection:* By showing that explicit symbolic task structure yields robustness and transfer, it motivated BlendRL to embed symbolic structure at the policy level rather than only in rewards.

---

## Synthesis: How Prior Work Led to This Paper

Relational Reinforcement Learning introduced first-order logic as a policy representation, showing how logical predicates and rules can drive action selection in an MDP, but relied on non-differentiable learning over predefined symbols. Deep Symbolic Reinforcement Learning separated neural perception from a symbolic planner in Atari, revealing the promise of symbolic structure for generalization while exposing brittleness from hand-crafted predicates and disjoint training. Logic Tensor Networks provided t‑norm–based differentiable semantics for first‑order logic, enabling gradients to flow through weighted rules. DeepProbLog demonstrated end-to-end learning where neural modules populate symbols that a probabilistic logic program reasons over, establishing a practical recipe for co-training perception and logic. Neural Logic Machines showed that differentiable multi-step relational inference improves policy learning on tasks demanding algorithmic generalization. Reward Machines formalized high-level task structure via automata, empirically linking explicit symbolic structure to robustness and transfer in RL. VIPER extracted interpretable decision trees from deep policies but did so post‑hoc, underscoring the need for jointly learned, faithful symbolic control.
Together, these works suggested a clear opportunity: marry the interpretability and structure of first-order reasoning with the reactive flexibility of deep policies in a single, end-to-end trainable agent. Building on LTN/DeepProbLog’s differentiable logic to make symbolic decisions optimizable by gradient descent, adopting NLM-style relational inference capacity, and addressing the brittleness of disjoint pipelines highlighted by deep symbolic RL and VIPER, the resulting synthesis naturally yields a blended policy architecture that inherits robustness benefits akin to Reward Machines while remaining reactive and learnable on Atari-scale environments.

---

*Analysis generated on: 2026-01-06T15:04:08.560298*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
