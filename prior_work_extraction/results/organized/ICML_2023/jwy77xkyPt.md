# Prior Work Analysis Report

## Target Paper
**Title:** jwy77xkyPt
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Learning Latent Dynamics for Planning** (2019)
- *Authors:* Danijar Hafner et al.
- *Connection:* F2C adopts PlaNet’s recurrent state-space model (RSSM) generative structure and control interface, extending it to multi-view emissions and a fused multi-encoder posterior tailored to control.

**Deep Markov Models** (2017)
- *Authors:* Rahul G. Krishnan et al.
- *Connection:* F2C inherits the variational treatment of sequential latent variables from DMM, then augments it with multi-view likelihood factorization and fused per-view inference for control.

### 💡 Inspiration

**Deep Variational Information Bottleneck** (2017)
- *Authors:* Alexander A. Alemi et al.
- *Connection:* F2C’s information-theoretic training objective follows the VIB principle—using variational mutual-information bounds to make the latent state capture task-relevant information—adapted to sequential multi-view control.

### 🔍 Gap Identification

**Joint Multimodal Learning with Deep Generative Models** (2016)
- *Authors:* Masahiro Suzuki et al.
- *Connection:* JMVAE exposed the difficulty of robust inference and imputation under missing modalities with joint encoders; F2C explicitly addresses this gap by replacing joint inference with per-view encoders combined via PoE within a state-space model.

### 📊 Baseline

**Dreamer: Reinforcement Learning with World Models** (2020)
- *Authors:* Danijar Hafner et al.
- *Connection:* F2C targets the same model-based control setting as Dreamer but replaces Dreamer’s single-view RSSM training with a multi-view fused posterior and information-theoretic objective, directly addressing Dreamer’s inability to scale to many views or handle missing views.

### 🔧 Extension

**Multimodal Generative Models for Scalable Weakly-Supervised Learning** (2018)
- *Authors:* Mike Wu et al.
- *Connection:* F2C directly builds on MVAE’s product-of-experts (PoE) posterior to combine per-view encoders, extending this fusion mechanism to sequential state-space inference so it scales linearly with views and remains robust to arbitrary missing-view subsets.

**Generalized Product of Experts for Modeling Multimodal Data** (2021)
- *Authors:* Thomas Sutter et al.
- *Connection:* F2C leverages the generalized PoE aggregation principle from MoPoE to ensure consistent posteriors when any subset of views is present, adapting it to temporally recursive inference for control.

---

## Synthesis

Fuse2Control (F2C) sits at the intersection of model-based control, multimodal fusion, and information-theoretic representation learning. Its state-space backbone traces directly to PlaNet’s recurrent state-space model (RSSM), providing the temporal latent dynamics and control interface that Dreamer popularized for efficient model-based RL. However, Dreamer and PlaNet assume single-view inputs and do not natively handle missing sensors or scale gracefully with many views—limitations F2C explicitly targets. To fuse multiple sensors, F2C adopts the product-of-experts (PoE) posterior from MVAE, which offers a principled way to combine per-view encoders and naturally supports training and inference with arbitrary subsets of modalities. Building on MoPoE’s generalized aggregation of modality subsets, F2C ensures consistent posteriors under missing views while retaining linear scaling with the number of sensors. The sequential variational machinery underlying the latent state is grounded in Deep Markov Models, which F2C extends by factorizing multi-view likelihoods and applying PoE at each time step. Finally, F2C’s core training signal is information-theoretic: inspired by the Deep Variational Information Bottleneck, it regularizes the latent state to preserve control-relevant information across time. Together, these strands—RSSM-based control, PoE-based multimodal fusion, and IB-driven objectives—directly combine to yield F2C’s key innovation: an information-theoretic multi-view state-space model that scales linearly and is robust to missing observations.

---
*Generated: 2026-01-06T23:09:26.564688*
