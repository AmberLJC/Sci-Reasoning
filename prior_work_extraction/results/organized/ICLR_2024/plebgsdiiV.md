# Prior Work Analysis Report

## Target Paper

**Title:** Kernel Metric Learning for In-Sample Off-Policy Evaluation of Deterministic RL Policies

**Conference:** ICLR 2024 (spotlight)

**Authors:** Haanvid Lee, Tri Wahyu Guntara, Jongmin Lee, Yung-Kyun Noh, Kee-Eung Kim

**Keywords:** off-policy evaluation, reinforcement learning, deterministic policy, continuous actions, metric learning

**Abstract:** 
> We consider off-policy evaluation (OPE) of deterministic target policies for reinforcement learning (RL) in environments with continuous action spaces. While it is common to use importance sampling for OPE, it suffers from high variance when the behavior policy deviates significantly from the target policy. In order to address this issue, some recent works on OPE proposed in-sample learning with importance resampling. Yet, these approaches are not applicable to deterministic target policies for ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Fitted Q Evaluation (FQE): Off-Policy Evaluation via Supervised Learning** (2019)
- *Authors:* Hoang Le et al.
- *Direct Connection:* FQE formalized policy evaluation by regressing TD targets, and the present method targets the MSE of precisely these TD update vectors while modifying the sampling via a kernel relaxation of the deterministic policy.

### 💡 Inspiration

**Balanced Off-Policy Evaluation in Finite MDPs** (2020)
- *Authors:* Nathan Kallus et al.
- *Direct Connection:* This work cast OPE as an in-sample, RKHS/IPM balancing problem with an explicit bias–variance trade-off, directly inspiring the idea to learn a kernel (and its metric) that minimizes the mean-squared error of Bellman update estimates.

**Kernel-based Reinforcement Learning** (2002)
- *Authors:* Daniel Ormoneit et al.
- *Direct Connection:* By showing how kernel smoothing over state–action space can approximate Bellman backups and how kernel bandwidth controls bias–variance, this paper motivated relaxing actions via a kernel and learning its metric for accurate TD update estimation.

**Balanced Policy Evaluation and Learning** (2019)
- *Authors:* Nathan Kallus
- *Direct Connection:* This paper introduced kernel/IPM balancing with explicit MSE control, providing the key insight of learning weighting metrics to trade bias for variance that is adapted here to learn action-kernel metrics for TD estimation.

### 🔍 Gap Identification

**Breaking the Curse of Horizon: Off-Policy Evaluation with Marginalized Importance Sampling** (2018)
- *Authors:* Qiang Liu et al.
- *Direct Connection:* MIS reduces variance by marginalizing actions but still presumes stochastic policies/coverage, highlighting the gap for deterministic continuous-action targets that motivates smoothing the target with a kernel.

### 📊 Baseline

**DualDICE: Behavior-Agnostic Estimation of Discounted Stationary Distribution Corrections** (2019)
- *Authors:* Ofir Nachum et al.
- *Direct Connection:* DualDICE provides a leading in-sample OPE approach that avoids action-density ratios via stationary distribution correction, serving as a principal comparator that the kernel-relaxation strategy seeks to outperform in deterministic continuous-action settings.

---

## Synthesis: How Prior Work Led to This Paper

Kernel/IPM-based balancing methods established that off-policy evaluation can be performed in-sample by learning weights that minimize a bias–variance objective rather than relying purely on likelihood ratios. Balanced Policy Evaluation and Learning provided the core idea of kernel-induced discrepancies and regularization to control MSE, while Balanced Off-Policy Evaluation in Finite MDPs demonstrated this principle for MDPs with explicit finite-horizon guarantees and an RKHS formulation that connects weighting choice to error in Bellman residuals. Independently, Fitted Q Evaluation (FQE) framed policy evaluation as regression on Bellman targets, making the mean-squared error of estimated TD update vectors the central quantity governing accuracy. Classic kernel-based reinforcement learning showed how kernel smoothing in state–action space approximates Bellman backups and how kernel bandwidth/metric dictates the bias–variance trade-off of such estimates. DualDICE further advanced in-sample OPE by eschewing action-density ratios through stationary distribution correction, becoming a strong baseline for continuous-action settings. Finally, Marginalized Importance Sampling revealed that marginalizing actions can reduce variance but still assumes stochastic policies or sufficient support, leaving deterministic continuous-action targets problematic. Together these works suggest a natural next step: retain the in-sample, MSE-centric viewpoint of FQE and kernel/IPM balancing, but address the deterministic-action singularity by softening the target with a kernel over actions and learning its metric to optimally trade bias and variance of TD updates. This synthesis both generalizes kernel smoothing to state-conditional action neighborhoods and operationalizes MSE-optimal metric selection, yielding an OPE method tailored to deterministic policies in continuous action spaces.

---

*Analysis generated on: 2026-01-06T13:46:58.362887*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
