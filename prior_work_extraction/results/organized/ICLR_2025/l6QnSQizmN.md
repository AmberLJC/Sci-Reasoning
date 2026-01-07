# Prior Work Analysis Report

## Target Paper

**Title:** Online Reinforcement Learning in Non-Stationary Context-Driven Environments

**Conference:** ICLR 2025 (spotlight)

**Authors:** Pouya Hamadanian, Arash Nasr-Esfahany, Malte Schwarzkopf, Siddhartha Sen, Mohammad Alizadeh

**Keywords:** catastrophic forgetting, reinforcement learning, context-driven MDP, online learning, non-stationary

**Abstract:** 
> We study online reinforcement learning (RL) in non-stationary environments, where a time-varying exogenous context process affects the environment dynamics. Online RL is challenging in such environments due to "catastrophic forgetting" (CF). The agent tends to forget prior knowledge as it trains on new experiences. Prior approaches to mitigate this issue assume task labels (which are often not available in practice), employ brittle regularization heuristics, or use off-policy methods that suffer...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Contextual Markov Decision Processes** (2015)
- *Authors:* Hallak et al.
- *Direct Connection:* LCPO builds on the Contextual MDP formulation where an exogenous context process modulates dynamics, anchoring policies on samples drawn from contexts outside the current distribution.

### 💡 Inspiration

**Learning without Forgetting** (2016)
- *Authors:* Li et al.
- *Direct Connection:* LCPO adopts LwF’s core idea of preserving old outputs via distillation, instantiating it as a policy KL on replayed states from previous contexts during on-policy updates.

**Policy Distillation** (2015)
- *Authors:* Rusu et al.
- *Direct Connection:* LCPO leverages distillation-style constraints to match prior policy behavior on old-context states, translating policy distillation’s functional preservation into a continual RL setting.

### 🔍 Gap Identification

**Overcoming Catastrophic Forgetting in Neural Networks** (2017)
- *Authors:* Kirkpatrick et al.
- *Direct Connection:* LCPO directly addresses EWC’s brittleness of parameter-importance regularization by shifting to functional (output-space) anchoring on past experiences to preserve prior behavior.

**Progress & Compress: A Scalable Framework for Continual Learning** (2018)
- *Authors:* Schwarz et al.
- *Direct Connection:* LCPO targets the continual RL setting without task labels that P&C assumes, replacing task-bound consolidation phases with label-free local constraints on old experiences.

### 📊 Baseline

**Proximal Policy Optimization Algorithms** (2017)
- *Authors:* Schulman et al.
- *Direct Connection:* LCPO modifies the PPO update by adding a context-aware local constraint on replayed old-context samples, making PPO the primary on-policy baseline it improves upon.

### 🔧 Extension

**Trust Region Policy Optimization** (2015)
- *Authors:* Schulman et al.
- *Direct Connection:* LCPO generalizes TRPO’s KL-based trust-region idea by applying a targeted, local KL constraint on states from prior contexts to anchor behavior while optimizing on current-context data.

---

## Synthesis: How Prior Work Led to This Paper

Trust-region policy methods established that constraining policy updates via a KL divergence improves stability, first globally with TRPO’s trust region and later approximately with PPO’s clipped surrogate objective. In parallel, continual learning revealed that preserving function outputs is often more reliable than parameter constraints: Learning without Forgetting introduced distillation to keep old predictions intact without storing task labels, and policy distillation showed how KL-based matching can preserve and consolidate behaviors in RL. Parameter-importance approaches like EWC offered a simple regularization route to mitigate forgetting, but their weight-space heuristics proved brittle under distribution shift. Continual RL frameworks such as Progress & Compress further emphasized consolidation across tasks but typically required explicit task boundaries. Meanwhile, the Contextual MDP formalism clarified non-stationarity driven by an exogenous context process, highlighting that the same state-action pair can induce different dynamics as context drifts.
Together, these strands suggested a natural opportunity: combine the stability of trust-region updates with output-space preservation from distillation, and target them specifically at states from past contexts in a label-free manner. LCPO synthesizes this by adding a local, context-aware KL constraint—computed on replayed samples from outside the current context distribution—into an on-policy update (e.g., PPO-style), thereby preserving prior behavior without relying on task labels or unstable off-policy corrections while optimizing return on the current context.

---

*Analysis generated on: 2026-01-06T09:01:13.526302*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
