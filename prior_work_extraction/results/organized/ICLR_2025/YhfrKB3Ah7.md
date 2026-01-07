# Prior Work Analysis Report

## Target Paper
**Title:** YhfrKB3Ah7
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Preference Learning with Gaussian Processes** (2005)
- *Authors:* Wei Chu et al.
- *Connection:* GP-based preference learning (GPPL) introduced the probit-link pairwise likelihood that underpins PBO; PABBO targets the resulting non-conjugate inference bottleneck by amortizing posterior inference with a neural-process surrogate.

**Conditional Neural Processes** (2018)
- *Authors:* Marta Garnelo et al.
- *Connection:* CNP introduced amortized, task-distribution-level function inference from context sets; PABBO adopts this neural-process paradigm to amortize inference over latent utility functions from preference data across tasks.

### 💡 Inspiration

**Meta-Learning Acquisition Functions for Transfer Learning in Bayesian Optimization** (2020)
- *Authors:* Matthias Volpp et al.
- *Connection:* This work demonstrated that acquisition strategies can be meta-learned across tasks (e.g., with policy-gradient training); PABBO directly builds on this idea to meta-learn the acquisition policy in the preferential setting while jointly training the surrogate.

### 🔍 Gap Identification

**Predictive Entropy Search for Efficient Global Optimization of Black-box Functions** (2014)
- *Authors:* José Miguel Hernández-Lobato et al.
- *Connection:* Information-theoretic acquisitions like PES (adapted in PBO) are computationally heavy; PABBO explicitly addresses this limitation by learning an amortized acquisition policy via reinforcement learning to avoid repeated costly acquisition computations.

### 📊 Baseline

**Preferential Bayesian Optimization** (2017)
- *Authors:* Javier González et al.
- *Connection:* This paper formalized PBO with pairwise-preference likelihoods and PES-style acquisitions, and PABBO directly replaces its per-iteration GP inference and acquisition computation with a fully amortized, meta-learned surrogate and policy.

### 🔧 Extension

**Attentive Neural Processes** (2019)
- *Authors:* Hyunjik Kim et al.
- *Connection:* ANP showed that attention improves neural-process surrogates; PABBO extends this line with a transformer neural-process architecture tailored to encode sets of comparisons for preference BO.

### 🔗 Related Problem

**Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks** (2019)
- *Authors:* Juho Lee et al.
- *Connection:* Set Transformer established transformer-based, permutation-invariant encoders for set-structured inputs; PABBO leverages this architectural principle in its transformer neural process to handle unordered context/query sets of comparisons.

---

## Synthesis

PABBO’s core innovation—fully amortizing preferential Bayesian optimization by jointly meta-learning the surrogate and acquisition—arises at the intersection of preference-based BO and amortized meta-inference. Preferential Bayesian Optimization (González et al., 2017) defined the problem setting of querying pairs and modeling latent utilities, typically with a GP preference model from Chu and Ghahramani (2005). However, the non-conjugate preference likelihood and information-theoretic acquisitions (e.g., Predictive Entropy Search; Hernández-Lobato et al., 2014) make each PBO step computationally intensive, creating a practical bottleneck for interactive human-in-the-loop use. Neural Processes (Garnelo et al., 2018) offered a blueprint for amortized inference across a task distribution, directly enabling PABBO to replace per-iteration GP inference with a learned, distribution-conditioned surrogate. Attentive Neural Processes (Kim et al., 2019) and Set Transformer (Lee et al., 2019) informed PABBO’s transformer neural process architecture, providing attention-based, permutation-invariant encoders tailored to set-structured context and comparison data. Complementing the surrogate, meta-learning acquisition policies across tasks had been shown feasible by Volpp et al. (2020), motivating PABBO’s reinforcement-learning-based acquisition that removes repeated expensive acquisition optimization. Together, these works shape PABBO’s direct lineage: from the PBO formulation and its computational pain points (GPPL and PES), through amortized meta-inference (NP/ANP) and set-attention architectures, to meta-learned acquisition policies—culminating in a practical, fully amortized framework for preference-driven black-box optimization.

---
*Generated: 2026-01-06T23:09:26.627666*
