# Prior Work Analysis Report

## Target Paper
**Title:** rJxFvAs7pq
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Policy Gradient Methods for Reinforcement Learning with Function Approximation** (1999)
- *Authors:* Richard S. Sutton et al.
- *Connection:* This work introduced the policy-gradient formulation with function approximation that underlies the actor update; the present paper adopts this framework in continuous state-action spaces with neural network policies to analyze global, last-iterate convergence.

**Actor-Critic Algorithms** (2000)
- *Authors:* Vijay R. Konda et al.
- *Connection:* Konda and Tsitsiklis established the two-time-scale actor–critic scheme and its stochastic approximation under Markovian sampling, which the current paper directly analyzes but now with multi-layer neural parametrizations and last-iterate global guarantees.

**The ODE method for convergence of stochastic approximation and reinforcement learning** (2000)
- *Authors:* V. S. Borkar et al.
- *Connection:* The ODE/SA framework for handling Markovian noise is a core technical tool that the paper leverages to control actor–critic updates under Markovian sampling and derive finite-sample, last-iterate convergence.

### 💡 Inspiration

**Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator** (2018)
- *Authors:* Maryam Fazel et al.
- *Connection:* By revealing a PL/gradient-dominance-type landscape enabling global convergence of policy gradient, this work inspired the present paper’s use of weak-PL-style arguments to obtain global, last-iterate convergence for actor–critic.

### 🔍 Gap Identification

**Finite-Sample Analysis of Actor-Critic for Discounted MDPs** (2019)
- *Authors:* Shaofeng Zou et al.
- *Connection:* This paper provided finite-sample AC analysis but relied on linear approximation, i.i.d./MDS noise and often averaged-iterate guarantees; the present work explicitly closes these gaps by addressing Markovian sampling, neural networks, continuous spaces, and last-iterate global convergence.

### 📊 Baseline

**Natural Actor-Critic Algorithms** (2009)
- *Authors:* Shalabh Bhatnagar et al.
- *Connection:* As a canonical actor–critic baseline with convergence under Markovian sampling (for linear function approximation), this work is generalized here to multi-layer neural actors/critics with global optimality and last-iterate guarantees.

### 🔧 Extension

**Gradient Descent Finds Global Minima of Over-parameterized Deep Neural Networks** (2019)
- *Authors:* Simon S. Du et al.
- *Connection:* Techniques for controlling optimization dynamics of over-parameterized neural networks inform the paper’s analysis of multi-layer actor/critic networks, which is adapted to the RL/Markovian setting to achieve global last-iterate guarantees.

---

## Synthesis

The paper’s core contribution—global, last-iterate convergence of actor–critic under Markovian sampling with multi-layer neural parameterization in continuous spaces—rests on a direct lineage that brings together classic RL foundations, stochastic approximation under Markovian noise, and modern global convergence insights. Sutton et al. (1999) provide the policy-gradient formulation with function approximation that defines the actor component the paper studies, while Konda and Tsitsiklis (2000) introduce the two-time-scale actor–critic architecture and its analysis under Markovian sampling—the operational template the new results extend. Borkar and Meyn (2000) furnish the ODE/SA toolkit for Markovian noise, which the authors adapt to control coupled actor–critic recursions without resorting to i.i.d. assumptions. On the performance side, existing finite-sample AC analyses such as Zou et al. (2019) expose key gaps—linear approximation, i.i.d. noise, non-global or averaged-iterate guarantees—that the present work explicitly closes via its MMCLG criteria. To move from local to global guarantees and to the last-iterate, the paper draws on the global-optimization perspective of policy gradient landscapes exemplified by Fazel et al. (2018), importing weak-PL/graduent-dominance style reasoning into an AC setting. Finally, to accommodate multi-layer neural parameterizations, the analysis leverages ideas from over-parameterized neural network optimization (Du et al., 2019), adapting them to RL with Markovian sampling. These strands jointly enable the paper’s O~(ε^-3) last-iterate global convergence bounds for neural actor–critic in continuous domains.

---
*Generated: 2026-01-06T23:09:26.467674*
