# Prior Work Analysis Report

## Target Paper

**Title:** "What Data Benefits My Classifier?" Enhancing Model Performance and Interpretability through Influence-Based Data Selection

**Conference:** ICLR 2024 (oral)

**Authors:** Anshuman Chhabra, Peizhao Li, Prasant Mohapatra, Hongfu Liu

**Keywords:** Data Selection, Interpretability, Fairness, Robustness

**Abstract:** 
> Classification models are ubiquitously deployed in society and necessitate high utility, fairness, and robustness performance. Current research efforts mainly focus on improving model architectures and learning algorithms on fixed datasets to achieve this goal. In contrast, in this paper, we address an orthogonal yet crucial problem: given a fixed convex learning model (or a convex surrogate for a non-convex model) and a function of interest, we assess what data benefits the model by interpretin...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Koh et al.
- *Direct Connection:* This work provides the core mechanism—per-example influence estimation via (approximate) inverse-Hessian–vector products for (locally) convex objectives—that the paper adapts to quantify how individual training points affect a chosen evaluation function and to interpret impacts in feature space.

**Data Shapley: Towards Equitable Valuation of Data for Machine Learning** (2019)
- *Authors:* Ghorbani et al.
- *Direct Connection:* By framing data valuation as measuring each point’s marginal contribution to model utility, this work motivates the paper’s objective of scoring training examples for their benefit, while the paper addresses Data Shapley’s computational cost by replacing Shapley values with tractable influence estimates.

### 💡 Inspiration

**Estimating Training Data Influence by Tracing Gradient Descent** (2020)
- *Authors:* Pruthi et al.
- *Direct Connection:* TracIn’s scalable gradient-path influence estimator informs the paper’s use of practical influence estimation to score data and serves as a direct comparator/alternative within the proposed influence-based selection framework.

### 📊 Baseline

**Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Group Loss** (2020)
- *Authors:* Sagawa et al.
- *Direct Connection:* GroupDRO is a primary robustness/fairness baseline whose limitation—needing group labels and modifying the training objective—is addressed by the paper’s influence-driven data selection that targets worst-group metrics without changing the loss.

### 🔧 Extension

**GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning** (2021)
- *Authors:* Killamsetty et al.
- *Direct Connection:* GLISTER’s bilevel, influence-based subset selection to optimize validation performance is directly generalized here to select data using influence signals targeted at functions beyond accuracy (fairness and robustness) and augmented with feature-space interpretability.

### 🔗 Related Problem

**FairBatch: Batch Selection for Model Fairness** (2021)
- *Authors:* Roh et al.
- *Direct Connection:* FairBatch’s idea of fairness-aware data selection for training motivates the paper’s broader, influence-based selection that directly optimizes fairness metrics and provides feature-space explanations rather than heuristic batch composition.

---

## Synthesis: How Prior Work Led to This Paper

Influence functions were adapted to modern machine learning by Koh and Liang, who showed how to estimate the effect of a single training point on a model’s parameters and predictions via inverse-Hessian–vector products under convexity assumptions; this provided a principled route from data to measured performance impact. GLISTER operationalized this influence signal for data subset selection, formulating a bilevel objective that greedily chooses training examples to maximize validation performance using first-order approximations. Data Shapley defined the goal of valuing individual datapoints by their marginal contribution to a target utility, but incurred prohibitive computational cost, highlighting the need for tractable proxies. TracIn introduced a scalable alternative by tracing gradients along the training trajectory to estimate point-wise influence, demonstrating that influence can guide practical data curation. For distributional robustness and fairness, GroupDRO reweighted objectives to protect worst-group performance but relied on group labels and specialized optimization, while FairBatch steered batch composition toward fairness, indicating that data selection itself can move fairness metrics without architectural changes. Collectively, these works exposed a clear opportunity: unify the valuation perspective with efficient influence estimation to select training data that optimizes arbitrary evaluation functions. The paper synthesizes this by adapting influence estimation for convex (or convex-surrogate) learners to score examples against utility, fairness, and robustness metrics, and by interpreting influence in feature space to explain and drive selection, thus providing a general, interpretable, and efficient data-centric route to improved performance.

---

*Analysis generated on: 2026-01-06T10:39:01.210800*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
