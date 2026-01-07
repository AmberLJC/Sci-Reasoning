# Prior Work Analysis Report

## Target Paper

**Title:** Learning to Reject Meets Long-tail Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Harikrishna Narasimhan, Aditya Krishna Menon, Wittawat Jitkrittum, Neha Gupta, Sanjiv Kumar

**Keywords:** Learning to reject, balanced error, evaluation metrics, selective classification, plug-in approach, long-tail learning, class imbalance, non-decomposable metrics

**Abstract:** 
> Learning to reject (L2R) is a classical problem where one seeks a classifier capable of abstaining on low-confidence samples. Most prior work on L2R has focused on minimizing the standard misclassification error. However, in many real-world applications, the label distribution is highly imbalanced,  necessitating alternate evaluation metrics such as the balanced error or the worst-group error that enforce equitable performance across both the head and tail classes. In this paper, we establish th...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**On optimum recognition error and reject trade-off** (1970)
- *Authors:* C. K. Chow
- *Direct Connection:* Chow’s Bayes rule for 0–1 loss with abstention is the conceptual starting point that this paper generalizes to balanced error and other non-decomposable metrics by deriving the coupled optimal classifier–rejector conditions.

**Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization** (2020)
- *Authors:* Shiori Sagawa et al.
- *Direct Connection:* By formalizing worst-group error as a target objective, this work provides the metric that the present paper extends its Bayes-optimal selective-classification theory and plug-in method to handle.

### 💡 Inspiration

**Long-tail Learning via Logit-Adjusted Softmax Loss** (2021)
- *Authors:* Aditya Krishna Menon et al.
- *Direct Connection:* The logit-adjustment insight—embedding class-prior–dependent costs to optimize balanced error—directly informs this paper’s plug-in estimator for the classifier and its coupling with the rejector under long-tail metrics.

### 🔍 Gap Identification

**Classification with a Reject Option using a Hinge Loss** (2008)
- *Authors:* Peter L. Bartlett et al.
- *Direct Connection:* This surrogate-based abstention method targets 0–1 error, and its limitation—ignoring class- or group-dependent costs—motivates the present work’s derivation of Bayes-optimal reject rules tailored to balanced error.

### 📊 Baseline

**SelectiveNet: A Deep Neural Network with an Integrated Reject Option** (2019)
- *Authors:* Yarin Geifman et al.
- *Direct Connection:* SelectiveNet is a primary selective-classification baseline that optimizes standard misclassification risk, which this paper shows can be grossly suboptimal under balanced error and thereby directly improves upon.

### 🔧 Extension

**Consistent Binary Classification with Generalized Performance Metrics** (2014)
- *Authors:* Oluwasanmi O. Koyejo et al.
- *Direct Connection:* Building on the confusion-matrix–based Bayes analysis and plug-in strategies for non-decomposable metrics, this paper extends the framework to the selective setting where reject decisions interact with label costs.

---

## Synthesis: How Prior Work Led to This Paper

Chow established the Bayes-optimal decision rule for classification with a reject option under 0–1 loss, tying abstention to posterior thresholds and class-dependent costs. Bartlett and Wegkamp introduced consistent surrogate losses for abstention, but still optimized standard misclassification risk, decoupled from class or group asymmetries. In deep learning, SelectiveNet integrated a rejector into a classifier to shape the risk–coverage curve, again targeting overall error rather than equity-aware metrics. Separately, Menon and colleagues showed that balanced error in long-tail regimes can be optimized by embedding class priors as costs via logit adjustment, giving a practical plug-in route to Bayes-optimal classification under imbalance. Koyejo and co-authors provided a general confusion-matrix perspective, deriving Bayes rules and plug-in strategies for non-decomposable metrics by linking decisions to metric-induced costs. Sagawa et al. formalized worst-group error through GroupDRO, elevating robustness to the worst subpopulation as an explicit metric to optimize.
Together, these works expose a gap: selective-classification methods focus on average 0–1 error, while long-tail and robustness metrics require decision rules that couple class/group-specific costs with rejection. The natural next step is to derive the Bayes-optimal classifier–rejector for equity-focused metrics (balanced and worst-group error) and to operationalize it via a plug-in approach. By marrying Chow’s abstention principle with logit-adjusted costs and confusion-matrix–based plug-in analysis, the current work produces a coupled decision rule and estimator that align rejection with class/group costs, overcoming the suboptimality of prior 0–1–centric selective methods.

---

*Analysis generated on: 2026-01-06T10:18:05.646582*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
