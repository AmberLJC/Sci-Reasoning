# Prior Work Analysis Report

## Target Paper

**Title:** Debiased Collaborative Filtering with Kernel-Based Causal Balancing

**Conference:** ICLR 2024 (spotlight)

**Authors:** Haoxuan Li, Chunyuan Zheng, Yanghao Xiao, Peng Wu, Zhi Geng, Xu Chen, Peng Cui

**Keywords:** Recommender System, Causal Inference, Bias, Debias, Balancing

**Abstract:** 
> Collaborative filtering builds personalized models from the collected user feedback. However, the collected data is observational rather than experimental, leading to various biases in the data, which can significantly affect the learned model. To address this issue, many studies have focused on propensity-based methods to combat the selection bias by reweighting the sample loss, and demonstrate that
balancing is important for debiasing both theoretically and empirically. However, there are two ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Counterfactual Risk Minimization: Learning from Logged Bandit Feedback** (2015)
- *Authors:* Adith Swaminathan and Thorsten Joachims
- *Direct Connection:* This work formalized IPS-based learning from logged implicit feedback, which the current paper analyzes for bias under finite-dimensional imbalance and augments with kernel-based balancing.

**Doubly Robust Policy Evaluation and Learning** (2011)
- *Authors:* Miroslav Dudík et al.
- *Direct Connection:* It introduced the doubly robust estimator whose bias the present work characterizes through function-class imbalance and then reduces via kernel-based causal balancing.

### 💡 Inspiration

**Balanced Policy Evaluation and Learning** (2018)
- *Authors:* Nathan Kallus
- *Direct Connection:* By framing off-policy error as worst-case loss over a function class and proposing RKHS/IPM balancing objectives, this work directly motivates the paper's kernel-based balancing of functions to control IPS/DR bias.

**Kernel Balancing: A Flexible Non-Parametric Weighting Method for Estimating Causal Effects** (2020)
- *Authors:* Chad Hazlett
- *Direct Connection:* It shows that matching RKHS mean embeddings yields weights that balance all functions in that RKHS, a principle the paper adopts to construct universal kernel-based causal balancing for recommendation.

### 🔍 Gap Identification

**Minimax Weighting for Off-Policy Evaluation with Partial Coverage** (2020)
- *Authors:* Masatoshi Uehara et al.
- *Direct Connection:* By showing IPS/DR bias can explode under partial coverage and can be bounded via function-class balancing, it highlights the exact limitation the paper addresses by choosing and effectively balancing that class via kernels.

### 📊 Baseline

**Recommendations as Treatments: Debiasing Learning and Evaluation** (2016)
- *Authors:* Tobias Schnabel et al.
- *Direct Connection:* This paper instantiated propensity-weighted collaborative filtering (e.g., IPS/SNIPS-MF) as the core debiasing baseline that the new method directly improves by specifying and enforcing balance over a function class.

### 🔧 Extension

**Balanced and Robust Causal Inference with Kernel Optimal Matching** (2020)
- *Authors:* Nathan Kallus
- *Direct Connection:* Providing convex programs that directly minimize RKHS imbalance with variance control, this method is extended to the user–item setting and coupled with IPS/DR training in the paper's kernel-based balancing scheme.

---

## Synthesis: How Prior Work Led to This Paper

Counterfactual Risk Minimization introduced inverse propensity scoring as a learning objective for logged bandit/implicit-feedback data, establishing the propensity-weighted risk that subsequent recommendation methods rely on. Recommendations as Treatments instantiated this idea for collaborative filtering, popularizing IPS/SNIPS-weighted matrix factorization and highlighting selection bias in observational feedback. Doubly Robust Policy Evaluation and Learning combined outcome modeling with propensity weighting to mitigate variance while preserving consistency, defining the DR estimators that many debiasing systems use. Balanced Policy Evaluation and Learning reframed off-policy error as worst-case loss over a function class and proposed RKHS/IPM-based balancing to control that error through explicit function-class matching. Kernel Balancing demonstrated that matching RKHS mean embeddings yields weights that balance an entire (potentially infinite) function class, providing a constructive kernel-based route to balance without specifying features. Kernel Optimal Matching operationalized this by solving convex programs that minimize RKHS imbalance subject to variance control. Minimax Weighting for Off-Policy Evaluation further showed that under partial coverage, IPS/DR bias is governed by imbalance over a chosen function class, emphasizing the need to pick and effectively balance that class.
Taken together, these works expose a gap: propensity/DR methods in recommendation lack a principled answer to which functions must be balanced and how to achieve that balance efficiently during training. The present paper synthesizes the balance-based view with kernel methods, analyzing IPS/DR bias for finite-dimensional classes and then using RKHS mean-embedding matching to deliver universal, kernel-based causal balancing with adaptive updates in collaborative filtering training, a natural next step given these insights.

---

*Analysis generated on: 2026-01-06T06:05:49.610744*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
