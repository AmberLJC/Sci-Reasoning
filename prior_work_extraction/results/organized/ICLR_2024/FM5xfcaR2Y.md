# Prior Work Analysis Report

## Target Paper

**Title:** Post-hoc bias scoring is optimal for fair classification

**Conference:** ICLR 2024 (spotlight)

**Authors:** Wenlong Chen, Yegor Klochkov, Yang Liu

**Keywords:** group fairness, post-hoc fair classification, Bayes optimal classifier, accuracy-fairness trade-off

**Abstract:** 
> We consider a binary classification problem under group fairness constraints, which can be one of Demographic Parity (DP), Equalized Opportunity (EOp), or Equalized Odds (EO). We propose an explicit characterization of Bayes optimal classifier under the fairness constraints, which turns out to be a simple modification rule of the unconstrained classifier. Namely, we introduce a novel instance-level measure of bias, which we call bias score, and the modification rule is a simple linear rule on to...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Equality of Opportunity in Supervised Learning** (2016)
- *Authors:* Moritz Hardt et al.
- *Direct Connection:* By introducing Equalized Odds/Opportunity and showing they can be enforced via post-hoc group-specific thresholding of scores, this work established the post-processing paradigm that the current paper generalizes and characterizes as Bayes-optimal via bias-score rules.

### 💡 Inspiration

**The Cost of Fairness in Binary Classification** (2018)
- *Authors:* Aditya Menon et al.
- *Direct Connection:* Their Bayes-risk analysis showed that optimal DP/EOp solutions amount to thresholding a modified score, directly motivating the paper’s instance-level bias score that formalizes this modification and extends it to EO with a simple linear rule.

### 🔍 Gap Identification

**On Fairness and Calibration** (2017)
- *Authors:* Geoff Pleiss et al.
- *Direct Connection:* Their result that calibrated scores cannot satisfy Equalized Odds without group-dependent thresholds highlighted the need for principled post-hoc threshold adjustments that the bias-score rule systematizes and proves optimal.

### 📊 Baseline

**Classification with Fairness Constraints: A Meta-Algorithm with Provable Guarantees** (2019)
- *Authors:* L. Elisa Celis et al.
- *Direct Connection:* As a leading baseline that enforces group-fairness via cost-sensitive learning and randomized post-processing, this method is supplanted here by a deterministic bias-score post-hoc rule with a Bayes-optimal characterization.

### 🔧 Extension

**A Reductions Approach to Fair Classification** (2018)
- *Authors:* Alekh Agarwal et al.
- *Direct Connection:* The reductions framework casts DP/EOp/EO as constrained risk minimization with Lagrange multipliers, a structure the current paper leverages to derive finite sufficient statistics (bias scores) and a closed-form post-hoc optimal modification instead of retraining.

### 🔗 Related Problem

**Decoupled Classifiers for Group-Fairness** (2018)
- *Authors:* Cynthia Dwork et al.
- *Direct Connection:* By advocating per-group decision rules to reconcile accuracy and fairness, this work foreshadowed the paper’s design that achieves the same effect post-hoc with a single global rule over bias scores rather than training separate models.

---

## Synthesis: How Prior Work Led to This Paper

Equality of Opportunity in Supervised Learning introduced Equalized Odds and Equal Opportunity and showed that fairness can be achieved by post-hoc group-specific thresholding of calibrated scores, establishing a powerful paradigm for black-box adjustments. The Cost of Fairness in Binary Classification then analyzed Bayes risk under statistical fairness, revealing that optimal fair decisions correspond to thresholding modified versions of the class-probability score. A Reductions Approach to Fair Classification reframed DP/EOp/EO as constrained ERM solved via Lagrangian multipliers, providing a practical and theoretically grounded route—through cost-sensitive classification—to navigate accuracy–fairness trade-offs. Classification with Fairness Constraints operationalized these ideas into a meta-algorithm that often relies on randomized post-processing or retraining to meet constraints with guarantees. Decoupled Classifiers for Group-Fairness emphasized that per-group decision rules can recover accuracy under constraints, advocating structural adjustments aligned with group membership. On Fairness and Calibration exposed the incompatibility between calibration and Equalized Odds, underscoring the necessity of group-dependent thresholds and motivating post-hoc adjustments rather than purely calibrated scoring.
Collectively, these works suggested that optimal fairness often amounts to simple threshold shifts derived from a constrained optimization view, yet they lacked a unified, instance-level quantity that yields provably Bayes-optimal post-hoc rules across DP, EOp, and EO (and their compositions). The current paper synthesizes these insights by deriving bias scores—finite sufficient statistics from the Lagrangian characterization—and proving that thresholding a single bias score (DP/EOp) or fitting a two-parameter linear rule (EO) is Bayes-optimal, delivering a simple, deterministic post-hoc procedure that preserves accuracy while satisfying group-fairness constraints, even with multiple sensitive attributes.

---

*Analysis generated on: 2026-01-06T10:47:17.669893*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
