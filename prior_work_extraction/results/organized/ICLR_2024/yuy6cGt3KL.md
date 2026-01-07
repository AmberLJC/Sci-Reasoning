# Prior Work Analysis Report

## Target Paper

**Title:** Empirical Analysis of Model Selection for Heterogeneous Causal Effect Estimation

**Conference:** ICLR 2024 (spotlight)

**Authors:** Divyat Mahajan, Ioannis Mitliagkas, Brady Neal, Vasilis Syrgkanis

**Keywords:** Heterogeneous Treatment Effect Estimation, Conditional Average Treatment Effect, Causal Inference, Model Selection

**Abstract:** 
> We study the problem of model selection in causal inference, specifically for conditional average treatment effect (CATE) estimation. Unlike machine learning, there is no perfect analogue of cross-validation for model selection as we do not observe the counterfactual potential outcomes. Towards this, a variety of surrogate metrics have been proposed for CATE model selection that use only observed data. However, we do not have a good understanding regarding their effectiveness due to limited comp...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Recursive partitioning for heterogeneous causal effects** (2016)
- *Authors:* Susan Athey and Guido Imbens
- *Direct Connection:* By proposing the transformed outcome approach used to proxy treatment effects from observed data, this paper supplied the factual-only “tau-risk” style metric that is systematically evaluated and tuned in the present analysis.

**Doubly Robust Policy Evaluation and Learning** (2011)
- *Authors:* Miroslav Dudík, John Langford, and Lihong Li
- *Direct Connection:* Their IPS/DR estimators for off-policy value are directly used as value-based surrogate selection metrics by scoring CATE models through induced policies, which this work rigorously benchmarks and tunes.

**Real-World Uplift Modeling with Significance and Policy Control** (2011)
- *Authors:* Nicholas J. Radcliffe and Patrick D. Surry
- *Direct Connection:* They introduced uplift curves and the Qini/AUUC family of metrics that serve as practical, widely used selection criteria, which this paper includes as key baselines for model selection without counterfactuals.

**Double/debiased machine learning for treatment and structural parameters** (2018)
- *Authors:* Victor Chernozhukov et al.
- *Direct Connection:* Its Neyman-orthogonal scores and cross-fitting principles underpin the doubly robust, orthogonalized risks (including R-loss/DR value) and motivate the paper’s emphasis on careful nuisance estimation and hyperparameter tuning.

### 📊 Baseline

**Metalearners for estimating heterogeneous treatment effects using machine learning** (2019)
- *Authors:* Sören R. Künzel, Jasjeet S. Sekhon, Peter J. Bickel, and Bin Yu
- *Direct Connection:* This paper formalized the S-/T-/X-learners that constitute the primary CATE model families between which the surrogate metrics select, providing core baselines for the empirical comparisons.

### 🔧 Extension

**Quasi-oracle estimation of heterogeneous treatment effects** (2021)
- *Authors:* Xinkun Nie and Stefan Wager
- *Direct Connection:* This work introduced the orthogonal R-loss that provides a computable surrogate objective for CATE and is repurposed and benchmarked here as a central model-selection criterion (with careful tuning of its nuisance estimates).

---

## Synthesis: How Prior Work Led to This Paper

Orthogonal learning for treatment effects established a computable surrogate risk: Nie and Wager’s R-loss provides an objective that depends only on observed outcomes and nuisance functions, enabling out-of-sample scoring of CATE models. Athey and Imbens earlier introduced the transformed outcome idea, turning observed data and propensities into a proxy label for treatment effect, which underlies tau-risk style factual-only selection. In parallel, off-policy evaluation advanced practical value-based surrogates: Dudík, Langford, and Li’s IPS/DR estimators estimate counterfactual policy value from observational data, furnishing natural criteria to rank CATE models via induced treat-versus-not-treat decisions. Uplift modeling supplied operational evaluation curves—Radcliffe and Surry’s Qini/AUUC—that summarize incremental impact and are often used to choose among uplift/CATE models. On the modeling side, Künzel et al. unified the S-/T-/X-learner meta-frameworks that produce a diverse set of CATE predictors among which selection is necessary. Finally, Chernozhukov et al.’s orthogonalization and cross-fitting formalized robust nuisance estimation, directly supporting both R-loss and DR-style selection metrics. Together these strands yielded multiple, competing surrogate selection criteria—orthogonal risk, transformed-outcome risk, uplift curves, and policy-value estimators—yet with limited head-to-head evaluation and unclear sensitivity to nuisance and tuning. The current work naturally synthesizes this landscape by benchmarking these specific surrogates across prominent CATE learners, systematically tuning their nuisance/hyperparameters (guided by orthogonalization principles), and augmenting evaluation with more realistic generative data—thereby revealing when each surrogate best aligns with true CATE accuracy and proposing improved model-selection strategies.

---

*Analysis generated on: 2026-01-06T07:31:39.665591*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
