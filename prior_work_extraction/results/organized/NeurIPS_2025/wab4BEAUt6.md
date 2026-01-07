# Prior Work Analysis Report

## Target Paper
**Title:** wab4BEAUt6
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**A Unified Approach to Interpreting Model Predictions** (2017)
- *Authors:* Scott M. Lundberg et al.
- *Connection:* Introduced SHAP as the game-theoretic framework and KernelSHAP for black-box models, defining the problem formulation that this paper solves more efficiently via a Fourier-domain closed form.

**Learning Decision Trees Using the Fourier Spectrum** (1993)
- *Authors:* Eyal Kushilevitz et al.
- *Connection:* Showed that decision trees admit sparse Fourier/Walsh spectra and provided algorithms to recover them, directly enabling this paper’s exact SHAP computation for trees via compact Fourier representations.

**Explaining Prediction Models and Individual Predictions with Feature Contributions** (2014)
- *Authors:* Erik Štrumbelj et al.
- *Connection:* Provided Monte Carlo Shapley estimation for general ML models, whose high computational cost the present work overcomes by replacing coalition sampling with a Fourier-based closed-form summation.

### 💡 Inspiration

**On the Spectral Bias of Neural Networks and its Implications for Function Approximation** (2019)
- *Authors:* Nasim Rahaman et al.
- *Connection:* Demonstrated that learned predictors emphasize low-frequency components, motivating the paper’s first-stage approximation of black-box models by compact Fourier representations.

### 🔍 Gap Identification

**GPUTreeShap: Fast Parallel Tree Shapley Explanations** (2022)
- *Authors:* Rory Mitchell et al.
- *Connection:* While GPUTreeShap accelerates TreeSHAP via parallelism, it still incurs per-instance costs; this work addresses that gap by deriving a Fourier-domain closed form enabling simple summations and amortized computation.

### 📊 Baseline

**From Local Explanations to Global Understanding with Explainable AI for Trees** (2020)
- *Authors:* Scott M. Lundberg et al.
- *Connection:* TreeSHAP provides exact polynomial-time SHAP for tree ensembles; the present paper offers an alternative exact path via a compact Fourier representation of trees and extends the approach to black-box models.

### 🔧 Extension

**Sobol’ Indices and Shapley Value** (2014)
- *Authors:* Art B. Owen
- *Connection:* Established a precise link between Shapley values and orthogonal ANOVA decompositions, which this paper extends by giving an explicit closed-form formula that computes SHAP directly from Fourier coefficients.

---

## Synthesis

The paper builds squarely on the SHAP framework introduced by Lundberg and Lee (2017), adopting its game-theoretic definition as the target attribution and its black-box setting as the problem scope. For tree models, TreeSHAP (Lundberg et al., 2020) is the exact baseline: it supplies a specialized dynamic program to compute SHAP, but it is model-class specific. Recent engineering advances like GPUTreeShap (Mitchell et al., 2022) parallelize TreeSHAP, yet they preserve per-instance runtime proportional to tree complexity, highlighting a gap in amortized, structure-exploiting computation that this work addresses.
A key theoretical lever comes from Owen (2014), who established a tight connection between Shapley values and orthogonal decompositions (ANOVA/Sobol). The present paper operationalizes and extends this idea to the Fourier domain, deriving a closed-form that “linearizes” SHAP into a simple sum over Fourier coefficients. This becomes especially powerful for models with compact spectra. The feasibility of such spectra is grounded in two strands: classic results showing decision trees have sparse Walsh/Fourier expansions and can be recovered efficiently (Kushilevitz & Mansour, 1993), and modern observations of spectral bias in learned predictors (Rahaman et al., 2019) indicating low-frequency dominance. Leveraging these, the authors propose a two-stage pipeline: compute a compact Fourier representation (exact for trees, approximate for black boxes), then obtain SHAP exactly from those coefficients via the new closed form. Compared to sampling-based SHAP estimators (e.g., Strumbelj & Kononenko, 2014), this eliminates Monte Carlo variance and enables amortized, parallel computation with a tunable accuracy–efficiency trade-off.

---
*Generated: 2026-01-06T23:08:23.945690*
