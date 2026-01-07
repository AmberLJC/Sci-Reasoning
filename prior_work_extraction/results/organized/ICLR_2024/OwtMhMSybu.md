# Prior Work Analysis Report

## Target Paper

**Title:** Unlocking the Power of Representations in Long-term Novelty-based Exploration

**Conference:** ICLR 2024 (spotlight)

**Authors:** Alaa Saade, Steven Kapturowski, Daniele Calandriello, Charles Blundell, Pablo Sprechmann, Leopoldo Sarra, Oliver Groth, Michal Valko, Bilal Piot

**Keywords:** Deep RL, exploration, density estimation, representation learning

**Abstract:** 
> We introduce Robust Exploration via Clustering-based Online Density Estimation (RECODE), a non-parametric method for novelty-based exploration that estimates visitation counts for clusters of states based on their similarity in a chosen embedding space. By adapting classical clustering to the nonstationary setting of Deep RL, RECODE can efficiently track state visitation counts over thousands of episodes. We further propose a novel generalization of the inverse dynamics loss, which leverages mas...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Unifying Count-Based Exploration and Intrinsic Motivation** (2016)
- *Authors:* Marc G. Bellemare et al.
- *Direct Connection:* RECODE adopts the pseudo-count view of novelty as a state-density estimate from this work and operationalizes it as visitation counts over clusters in a learned embedding space to scale to high-dimensional observations.

### 💡 Inspiration

**Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning** (2017)
- *Authors:* Haoran Tang et al.
- *Direct Connection:* RECODE generalizes the hashing-based count approximation introduced here by using adaptive online clustering in embedding space, mitigating fixed-hash collisions and enabling life-long count tracking.

**Curiosity-driven Exploration by Self-supervised Prediction** (2017)
- *Authors:* Deepak Pathak et al.
- *Direct Connection:* RECODE’s DETOCS representation objective explicitly generalizes ICM’s inverse-dynamics loss from single-step action prediction to masked multi-step prediction with a transformer, yielding more temporally informative embeddings for density estimation.

### 🔍 Gap Identification

**Count-Based Exploration with Neural Density Models** (2017)
- *Authors:* Georg Ostrovski et al.
- *Direct Connection:* By replacing PixelCNN-based neural density models—which this paper showed are effective but computationally heavy and potentially unstable in nonstationary RL—with a streaming, non-parametric clustering estimator, RECODE directly addresses the parametric density limitations highlighted here.

### 📊 Baseline

**State Entropy Maximization with Random Encoders for Efficient Exploration (RE3)** (2021)
- *Authors:* Younggyo Seo et al.
- *Direct Connection:* RECODE directly improves on RE3’s k-NN entropy bonus in feature space by providing a memory-bounded, streaming clustering density that yields consistent visitation counts rather than local k-NN estimates, enhancing long-horizon stability.

### 🔗 Related Problem

**Never Give Up: Learning Directed Exploration Strategies** (2020)
- *Authors:* Adrià Puigdomènech Badia et al.
- *Direct Connection:* Drawing on NGU’s non-parametric episodic novelty via k-NN in embedding space, RECODE replaces per-episode k-NN with a life-long clustering-based density estimator to maintain long-term visitation statistics crucial for hard-exploration benchmarks.

---

## Synthesis: How Prior Work Led to This Paper

Pseudo-counts established that exploration bonuses can be derived from density estimates over states, connecting novelty to visitation statistics in a principled way. Neural density models then instantiated this idea with PixelCNN, showing practical gains but also exposing computational burden and instability when the representation and data distribution shift during learning. To scale counts to continuous, high-dimensional observations, hashing-based methods proposed SimHash keys to approximate counts, demonstrating that non-parametric schemes can be both simple and effective yet susceptible to collision and rigidity. Random-encoder k-NN–based state entropy showed that local density in feature space can drive efficient exploration without heavy training, while also revealing sensitivity to representation choice and challenges in maintaining coherent long-term statistics. Episodic novelty via k-NN memories highlighted the value of non-parametric, life-long signals, but its per-episode nature limited persistent count accumulation across thousands of episodes. In parallel, inverse dynamics–based self-supervision provided a practical way to shape representations around controllable aspects of the environment, though its single-step formulation is often myopic in long-horizon tasks.
Synthesizing these insights, the current work replaces parametric density with a streaming, non-parametric clustering estimator to compute pseudo-counts in embedding space, avoiding hash rigidity and k-NN locality while supporting life-long tracking. It complements this with a masked, multi-step generalization of inverse dynamics using transformers to learn temporally predictive embeddings that stabilize the density estimator, naturally addressing the nonstationarity and horizon limits surfaced by prior methods.

---

*Analysis generated on: 2026-01-06T08:46:37.890769*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
