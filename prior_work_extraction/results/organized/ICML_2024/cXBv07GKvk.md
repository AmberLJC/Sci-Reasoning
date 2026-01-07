# Prior Work Analysis Report

## Target Paper
**Title:** cXBv07GKvk
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**The Bayesian Learning Rule** (2021)
- *Authors:* Mohammad Emtiyaz Khan et al.
- *Connection:* The Bayesian Learning Rule provides the theoretical framework that casts optimizer updates as variational inference steps, a foundation used to derive VON and thereby the improved IVON updates.

**Weight Uncertainty in Neural Networks** (2015)
- *Authors:* Charles Blundell et al.
- *Connection:* This work established mean-field variational learning for neural networks, defining the posterior parameterization (factorized Gaussian over weights) that IVON employs and scales to modern deep architectures.

### 💡 Inspiration

**VOGN: Variational Online Gauss–Newton** (2018)
- *Authors:* Wu Lin et al.
- *Connection:* VOGN introduced the core idea of online variational learning with diagonal Gaussian posteriors using Gauss–Newton/Fisher curvature, which IVON extends toward Adam-level efficiency and modern large-scale settings.

### 🔍 Gap Identification

**Practical Deep Learning with Bayesian Principles** (2019)
- *Authors:* Kazuki Osawa et al.
- *Connection:* By demonstrating scalable Bayesian training via noisy natural gradients with KFAC but at notable extra cost, this work highlighted the need for Adam-cost variational methods that IVON delivers.

### 📊 Baseline

**Variational Online Newton** (2023)
- *Authors:* Gian Maria Marconi et al.
- *Connection:* IVON is a direct improvement over VON, keeping the same variational online-Newton formulation but introducing refinements that make it as fast as Adam while remaining stable and effective on very large networks.

**Adam: A Method for Stochastic Optimization** (2015)
- *Authors:* Diederik P. Kingma et al.
- *Connection:* Adam is the primary training baseline that IVON is designed to match or outperform while providing calibrated predictive uncertainty.

---

## Synthesis

IVON’s core contribution—showing that variational learning can train very large networks at Adam-like cost with superior uncertainty—arises from a clear lineage within variational second-order methods. The immediate precursor is Variational Online Newton (VON), which formulated variational learning as an online Newton-style update with diagonal posterior parameters; IVON directly improves this method to be robust and performant on modern large models. Earlier, VOGN (Variational Online Gauss–Newton) introduced the practical recipe for online variational updates using Gauss–Newton/Fisher curvature, seeding the idea that one can maintain a Gaussian posterior over weights with per-parameter second-order statistics at near–first-order cost. These algorithmic developments rest on the Bayesian Learning Rule, which unifies optimization and variational inference, providing the theoretical footing for deriving such updates and connecting adaptive optimizers with approximate Bayesian learning.

Foundationally, Weight Uncertainty in Neural Networks established mean-field variational posteriors for deep nets, but its perceived limitations on large models helped crystallize the widespread belief that IVON decisively challenges. In parallel, Practical Deep Learning with Bayesian Principles showed that scalable Bayesian training is possible via noisy natural gradients (e.g., KFAC), but with significant additional curvature-computation overhead—precisely the gap IVON closes by achieving Bayesian-quality uncertainty at Adam-level cost. Finally, Adam serves as the practical baseline whose compute profile and performance IVON targets and surpasses, anchoring the paper’s empirical claim that variational learning is effective for today’s large deep networks.

---
*Generated: 2026-01-06T23:09:26.495629*
