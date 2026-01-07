# Prior Work Analysis Report

## Target Paper
**Title:** 2dz6psiiA0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Action understanding as inverse planning** (2009)
- *Authors:* Chris L. Baker et al.
- *Connection:* The proposed planner instantiates Baker et al.’s Bayesian Theory-of-Mind formalism by performing stepwise Bayesian updates over latent beliefs/desires via inverse planning, directly grounding our mental-state posteriors and likelihoods in that framework.

**A Framework for Sequential Planning in Multiagent Settings** (2005)
- *Authors:* P. J. Gmytrasiewicz et al.
- *Connection:* Our treatment of multi-step ToM as recursive belief modeling with sequential Bayesian updates is directly inherited from the I-POMDP framework, which provides the theoretical scaffold for scalable multi-step inference about other agents’ beliefs and intentions.

### 💡 Inspiration

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Connection:* Our weak-to-strong control—using a smaller specialist to guide a larger model—adapts the AI-feedback principle from Constitutional AI to transfer ToM-specific likelihood evaluation and reasoning behavior to larger LMs.

### 🔍 Gap Identification

**Machine Theory of Mind** (2018)
- *Authors:* Neil C. Rabinowitz et al.
- *Connection:* ToMnet’s monolithic, environment-specific learning highlighted poor scalability and generalization in deep ToM systems; our Bayesian planner explicitly addresses this gap with modular stepwise updates and cross-model transfer instead of end-to-end specialization.

**Large Language Models Still Can’t Plan** (2023)
- *Authors:* Varun Valmeekam et al.
- *Connection:* This work identifies the long-horizon planning failures of LLMs; our approach tackles that limitation by offloading multi-step reasoning to an explicit Bayesian planning loop and stabilizing it with ToM-specific likelihood estimation.

### 🔧 Extension

**Plan Recognition as Planning** (2009)
- *Authors:* M. Ramírez et al.
- *Connection:* We extend the plan-recognition-as-planning idea by using cost-based plan likelihoods as ToM-specific likelihood estimates, replacing hand-crafted or domain simulators with specialized small LMs to compute these likelihoods within our Bayesian updater.

### 🔗 Related Problem

**A Rational Speech Act model of pragmatic reasoning** (2016)
- *Authors:* Noah D. Goodman et al.
- *Connection:* We adopt RSA’s perspective of social cognition as recursive Bayesian inference about mental states, generalizing its pragmatic reasoning mechanism to multimodal ToM planning with sequential updates.

---

## Synthesis

The paper’s core innovation—scalable, multimodal Theory-of-Mind via a Bayesian planner with weak-to-strong control—sits squarely on two intertwined lineages: Bayesian ToM and weak-oversight transfer. From the Bayesian side, Baker et al. established ToM as inverse planning with explicit belief–desire posteriors, while I-POMDPs (Gmytrasiewicz & Doshi) provided the recursive, multi-step belief modeling and sequential updating needed for long-horizon social reasoning. Ramírez & Geffner’s plan-recognition-as-planning contributed the operational link between plans, costs, and observation likelihoods; the present work extends this by delegating ToM-specific likelihood estimation to smaller, specialized LMs that plug directly into our Bayesian updater. On the empirical front, two gaps motivate our design: ToMnet (Rabinowitz et al.) demonstrated the promise of learned ToM but suffered from environment-specificity and limited scalability, and Valmeekam et al. showed LLMs’ persistent failures on long-horizon planning. Our modular Bayesian loop explicitly addresses both, separating inference from representation and scaling across modalities. Finally, the transfer mechanism draws on weak-oversight principles from Constitutional AI—using weaker AI feedback to shape stronger models—repurposed here to transmit ToM-specific likelihood estimation and reasoning behavior from small to large LMs. Complementing these threads, the RSA framework reinforces the paper’s commitment to recursive Bayesian inference about mental states, now realized in a multimodal, long-form planning setting.

---
*Generated: 2026-01-06T23:07:19.563660*
