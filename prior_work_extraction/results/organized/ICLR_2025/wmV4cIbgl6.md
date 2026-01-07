# Prior Work Analysis Report

## Target Paper

**Title:** CausalRivers - Scaling up benchmarking of causal discovery for real-world time-series

**Conference:** ICLR 2025 (spotlight)

**Authors:** Gideon Stein, Maha Shadaydeh, Jan Blunk, Niklas Penzel, Joachim Denzler

**Keywords:** Causal Discovery, Benchmarking, Time-series

**Abstract:** 
> Causal discovery, or identifying causal relationships from observational data, is a notoriously challenging task, with numerous methods proposed to tackle it.
Despite this, in-the-wild evaluation of these methods is still lacking, as works frequently rely on synthetic data evaluation and sparse real-world examples under critical theoretical assumptions.
Real-world causal structures, however, are often complex, evolving over time, non-linear, and influenced by unobserved factors, making
it hard t...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**CauseMe: a benchmarking platform for causal inference in time series** (2020)
- *Authors:* Jakob Runge et al.
- *Direct Connection:* CauseMe established realistic time-series causal discovery benchmarking and protocols, and CausalRivers directly extends this line by scaling the benchmark and providing denser, domain-grounded ground truth via river networks to address CauseMe’s limited scope and partial ground truths.

### 🔍 Gap Identification

**Distinguishing cause from effect using observational data: Methods and benchmarks** (2016)
- *Authors:* Joris M. Mooij et al.
- *Direct Connection:* The Tübingen cause-effect pairs benchmark set a precedent for real-world causal evaluation but is pairwise and non-time-series, a limitation CausalRivers addresses by offering multivariate, network-level, time-resolved ground truth.

### 📊 Baseline

**Detecting causal associations in large nonlinear time series datasets (PCMCI+)** (2019)
- *Authors:* Jakob Runge et al.
- *Direct Connection:* PCMCI+ is a principal high-dimensional time-series causal discovery method whose handling of autocorrelation and confounding is explicitly stress-tested as a core baseline within CausalRivers.

**DYNOTEARS: Structure Learning from Time-Series Data** (2020)
- *Authors:* Elena Pamfil et al.
- *Direct Connection:* DYNOTEARS provides a dynamic DAG learning approach with lagged dependencies that CausalRivers adopts as a main competitor to expose the limits of linearity and stationarity on real river discharge data.

**Causal Discovery in Time Series Using Convolutional Neural Networks (TCDF)** (2019)
- *Authors:* Nicki Nauta et al.
- *Direct Connection:* TCDF introduces a nonlinear, lag-selective neural approach that CausalRivers includes as a primary baseline to evaluate scalability and interpretability under exogenous hydrometeorological drivers.

**Detecting causality in complex ecosystems via convergent cross mapping** (2012)
- *Authors:* George Sugihara et al.
- *Direct Connection:* Convergent Cross Mapping is a widely used nonlinear pairwise causality test in geosciences that CausalRivers benchmarks to assess robustness under common drivers and transport delays inherent to river networks.

### 🔗 Related Problem

**Causal structure learning from time series with latent variables (tsFCI)** (2018)
- *Authors:* Daniel Malinsky et al.
- *Direct Connection:* tsFCI’s treatment of latent confounders in time series directly informs CausalRivers’ emphasis on hidden drivers (e.g., precipitation, regulation) and motivates evaluation protocols that credit partially oriented graphs.

---

## Synthesis: How Prior Work Led to This Paper

A series of works laid the groundwork for evaluating causal discovery on time series and highlighted critical gaps. CauseMe introduced the first dedicated platform for benchmarking time-series causal inference with realistic noise, confounding, and lag structures, seeding community standards for protocols and metrics. PCMCI+ provided a scalable conditional-independence framework tailored to autocorrelated, high-dimensional time series, clarifying how to control false positives under strong temporal dependence. DYNOTEARS framed dynamic DAG learning directly from time-indexed observations with explicit lags, but under linear-Gaussian and stationarity assumptions. TCDF contributed a nonlinear, attention-like lag-selection mechanism for multivariate series, emphasizing interpretability of temporal effects. tsFCI adapted FCI to time series with latent variables, formalizing evaluation on partially oriented graphs in the presence of hidden confounders. Convergent Cross Mapping offered a nonlinear pairwise causality tool popular in geosciences, yet known to be sensitive to shared drivers and time delays. The Tübingen cause-effect benchmark established real-world evaluation culture but remained pairwise and non-temporal. Taken together, these works underscored the need for a large-scale, multivariate, in-the-wild time-series benchmark with domain-grounded ground truth and natural interventions. The current paper synthesizes CauseMe’s benchmarking ethos, PCMCI+/DYNOTEARS/TCDF/tsFCI’s methodological targets, and CCM’s geoscience relevance, and advances the field by delivering a dense hydrological network with known flow topology and high-frequency dynamics to rigorously test method assumptions about nonlinearity, evolving structure, lags, and hidden confounding.

---

*Analysis generated on: 2026-01-06T11:00:02.930965*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
