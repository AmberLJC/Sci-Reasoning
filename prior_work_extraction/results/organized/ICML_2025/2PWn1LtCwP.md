# Prior Work Analysis Report

## Target Paper
**Title:** 2PWn1LtCwP
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Distribution-Free Predictive Inference for Regression** (2018)
- *Authors:* Jing Lei et al.
- *Connection:* Introduces split conformal prediction as a general, distribution-free calibration framework that the proposed survival method builds on to obtain finite-sample calibrated lower bounds.

**Correcting for noncompliance and dependent censoring in an AIDS clinical trial with inverse probability of censoring weighted (IPCW) log-rank tests** (2000)
- *Authors:* James M. Robins et al.
- *Connection:* Establishes IPCW for right-censored data, underpinning the paper’s use of censoring-model-based weighting inside conformal calibration to address informative dropout.

**Nonparametric Estimation from Incomplete Observations** (1958)
- *Authors:* Edward L. Kaplan et al.
- *Connection:* Defines the canonical right-censoring framework and survival function estimation that the paper’s problem formulation and evaluation hinge upon.

### 💡 Inspiration

**Doubly robust estimation in missing data and causal inference** (2005)
- *Authors:* Hyunseung Bang et al.
- *Connection:* Introduces the doubly robust paradigm that directly motivates this paper’s asymptotic double robustness—validity when either the censoring model or the survival outcome model is correct.

### 🔧 Extension

**Conformalized Quantile Regression** (2019)
- *Authors:* Yaniv Romano et al.
- *Connection:* Provides the conformal calibration of lower quantiles that this paper adapts to survival times, replacing standard scores with censoring-aware, weighted scores after imputation.

**Conformal Prediction under Covariate Shift** (2019)
- *Authors:* Ryan J. Tibshirani et al.
- *Connection:* Establishes importance-weighted conformal calibration, a key ingredient the paper leverages to correct for censoring-induced selection via weights tied to the censoring mechanism.

### 🔗 Related Problem

**Linear regression with censored data** (1979)
- *Authors:* James Buckley et al.
- *Connection:* Introduces imputation-based handling of censoring in regression, inspiring the paper’s strategy of imputing latent censoring times before conformal calibration.

---

## Synthesis

The paper’s core idea—distribution-free lower prediction bounds for survival times under general right censoring with an asymptotic doubly robust guarantee—stands on two pillars: conformal calibration and semiparametric missing-data theory. Split conformal inference (Lei et al., 2018) and conformalized quantile regression (Romano et al., 2019) supply the calibration machinery for lower bounds, which the authors adapt to survival outcomes. Crucially, they integrate importance-weighted conformal calibration (Tibshirani et al., 2019) so that the nonconformity scores are reweighted to offset selection induced by censoring, paralleling the inverse-probability-of-censoring-weighting logic established by Robins and collaborators (Robins et al., 2000). The methodological innovation is to first impute latent censoring times with a flexible ML model—an idea in the spirit of imputation strategies for censored regression dating back to Buckley–James (1979)—and then conformally calibrate a survival model on the imputed data using censoring-aware weights. The asymptotic double robustness property directly echoes the Bang–Robins (2005) paradigm: validity holds if either the censoring model (used for imputation/weights) or the survival model is well specified. Finally, the right-censoring formulation and empirical evaluation are grounded in the classical Kaplan–Meier framework (Kaplan–Meier, 1958). Together, these works directly enable the paper’s leap from prior conformal survival procedures limited to type-I censoring to a robust, general right-censoring solution with principled guarantees.

---
*Generated: 2026-01-06T23:07:19.624834*
