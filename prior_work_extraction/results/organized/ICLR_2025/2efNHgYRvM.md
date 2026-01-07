# Prior Work Analysis Report

## Target Paper

**Title:** On the Identification of Temporal Causal Representation with Instantaneous Dependence

**Conference:** ICLR 2025 (oral)

**Authors:** Zijian Li, Yifan Shen, Kaitao Zheng, Ruichu Cai, Xiangchen Song, Mingming Gong, Guangyi Chen, Kun Zhang

**Keywords:** Causal Representation Learning, Instantaneous Dependency, Identification

**Abstract:** 
> Temporally causal representation learning aims to identify the latent causal process from time series observations, but most methods require the assumption that the latent causal processes do not have instantaneous relations. Although some recent methods achieve identifiability in the instantaneous causality case, they require either interventions on the latent variables or grouping of the observations, which are in general difficult to obtain in real-world scenarios. To fill this gap, we propos...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Unsupervised Feature Extraction by Time-Contrastive Learning and Nonlinear ICA** (2016)
- *Authors:* Aapo Hyvärinen and Hiroshi Morioka
- *Direct Connection:* This work introduced the auxiliary/context variable and “sufficient variability” idea via nonstationary time segments, which IDOL leverages as contextual information to prove identifiability of latent processes.

### 💡 Inspiration

**DYNOTEARS: Structure Learning from Time-Series Data** (2020)
- *Authors:* Silviu Pamfil et al.
- *Direct Connection:* DYNOTEARS’ parameterization and sparsity over both instantaneous and lagged edges inspired IDOL’s sparse influence constraint on latent time-delayed and instantaneous relations.

### 🔍 Gap Identification

**CITRIS: Causal Identifiability from Temporal Intervened Sequences** (2022)
- *Authors:* Phillip Lippe et al.
- *Direct Connection:* CITRIS achieves identifiability of temporal causal latents with instantaneous relations but requires known interventions on latents, a key practicality gap IDOL closes by avoiding interventions.

**The Incomplete Rosetta Stone Problem: Identifiability Results for Multi-View Nonlinear ICA** (2021)
- *Authors:* Alberto Gresele et al.
- *Direct Connection:* This work obtains identifiability through grouped/multi-view observations, highlighting the grouping requirement that IDOL circumvents by exploiting intrinsic temporal context instead.

### 🔧 Extension

**Nonlinear ICA Using Auxiliary Variables and Generalized Contrastive Learning** (2019)
- *Authors:* Aapo Hyvärinen et al.
- *Direct Connection:* It formalized identifiability with auxiliary variables beyond stationarity, providing the precise sufficient-variability condition and proof template that IDOL adapts to latent temporal causal models with instantaneous links.

**Variational Autoencoders and Nonlinear ICA: A Unifying Framework** (2020)
- *Authors:* Ilyes Khemakhem et al.
- *Direct Connection:* By showing how auxiliary-variable identifiability can be embedded in a VAE objective (iVAE), this work directly informs IDOL’s temporally varying VAE-style estimator consistent with its identifiability assumptions.

### 🔗 Related Problem

**Detecting causal associations in large nonlinear time series datasets with the PCMCI method** (2019)
- *Authors:* Jakob Runge et al.
- *Direct Connection:* PCMCI/PCMCI+ clarified how contemporaneous (instantaneous) and lagged dependencies can be disentangled in time series under sparsity, informing IDOL’s separation of instantaneous vs. delayed latent influences.

---

## Synthesis: How Prior Work Led to This Paper

Time-Contrastive Learning showed that nonstationary time segments can serve as auxiliary variables to enable nonlinear ICA, crystallizing the sufficient variability notion for identifiability. Building on this, auxiliary-variable nonlinear ICA generalized the principle beyond time segmentation and provided a precise identifiability framework that ties context variability to the uniqueness of latent sources. The iVAE framework connected these identifiability conditions to practical learning by embedding auxiliary variables in a VAE objective via conditional exponential-family modeling. In time series causal discovery, DYNOTEARS introduced a sparse parameterization that jointly models instantaneous and lagged effects, showing how sparsity can recover mixed contemporaneous and temporal dependencies. Complementarily, PCMCI established how to disentangle contemporaneous from lagged links under sparsity and time-ordering constraints using conditional independence testing. On the representation-learning side, CITRIS demonstrated that temporal causal latents, including instantaneous relations, can be identified if interventions on the latent variables are available, while multi-view nonlinear ICA results showed identifiability via grouped observations across views. Together, these works revealed a gap: identifiability of temporal latent causal processes with instantaneous dependence without relying on interventions or grouped observations. The present framework synthesizes auxiliary-variable identifiability with the sparsity insights from time-series causal discovery, leveraging intrinsic temporal context as the auxiliary signal and imposing a sparse influence constraint over instantaneous and lagged latent relations. This combination naturally enables identifiability and guides a temporally varying VAE-style estimator that is practical in real-world settings where interventions and grouping are unavailable.

---

*Analysis generated on: 2026-01-06T19:47:48.522312*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
