# Prior Work Analysis Report

## Target Paper

**Title:** Robust agents learn causal world models

**Conference:** ICLR 2024 (oral)

**Authors:** Jonathan Richens, Tom Everitt

**Keywords:** causality, generalisation, causal discovery, domain adaptation, out-of-distribution generalization

**Abstract:** 
> It has long been hypothesised that causal reasoning plays a fundamental role in robust and general intelligence. However, it is not known if agents must learn causal models in order to generalise to new domains, or if other inductive biases are sufficient. We answer this question, showing that any agent capable of satisfying a regret bound for a large set of distributional shifts must have learned an approximate causal model of the data generating process, which converges to the true causal mode...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Causality: Models, Reasoning, and Inference** (2009)
- *Authors:* Judea Pearl et al.
- *Direct Connection:* This work provides the structural causal model (SCM) framework and intervention semantics that the paper relies on to define a “causal world model” and to formalize distributional shifts as interventions over the data-generating process.

**Agent Incentives: A Causal Perspective** (2021)
- *Authors:* Tom Everitt et al.
- *Direct Connection:* By introducing causal influence diagrams to formalize agents, decisions, and interventions, this work provides the agent–causal formalism that the paper uses to relate an agent’s internal model and low regret under distributional shifts to the true SCM.

### 💡 Inspiration

**A general theory of transportability** (2013)
- *Authors:* Elias Bareinboim et al.
- *Direct Connection:* By formalizing when and how causal knowledge can be transported across domains via selection diagrams, this work inspires the paper’s framing that broad cross-domain performance requires internalizing the causal generative process to enable transport across many shifts.

### 🔍 Gap Identification

**Invariant Risk Minimization** (2019)
- *Authors:* Martin Arjovsky et al.
- *Direct Connection:* IRM’s proposal to learn predictors invariant across environments motivates the present paper’s stronger necessity result by addressing IRM’s limitation that invariance alone lacks guarantees of recovering the true causal model or ensuring robustness to large intervention families.

### 🔧 Extension

**Causal inference using invariant prediction: identification and confidence sets** (2016)
- *Authors:* Jonas Peters et al.
- *Direct Connection:* The invariance principle that conditional mechanisms stable across environments reveal causal parents is generalized here to the agentic setting, underpinning the paper’s claim that robustness across many shifts forces learning of the underlying causal structure.

### 🔗 Related Problem

**Invariant Models for Causal Transfer Learning** (2018)
- *Authors:* Carles Rojas-Carulla et al.
- *Direct Connection:* This work shows that exploiting invariant conditional mechanisms enables transfer across tasks, a principle the paper elevates from predictive transfer to agent regret guarantees and strengthens from a sufficiency heuristic to a necessity theorem for causal world models.

---

## Synthesis: How Prior Work Led to This Paper

Structural causal models and do-interventions codified a precise notion of data-generating mechanisms and how they change, establishing the language to talk about interventions and counterfactuals. Building on this, the invariance principle showed that conditionals that remain stable across environments identify causal parents, providing a concrete criterion for extracting causal structure from distribution shift. Transportability theory then specified when causal relations and estimands can be moved across domains via selection diagrams, clarifying that successful cross-domain reasoning rests on correctly modeling the underlying causal structure of mechanisms and changes. In machine learning, Invariant Risk Minimization operationalized the invariance idea for predictors, proposing to learn representations whose conditionals are stable across environments, while subsequent analyses exposed that such invariance constraints can fail to recover the true causal model. Complementing this, invariant models for causal transfer learning demonstrated empirically and theoretically that leveraging stable mechanisms aids task transfer, reinforcing that mechanism invariance is the key signal. Finally, causal influence diagrams grounded agents and decisions within causal graphs, letting one formally connect internal models, interventions, and outcomes.
Together these threads reveal an opportunity: if robustness across many shifts hinges on correctly capturing invariant mechanisms, then sustained low regret should only be achievable by internalizing the causal generative process itself. The paper synthesizes the invariance and transportability insights within an explicit agent–causal formalism, upgrading prior sufficiency heuristics into a necessity theorem: any agent that maintains regret guarantees across a rich family of shifts must have learned an approximate SCM that converges to the true one when optimal.

---

*Analysis generated on: 2026-01-06T17:40:41.341786*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
