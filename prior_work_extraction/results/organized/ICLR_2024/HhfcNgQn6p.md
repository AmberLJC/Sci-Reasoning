# Prior Work Analysis Report

## Target Paper

**Title:** Towards a statistical theory of data selection under weak supervision

**Conference:** ICLR 2024 (oral)

**Authors:** Germain Kolossov, Andrea Montanari, Pulkit Tandon

**Keywords:** Data Selection, Empirical Risk Minimization, Influence Functions, High dimensional asymptotics

**Abstract:** 
> Given a sample of size $N$, it is often useful to select a subsample of smaller size $n<N$ to be used for statistical estimation or learning.  Such a data selection step is useful to reduce the requirements of data labeling and the computational complexity of learning. We assume to be given $N$ unlabeled samples $x_{i}$, and to be given access to a  'surrogate model' that can predict labels $y_i$ better than random guessing. Our goal is to select a subset of the samples, to be denoted by {$x_{i}...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* Provides the influence-function calculus used to quantify how selecting or reweighting examples perturbs ERM solutions and downstream risk, a core analytical tool in this work.

**A Modern Maximum Likelihood Theory for High-Dimensional Logistic Regression** (2019)
- *Authors:* Prasad Sur et al.
- *Direct Connection:* Supplies precise high-dimensional asymptotics for GLM estimators that are adapted here to characterize generalization when training after subset selection guided by a surrogate.

**Surprises in High-Dimensional Ridgeless Least Squares** (2019)
- *Authors:* Trevor Hastie et al.
- *Direct Connection:* Provides analytic risk formulas for overparameterized ridge/least-squares models that this paper leverages to compare training on the full dataset versus selected subsets under high-dimensional asymptotics.

### 💡 Inspiration

**Beyond Neural Scaling Laws: Beating Power Law Scaling via Data Pruning** (2022)
- *Authors:* Robert Sorscher et al.
- *Direct Connection:* Demonstrates empirically that carefully selected subsets can outperform full-data training, directly motivating this paper’s theoretical investigation of when and why such data selection works under weak supervision.

### 🔍 Gap Identification

**Optimal Subsampling for Large Sample Logistic Regression** (2018)
- *Authors:* HaiYing Wang et al.
- *Direct Connection:* Introduces inverse-probability (Horvitz–Thompson) reweighted estimators and score-based sampling for GLMs, whose popular unbiased reweighting rationale is explicitly analyzed and shown to be suboptimal in this paper’s weak-supervision setting.

### 📊 Baseline

**GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning** (2021)
- *Authors:* Killamsetty et al.
- *Direct Connection:* Uses influence-function-based bilevel optimization with a proxy/validation signal to pick training subsets, which this paper formalizes and analyzes statistically under a surrogate-driven weak supervision model.

---

## Synthesis: How Prior Work Led to This Paper

Influence functions provided a tractable way to approximate how upweighting or removing individual examples perturbs ERM solutions and predictions, enabling principled reasoning about data importance at training time. In large-sample GLM settings, optimal subsampling methods proposed selecting points with probabilities tied to score or leverage and correcting with inverse-probability (Horvitz–Thompson) reweighting to achieve unbiased estimating equations; this established a widely used, theoretically justified reweighting paradigm. High-dimensional asymptotics for GLMs characterized by precise limit theorems showed how logistic MLE behaves when the number of parameters scales with sample size, while parallel risk formulas for ridge and ridgeless least squares quantified generalization as a function of sample size, regularization, and feature geometry. On the algorithmic side, generalization-driven subset selection frameworks operationalized influence-function and bilevel ideas to select training data using a proxy or validation signal. Empirically, recent data-pruning studies showed that small, carefully chosen subsets—often guided by early-training or surrogate signals—can match or even surpass performance from using the entire dataset.
Together, these works revealed a tantalizing opportunity: theory described ERM behavior in high dimensions and offered IF-based sensitivity tools, while practical subset selection relied on surrogate or proxy signals and unbiased reweighting heuristics. The present paper synthesizes these strands, formalizing a weak-supervision model with a surrogate that is better than random, and using low- and high-dimensional asymptotics plus influence-function analysis to pinpoint when selection can outperform full-data ERM and why popular unbiased reweighting can be harmful—thus turning empirical observations into a predictive statistical theory.

---

*Analysis generated on: 2026-01-06T17:05:46.235298*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
