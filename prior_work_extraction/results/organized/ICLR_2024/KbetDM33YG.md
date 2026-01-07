# Prior Work Analysis Report

## Target Paper

**Title:** Online GNN Evaluation Under Test-time Graph Distribution Shifts

**Conference:** ICLR 2024 (spotlight)

**Authors:** Xin Zheng, Dongjin Song, Qingsong Wen, Bo Du, Shirui Pan

**Keywords:** Graph neural networks, Model evaluation, Distribution shift

**Abstract:** 
> Evaluating the performance of a well-trained GNN model on real-world graphs is a pivotal step for reliable GNN online deployment and serving. 
Due to a lack of test node labels and unknown potential training-test graph data distribution shifts, conventional model evaluation encounters limitations in calculating performance metrics (e.g., test error) and measuring graph data-level discrepancies, particularly when the training graph used for developing GNNs remains unobserved during test time.
In ...

---

## Key Prior Works (6 papers with direct influence)

### 💡 Inspiration

**Test-Time Training with Self-Supervision for Generalization under Distribution Shift** (2020)
- *Authors:* Yu Sun et al.
- *Direct Connection:* By demonstrating that self-supervised objectives can drive useful label-free adaptation at test time, this paper directly inspires the idea of retraining a deployed GNN on unlabeled test graphs and reading out model behavior changes as a proxy for generalization.

### 🔍 Gap Identification

**A Simple Baseline for Detecting Dataset Shift** (2019)
- *Authors:* Stephan Rabanser et al.
- *Direct Connection:* This work detects shift via two-sample testing that requires access to the training/source distribution, a dependence the current paper explicitly removes by proposing label- and source-free online evaluation via learning-behavior discrepancy.

**To Trust or Not to Trust A Classifier** (2018)
- *Authors:* Heinrich Jiang et al.
- *Direct Connection:* Trust Score estimates correctness without test labels by comparing test points to training data, a requirement the present work overcomes by eliminating reliance on the (often unavailable) training graph and instead exploiting model retraining dynamics.

**Detecting and Correcting for Label Shift with Black Box Predictors** (2018)
- *Authors:* Zachary C. Lipton et al.
- *Direct Connection:* This label-shift framework depends on estimating source/target label marginals or black-box prediction distributions from the source, highlighting the limitation the new online GNN evaluation addresses when the training graph (and its label distribution) is unavailable.

### 🔧 Extension

**TENT: Fully Test-Time Adaptation by Entropy Minimization** (2021)
- *Authors:* Dequan Wang et al.
- *Direct Connection:* This work showed that a trained model can be updated on unlabeled test inputs via entropy minimization, and the present paper repurposes this label-free, per-batch test-time updating in GNNs and uses the induced change in predictions as the LeBeD learning-behavior discrepancy signal to estimate test error under shift.

### 🔗 Related Problem

**Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles** (2017)
- *Authors:* Balaji Lakshminarayanan et al.
- *Direct Connection:* Ensemble disagreement was shown to correlate strongly with errors, and the present work leverages this insight by replacing multi-model disagreement with intra-model learning-behavior discrepancy induced by brief retraining as a single-model proxy for accuracy under shift.

---

## Synthesis: How Prior Work Led to This Paper

Shift detection methods commonly rely on direct comparisons between training and test distributions: two-sample testing over features or predictions can flag dataset shift, but it presupposes access to the source data distribution (Rabanser et al.). Relatedly, Trust Score estimates correctness without labels by contrasting test points against training data neighborhoods (Jiang et al.), and label-shift correction leverages source and target label marginals or black-box source predictions (Lipton et al.), all of which depend on information from the training domain. In contrast, test-time adaptation lines of work showed that models can be updated on unlabeled test inputs: entropy minimization enables label-free per-batch optimization at deployment (Wang et al., TENT), and self-supervised auxiliary objectives provide another practical route to test-time updating under distribution shift (Sun et al., Test-Time Training). Independently, uncertainty research established that behavioral disagreement—e.g., across ensemble members—tracks prediction errors, especially out of distribution (Lakshminarayanan et al.). Together these threads expose an opportunity: evaluate reliability on unlabeled test graphs without any access to the training graph. Building on the feasibility of label-free test-time updates, and the insight that disagreement signals error, the current paper retrains the deployed GNN briefly on the test graph and measures the induced change in its behavior as a proxy for generalization, complemented by a parameter-free optimality criterion to govern this retraining when no labels or source data are available—thus turning adaptation dynamics into an online evaluation signal under graph distribution shifts.

---

*Analysis generated on: 2026-01-06T09:32:55.552436*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
