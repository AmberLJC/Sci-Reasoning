# Prior Work Analysis Report

## Target Paper
**Title:** 3eHNvPHL9Z
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Bayesian Learning for Neural Networks** (1996)
- *Authors:* Radford M. Neal
- *Connection:* Established the foundational viewpoint that a distribution over parameters induces a prior over functions, a lens this paper adopts to analyze how a seemingly uniform parameter prior yields a rich, biased function prior.

**Deep Neural Networks as Gaussian Processes** (2018)
- *Authors:* Jaehoon Lee et al.
- *Connection:* Formalized the function-space perspective of randomly initialized networks, underpinning this paper’s argument that parameter redundancy drives a non-uniform function prior under ostensibly ‘flat’ parameter sampling.

### 💡 Inspiration

**Deep learning generalizes because the parameter-function map is biased towards simple functions** (2018)
- *Authors:* Guillermo Valle-Pérez et al.
- *Connection:* Proposed that many more parameter settings implement simple functions than complex ones, directly motivating this paper’s core claim that a flat prior over parameters induces a non-uniform simplicity bias over functions.

### 🔍 Gap Identification

**Reconciling modern machine-learning practice and the classical bias–variance trade-off** (2019)
- *Authors:* Mikhail Belkin et al.
- *Connection:* Framed the interpolation generalization puzzle (and double descent), the specific gap this paper addresses by proving that typical random interpolators generalize when a narrow teacher exists.

**Understanding deep learning requires rethinking generalization** (2017)
- *Authors:* Chiyuan Zhang et al.
- *Connection:* Showed that overparameterized networks can memorize yet still generalize, highlighting the need for a bias-based explanation that this paper supplies via the induced function prior from uniform parameters.

### 🔧 Extension

**Neural networks are biased towards simple functions** (2020)
- *Authors:* Samuel E. Mingard et al.
- *Connection:* Provided empirical and theoretical evidence quantifying the simplicity bias in neural networks, which this work extends to the conditional setting of interpolators and formalizes via the ‘narrow teacher’ lens.

### 🔗 Related Problem

**Benign overfitting in linear regression** (2020)
- *Authors:* Peter L. Bartlett et al.
- *Connection:* Characterized when interpolating linear models generalize due to low effective dimension, informing this paper’s ‘narrow teacher’ condition as the nonlinear neural-network analogue of small intrinsic complexity.

---

## Synthesis

The present work explains why a neural network sampled uniformly over parameters, conditioned on interpolating the data, can nonetheless generalize: a flat parameter prior induces a highly non-uniform prior over functions that favors simpler hypotheses, especially those implementable by narrow networks. This insight directly builds on the function-space view inaugurated by Neal (1996) and modernized by Lee et al. (2018), which assert that distributions over weights define priors over functions. Valle-Pérez et al. (2018) and Mingard et al. (2020) then argued and quantified that the parameter–function map is exponentially biased toward simple functions because many more parameter settings realize them—precisely the mechanism this paper formalizes for the conditional distribution over interpolators. The central motivation arises from the interpolation generalization puzzle articulated by Zhang et al. (2017) and Belkin et al. (2019): despite fitting the data exactly, overparameterized networks often generalize, a phenomenon this work explains without relying on optimization dynamics. Finally, the paper’s ‘narrow teacher’ assumption mirrors the low effective complexity conditions underpinning benign overfitting in linear models (Bartlett et al., 2020), translating that intuition to nonlinear networks: when labels are realizable by a smaller (narrow) network, the induced function prior concentrates mass on such simpler solutions. Together, these works directly shape the paper’s core innovation: a rigorous, function-prior explanation for why typical interpolating neural networks generalize under narrow teachers.

---
*Generated: 2026-01-06T23:09:26.465656*
