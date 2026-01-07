# Prior Work Analysis Report

## Target Paper

**Title:** NetFormer: An interpretable model for recovering dynamical connectivity in neuronal population dynamics

**Conference:** ICLR 2025 (spotlight)

**Authors:** Ziyu Lu, Wuwei Zhang, Trung Le, Hao Wang, Uygar Sümbül, Eric Todd SheaBrown, Lu Mi

**Keywords:** neuronal dynamics, dynamical connectivity, interpretability, attention mechanism, transformer

**Abstract:** 
> Neuronal dynamics are highly nonlinear and nonstationary. Traditional methods for extracting the underlying network structure from neuronal activity recordings mainly concentrate on modeling static connectivity, without accounting for key nonstationary aspects of biological neural systems, such as ongoing synaptic plasticity and neuronal modulation. To bridge this gap, we introduce the NetFormer model, an interpretable approach applicable to such systems. In NetFormer, the activity of each neuro...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**A point process framework for relating neural spiking activity to spiking history, neural ensemble, and extrinsic covariate effects** (2005)
- *Authors:* Truccolo et al.
- *Direct Connection:* This paper established the GLM/point-process formulation in which coupling filters encode directed effective connectivity from population spike histories, the formal modeling setup NetFormer generalizes to state- and time-dependent interactions via attention.

### 💡 Inspiration

**Neural Relational Inference for Interacting Systems** (2018)
- *Authors:* Kipf et al.
- *Direct Connection:* NRI introduced learning interaction graphs from trajectories via learned pairwise messages, an idea NetFormer instantiates with query–key attention to yield an interpretable, time-varying connectivity matrix.

**Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting** (2021)
- *Authors:* Lim et al.
- *Direct Connection:* TFT demonstrated how attention mechanisms can be structured for interpretability over variables and time, a design principle NetFormer leverages so attention weights correspond directly to dynamic neuron–neuron connectivity.

### 🔍 Gap Identification

**Recurrent Switching Linear Dynamical Systems** (2017)
- *Authors:* Linderman et al.
- *Direct Connection:* rSLDS captured neural nonstationarities via switching latent modes rather than changing pairwise couplings, highlighting a gap that NetFormer fills by letting directed connections vary continuously with state through attention.

### 📊 Baseline

**Spatio-temporal correlations and visual signalling in a complete neuronal population** (2008)
- *Authors:* Pillow et al.
- *Direct Connection:* Their coupled spike-train GLM is a canonical baseline for inferring directed but stationary synaptic influences, whose static-coupling limitation NetFormer directly addresses by making weights a function of instantaneous neural state.

**Discovering Latent Network Structure in Point Process Data** (2014)
- *Authors:* Linderman and Adams
- *Direct Connection:* Network Hawkes models infer sparse directed interaction matrices from event data under stationary kernels, and NetFormer replaces this assumption with a state-conditioned attention matrix to capture nonstationary, nonlinear interactions.

### 🔧 Extension

**Neural Granger Causality for Nonlinear Time Series** (2018)
- *Authors:* Tank et al.
- *Direct Connection:* By showing neural networks can recover directed dependencies via lag-structured inputs and sparsity, this work is extended in NetFormer by tying directional influence to query–key similarities, enabling nonlinear, state-dependent Granger effects.

---

## Synthesis: How Prior Work Led to This Paper

A point-process GLM view of neural population activity established that directed effective connectivity can be encoded by coupling filters on spike histories, providing a rigorous bridge between statistical models and synaptic influence (Truccolo et al.). This formulation became a workhorse baseline, exemplified by coupled GLMs applied to complete retinal populations, but these couplings were effectively stationary once fit (Pillow et al.). Parallel work with network Hawkes processes inferred sparse directed interaction matrices from events, again assuming stationary kernels and linear superposition (Linderman and Adams). To address nonstationarity, recurrent switching linear dynamical systems modeled neural dynamics with discrete mode switches, capturing changes in regime but not continuous, state-contingent changes in pairwise influence (Linderman et al.). In a different vein, Neural Relational Inference showed how interaction graphs could be learned from trajectories via learned pairwise messages, placing graph discovery at the heart of dynamical modeling (Kipf et al.). Neural Granger causality demonstrated that neural networks can recover directed dependencies from lagged inputs under sparsity constraints, but typically with time-invariant structures (Tank et al.). Finally, Temporal Fusion Transformers illustrated how attention can be architected for interpretability over variables and time (Lim et al.). Together, these works exposed a gap: interpretable, directed network inference that is both nonlinear and continuously state- (thus time-) dependent. NetFormer synthesizes the GLM/Hawkes interpretability of directed influence with NRI-style graph-from-dynamics and TFT’s interpretable attention by treating each neuron’s recent history as a token and using query–key mappings to produce a state-conditioned attention matrix, yielding an analytically grounded, nonstationary effective connectivity model.

---

*Analysis generated on: 2026-01-06T13:21:46.674641*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
