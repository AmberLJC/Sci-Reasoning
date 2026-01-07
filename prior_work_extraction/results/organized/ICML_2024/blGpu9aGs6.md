# Prior Work Analysis Report

## Target Paper
**Title:** blGpu9aGs6
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR** (2017)
- *Authors:* Wachter et al.
- *Connection:* Introduced counterfactual explanations as actionable changes to flip model decisions, providing the conceptual basis for framing recourse as feasible, low-cost interventions that this paper seeks to guarantee during model training.

**Actionable Recourse in Linear Classification** (2019)
- *Authors:* Ustun et al.
- *Connection:* Formalized algorithmic recourse as an optimization problem over actionable feature changes with costs and constraints; the present work directly adopts this actionable-recourse notion and its cost-bounded action sets when defining ‘reasonable actions’ and recourse coverage objectives for trees.

### 💡 Inspiration

**Towards Deep Learning Models Resistant to Adversarial Attacks** (2018)
- *Authors:* Madry et al.
- *Connection:* Provided the min–max adversarial training framework the authors leverage conceptually, recasting recourse assurance as a robust optimization over allowable actions and using worst-case losses to design a recourse-aware splitting objective.

### 🔍 Gap Identification

**FACE: Feasible and Actionable Counterfactual Explanations** (2020)
- *Authors:* Poyiadzi et al.
- *Connection:* Demonstrated that post-hoc counterfactual methods can fail to find feasible actions for models trained purely for accuracy, motivating this paper’s shift to training-time constraints that maximize the existence of reasonable recourse.

### 📊 Baseline

**Classification and Regression Trees** (1984)
- *Authors:* Breiman et al.
- *Connection:* Established the top-down greedy tree-induction paradigm that the authors directly modify, replacing the standard impurity-based split criterion with a recourse-aware, adversarially-evaluated objective to ensure action existence.

### 🔧 Extension

**Random Forests** (2001)
- *Authors:* Breiman
- *Connection:* The proposed recourse-aware splitting procedure is explicitly extended from single trees to random forests by applying the modified split objective within each tree under bagging, preserving ensemble accuracy while improving recourse coverage.

### 🔗 Related Problem

**Evasion and Hardening of Tree Ensemble Classifiers** (2016)
- *Authors:* Kantchelian et al.
- *Connection:* Showed how adversarial objectives can be posed and optimized for trees/ensembles; this informed the paper’s use of adversarial-style reasoning to evaluate splits and harden tree models with respect to action-bounded perturbations.

---

## Synthesis

The paper’s core idea—training decision trees and forests to be accurate while guaranteeing the existence of reasonable recourse—emerges from two converging lines of work. First, counterfactual explanations (Wachter et al.) and actionable recourse (Ustun et al.) established the intervention-based view of changing predictions through feasible, cost-bounded actions. Subsequent work exposed a key gap: post-hoc methods can fail to find feasible actions for models optimized solely for accuracy (Poyiadzi et al.), motivating a move from explaining fixed models to learning models that facilitate recourse. Second, adversarial robustness introduced the min–max training lens (Madry et al.), which the authors adapt to the recourse setting by treating action-bounded interventions as the adversary and optimizing splits under worst-case outcomes. Prior robustness work for trees (Kantchelian et al.) demonstrated that adversarial objectives are meaningful and optimizable for tree models, guiding how to incorporate robustness-style evaluations into split selection. Technically, the method is a direct modification of the classic top-down CART procedure (Breiman et al.), replacing impurity with a recourse-aware, adversarially computed objective, and it naturally extends to the random forest framework (Breiman 2001) by applying the same split logic within bagged trees. Together, these works directly shape the paper’s formulation and algorithm: recourse as actionable, feasible interventions; the identification of non-existence as the central limitation to address; and adversarial optimization as the mechanism to enforce recourse during learning.

---
*Generated: 2026-01-06T23:09:26.473729*
