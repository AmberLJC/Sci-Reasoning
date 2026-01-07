# Prior Work Analysis Report

## Target Paper
**Title:** CXkJh2ITml
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Mutual Information for the Multi-Layer Generalized Linear Model** (2017)
- *Authors:* Andre Manoel et al.
- *Connection:* Introduced the multi-layer generalized linear model (ML-GLM) teacher–student framework and AMP/replica characterizations for deep compositions, which this paper adopts to model deep random Gaussian networks and to derive Bayes-optimal predictions.

### 🔍 Gap Identification

**On the Power of Over-parameterization in Neural Networks Beyond Lazy Training** (2019)
- *Authors:* Zeyuan Allen-Zhu et al.
- *Connection:* Identified regimes and tasks where kernel/NTK methods are provably suboptimal while feature-learning neural networks succeed, motivating the paper’s investigation of sample-rich regimes where ridge/kernel become suboptimal but neural networks achieve near-zero error.

### 📊 Baseline

**High-dimensional asymptotics of prediction: Ridge regression and classification** (2018)
- *Authors:* Edgar Dobriban et al.
- *Connection:* Established closed-form risk asymptotics for ridge regression and classification with Gaussian design, which the present work leverages to show that optimally regularized ridge attains the Bayes-optimal error for deep random-network teachers in the proportional regime.

### 🔧 Extension

**Optimal Errors and Phase Transitions in High-Dimensional Generalized Linear Models** (2019)
- *Authors:* Jean Barbier et al.
- *Connection:* Provided rigorous Bayes-optimal error formulas and phase-transition characterizations for GLMs that the present work specializes and extends to multi-layer random networks with extensive width to obtain closed-form test errors.

**Generalisation error in learning with random features and neural networks** (2020)
- *Authors:* Federico Gerace et al.
- *Connection:* Derived learning-curve predictions for random features and two-layer neural networks in the high-dimensional teacher–student setting; the current paper generalizes this line to deep random networks and compares Bayes-optimal, kernel, RF, and ridge errors in closed form.

### 🔗 Related Problem

**A Random Matrix Perspective on Random Features: Beyond the Kernel Approximation** (2017)
- *Authors:* Olivier Louart et al.
- *Connection:* Developed RMT tools for analyzing random feature Gram matrices and their generalization behavior, informing this paper’s explicit test-error calculations for random features and kernels induced by deep random networks.

**A Modern Maximum-Likelihood Theory for High-Dimensional Logistic Regression** (2019)
- *Authors:* Pragya Sur et al.
- *Connection:* Characterized high-dimensional test error of logistic regression with Gaussian covariates; the current work benchmarks against these asymptotics to show logistic loss achieves near-Bayes-optimal classification in the deep random-teacher setting.

---

## Synthesis

The core advance of this paper—closed-form Bayes-optimal test errors for learning deep, extensive-width random Gaussian networks, together with exact learning curves for ridge, kernel, and random-features methods—rests on the teacher–student ML-GLM framework and its Bayes-optimal characterization. Manoel et al. introduced the multi-layer GLM model and AMP/replica methodology that precisely match the present paper’s deep compositional random network setting, while Barbier et al. provided rigorous Bayes-optimal error formulas and phase-transition results for GLMs that are here specialized to the deep, extensive-width regime and distilled into closed-form expressions. Building on the two-layer random-features and neural-network analyses of Gerace et al., this work extends the scope to arbitrarily deep random networks and compares multiple learners within a unified asymptotic framework. The ridge and kernel baselines are anchored by Dobriban and Wager’s high-dimensional risk formulas and Louart et al.’s random-matrix perspective on random features, which together enable explicit error characterizations for ridge, kernel, and random-features regression and reveal when optimally regularized ridge/kernel achieve Bayes-optimality. For classification, Sur and Candès’ sharp asymptotics for logistic regression inform the result that logistic loss is near-optimal under the deep random teacher. Finally, theoretical separations between kernel/lazy training and feature-learning networks, as highlighted by Allen-Zhu and Li, motivate and contextualize the paper’s finding that in sample-rich regimes ridge/kernel become suboptimal while neural networks attain vanishing error.

---
*Generated: 2026-01-06T23:09:26.542047*
