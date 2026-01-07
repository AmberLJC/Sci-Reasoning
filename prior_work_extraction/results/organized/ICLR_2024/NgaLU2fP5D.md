# Prior Work Analysis Report

## Target Paper

**Title:** Predictive, scalable and interpretable knowledge tracing on structured domains

**Conference:** ICLR 2024 (spotlight)

**Authors:** Hanqi Zhou, Robert Bamler, Charley M Wu, Álvaro Tejero-Cantero

**Keywords:** knowledge tracing, interpretable representations, knowledge graphs, probabilistic models, variational inference, continual learning

**Abstract:** 
> Intelligent tutoring systems optimize the selection and timing of learning materials to enhance understanding and long-term retention. This requires estimates of both the learner's progress ("knowledge tracing"; KT), and the prerequisite structure of the learning domain ("knowledge mapping"). While recent deep learning models achieve high KT accuracy, they do so at the expense of the interpretability of psychologically-inspired models. In this work, we present a solution to this trade-off. PSI-K...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Knowledge Tracing: Modeling the Acquisition of Procedural Knowledge** (1995)
- *Authors:* Albert T. Corbett et al.
- *Direct Connection:* PSI-KT generalizes BKT’s interpretable latent skill-mastery dynamics by embedding them in a hierarchical generative model that couples mastery with person-specific traits and prerequisite structure.

**Probabilistic Models for Some Intelligence and Attainment Tests** (1960)
- *Authors:* Georg Rasch
- *Direct Connection:* PSI-KT adopts the IRT-style ability–difficulty parameterization to model response likelihoods, providing psychologically interpretable learner and item parameters within its generative framework.

**DINA model and Q-matrix validation** (2009)
- *Authors:* Jimmy de la Torre
- *Direct Connection:* PSI-KT builds on the Q-matrix idea from cognitive diagnosis to tie items to concepts for interpretability, while relaxing DINA’s binary mastery and independence assumptions via continuous traits and explicit prerequisite structure.

### 💡 Inspiration

**Graph-based Knowledge Tracing** (2019)
- *Authors:* Hiroto Nakagawa et al.
- *Direct Connection:* PSI-KT takes the insight of leveraging an explicit concept prerequisite graph from GKT but replaces GNN black boxes with a transparent probabilistic mechanism that propagates effects along the graph.

**A Trainable Spaced Repetition Model for Language Learning** (2016)
- *Authors:* Burr Settles et al.
- *Direct Connection:* PSI-KT incorporates timing- and forgetting-sensitive dynamics inspired by half-life regression, encoding learner-specific retention parameters within a scalable Bayesian hierarchy.

### 📊 Baseline

**Deep Knowledge Tracing** (2015)
- *Authors:* Chris Piech et al.
- *Direct Connection:* PSI-KT targets DKT’s strong predictive performance yet opaque dynamics by introducing an interpretable generative model that supports multi-step forecasting without sacrificing accuracy.

---

## Synthesis: How Prior Work Led to This Paper

Bayesian Knowledge Tracing framed student learning as a probabilistic process of latent skill mastery with interpretable transitions, offering psychological clarity but limited structural expressivity. Item Response Theory introduced the ability–difficulty parameterization that grounds responses on a shared latent scale, enabling transparent learner and item factors. Cognitive diagnosis work on the DINA model established the Q-matrix link from items to skills, formalizing concept-level interpretability but assuming binary mastery and largely independent skills. Graph-based Knowledge Tracing showed that injecting an explicit prerequisite graph can improve prediction by propagating concept influences, though it relies on opaque graph neural computations. Deep Knowledge Tracing demonstrated that recurrent deep models can deliver high predictive accuracy, but at the cost of interpretability and principled multi-step forecasting. Finally, half-life regression in spaced repetition highlighted the importance of time and forgetting, capturing retention with simple, learner-specific parameters.
Together these ideas revealed a gap: a model that unifies interpretable person–item parameters, explicit concept structure, and time-sensitive learning dynamics, while retaining the predictive strength of modern KT and scaling to many learners. The present work synthesizes IRT-like response modeling with BKT-like latent dynamics, relaxes DINA’s binary mastery using continuous traits, operationalizes prerequisite graphs in a transparent generative mechanism as in GKT, and incorporates half-life style retention effects. With scalable Bayesian inference, this yields interpretable, structured, and predictive multi-step knowledge tracing.

---

*Analysis generated on: 2026-01-06T07:15:55.693494*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
