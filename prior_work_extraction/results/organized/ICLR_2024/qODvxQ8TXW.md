# Prior Work Analysis Report

## Target Paper

**Title:** Masks, Signs, And Learning Rate Rewinding

**Conference:** ICLR 2024 (spotlight)

**Authors:** Advait Harshal Gadhikar, Rebekka Burkholz

**Keywords:** sparsity, pruning, lottery tickets, learning rate rewinding, iterative magnitude pruning

**Abstract:** 
> Learning Rate Rewinding (LRR) has been established as a strong variant of Iterative Magnitude Pruning (IMP) to find lottery tickets in deep overparameterized neural networks. While both iterative pruning schemes couple structure and parameter learning, understanding how LRR excels in both aspects can bring us closer to the design of more flexible deep learning algorithms that can optimize diverse sets of sparse architectures. To this end, we conduct experiments that disentangle the effect of mas...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Comparing Rewinding and Fine-Tuning in Neural Network Pruning** (2020)
- *Authors:* Alex Renda et al.
- *Direct Connection:* This work introduced Learning Rate Rewinding (resetting only the learning-rate schedule when retraining pruned networks) and showed it outperforms weight rewinding, providing the exact pruning variant whose superior behavior this paper explains via sign dynamics and mask/parameter disentanglement.

**The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks** (2019)
- *Authors:* Jonathan Frankle et al.
- *Direct Connection:* It established the IMP framework and the lottery ticket problem formulation—coupling mask discovery with parameter training—that this paper directly probes to separate mask learning from parameter optimization.

### 💡 Inspiration

**Deconstructing Lottery Tickets: Zeros, Signs, and the Supermask** (2019)
- *Authors:* Hattie Zhou et al.
- *Direct Connection:* It revealed the central role of weight signs and masks (supermasks), directly inspiring this paper’s focus on early sign flips and robustness to sign perturbations as the mechanism behind LRR’s advantage.

### 🔍 Gap Identification

**Rethinking the Value of Network Pruning** (2019)
- *Authors:* Zhuang Liu et al.
- *Direct Connection:* Its finding that training pruned architectures from scratch can match fine-tuning raised the open question of how much performance stems from the mask versus parameters—a gap this paper addresses by isolating and analyzing these two components under LRR.

### 📊 Baseline

**Stabilizing the Lottery Ticket Hypothesis** (2020)
- *Authors:* Jonathan Frankle et al.
- *Direct Connection:* By showing that weight rewinding to an early checkpoint strengthens IMP, it serves as the principal alternative baseline to LRR and motivates this paper’s analysis of why LRR outperforms weight rewinding in both mask identification and sparse optimization.

### 🔗 Related Problem

**What’s Hidden in a Randomly Weighted Neural Network?** (2020)
- *Authors:* Vijay Ramanujan et al.
- *Direct Connection:* By demonstrating that learning only a mask over fixed random weights can yield high accuracy, it motivates this paper’s experimental disentanglement of mask learning from parameter optimization and tests on optimizing diverse (including random) masks.

---

## Synthesis: How Prior Work Led to This Paper

Learning Rate Rewinding (LRR) was introduced as a retraining strategy that resets only the learning-rate schedule after pruning and was empirically shown to outperform weight rewinding, elevating it as a strong variant of iterative magnitude pruning. The Lottery Ticket Hypothesis defined the iterative magnitude pruning (IMP) setting by coupling mask discovery with parameter training, establishing the canonical procedure for uncovering sparse, trainable subnetworks. Stabilizing the Lottery Ticket Hypothesis further refined IMP by rewinding weights to an early checkpoint, creating the key alternative to LRR and framing the question of why different rewinding strategies succeed. Deconstructing Lottery Tickets highlighted that weight signs and binary masks can be sufficient to support learning, revealing that sign patterns are a critical representational degree of freedom. Complementarily, What’s Hidden in a Randomly Weighted Neural Network showed that masks alone can induce high accuracy over fixed random weights, underscoring that mask learning can be meaningfully separated from parameter optimization. Rethinking the Value of Network Pruning reported that training pruned architectures from scratch can match fine-tuning, sharpening the inquiry into the relative contributions of mask structure and parameter states.
Together, these works exposed a gap: why LRR so reliably excels at both identifying masks and optimizing sparse networks. Building on the sign-centric insights and mask-only results, it is natural to hypothesize that LRR’s advantage stems from enabling early sign flips and robustness to sign perturbations. This synthesis motivated disentangling mask learning from parameter optimization empirically and proving, in simplified settings, that LRR escapes problematic initial sign configurations more often than IMP.

---

*Analysis generated on: 2026-01-06T11:36:30.151343*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
