# Prior Work Analysis Report

## Target Paper

**Title:** Counterfactual Realizability

**Conference:** ICLR 2025 (spotlight)

**Authors:** Arvind Raghavan, Elias Bareinboim

**Keywords:** causal inference, experiment design, causal reinforcement learning, counterfactual reasoning

**Abstract:** 
> It is commonly believed that, in a real-world environment, samples can only be drawn from observational and interventional distributions, corresponding to Layers 1 and 2 of the *Pearl Causal Hierarchy*. Layer 3, representing counterfactual distributions, is believed to be inaccessible by definition. However, Bareinboim, Forney, and Pearl (2015) introduced a procedure that allows an agent to sample directly from a counterfactual distribution, leaving open the question of what other counterfactual...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Causality: Models, Reasoning, and Inference (2nd ed.)** (2009)
- *Authors:* Pearl
- *Direct Connection:* The structural causal model framework and the abduction–action–prediction/twin-network machinery defined here provide the formal semantics of counterfactuals that the realizability criterion and algorithm analyze.

### 💡 Inspiration

**Counterfactuals in Causal Inference: A Procedure for Direct Sampling** (2015)
- *Authors:* Bareinboim et al.
- *Direct Connection:* This work introduced a concrete experimental procedure showing that certain counterfactual distributions can be sampled directly, which the present paper generalizes by characterizing exactly which counterfactual queries are realizable under physical constraints.

### 🔍 Gap Identification

**Single World Intervention Graphs (SWIGs): A Unification of the Counterfactual and Graphical Approaches to Causality** (2013)
- *Authors:* Richardson et al.
- *Direct Connection:* By formalizing single-world representations and the non-joint observability of cross-world potential outcomes, this work crystallized the physical infeasibility constraints that the realizability definition encodes and reasons about.

**Statistics and Causal Inference** (1986)
- *Authors:* Holland
- *Direct Connection:* The 'fundamental problem of causal inference'—that one cannot subject the same unit to multiple treatments—directly motivates the paper’s formal constraint model for deciding which counterfactual distributions can be sampled.

### 🔧 Extension

**Complete Identification of Counterfactuals in Graphical Models of Causation** (2008)
- *Authors:* Shpitser et al.
- *Direct Connection:* Its completeness results and counterfactual graph manipulations for deciding identifiability are directly adapted as proof techniques and algorithmic templates for establishing completeness of the realizability decision procedure.

**Causal inference by surrogate experiments: z-identifiability** (2012)
- *Authors:* Bareinboim et al.
- *Direct Connection:* The notion of constraining which interventions are physically performable via surrogate experiments is explicitly generalized here from interventional to counterfactual targets to decide realizability.

---

## Synthesis: How Prior Work Led to This Paper

The structural causal model program established the semantics of counterfactuals via abduction–action–prediction and the twin-network construction, providing a precise graphical language for counterfactual variables and their cross-world dependencies. Building on that formalism, completeness results for counterfactual identification showed how to algorithmically analyze counterfactual queries using graphical manipulations, setting a template for rigorous decision procedures over counterfactual quantities. The surrogate-experiment (z-identifiability) line then introduced the idea of constraining which interventions are physically performable, characterizing when a target interventional distribution can be obtained by experimenting on a surrogate set. In parallel, the SWIG framework clarified that counterfactuals are inherently single-world objects and highlighted the non-joint observability of cross-world potential outcomes, making explicit key physical infeasibility constraints. Classic potential-outcomes work emphasized the fundamental problem of causal inference—that the same unit cannot receive multiple treatments—underscoring why many cross-world constructs are not directly observable. Most pointedly, a 2015 procedure by Bareinboim, Forney, and Pearl demonstrated that, contrary to common belief, certain counterfactual distributions can in fact be sampled directly under appropriate experimental designs. Taken together, these works reveal both a semantic and experimental scaffold: rigorous counterfactual graph calculus, constraints on which interventions are feasible, and a proof-of-concept that some counterfactuals are experimentally attainable. The natural next step is to close the gap between isolated procedures and general principles by defining realizability—the ability to sample a target distribution—and providing a complete algorithm that, using twin-network semantics and surrogate-experiment constraints, decides exactly which counterfactual queries admit physical sampling under foundational impossibility constraints.

---

*Analysis generated on: 2026-01-06T06:50:13.803134*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
