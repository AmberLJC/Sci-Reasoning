# Prior Work Analysis Report

## Target Paper

**Title:** Robust Adversarial Reinforcement Learning via Bounded Rationality Curricula

**Conference:** ICLR 2024 (spotlight)

**Authors:** Aryaman Reddi, Maximilian Tölle, Jan Peters, Georgia Chalvatzaki, Carlo D'Eramo

**Keywords:** reinforcement learning, adversarial, bounded rationality, curriculum

**Abstract:** 
> Robustness against adversarial attacks and distribution shifts is a long-standing goal of Reinforcement Learning (RL). To this end, Robust Adversarial Reinforcement Learning (RARL) trains a protagonist against destabilizing forces exercised by an adversary in a competitive zero-sum Markov game, whose optimal solution, i.e., rational strategy, corresponds to a Nash equilibrium. However, finding Nash equilibria requires facing complex saddle point optimization problems, which can be prohibitive to...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Quantal Response Equilibria for Normal Form Games** (1995)
- *Authors:* Richard D. McKelvey et al.
- *Direct Connection:* This paper provides the bounded-rationality equilibrium concept (logit/QRE) and rationality parameter that underpins the paper’s entropy-regularized min–max objective and the idea of scheduling agents’ rationality.

**Markov Games as a Framework for Multi-Agent Reinforcement Learning** (1994)
- *Authors:* Michael L. Littman
- *Direct Connection:* Littman’s formulation of zero-sum Markov games and their Nash equilibria provides the formal problem setting that this work relaxes via entropy regularization to target QRE instead of strict Nash.

### 💡 Inspiration

**Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor** (2018)
- *Authors:* Tuomas Haarnoja et al.
- *Direct Connection:* SAC introduces the maximum-entropy RL objective and temperature-controlled stochastic policies that this work adopts for both agents to implement bounded rationality and derive soft best responses in the two-player game.

### 🔍 Gap Identification

**Action Robust Reinforcement Learning** (2019)
- *Authors:* Chen Tessler et al.
- *Direct Connection:* By modeling adversarial action perturbations, this work highlights brittleness and optimization difficulties of worst-case min–max training, motivating the need for smoother, regularized objectives pursued here.

**Adversarial Policies: Attacking Deep Reinforcement Learning** (2019)
- *Authors:* Adam Gleave et al.
- *Direct Connection:* This paper shows learned adversaries can reliably exploit RL policies in zero-sum settings, directly motivating adversarial training schemes whose instability the present work mitigates via bounded-rationality curricula.

### 📊 Baseline

**Robust Adversarial Reinforcement Learning** (2017)
- *Authors:* Lerrel Pinto et al.
- *Direct Connection:* RARL establishes the protagonist–adversary zero-sum training paradigm that this work directly modifies by adding entropy regularization and replacing the Nash target with a bounded-rationality QRE, forming the primary baseline being improved.

### 🔧 Extension

**Smoothing Techniques for Computing Equilibria in Extensive-Form Games** (2010)
- *Authors:* Sanae Hoda et al.
- *Direct Connection:* Hoda et al. show that entropy (dilated-entropy) regularization smooths saddle-point problems and yields QRE solutions, an insight this paper extends to zero-sum Markov games to ease adversarial RL optimization.

---

## Synthesis: How Prior Work Led to This Paper

RARL introduced training a protagonist against a learned adversary in a zero-sum setting, targeting Nash equilibria but exposing the practical difficulty of nonconvex, nonconcave saddle-point optimization. Quantal Response Equilibrium (QRE), defined by McKelvey and Palfrey, formalized bounded rationality via logit (entropy-regularized) best responses governed by a rationality parameter, offering a smoother alternative to strict Nash. In extensive-form games, Hoda and colleagues demonstrated that adding entropy (dilated-entropy) regularization smooths the optimization landscape and that the resulting equilibria correspond to QRE, making computation more tractable. In single-agent RL, Soft Actor-Critic established the maximum-entropy objective and temperature-controlled stochastic policies, providing a practical mechanism to implement bounded rationality and soft best responses. Littman’s Markov games framework supplied the formal zero-sum, multi-agent substrate within which these ideas can be combined. Complementary robust RL work on action perturbations revealed brittleness and conservatism in worst-case formulations, while adversarial policy attacks underscored the real vulnerability of standard policies to learned opponents. Taken together, these works exposed both the need for adversarial robustness and the optimization challenges of aiming directly for Nash. The natural synthesis is to entropy-regularize the two-player Markov game so that the learning dynamics target QRE, not Nash, and to exploit the rationality parameter as a controllable knob. By scheduling (curricularizing) agents’ bounded rationality—enabled by maximum-entropy control—the method smooths training early and progressively sharpens toward harder opponents, yielding a tractable path to robust policies.

---

*Analysis generated on: 2026-01-07T00:19:05.222946*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
