# Prior Work Analysis Report

## Target Paper
**Title:** mIomqOskaa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks** (2019)
- *Authors:* Frankle et al.
- *Connection:* Established that fixed sparse subnetworks can be trained to match dense performance, directly motivating this paper’s use of fixed sparsity as a principled alternative to scaling dense DRL networks.

**On Lazy Training in Differentiable Programming** (2019)
- *Authors:* Chizat et al.
- *Connection:* Characterized the lazy/NTK regime where very wide networks lose feature-learning plasticity; the present work builds on this lens to argue and empirically show that sparsity counteracts plasticity loss when scaling DRL.

### 💡 Inspiration

**What’s Hidden in a Randomly Weighted Neural Network?** (2020)
- *Authors:* Ramanujan et al.
- *Connection:* Showed that suitable subnetworks (supermasks) exist at random initialization, inspiring the hypothesis tested here that even random one-shot pruning can confer beneficial inductive bias for RL scaling.

### 🔍 Gap Identification

**Rigging the Lottery: Making All Tickets Winners** (2020)
- *Authors:* Evci et al.
- *Connection:* Demonstrated dynamic sparse training can match dense models but at added algorithmic complexity; this paper shows a simpler static alternative (one-shot random pruning) suffices to unlock DRL scaling.

### 📊 Baseline

**Phasic Policy Gradient** (2021)
- *Authors:* Cobbe et al.
- *Connection:* Proposed decoupling policy/value updates to mitigate representation interference in PPO; the current work targets the same interference but via architecture-level sparsity and reports improvements over dense baselines.

### 🔧 Extension

**SNIP: Single-shot Network Pruning based on Connection Sensitivity** (2019)
- *Authors:* Lee et al.
- *Connection:* Introduced pruning-once-before-training; the present work adopts this exact timing and simplifies the selection rule to random masking to isolate the effect of static sparsity in DRL.

### 🔗 Related Problem

**Gradient Surgery for Multi-Task Learning** (2020)
- *Authors:* Yu et al.
- *Connection:* Formalized gradient conflict/interference and proposed PCGrad; this paper addresses an analogous interference between RL losses by showing fixed sparsity inherently reduces gradient conflicts without gradient surgery.

---

## Synthesis

The paper’s core idea—that static network sparsity alone can unlock the scaling potential of deep reinforcement learning—stands on two converging intellectual threads: sparse subnetworks and RL-specific optimization pathologies. Foundational pruning work, especially the Lottery Ticket Hypothesis, established that fixed sparse subnetworks can train as well as dense models, legitimizing sparse connectivity as a first-class design choice rather than a post-hoc compression tool. One-shot pruning at initialization (SNIP) provided the exact operational timing adopted here; the authors deliberately simplify its sensitivity-based criterion to random masking to isolate sparsity’s intrinsic benefits. Complementary evidence from Ramanujan et al. suggested that performant subnetworks can be identified within randomly initialized weights, reinforcing the plausibility of random masks. While RigL showed dynamic sparse training can match dense networks, its complexity motivated the present work’s focus on static masks as a simpler path to scale.

On the RL side, Phasic Policy Gradient targeted gradient interference between policy and value updates through training-phase decoupling; this paper instead shows architecture-level sparsity naturally reduces such interference while improving scaling. The broader notion of gradient conflicts, crystallized by PCGrad, frames the optimization challenge that sparsity helps alleviate. Finally, the lazy-training perspective of Chizat et al. provides the theoretical backdrop for “plasticity loss” in wide networks; the authors leverage this lens to argue that sparsity preserves feature-learning dynamics as models scale. Together, these works directly shaped the paper’s thesis: fixed, one-shot sparsity is a simple, principled lever for overcoming plasticity loss and gradient interference in large DRL models.

---
*Generated: 2026-01-06T23:07:19.612977*
