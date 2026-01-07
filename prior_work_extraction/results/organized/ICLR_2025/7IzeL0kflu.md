# Prior Work Analysis Report

## Target Paper

**Title:** Simplifying Deep Temporal Difference Learning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Matteo Gallici, Mattie Fellows, Benjamin Ellis, Bartomeu Pou, Ivan Masmitja, Jakob Nicolaus Foerster, Mario Martin

**Keywords:** Reinforcement Learning, TD, Theory, Q-learning, Parallelisation, Network Normalisation

**Abstract:** 
> $Q$-learning played a foundational role in the field reinforcement learning (RL).
However, TD algorithms with off-policy data, such as $Q$-learning, or nonlinear function approximation like deep neural networks require several additional tricks to stabilise training, primarily a large replay buffer and target networks. Unfortunately, the delayed updating of frozen network parameters in the target network harms the sample efficiency and, similarly, the large replay buffer introduces memory and im...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**An analysis of temporal-difference learning with function approximation** (1997)
- *Authors:* John N. Tsitsiklis and Benjamin Van Roy
- *Direct Connection:* It formalized TD learning as a projected fixed-point problem and characterized when contraction and convergence hold, providing the theoretical framework that this paper leverages to show normalization can restore convergence off-policy.

### 💡 Inspiration

**Learning values across many orders of magnitude (PopArt)** (2016)
- *Authors:* Hado van Hasselt et al.
- *Direct Connection:* PopArt showed that adaptive normalization of value targets stabilizes value learning, inspiring the present work’s use of normalization—shifted from targets to features—to achieve provable TD stability.

### 🔍 Gap Identification

**Residual algorithms: Reinforcement learning with function approximation** (1995)
- *Authors:* Leemon C. Baird
- *Direct Connection:* Baird’s counterexample demonstrated divergence of off-policy TD with function approximation, the precise instability this paper addresses via network normalization in place of target networks or replay.

**Fast Gradient-Descent Methods for Temporal-Difference Learning with Linear Function Approximation** (2009)
- *Authors:* Richard S. Sutton et al.
- *Direct Connection:* GTD/TDC provided provably convergent off-policy TD for linear function approximation using two-timescale updates, whose complexity and restriction this paper overcomes by achieving convergence in deep networks through simple normalization.

**An emphatic approach to off-policy temporal-difference learning** (2016)
- *Authors:* Richard S. Sutton et al.
- *Direct Connection:* Emphatic TD restored stability off-policy via importance-weighted state emphases, motivating this paper’s alternative route that attains stability by architectural normalization rather than specialized weighting.

### 📊 Baseline

**Human-level control through deep reinforcement learning** (2015)
- *Authors:* Volodymyr Mnih et al.
- *Direct Connection:* This work established target networks and experience replay as the default stabilizers for off-policy deep Q-learning, which the current paper explicitly removes by proving that normalization alone can ensure stable TD updates.

### 🔧 Extension

**Layer Normalization** (2016)
- *Authors:* Jimmy Lei Ba et al.
- *Direct Connection:* This paper introduces layer-wise feature normalization, which the current work embeds in Q-networks and theoretically analyzes to prove TD convergence without target networks or replay.

---

## Synthesis: How Prior Work Led to This Paper

Deep Q-learning demonstrated that large replay buffers and slowly updated target networks can stabilize off-policy bootstrapping with nonlinear function approximators, establishing these mechanisms as de facto requirements for practical TD learning. Earlier theoretical work had already cast TD as a projected fixed-point iteration and characterized when contraction holds, laying the groundwork to reason about stability with function approximation. Baird’s counterexample pinpointed the core pathology—off-policy bootstrapping with function approximation can diverge—thereby crystallizing the deadly triad as a central obstacle. In response, gradient TD methods achieved provable off-policy convergence in the linear setting via two-timescale stochastic approximation, while emphatic TD restored stability through emphasis weighting; both validated that modifying the update dynamics can fix divergence but at the cost of algorithmic complexity or strong assumptions. In parallel, normalization emerged as a stabilizing ingredient in deep learning: layer normalization provided feature-wise, input-independent normalization within networks, and PopArt showed that adaptive normalization of value targets can regularize learning across scales in RL.
Together these works suggested an opening: if normalization can regularize representations or targets and fixed-point theory prescribes contraction for stability, then the right normalization might restore contraction for off-policy TD with deep networks. The present paper synthesizes these insights by placing normalization inside the Q-network and proving that such regularization alone can ensure convergent off-policy TD updates, removing the need for target networks and replay, while retaining the empirical robustness previously attributed to those mechanisms.

---

*Analysis generated on: 2026-01-06T14:36:32.205798*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
