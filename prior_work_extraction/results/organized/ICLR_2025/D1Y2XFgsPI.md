# Prior Work Analysis Report

## Target Paper

**Title:** Imputation for prediction: beware of diminishing returns.

**Conference:** ICLR 2025 (spotlight)

**Authors:** Marine Le Morvan, Gael Varoquaux

**Keywords:** imputation, missing

**Abstract:** 
> Missing values are prevalent across various fields, posing challenges for training and deploying predictive models. In this context, imputation is a common practice, driven by the hope that accurate imputations will enhance predictions. However, recent theoretical and empirical studies indicate that simple constant imputation can be consistent and competitive. This empirical study aims at clarifying 
*if* and *when* investing in advanced imputation methods yields significantly better predictions...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Linear models with missing values: Why and how to use mean imputation for prediction** (2021)
- *Authors:* Marine Le Morvan et al.
- *Direct Connection:* This work provided the key theoretical insight that simple constant (mean) imputation—especially when paired with missingness indicators—can yield consistent and competitive predictive performance, directly motivating the present paper’s empirical investigation of when more accurate imputations actually translate into better predictions.

**Handling Missing Values when Applying Classification Models** (2007)
- *Authors:* Maya Z. Saar-Tsechansky and Foster Provost
- *Direct Connection:* By showing that modeling missingness explicitly (e.g., via indicators or selective imputation) can improve predictive accuracy, this paper established the practice the current study systematically tests across models and datasets, including the surprising benefits under MCAR.

**Multiple Imputation for Nonresponse in Surveys** (1987)
- *Authors:* Donald B. Rubin
- *Direct Connection:* Rubin’s framework formalized multiple imputation for valid inference, setting up the central contrast probed here: high imputation fidelity need not entail superior predictive risk, a premise this paper evaluates empirically.

### 🔍 Gap Identification

**Missing covariate data in clinical research: when and when not to use the missing-indicator method for analysis** (2012)
- *Authors:* Rolf H. H. Groenwold et al.
- *Direct Connection:* This paper’s caution against missingness indicators for estimation highlights a tension the current study addresses from a predictive perspective, clarifying when indicators help predictions—even under MCAR.

### 📊 Baseline

**mice: Multivariate Imputation by Chained Equations in R** (2011)
- *Authors:* Stef van Buuren and Karin Groothuis-Oudshoorn
- *Direct Connection:* As the canonical multiple-imputation pipeline widely presumed to enhance downstream modeling, MICE is a primary baseline whose imputation-vs-prediction tradeoffs the current paper quantifies against simple constant imputation and indicators.

**missForest—non-parametric missing value imputation for mixed-type data** (2012)
- *Authors:* Daniel J. Stekhoven and Peter Bühlmann
- *Direct Connection:* missForest represents a strong nonparametric imputer with high imputation accuracy that the present study benchmarks to test whether such gains meaningfully improve predictive performance, particularly with expressive predictors.

**GAIN: Missing Data Imputation using Generative Adversarial Nets** (2018)
- *Authors:* Jinsung Yoon et al.
- *Direct Connection:* As a state-of-the-art deep imputation method that often reports superior imputation metrics, GAIN is a direct baseline used to examine the diminishing returns from better imputations to downstream prediction.

---

## Synthesis: How Prior Work Led to This Paper

Rubin’s multiple imputation framework established principled inference with missing data, shaping decades of practice that implicitly equated better imputation with better downstream analyses. MICE operationalized this idea via chained equations, becoming the default advanced pipeline for tabular missingness, while missForest demonstrated strong nonparametric imputations for mixed data and GAIN pushed imputation accuracy further with deep adversarial training. In parallel, Saar-Tsechansky and Provost showed that explicitly modeling missingness—through indicators or selective imputation—can boost predictive accuracy, highlighting that missingness patterns themselves may be informative. Clinical guidance by Groenwold and colleagues cautioned against missing-indicator methods for estimation, implicitly separating inferential validity from predictive utility. Most crucially, theoretical results by Le Morvan and collaborators showed that simple constant imputation, especially paired with missingness indicators, can be consistent and competitive for prediction with linear models, reframing imputation as a means to minimize predictive risk rather than solely to reconstruct data. Together, these works revealed a gap: despite increasingly accurate imputers, evidence was mixed on whether such gains translate into better predictions, particularly with expressive learners and when missingness is modeled directly. The current paper synthesizes these insights by systematically quantifying the returns from imputation accuracy to predictive performance across diverse datasets and model classes, showing diminishing gains with expressive models and consistent benefits from missingness indicators—even under MCAR—thereby clarifying when investment in advanced imputation is warranted for prediction.

---

*Analysis generated on: 2026-01-06T10:52:05.147898*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
