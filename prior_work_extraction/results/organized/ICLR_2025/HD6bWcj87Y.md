# Prior Work Analysis Report

## Target Paper

**Title:** Data Shapley in One Training Run

**Conference:** ICLR 2025 (oral)

**Authors:** Jiachen T. Wang, Prateek Mittal, Dawn Song, Ruoxi Jia

**Keywords:** Shapley value, data valuation.

**Abstract:** 
> Data Shapley offers a principled framework for attributing the contribution of data within machine learning contexts. However, the traditional notion of Data Shapley requires re-training models on various data subsets, which becomes computationally infeasible for large-scale models. Additionally, this retraining-based definition cannot evaluate the contribution of data for a specific model training run, which may often be of interest in practice. This paper introduces a novel concept, In-Run Dat...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Data Shapley: Equitable Valuation of Data for Machine Learning** (2019)
- *Authors:* Amirata Ghorbani and James Zou
- *Direct Connection:* This work formalized data valuation via the Shapley value and introduced retraining-based estimators (e.g., TMC/Aumann-Shapley), whose computational cost and lack of per-run specificity are the exact limitations In-Run Data Shapley replaces with gradient-trajectory credits in a single training run.

**Values of Non-Atomic Games** (1974)
- *Authors:* Robert J. Aumann and Lloyd S. Shapley
- *Direct Connection:* The Aumann–Shapley path-integral notion of marginal contributions underlies our view of each SGD step as an infinitesimal game, enabling Shapley credits to be accumulated over the training path without subset retraining.

### 💡 Inspiration

**Estimating Training Data Influence by Tracing Gradient Descent (TracIn)** (2020)
- *Authors:* Avijit Pruthi et al.
- *Direct Connection:* TracIn’s insight that the sequence of SGD updates encodes data attribution informs our per-iteration accumulation, which we recast from an influence heuristic into principled Shapley contributions computed along the training trajectory.

### 📊 Baseline

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh and Percy Liang
- *Direct Connection:* As the standard non-retraining baseline for training-point contribution to a fixed model, influence functions’ Hessian-based formulation is the approach our in-run Shapley replaces with a scalable, Hessian-free credit assignment during training.

### 🔧 Extension

**Towards Efficient Data Valuation Based on the Shapley Value** (2019)
- *Authors:* Ruoxi Jia et al.
- *Direct Connection:* By showing that exploiting algorithmic structure (e.g., kNN-Shapley) can make Shapley tractable, this paper directly motivates our strategy of exploiting SGD’s per-step gradient structure to compute Shapley-like credits without retraining.

### 🔗 Related Problem

**Representer Point Selection for Explaining Deep Neural Networks** (2018)
- *Authors:* Chih-Kuan Yeh et al.
- *Direct Connection:* This work demonstrated model-specific training-point attribution from a single trained model, foreshadowing our model/run-specific valuation while we supply an axiomatic Shapley grounding and compute credits online during training.

---

## Synthesis: How Prior Work Led to This Paper

Data Shapley established the game-theoretic formulation of valuing training data via marginal contributions over subsets and proposed Monte Carlo and Aumann–Shapley estimators, but these required repeated retraining and captured an average notion of value across training randomness. Building on this, work on efficient Shapley computation showed that leveraging model-specific structure—such as closed-form behavior in kNN—can make exact or approximate Shapley practical, highlighting the importance of algorithm-aware shortcuts rather than generic subset enumeration. Influence functions provided a non-retraining route to estimate the effect of upweighting or removing a point on a fixed model’s loss via Hessian-inverse sensitivity, but their instability and cost in deep models limited scalability. TracIn revealed that the trajectory of SGD encodes attribution signal: summing gradient alignments across checkpoints yields a faithful, run-specific estimate of example influence without Hessians. The Aumann–Shapley framework offered a principled path-integral view of marginal contributions for non-atomic participants, suggesting credit accumulation along a continuous process. Finally, representer-point methods showed that training-point attributions can be computed for a specific trained model in one run by exploiting structural decompositions. Together, these works expose a gap: Shapley-based valuations were principled but retraining-heavy, while trajectory-based or model-specific attributions were scalable but lacked Shapley guarantees. The natural synthesis is to treat SGD as the path over which infinitesimal data contributions accrue, using per-step gradients to compute and aggregate Shapley-like marginal credits, thereby yielding principled, run-specific data values with negligible overhead.

---

*Analysis generated on: 2026-01-06T08:11:30.920099*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
