# Prior Work Analysis Report

## Target Paper

**Title:** Signature Kernel Conditional Independence Tests in Causal Discovery for Stochastic Processes

**Conference:** ICLR 2025 (spotlight)

**Authors:** Georg Manten, Cecilia Casolo, Emilio Ferrucci, Søren Wengel Mogensen, Cristopher Salvi, Niki Kilbertus

**Keywords:** causality, dynamical systems, stochastic processes, causal discovery, signature kernel

**Abstract:** 
> Inferring the causal structure underlying stochastic dynamical systems from observational data holds great promise in domains ranging from science and health to finance. Such processes can often be accurately modeled via stochastic differential equations (SDEs), which naturally imply causal relationships via `which variables enter the differential of which other variables'. In this paper, we develop conditional independence (CI) constraints on coordinate processes over selected intervals that ar...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Causal Interpretation of Stochastic Differential Equations** (2020)
- *Authors:* Søren Wengel Mogensen and Niels Richard Hansen
- *Direct Connection:* Their formulation that causal edges in SDEs are determined by which coordinates enter each other’s differentials directly underpins the acyclic dependence graph (with self-loops) on which our interval CI constraints and identifiability results are built.

**Markov Properties for Acyclic Directed Mixed Graphs** (2003)
- *Authors:* Thomas S. Richardson
- *Direct Connection:* The ADMG framework and m-separation criterion provide the ancestral-graph target and separation semantics we use to formalize recovery under partial observation and latent confounding.

**Kernel Measures of Conditional Dependence** (2008)
- *Authors:* Kenji Fukumizu, Arthur Gretton, Xiaohai Sun, Bernhard Schölkopf
- *Direct Connection:* Their characterization of conditional independence via conditional cross-covariance operators in RKHS forms the statistical backbone for our consistent signature-kernel CI test on path-valued variables.

### 💡 Inspiration

**Graphical models for marked point processes based on local independence** (2008)
- *Authors:* Vanessa Didelez
- *Direct Connection:* The local independence principle establishing conditional independence relationships over time intervals for continuous-time processes motivates our construction of interval-based CI constraints for SDE coordinate processes.

**The Signature Kernel** (2021)
- *Authors:* Cristopher Salvi et al.
- *Direct Connection:* Signature kernels provide characteristic, efficiently computable RKHS embeddings for paths, enabling our nonparametric CI testing of entire process segments central to the practical CI oracle.

### 🔍 Gap Identification

**Detecting causal associations in large nonlinear time series using PCMCI** (2019)
- *Authors:* Jakob Runge et al.
- *Direct Connection:* PCMCI’s time-ordered CI paradigm highlights the value of exploiting temporal direction but is limited to discrete-time lag graphs and does not address latent confounding, motivating our move to SDE-induced ancestral graphs and interval CIs with partial observability.

### 🔧 Extension

**Kernel-based Conditional Independence Test and Application in Causal Discovery** (2011)
- *Authors:* Kun Zhang, Jonas Peters, Dominik Janzing, Bernhard Schölkopf
- *Direct Connection:* We adapt the practical KCI testing scheme by replacing Euclidean kernels with signature kernels on path space and proving its validity for CI between coordinate-process segments of SDEs.

---

## Synthesis: How Prior Work Led to This Paper

Stochastic differential equations can encode causal structure through their coefficients: which coordinates enter each other’s differentials determines directed dependencies and naturally allows self-loops, as formalized by Mogensen and Hansen. Beyond pointwise conditioning, Didelez introduced local independence for continuous-time processes, articulating conditional independence constraints over time intervals that align with the way information flows in continuous time. When variables are partially observed, Richardson’s acyclic directed mixed graphs and m-separation provide the correct graphical semantics for ancestral targets under marginalization and latent confounding. In time series, PCMCI demonstrated how leveraging temporal ordering within CI-based discovery boosts orientation power, but its discrete-time lag framework and lack of principled latent-variable handling leave gaps for continuous-time systems. On the statistical testing side, Fukumizu et al. grounded conditional independence in operators on reproducing kernel Hilbert spaces, enabling consistent nonparametric CI tests, with Zhang et al. providing a practical KCI procedure widely used in causal discovery. For sequential data, Salvi and collaborators developed signature kernels, yielding characteristic, efficiently computable embeddings of entire paths suitable for hypothesis testing on processes. Bringing these threads together, a natural opportunity emerges: define CI constraints tailored to SDE-induced dependence graphs over selected intervals and use them for sound, complete causal discovery of ancestral graphs—even under partial observation—while supplying a practical oracle by marrying RKHS CI testing with signature kernels to handle path-valued variables. This synthesis replaces discrete lag models with SDE-native interval CIs, exploits time directionality for unique orientation, and supplies a consistent, flexible CI test that operates directly on trajectory segments.

---

*Analysis generated on: 2026-01-06T11:06:32.247836*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
