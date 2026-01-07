# Prior Work Analysis Report

## Target Paper

**Title:** How much of my dataset did you use? Quantitative Data Usage Inference in Machine Learning

**Conference:** ICLR 2025 (oral)

**Authors:** Yao Tong, Jiayuan Ye, Sajjad Zarifzadeh, Reza Shokri

**Keywords:** Machine Learning, Privacy, Dataset Usage Inference, Dataset Ownership, Membership Inference Attack, Dataset Copyright

**Abstract:** 
> How much of my data was used to train a machine learning model? This is a critical question for data owners assessing the risk of unauthorized usage of their data to train models. However, previous work mistakenly treats this as a binary problem—inferring whether all-or-none or any-or-none of the data was used—which is fragile when faced with real, non-binary data usage risks. To address this, we propose a fine-grained analysis called Dataset Usage Cardinality Inference (DUCI), which estimates t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Membership Inference Attacks against Machine Learning Models** (2017)
- *Authors:* Reza Shokri et al.
- *Direct Connection:* This work established per-example membership scoring and calibration via shadow models, which the current paper repurposes—after debiasing—as the core sufficient statistics to estimate the fraction of a claimant dataset used in training.

**Membership Inference Attacks From First Principles** (2022)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* By casting membership testing as a likelihood-ratio problem and linking calibrated posteriors to optimal inference, this work motivates the paper’s use of debiased per-sample posteriors and its claim of matching the optimal MLE while being far more efficient.

### 💡 Inspiration

**Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting** (2018)
- *Authors:* Samuel Yeom et al.
- *Direct Connection:* The simple loss-threshold membership test from Yeom et al. provides scalable, per-sample membership guesses that the proposed method explicitly debiases and aggregates to infer dataset usage cardinality.

### 🔍 Gap Identification

**Radioactive Data: Tracing through training** (2020)
- *Authors:* Alexandre Sablayrolles et al.
- *Direct Connection:* This dataset-usage auditing approach framed the task as a binary presence test via data watermarking, a limitation that the present work overcomes by estimating the exact usage proportion without modifying the data.

### 🔧 Extension

**Comprehensive Privacy Analysis of Deep Learning: Passive and Active White-box Inference Attacks against Centralized and Federated Learning** (2019)
- *Authors:* Milad Nasr et al.
- *Direct Connection:* Stronger white-box membership signals from Nasr et al. serve as plug-in membership scores whose systematic biases the new algorithm corrects before aggregating them to quantify dataset usage.

### 🔗 Related Problem

**Knock Knock, Who’s There? Membership Inference on Aggregate Location Data** (2018)
- *Authors:* Ioannis Pyrgelis et al.
- *Direct Connection:* Demonstrating that aggregating individual-membership evidence can answer a binary group-inclusion query directly informs the paper’s move to aggregate debiased membership posteriors to estimate group cardinality rather than mere presence.

---

## Synthesis: How Prior Work Led to This Paper

Early work on membership inference established that model outputs carry per-example signals distinguishing training members from non-members; shadow-model calibration provided a way to turn those outputs into membership scores with measurable error rates. A simple and scalable refinement showed that the loss itself can act as an effective membership statistic, motivating practical, per-sample guesses that are easy to compute. White-box analyses then expanded the space of usable signals and clarified how architectural and training choices shape the score distributions for members versus non-members. A first-principles treatment cast membership testing as a likelihood-ratio problem, connecting well-calibrated posteriors to optimal decision rules and implicitly to maximum-likelihood mixture estimation when multiple examples are considered. In parallel, dataset-usage auditing emerged as a binary presence test—most notably via data watermarking that can verify if any of a marked dataset was used—while work on aggregate privacy demonstrated that summing individual membership evidence can answer group-level inclusion questions, albeit still as yes/no decisions. Taken together, these lines revealed two opportunities: per-sample membership posteriors can be calibrated and combined, and current dataset-usage audits are overly binary. The natural next step is to debias per-example membership guesses and aggregate them as sufficient statistics for estimating the mixture proportion of members within a claimant dataset, yielding an estimator that matches the optimal MLE implied by likelihood-ratio theory while avoiding the heavy computation of explicit mixture-model fitting.

---

*Analysis generated on: 2026-01-06T18:27:44.349501*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
