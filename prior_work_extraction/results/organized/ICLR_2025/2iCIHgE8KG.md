# Prior Work Analysis Report

## Target Paper

**Title:** Discovering Temporally Compositional Neural Manifolds with Switching Infinite GPFA

**Conference:** ICLR 2025 (spotlight)

**Authors:** Changmin Yu, Maneesh Sahani, Máté Lengyel

**Keywords:** Computational neuroscience, neural data analysis, Bayesian nonparametrics, latent variable modelling;

**Abstract:** 
> Gaussian Process Factor Analysis (GPFA) is a powerful latent variable model for extracting low-dimensional manifolds underlying population neural activities. However, one limitation of standard GPFA models is that the number of latent factors needs to be pre-specified or selected through heuristic-based processes, and that all factors contribute at all times. We propose the infinite GPFA model, a fully Bayesian non-parametric extension of the classical GPFA by incorporating an Indian Buffet Proc...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Gaussian-process factor analysis for low-dimensional single-trial analysis of neural population activity** (2009)
- *Authors:* Byron M. Yu et al.
- *Direct Connection:* The proposed model directly extends GPFA’s formulation of GP-driven latent trajectories and linear loadings by replacing its fixed, always-active factor set with a nonparametric, time-selective feature allocation.

**The Indian Buffet Process: An Introduction and Review** (2011)
- *Authors:* Thomas L. Griffiths et al.
- *Direct Connection:* The IBP provides the core infinite latent feature prior that enables the paper’s ‘infinite GPFA’ construction and automatic determination of how many factors are needed.

### 💡 Inspiration

**Dependent Indian Buffet Processes** (2010)
- *Authors:* Sinead A. Williamson et al.
- *Direct Connection:* The idea of introducing dependencies (e.g., via GPs) into IBP feature usage directly informs the paper’s temporally varying on/off gating of factors to achieve compositional activity over time.

### 🔍 Gap Identification

**Recurrent Switching Linear Dynamical Systems** (2017)
- *Authors:* Scott W. Linderman et al.
- *Direct Connection:* This switching LDS framework highlights the utility of discrete switching in neural dynamics but is limited to one regime at a time, motivating the paper’s factor-wise, compositional switching within a GPFA manifold.

### 🔧 Extension

**Nonparametric Bayesian Sparse Factor Models with the Indian Buffet Process** (2011)
- *Authors:* David M. Knowles et al.
- *Direct Connection:* This work’s use of an IBP prior to infer the number of factors and induce sparsity in factor loadings is explicitly adapted to endow GPFA with an unbounded, data-driven set of latent factors.

### 🔗 Related Problem

**The Beta Process Autoregressive HMM** (2011)
- *Authors:* Emily B. Fox et al.
- *Direct Connection:* By using a beta-process/IBP construction for an unbounded set of dynamical regimes, this work motivates the paper’s nonparametric feature allocation for time series, which is extended here to continuous GP latent factors with concurrent (compositional) activation.

---

## Synthesis: How Prior Work Led to This Paper

Gaussian-process factor analysis (GPFA) established a framework in which low-dimensional neural trajectories are modeled as smooth Gaussian processes combined through a linear loading matrix, but with a fixed number of factors that contribute at all times. Nonparametric Bayesian sparse factor models with the Indian Buffet Process (IBP) showed how an IBP prior can infer the number of factors and induce sparse loadings in factor analysis, offering a principled route to remove manual factor selection. The Indian Buffet Process itself provided the infinite latent feature prior enabling unbounded factor spaces. Dependent IBP models introduced covariate-dependent feature usage—often instantiated via Gaussian processes—demonstrating how feature activations can vary smoothly with time, furnishing a mechanism for temporally structured on/off gating. Recurrent switching linear dynamical systems (rSLDS) demonstrated the value of discrete switching for neural dynamics but restricted switching to single regimes rather than additive, compositional latent contributions. The beta process autoregressive HMM similarly used beta/IBP constructions to allow an unbounded set of dynamical atoms, but activations were regime-based rather than factor-wise and concurrent. Together, these works revealed an opportunity to merge GPFA’s smooth latent trajectories with IBP-driven, temporally dependent feature allocation, yielding a model that learns both how many factors are needed and which subset is active at each moment. The present paper synthesizes these insights by placing an (dependent) IBP prior over the factor loading process in GPFA, enabling temporally compositional switching of an unbounded factor set and addressing the key limitations of fixed dimensionality and always-on factors while retaining GPFA’s neural-manifold interpretability.

---

*Analysis generated on: 2026-01-06T19:23:49.097690*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
