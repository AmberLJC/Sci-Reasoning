# Prior Work Analysis Report

## Target Paper
**Title:** rqyXubsBhH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Least Ambiguous Set-Valued Classifiers With Bounded Error Levels** (2019)
- *Authors:* R. Sadinle et al.
- *Connection:* Introduced the formal problem of set-valued classification and the trade-off between coverage/error and set size that underlies presenting a set of admissible labels to an expert, which this paper adopts as the basic decision-support paradigm.

**Counterfactual Risk Minimization: Learning from Logged Bandit Feedback** (2015)
- *Authors:* A. Swaminathan et al.
- *Connection:* Supplies the counterfactual (off-policy) learning framework the paper uses to optimize which prediction sets to show based on logged human–system interactions without needing a parametric expert model.

### 💡 Inspiration

**Does the Model Help? On the Complementarity of Human–Machine Predictions** (2021)
- *Authors:* G. Bansal et al.
- *Connection:* Empirically demonstrates that naive model outputs often fail to improve human decisions, motivating the paper’s key idea to design prediction sets specifically optimized (via counterfactual learning) for human–AI complementarity.

### 🔍 Gap Identification

**Predict Responsibly: Improving Accuracy by Learning to Defer to a Human** (2018)
- *Authors:* J. Madras et al.
- *Connection:* Represents the stylized-expert modeling approach (learning-to-defer) that this paper explicitly seeks to avoid by learning from actual expert behavior via counterfactual evaluation.

**Consistent Estimators for Learning to Defer to an Expert** (2020)
- *Authors:* H. Mozannar et al.
- *Connection:* Formalizes defer-to-expert learning under assumptions about expert accuracy; the present work addresses the limitation of assuming or modeling the expert by learning directly from logged interactions.

### 📊 Baseline

**Classification with Valid and Adaptive Coverage** (2020)
- *Authors:* Y. Romano et al.
- *Connection:* Provides practical conformal prediction-set methods (e.g., APS/RAPS) that serve as the default way to construct label sets; the present work builds on these sets but learns, from interaction data, which sets to present to optimize downstream human accuracy.

### 🔧 Extension

**Doubly Robust Policy Evaluation and Learning** (2011)
- *Authors:* M. Dudík et al.
- *Connection:* Provides IPS/DR estimators for unbiased and variance-reduced off-policy evaluation that the paper adapts to estimate the performance of alternative prediction-set policies from observational logs.

---

## Synthesis

The paper’s central innovation—optimizing set-valued model outputs for human decision support using counterfactual learning—sits at the intersection of set-valued prediction and off-policy policy optimization. The set-based decision-support paradigm is grounded in Sadinle et al., who formalized set-valued classification and its core trade-off between error control and set size. Romano et al. then made such sets practically viable in multiclass settings through conformal prediction methods like APS/RAPS; these serve as the default mechanisms to construct prediction sets and constitute the primary baseline the present work seeks to improve upon. However, prior approaches to human–AI collaboration commonly relied on modeling expert behavior—exemplified by learning-to-defer methods from Madras et al. and the consistency-focused framework of Mozannar and Sontag—which require stylized or parametric assumptions about experts. The current paper explicitly targets this gap by leveraging logged interactions to learn which prediction sets to present without positing an expert model. This shift is enabled by the counterfactual learning literature: Swaminathan and Joachims provide the counterfactual risk minimization framework for learning from logged bandit feedback, while Dudík, Langford, and Li offer IPS/DR estimators that make off-policy evaluation statistically principled and efficient. Finally, empirical evidence from Bansal et al. that naive model outputs often fail to aid humans motivates optimizing the content of prediction sets specifically for complementarity. Together, these works directly shape the paper’s formulation and methodology for counterfactual prediction sets.

---
*Generated: 2026-01-06T23:09:26.487070*
