# Prior Work Analysis Report

## Target Paper
**Title:** cNmu0hZ4CL
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Representational similarity analysis—connecting the branches of systems neuroscience** (2008)
- *Authors:* Kriegeskorte et al.
- *Connection:* Defined the core problem of comparing neural representations via geometric similarity, which this paper generalizes to the case of noisy, time-evolving population trajectories.

**Wasserstein geometry of Gaussian measures** (2011)
- *Authors:* Takatsu
- *Connection:* Establishes the geometric structure (Bures–Wasserstein) for Gaussian measures, supplying the theoretical framework that underlies the proposed GP-based Wasserstein metric for neural dynamics.

### 💡 Inspiration

**Gaussian-process factor analysis for low-dimensional single-trial analysis of neural population activity** (2009)
- *Authors:* Yu et al.
- *Connection:* Modeled neural population activity as Gaussian processes over time; the present work adopts this GP view to represent noisy neural trajectories and then defines distances between these GP-distributions.

### 🔍 Gap Identification

**Reliability of dissimilarity measures for multi-voxel pattern analysis** (2016)
- *Authors:* Walther et al.
- *Connection:* Introduced noise-unbiased dissimilarities (e.g., crossnobis) highlighting the need to account for measurement noise, which this paper extends to the full temporal (trajectory-level) noise structure via Gaussian processes.

### 📊 Baseline

**Similarity of Neural Network Representations Revisited** (2019)
- *Authors:* Kornblith et al.
- *Connection:* Provided a widely adopted baseline metric (CKA) for representation comparison; the present work shows such static, deterministic metrics fail on noisy dynamics and replaces them with an OT-based GP metric.

### 🔧 Extension

**On a formula for the L2 Wasserstein metric between measures on Euclidean and Hilbert spaces** (1990)
- *Authors:* Gelbrich
- *Connection:* Provides the closed-form W2 distance between Gaussian measures (including in Hilbert spaces), which the authors extend/apply to derive an optimal-transport distance between Gaussian processes representing neural trajectories.

### 🔗 Related Problem

**SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability** (2017)
- *Authors:* Raghu et al.
- *Connection:* Serves as a principal method for comparing representational subspaces; its neglect of trial noise and temporal covariance is an implicit limitation the proposed OT-GP metric addresses.

---

## Synthesis

The paper’s core contribution—an optimal transport distance between noisy neural trajectories modeled as Gaussian processes—sits at the intersection of representational similarity analysis, neural time-series modeling, and Wasserstein geometry. Kriegeskorte et al. (2008) established the foundational goal of comparing representational geometries across systems, a task for which SVCCA (Raghu et al., 2017) and especially CKA (Kornblith et al., 2019) became standard baselines. However, these tools largely treat responses as deterministic and static, a mismatch for biological systems with trial-to-trial variability and temporally unfolding population activity. Walther et al. (2016) crystallized how noise biases similarity measures and introduced noise-unbiased distances, motivating the present work to handle noise rigorously—not only in magnitude but also in its temporal covariance. To do so, the authors adopt the Gaussian process view of neural population trajectories introduced by Yu et al. (2009), which provides a probabilistic, time-continuous representation of dynamics and variability. The key mathematical step then leverages optimal transport theory specialized to Gaussian measures: Gelbrich (1990) supplies the closed-form 2-Wasserstein distance for Gaussian measures (including in Hilbert spaces), and Takatsu (2011) characterizes the Wasserstein geometry of Gaussians via the Bures–Wasserstein metric. Building directly on these results, the paper derives a principled OT distance between Gaussian processes, yielding a metric that remains sensitive to geometric differences in dynamics while correctly accounting for structured noise—thereby overcoming the central limitations of RSA/CKA-style baselines.

---
*Generated: 2026-01-06T23:09:26.619534*
