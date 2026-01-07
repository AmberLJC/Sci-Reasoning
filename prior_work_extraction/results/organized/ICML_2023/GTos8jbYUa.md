# Prior Work Analysis Report

## Target Paper
**Title:** GTos8jbYUa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Deep Kalman Filters** (2015)
- *Authors:* R. G. Krishnan et al.
- *Connection:* Deep Kalman Filters established deep generative state-space modeling with variational inference, and NCDSSM builds on this framework while addressing its limitation of amortizing inference over all dynamic states by filtering/marginalizing them and amortizing only auxiliary variables.

**Stochastic Processes and Filtering Theory** (1970)
- *Authors:* A. H. Jazwinski
- *Connection:* NCDSSM’s exact inference over continuous-time latent dynamics with discrete observations is enabled by continuous–discrete filtering theory (Kalman–Bucy and related results) laid out in Jazwinski’s classical framework.

### 💡 Inspiration

**Deep Variational Bayes Filters: Unsupervised Learning of State Space Models from Raw Data (DVBF)** (2016)
- *Authors:* M. Karl et al.
- *Connection:* DVBF introduced auxiliary process variables and amortized inference only for these auxiliaries to maintain tractable filtering; NCDSSM adopts this disentanglement principle and adapts it to continuous-time dynamics with exact Bayesian filtering of the dynamic states.

### 🔍 Gap Identification

**GP-VAE: Deep Probabilistic Time Series Imputation using Gaussian Process Priors** (2020)
- *Authors:* V. Fortuin et al.
- *Connection:* GP-VAE addresses irregular sampling via GP priors but is constrained by GP expressivity and scaling; NCDSSM targets this limitation by learning flexible neural continuous–discrete dynamics while retaining principled Bayesian inference through filtering.

### 📊 Baseline

**Latent ODEs for Irregularly-Sampled Time Series** (2019)
- *Authors:* Y. Rubanova et al.
- *Connection:* Latent ODEs formulated continuous-time latent variable models for irregular sampling but rely on trajectory-level amortized encoders; NCDSSM directly targets this gap by replacing amortized state inference with continuous–discrete Bayesian filtering and marginalization of dynamic states.

### 🔧 Extension

**A Disentangled Recognition and Nonlinear Dynamics Model for Unsupervised Learning of Structured State Space Models (KVAE)** (2017)
- *Authors:* M. Fraccaro et al.
- *Connection:* NCDSSM generalizes KVAE’s core idea of introducing auxiliary variables to decouple recognition from linear-Gaussian dynamics—and using Kalman-style marginalization of dynamic states—to the continuous-time, irregularly observed (continuous–discrete) setting.

### 🔗 Related Problem

**Neural Controlled Differential Equations for Irregular Time Series** (2020)
- *Authors:* P. Kidger et al.
- *Connection:* Neural CDEs crystallized the continuous-time formulation for irregularly sampled data; NCDSSM adopts the continuous-time viewpoint but contributes a generative, Bayesian state-space treatment with filtering-based inference rather than purely supervised controlled dynamics.

---

## Synthesis

NCDSSM sits at the intersection of deep state-space modeling and continuous-time learning for irregularly sampled series. Its core move—amortizing inference only for auxiliary variables while performing exact Bayesian updates for the dynamic states—directly builds on the disentanglement principle pioneered by DVBF and made operational in KVAE, where a linear–Gaussian substructure enables Kalman-style marginalization of states. NCDSSM extends this blueprint from discrete-time to continuous–discrete systems, invoking Jazwinski’s continuous-time filtering theory to compute accurate posteriors for continuous dynamics observed at discrete times. This addresses a key limitation of the Latent ODE line of work: although Latent ODEs established the modern continuous-time latent generative formulation for irregular sampling, they rely on trajectory-level amortized encoders and do not exploit Bayesian filtering structure, which NCDSSM provides. Neural CDEs further motivated the continuous-time perspective for irregular data, but are predominantly supervised; NCDSSM contributes a fully generative, Bayesian alternative with closed-form filtering updates. Finally, GP-VAE highlighted the benefits of continuous-time priors for imputation under irregular sampling but exposed expressivity and scalability constraints inherent to GP priors; NCDSSM replaces these with flexible neural continuous–discrete dynamics while still enjoying exact (filtering-based) inference for the dynamic states. Together, these works directly shaped NCDSSM’s key innovation: disentangled, auxiliary-variable recognition coupled with continuous–discrete Bayesian filtering and state marginalization.

---
*Generated: 2026-01-06T23:09:26.573388*
