# Prior Work Analysis Report

## Target Paper
**Title:** lQ2o7JteMO
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Principal Stratification in Causal Inference** (2002)
- *Authors:* Constantine E. Frangakis et al.
- *Connection:* Principal stratification formalized surrogate-based causal reasoning; the current paper’s core claim—that long-term treatments violate surrogate/principal surrogacy conditions—directly builds on and critiques this foundational framework.

**A New Approach to Causal Inference in Mortality Studies with a Sustained Exposure Period—Application of the G-Formula** (1986)
- *Authors:* James M. Robins
- *Connection:* Robins introduced potential-outcome formulations for sustained (longitudinal) exposures, which the present paper adopts to define the estimand for continual long-term treatment effects before mapping it to an RL value estimation problem.

**Doubly Robust Policy Evaluation and Learning** (2011)
- *Authors:* Miroslav Dudík et al.
- *Connection:* The doubly robust estimator for off-policy evaluation originated here; Tran, Bibaut, and Kallus leverage the same DR principle as the backbone for estimating long-term causal effects and for valid inference.

### 🔍 Gap Identification

**The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects** (2019)
- *Authors:* Susan Athey et al.
- *Connection:* This paper crystallized the surrogate-index approach for inferring long-run effects from short-run experiments, and its reliance on surrogacy is the explicit limitation Tran, Bibaut, and Kallus argue fails for continual (long-term) treatments, motivating their RL-based alternative.

### 🔧 Extension

**Doubly Robust Off-policy Value Evaluation for Reinforcement Learning** (2016)
- *Authors:* Nan Jiang et al.
- *Connection:* This work extended doubly robust estimation to MDPs, providing the concrete RL-OPE machinery that the current paper repurposes to estimate long-term effects of continual exposure from short-horizon experiments.

**Statistically Efficient Off-Policy Policy Evaluation for Reinforcement Learning** (2020)
- *Authors:* Nathan Kallus et al.
- *Connection:* Their semiparametric efficiency theory and DR-based estimators with valid asymptotic inference directly enable the paper’s construction of confidence intervals for long-term treatment effects via an RL-OPE reduction.

---

## Synthesis

The paper’s core innovation is to recast the problem of learning long-term causal effects of continual treatment from short-term experiments as an off-policy evaluation problem in reinforcement learning and to use doubly robust estimators to obtain point estimates and confidence intervals. This departs from the dominant surrogate-based paradigm. Athey, Chetty, Imbens, and Kang (2019) formalized the surrogate index approach for extrapolating long-run impacts using short-run proxies; Tran, Bibaut, and Kallus pinpoint that approach’s key limitation—surrogacy fails when the treatment exerts direct effects via continued exposure—thus motivating a different framework. This critique is grounded in the surrogacy/principal stratification foundations of Frangakis and Rubin (2002), which the present paper leverages to define precisely why surrogate conditions are untenable for long-term treatments. For the target estimand and longitudinal structure, the work draws on Robins (1986), whose g-formula and sustained-exposure framework provide the causal formalization of continuous treatment over time. The methodological leap is then enabled by the doubly robust lineage in off-policy evaluation: Dudík, Langford, and Li (2011) introduced DR estimators, Jiang and Li (2016) adapted DR to MDPs, and Kallus and Uehara (2020) established semiparametric efficiency and asymptotically valid inference for RL-OPE. Building directly on these DR-OPE advances, the paper shows how to identify and efficiently estimate the long-term effect of a continual intervention from short-horizon randomized data, complete with confidence intervals, without relying on invalid surrogacy assumptions.

---
*Generated: 2026-01-06T23:09:26.405659*
