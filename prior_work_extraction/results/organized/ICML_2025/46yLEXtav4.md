# Prior Work Analysis Report

## Target Paper
**Title:** 46yLEXtav4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Poisoning Attacks against Support Vector Machines** (2012)
- *Authors:* Battista Biggio et al.
- *Connection:* This paper introduced the bilevel optimization view of data poisoning that the present work generalizes from a single attacker to a coordinating collective optimizing joint impact under risk and feasibility constraints.

**Shilling Attacks Against Collaborative Filtering Recommender Systems** (2007)
- *Authors:* Bamshad Mobasher et al.
- *Connection:* This classic formulation of coordinated profile injection in product-rating platforms provides the domain and collusion paradigm that the current paper formalizes statistically and algorithmically for modern learning-based platforms.

### 💡 Inspiration

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Connection:* The paper’s a priori assessment of how small data changes affect a trained model and downstream platform decisions builds directly on influence-function approximations that can be computed from observed data.

### 🔍 Gap Identification

**Towards Poisoning of Deep Neural Networks** (2017)
- *Authors:* Luis Muñoz-González et al.
- *Connection:* Back-gradient poisoning requires white-box access and differentiating through training; the present work explicitly addresses this limitation by developing coordination algorithms that rely on statistically estimable quantities accessible to collectives.

### 📊 Baseline

**Poisoning Attacks to Graph-Based Recommender Systems** (2018)
- *Authors:* Minghao Fang et al.
- *Connection:* As a leading poisoning approach in recommendation domains, it serves as a baseline that the present work conceptually extends by enabling coordinated, risk-aware manipulation grounded in estimable platform-response effects.

### 🔧 Extension

**Using Machine Teaching to Attack Machine Learners** (2015)
- *Authors:* Shike Mei et al.
- *Connection:* By casting poisoning as optimal teaching of a learner, this work motivates the present paper’s set-level design of coordinated perturbations, which extends the teaching perspective to collective action with implementable, data-driven surrogates.

### 🔗 Related Problem

**Strategic Classification** (2016)
- *Authors:* Moritz Hardt et al.
- *Connection:* This work formalized strategic responses to learning systems, highlighting endogeneity and motivating the present paper’s shift to pre-training, collective data manipulation with methods that anticipate and quantify impact before acting.

---

## Synthesis

The core innovation of this paper is a statistical and algorithmic framework that enables collectives to forecast and coordinate the impact of their data manipulations on learning platforms using quantities inferable from observed data. The intellectual lineage starts with Biggio et al. (2012), which framed data poisoning as a bilevel optimization problem—an attacker optimizes data to influence a learner’s retrained model—providing the foundation that this work broadens from individual adversaries to coalitions with joint objectives and risk considerations. Mei and Zhu (2015) advanced a set-level, teaching perspective on poisoning; this paper extends that perspective to collective action, replacing full-information assumptions with implementable estimators. Muñoz-González et al. (2017) demonstrated gradient-based poisoning via backpropagating through training, but required white-box access; this limitation directly motivates the present work’s reliance on statistically estimable surrogates. The key enabler for such a priori assessments is influence-function methodology (Koh and Liang, 2017), which permits predicting model and decision changes from small data perturbations using only trained-model derivatives—exactly the kind of observable quantities accessible to collectives. In the application domain, classic shilling attacks (Mobasher et al., 2007) and modern poisoning of recommender systems (Fang et al., 2018) supply both the manipulation paradigm and concrete baselines; the current framework formalizes and generalizes these into coordinated, risk-aware strategies. Finally, strategic classification (Hardt et al., 2016) situates the work within the broader literature on endogenous responses to learning, underscoring the need for anticipatory, incentive-aware algorithms that the paper delivers for collective, pre-training manipulation.

---
*Generated: 2026-01-06T23:07:19.585971*
