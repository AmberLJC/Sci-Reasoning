# Prior Work Analysis Report

## Target Paper
**Title:** 60F0fVbknK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Causal Discovery from Subsampled Time Series** (2016)
- *Authors:* Antti Hyttinen et al.
- *Connection:* This paper formalized the causal discovery problem under subsampling, showing identifiability challenges and motivating methods that can recover causal structure when measurements occur at a coarser timescale—precisely the setting DHT-CIT targets without interventions.

**Dynamic Bayesian Networks: Representation, Inference and Learning** (2002)
- *Authors:* Kevin P. Murphy
- *Connection:* The two-slice temporal Bayes net (2TBN) template in DBNs provides the foundational two-time-slices representation that DHT-CIT exploits to encode descendant relations and perform CI-based orientation from only two observed slices.

**Causal inference in time series** (2012)
- *Authors:* Michael Eichler
- *Connection:* Eichler’s graphical framework for time-series causality grounds the use of conditional independences across lags and contemporaneous variables, which DHT-CIT adapts to the subsampled two-slice setting to test descendant relations.

### 🔍 Gap Identification

**Causal discovery from temporally aggregated time series** (2017)
- *Authors:* Mingming Gong et al.
- *Connection:* By demonstrating how temporal aggregation/subsampling induces spurious dependencies and misleads standard time-series causal methods, this work exposes the specific failure modes that the proposed two-time-slices strategy is designed to overcome.

### 📊 Baseline

**Detecting causal associations in large nonlinear time series datasets (PCMCI)** (2019)
- *Authors:* Jakob Runge et al.
- *Connection:* PCMCI/PCMCI+ are leading CI-based time-series baselines which assume measurements at the causal timescale; the new DHT-CIT directly modifies the CI-testing paradigm to operate on two-time-slices under subsampling where PCMCI-type methods struggle.

**Estimation of a Structural Vector Autoregression Model Using Non-Gaussianity** (2010)
- *Authors:* Aapo Hyvärinen et al.
- *Connection:* SVAR/VAR-LiNGAM methods identify causal ordering in time series under non-Gaussianity at the correct sampling rate; DHT-CIT explicitly addresses their breakdown under subsampling by leveraging two-time-slices CI tests to recover causal order.

### 🔗 Related Problem

**Causal structure learning from time series with latent variables** (2018)
- *Authors:* Daniel Malinsky et al.
- *Connection:* This extension of constraint-based causal discovery to time series with latent confounding highlights limits of CI-based methods under realistic violations, informing DHT-CIT’s design of CI tests and ordering logic that remain valid under subsampling-induced missing slices.

---

## Synthesis

The core innovation of DHT-CIT—recovering causal relations from subsampled time series using only two time-slices—emerges from a line of work defining and stressing the subsampling problem and the limits of standard time-series causal discovery. Hyttinen et al. (2016) framed causal discovery under subsampling and exposed identifiability barriers when the measurement rate is coarser than the causal timescale, providing the precise problem formulation this paper tackles. Gong et al. (2017) further showed how temporal aggregation yields spurious dependencies that mislead conventional methods, directly motivating the need for a new strategy that remains valid under coarse sampling without relying on expensive interventions.

Against this backdrop, leading CI-based and structural methods—PCMCI (Runge et al., 2019) and SVAR/VAR-LiNGAM (Hyvärinen et al., 2010)—serve as primary baselines that presume correctly sampled dynamics; their failure modes under subsampling sharpen the gap DHT-CIT fills. The idea to operate on two observed slices is grounded in the two-slice temporal Bayes net abstraction from dynamic Bayesian networks (Murphy, 2002), while Eichler’s (2012) graphical time-series causality provides the conditional independence semantics that DHT-CIT adapts to tests of descendant relations in the subsampled two-slice regime. Finally, insights from Malinsky and Spirtes (2018) on learning with latent variables inform robust CI-testing and orientation choices when many intermediate time-slices are unobserved (effectively latent). Together, these works directly shape the paper’s problem, its two-slice representation, its CI-testing machinery, and the specific gaps it closes.

---
*Generated: 2026-01-06T23:09:26.431404*
