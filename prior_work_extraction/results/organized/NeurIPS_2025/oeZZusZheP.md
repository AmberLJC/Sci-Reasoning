# Prior Work Analysis Report

## Target Paper
**Title:** oeZZusZheP
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Action understanding as inverse planning** (2009)
- *Authors:* Chris L. Baker et al.
- *Connection:* AutoToM directly instantiates Baker et al.’s framing of Theory-of-Mind as Bayesian inverse planning—inferring latent goals and beliefs from observed actions—but automates the construction and refinement of the agent model rather than handcrafting it.

**Reasoning about reasoning by nested conditioning: Modeling theory of mind with probabilistic programs** (2014)
- *Authors:* Andreas Stuhlmüller et al.
- *Connection:* AutoToM inherits the probabilistic-programming view of ToM from Stuhlmüller & Goodman, using nested conditioning over explicit agent models and coupling it with an LLM-backed, automated model-revision loop.

### 💡 Inspiration

**DreamCoder: Growing generalizable, interpretable knowledge with wake–sleep program learning** (2021)
- *Authors:* Kevin Ellis et al.
- *Connection:* AutoToM is inspired by DreamCoder’s automated, interpretable program-structure growth, adapting the idea to discover and refine symbolic agent models for ToM while performing Bayesian inverse planning with an LLM proposal mechanism.

### 📊 Baseline

**Theory of mind may have spontaneously emerged in large language models** (2023)
- *Authors:* Mikolaj P. Kosinski
- *Connection:* AutoToM addresses the prompting-only ToM approach exemplified by Kosinski by embedding LLMs inside a model-based inverse-planning pipeline, thereby overcoming the systematic errors of pure prompting with uncertainty-calibrated inference and model refinement.

### 🔧 Extension

**Bayesian Theory of Mind: Modeling joint belief–desire attribution** (2011)
- *Authors:* Chris L. Baker et al.
- *Connection:* AutoToM extends the BToM belief–desire framework by letting an LLM propose and refine the set of mental state variables (and temporal context) used for inference, automating what BToM specified manually.

**Learning the preferences of others by inverse planning** (2016)
- *Authors:* Owain Evans et al.
- *Connection:* AutoToM builds on Evans et al.’s Bayesian inverse planning for preference/goal inference, but generalizes it by automatically discovering which mental variables are needed for a given task and iteratively refining them based on uncertainty.

### 🔗 Related Problem

**Machine Theory of Mind** (2018)
- *Authors:* Neil C. Rabinowitz et al.
- *Connection:* Targeting the same goal of agent modeling, AutoToM departs from ToMnet’s learned black-box embeddings by returning to explicit generative models and improving transferability and interpretability via uncertainty-guided model revision.

---

## Synthesis

AutoToM’s core innovation—automated agent modeling for scalable, robust Theory-of-Mind via Bayesian inverse planning—emerges from a direct lineage in model-based cognitive science and programmatic model discovery. The foundation is Baker et al.’s inverse-planning paradigm and the Bayesian Theory-of-Mind formulation, which cast mental inference as Bayesian inversion of an explicit agent model with belief–desire variables. Stuhlmüller and Goodman’s probabilistic-programming view of ToM further anchored the idea that nested reasoning and conditioning over explicit agent models can support interpretable mental-state inference. Building on this base, Evans et al. extended inverse planning to preference/goal inference, which AutoToM generalizes by automatically selecting which mental variables matter for each task. In contrast to learned black-box predictors like ToMnet (Rabinowitz et al.), AutoToM returns to explicit generative models but makes them scalable by using an LLM to propose model structure and by iteratively revising the model based on inference uncertainty—an idea inspired by DreamCoder’s automated, interpretable program growth. Finally, AutoToM directly responds to the recent practice of prompting LLMs for ToM (e.g., Kosinski) by moving beyond surface prompting to a model-based pipeline, thereby mitigating systematic errors and providing calibrated uncertainty and interpretability. Together, these works converge on AutoToM’s key insight: combine explicit inverse-planning models with automated, uncertainty-guided structure discovery to achieve robust, generalizable mental inference.

---
*Generated: 2026-01-06T23:08:23.950783*
