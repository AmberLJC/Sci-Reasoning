# Prior Work Analysis Report

## Target Paper

**Title:** DrM: Mastering Visual Reinforcement Learning through Dormant Ratio Minimization

**Conference:** ICLR 2024 (spotlight)

**Authors:** Guowei Xu, Ruijie Zheng, Yongyuan Liang, Xiyao Wang, Zhecheng Yuan, Tianying Ji, Yu Luo, Xiaoyu Liu, Jiaxin Yuan, Pu Hua, Shuzhen Li, Yanjie Ze, Hal Daumé III, Furong Huang, Huazhe Xu

**Keywords:** Visual RL; Dormant Ratio

**Abstract:** 
> Visual reinforcement learning (RL) has shown promise in continuous control tasks.
Despite its progress, current algorithms are still unsatisfactory in virtually every aspect of the performance such as sample efficiency, asymptotic performance, and their robustness to the choice of random seeds.
In this paper, we identify a major shortcoming in existing visual RL methods that is the agents often exhibit sustained inactivity during early training, thereby limiting their ability to explore effectiv...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Network Trimming: A Data-Driven Neuron Pruning Approach towards Efficient Deep Architectures** (2016)
- *Authors:* Shao-Hua Hu et al.
- *Direct Connection:* DrM adopts and repurposes the APoZ-style idea—measuring the fraction of zero activations—as the dormant ratio to quantify and then minimize neuron inactivity in policy/value networks.

### 💡 Inspiration

**VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning** (2021)
- *Authors:* Adrien Bardes et al.
- *Direct Connection:* DrM is inspired by VICReg’s use of per-dimension batch statistics to prevent collapse, translating the variance-preserving principle into a neuron-activation regularizer that keeps policy-network units alive.

### 🔍 Gap Identification

**Reinforcement Learning with Augmented Data** (2020)
- *Authors:* Michael Laskin et al.
- *Direct Connection:* RAD’s reliance on image augmentations improves pixel-based control but still exhibits prolonged early inactivity and seed brittleness, a limitation DrM addresses by directly minimizing neuron dormancy.

**CURL: Contrastive Unsupervised Representations for Reinforcement Learning** (2020)
- *Authors:* Aravind Srinivas et al.
- *Direct Connection:* CURL shows representation learning boosts sample efficiency yet does not prevent inactive early exploration; DrM explicitly targets this failure mode via a neuron-activation regularizer.

**Improving Sample Efficiency in Model-Free Reinforcement Learning from Images** (2019)
- *Authors:* Denis Yarats et al.
- *Direct Connection:* SAC+AE demonstrates auxiliary reconstruction helps visual RL but still suffers from seed sensitivity and inactivity, motivating DrM’s shift to regulating internal neuron activity rather than only representations.

### 📊 Baseline

**Mastering Visual Continuous Control: Improved Data-Augmented Reinforcement Learning** (2021)
- *Authors:* Denis Yarats et al.
- *Direct Connection:* DrM is built on the standard DrQ-v2 visual RL training stack and targets its observed early-stage motor inactivity by adding a dormant-ratio regularizer to the actor/critic networks.

---

## Synthesis: How Prior Work Led to This Paper

Data-augmented visual RL methods like DrQ-v2 and RAD established that simple pixel-space augmentations can markedly improve sample efficiency in continuous control, yet they also revealed a persistent failure mode during early training: agents often remain motorically idle and are sensitive to random seeds. Contrastive representation learning in CURL and auxiliary reconstruction in SAC+AE further advanced the representation side of pixel-based RL, but neither prevented the recurrent phenomenon of inactive early exploration, suggesting that representation quality alone does not guarantee actionful behavior. Separately, pruning research introduced APoZ, a concrete, per-neuron measure of inactivity defined as the fraction of zero activations; this showed that neurons with consistently zero outputs are effectively dormant and can be systematically identified. In self-supervised learning, VICReg demonstrated that regulating per-dimension batch statistics—specifically ensuring sufficient variance—prevents feature collapse, highlighting the power of activation-level regularization as a stabilizer.

Together these works expose a gap: leading visual RL pipelines optimize data and representations but do not control the internal activation state of policy and value networks, allowing prolonged dormancy that manifests as motor inactivity. The natural next step is to instrument networks with an APoZ-like dormant ratio and actively regulate it, importing the anti-collapse intuition from VICReg into the RL setting. DrM synthesizes these insights by measuring neuron dormancy in standard DrQ-v2–style agents and minimizing it during training, thereby converting internal activation health into a practical driver of robust, active exploration and improved sample efficiency.

---

*Analysis generated on: 2026-01-06T16:07:15.553996*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
