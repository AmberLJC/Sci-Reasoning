# Prior Work Analysis Report

## Target Paper
**Title:** EdRb84fiJY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Random Features for Large-Scale Kernel Machines** (2007)
- *Authors:* Ali Rahimi et al.
- *Connection:* Introduces the random features framework that underpins the paper’s spiked Random Features (sRF) modeling of the post-update network.

**Generalization error of random features and two-layer neural networks** (2019)
- *Authors:* Song Mei et al.
- *Connection:* Provides high-dimensional asymptotics for random features and two-layer networks that the present work extends to a spiked RF setting induced by a single gradient step.

### 💡 Inspiration

**One-step feature learning in two-layer networks via a spiked random features model** (2022)
- *Authors:* Jimmy Ba et al.
- *Connection:* Provides the key insight to model the effect of a single gradient step as a spiked Random Features (sRF) model, which this paper adopts and analyzes asymptotically.

### 🔍 Gap Identification

**On Lazy Training in Differentiable Programming** (2019)
- *Authors:* Lenaic Chizat et al.
- *Connection:* Identifies the lazy/NTK regime where features do not adapt, motivating the present paper’s focus on quantifying feature learning that occurs immediately after one gradient step.

### 📊 Baseline

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Connection:* Serves as the kernel-regime baseline the paper explicitly seeks to improve upon by analyzing how a two-layer network, after a single gradient step, departs from NTK behavior.

### 🔧 Extension

**Gaussian Universality of Random Features Models** (2023)
- *Authors:* Yatin Dandi et al.
- *Connection:* Supplies the Gaussian universality machinery the paper leverages to derive exact asymptotics for the sRF model in the proportional high-dimensional limit.

### 🔗 Related Problem

**Spectral bias and task-model alignment explain generalization in kernel regression and infinitely wide neural networks** (2021)
- *Authors:* Berk Canatar et al.
- *Connection:* Clarifies how alignment with task-relevant directions governs generalization, informing the paper’s finding that the one-step gradient induces alignment enabling nonlinear learning.

---

## Synthesis

The core innovation of this paper—an exact asymptotic characterization of feature learning in two-layer networks after a single gradient step—emerges from a precise intellectual lineage. The NTK framework of Jacot et al. (2018) and the lazy-training perspective of Chizat and Bach (2019) established the kernel regime as a powerful but feature-static baseline, highlighting a central gap: wide networks in the proportional regime cannot capture nonlinear structure without adapting features. Random features, introduced by Rahimi and Recht (2007), provided a tractable surrogate for analyzing wide networks, while Mei, Misiakiewicz, and Montanari (2019) developed high-dimensional asymptotics that grounded rigorous learning-curve predictions for RF and two-layer models. The decisive conceptual step came with Ba et al. (2022), who proposed modeling the immediate effect of a single gradient step as inducing a low-rank spike in the random features—precisely the sRF model adopted here. Building on this, Dandi et al. (2023) furnished Gaussian universality tools that justify replacing complex data/weight distributions with Gaussian equivalents, enabling exact asymptotics for the sRF model in the proportional limit. Complementing these, Canatar, Bordelon, and Pehlevan (2021) elucidated task-model alignment and spectral bias, clarifying why gradient-induced alignment can unlock nonlinear learning beyond NTK. Together, these works directly enable the paper’s main result: a rigorous, high-dimensional description of generalization improvements over the kernel regime achieved by one-step feature learning.

---
*Generated: 2026-01-06T23:09:26.423156*
