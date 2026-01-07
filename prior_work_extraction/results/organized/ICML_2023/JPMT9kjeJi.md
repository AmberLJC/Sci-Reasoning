# Prior Work Analysis Report

## Target Paper
**Title:** JPMT9kjeJi
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Causality: Models, Reasoning, and Inference** (2009)
- *Authors:* Judea Pearl
- *Connection:* CounTS instantiates Pearl’s abduction–action–prediction paradigm to perform counterfactual reasoning over time, operationalizing these three steps in a learned temporal generative model.

**Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR** (2018)
- *Authors:* Sandra Wachter et al.
- *Connection:* The paper adopts Wachter et al.’s formulation of counterfactual explanations (minimal changes that flip a decision) and extends it from static inputs to temporally coherent time series.

**Structured Inference Networks for Nonlinear State Space Models** (2017)
- *Authors:* Rahul G. Krishnan et al.
- *Connection:* The variational state-space modeling machinery (posterior inference from histories and forward generative simulation) from Deep Kalman Filters provides the backbone that CounTS adapts for counterfactual abduction and prediction in sequences.

### 💡 Inspiration

**Actionable Recourse in Linear Classification** (2019)
- *Authors:* Berk Ustun et al.
- *Connection:* CounTS incorporates the notion of actionable, cost-constrained changes introduced by Ustun et al., generalizing recourse constraints to temporally evolving features.

### 🔍 Gap Identification

**Algorithmic Recourse: from Counterfactual Explanations to Interventions** (2021)
- *Authors:* Amir-Hossein Karimi et al.
- *Connection:* Karimi et al. highlight that valid recourse must respect causal interventions; CounTS addresses this gap by embedding interventions within a learned temporal causal generative model to ensure feasible counterfactual trajectories.

### 📊 Baseline

**Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations** (2020)
- *Authors:* Ramaravind K. Mothilal et al.
- *Connection:* CounTS borrows multi-objective criteria (proximity, sparsity, diversity) from DiCE as evaluation/optimization signals and demonstrates improved, temporally plausible counterfactuals over such static baselines.

### 🔧 Extension

**Causal Effect Inference with Deep Latent-Variable Models** (2017)
- *Authors:* Christos Louizos et al.
- *Connection:* CounTS extends the CEVAE idea—counterfactual inference via variational latent-variable models—by building a sequential variant that supports abduction, intervention, and predictive rollout in time series.

---

## Synthesis

CounTS sits at the intersection of counterfactual explanation and sequential generative modeling. Pearl’s causal framework provides the conceptual core: counterfactuals are computed via abduction, action, and prediction. Wachter et al. formalized counterfactual explanations as minimally perturbed inputs that achieve target outcomes; CounTS adopts this objective but elevates it to the time-series setting by enforcing temporal coherence and feasibility over trajectories. To make such counterfactual inference learnable end-to-end, CounTS builds on the variational causal machinery of CEVAE, extending the idea of counterfactuals through deep latent-variable models from static settings to sequences. This extension is enabled by variational state-space modeling—specifically, the Structured Inference Networks/Deep Kalman Filters line—which CounTS repurposes for posterior abduction from observed histories and forward generative rollout under interventions. On the actionability front, Ustun et al.’s notion of cost-constrained, actionable recourse directly informs CounTS’s design of temporal intervention constraints, while Karimi et al.’s critique—that recourse must align with causal interventions—motivates embedding interventions within the learned generative model to ensure valid, feasible changes. Finally, DiCE serves both as a practical baseline and a source of evaluation criteria (proximity, sparsity, diversity), which CounTS adapts to sequential data; the model demonstrates superior, actionable counterfactual sequences without sacrificing predictive accuracy.

---
*Generated: 2026-01-06T23:09:26.532945*
