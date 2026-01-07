# Prior Work Analysis Report

## Target Paper

**Title:** Noisy Interpolation Learning with Shallow Univariate ReLU Networks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Nirmit Joshi, Gal Vardi, Nathan Srebro

**Keywords:** Interpolation Learning, Benign Overfitting, ReLU Networks

**Abstract:** 
> Understanding how overparameterized neural networks generalize despite perfect interpolation of noisy training data is a fundamental question. Mallinar et. al. (2022) noted that neural networks seem to often exhibit ``tempered overfitting'', wherein the population risk does not converge to the Bayes optimal error, but neither does it approach infinity, yielding non-trivial generalization. However, this has not been studied rigorously.  We provide the first rigorous analysis of the overfiting beh...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Benign Overfitting in Linear Regression** (2020)
- *Authors:* Peter L. Bartlett et al.
- *Direct Connection:* It formalized the benign-overfitting paradigm for minimum-norm interpolation in linear models, providing the conceptual and technical baseline that this work extends beyond linear predictors to shallow ReLU networks and contrasts with its tempered/catastrophic findings.

**A Function Space View of Deep ReLU Networks** (2019)
- *Authors:* John Ongie et al.
- *Direct Connection:* Their function-space and spline characterization of shallow ReLU networks—especially in 1D as linear splines with data-aligned knots—provides the structural lens the current paper exploits to analyze how the minimum-ℓ2-norm interpolant propagates label noise between samples.

**Breaking the Curse of Dimensionality with Convex Neural Networks** (2017)
- *Authors:* Francis Bach
- *Direct Connection:* This work introduced a function-space regularization framework and representer-type insights for shallow ReLU networks, motivating the study of minimum-parameter-norm interpolants that the present paper adopts to derive rigorous overfitting behavior.

### 🔍 Gap Identification

**Tempered Overfitting in Neural Networks** (2022)
- *Authors:* Mallinar et al.
- *Direct Connection:* This paper empirically documented 'tempered overfitting' under label noise, and the current work directly answers it by giving the first rigorous, nuanced analysis (L1 tempered vs. L2 catastrophic) for minimum-ℓ2-norm interpolants of two-layer ReLU networks.

### 🔗 Related Problem

**Harmless (Benign) Interpolation of Noisy Data in Regression** (2021)
- *Authors:* Adhitya Muthukumar et al.
- *Direct Connection:* Their precise risk analysis for ridgeless (minimum-norm) linear regression serves as the main comparative template that this paper departs from, by showing qualitatively different behavior for minimum-ℓ2-norm ReLU interpolants—bounded L1 but divergent L2 risk.

**Consistency of Interpolation with Kernel Methods** (2019)
- *Authors:* Alexander Rakhlin and Xiyu Zhai
- *Direct Connection:* By establishing when minimum-norm kernel interpolants generalize under noise, this work frames the interpolation-learning question that the current paper resolves in the non-kernel, parameter-norm–regularized ReLU setting with contrasting (tempered vs. catastrophic) outcomes.

---

## Synthesis: How Prior Work Led to This Paper

Mallinar and colleagues observed that when neural networks interpolate noisy labels, test error often does not blow up but also does not reach Bayes error, dubbing the phenomenon “tempered overfitting.” In parallel, Bartlett et al. established the formal notion of benign overfitting for minimum-norm interpolants in linear regression, identifying when perfect fit can still yield near-optimal risk. Muthukumar et al. sharpened this in ridgeless linear regression by providing explicit risk characterizations for minimum-norm solutions, clarifying when interpolation remains harmless. For nonparametric interpolants, Rakhlin and Zhai proved consistency guarantees for minimum-norm kernel fits under noise, reinforcing that interpolation need not be pathological. On the representational side, Ongie et al. provided a function-space view of shallow ReLU networks, showing in one dimension they realize linear splines with knots aligned to data, a structure crucial for precise noise propagation analysis. Bach’s convex neural networks perspective supplied representer-style intuition linking parameter norms to function-space regularizers, legitimizing a minimum-parameter-norm lens for shallow ReLU. Together, these threads highlighted a sharp gap: while minimum-norm interpolants can be analyzed rigorously in linear and kernel settings, the overfitting behavior of minimum-ℓ2-norm shallow ReLU interpolants under noise was unresolved. Leveraging the 1D spline structure and the minimum-norm perspective, the current work fills this gap, proving that interpolation with shallow ReLUs yields bounded L1 risk yet catastrophic L2 risk, thereby formalizing and refining the tempered-overfitting observation.

---

*Analysis generated on: 2026-01-06T23:39:57.427541*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
