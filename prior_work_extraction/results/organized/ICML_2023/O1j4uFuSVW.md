# Prior Work Analysis Report

## Target Paper
**Title:** O1j4uFuSVW
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Efficient computation of equilibria for extensive two-person games** (1996)
- *Authors:* D. Koller et al.
- *Connection:* The paper’s representation and complexity in terms of total actions across information sets (A_X + B_Y) is inherited from the sequence-form/realization-plan framework introduced here, which underlies both the lower bound and the FTRL updates on the game tree.

**Regret Minimization in Games with Incomplete Information** (2008)
- *Authors:* M. Zinkevich et al.
- *Connection:* This work introduced counterfactual regret decomposition and self-play learning in imperfect-information extensive-form games, the fundamental framework that the new Balanced/Adaptive FTRL algorithms build upon and adapt to trajectory feedback.

**Smoothing techniques for computing Nash equilibria of sequential games** (2010)
- *Authors:* S. Hoda et al.
- *Connection:* This work introduced the treeplex geometry and dilated-entropy style regularizers that enable per-information-set regularization; the paper’s Balanced FTRL explicitly leverages this geometry via carefully chosen (and in Adaptive FTRL, learned) weights across the game tree.

### 📊 Baseline

**Monte Carlo Sampling for Regret Minimization in Extensive Games** (2009)
- *Authors:* M. Lanctot
- *Connection:* Outcome-sampling CFR established learning from single trajectories in IIGs; the present paper directly targets this trajectory-feedback regime and improves its sample complexity guarantees by replacing regret matching with carefully regularized FTRL.

### 🔧 Extension

**Optimistic Regret Minimization for Extensive-Form Games** (2019)
- *Authors:* G. Farina et al.
- *Connection:* Building on first-order (FTRL/OMD) methods tailored to the tree structure, the paper extends these ideas to bandit (trajectory) feedback and introduces balanced/adaptive regularization to match problem-dependent optimal rates.

### 🔗 Related Problem

**Solving Large Imperfect-Information Games Efficiently with CFR+** (2015)
- *Authors:* O. Tammelin
- *Connection:* CFR+ is the dominant practical baseline for self-play in IIGs; its reliance on regret matching and sampling highlights the performance/variance limitations that the proposed FTRL-based, structure-adaptive approach addresses theoretically in the trajectory-feedback setting.

---

## Synthesis

The core innovation of Adapting to game trees in zero-sum imperfect information games is to obtain near-optimal sample complexity for self-play under trajectory feedback by tailoring FTRL to the tree structure and by learning (or pre-setting) per-information-set regularization. The intellectual lineage begins with Koller, Megiddo, and von Stengel’s sequence-form representation, which defines realization plans and makes the dependence on the total number of actions across information sets explicit—precisely the dimension appearing in the new lower and upper bounds. Zinkevich et al. then introduced counterfactual regret minimization (CFR), providing the decomposition over information sets and the self-play paradigm in imperfect-information extensive-form games that this work operates within. Lanctot’s Monte Carlo CFR established trajectory (outcome) sampling as a way to learn with bandit-like feedback, forming the direct baseline whose sample complexity and variance properties motivate the shift to FTRL. On the optimization side, Hoda et al. developed the treeplex geometry and dilated-entropy regularizers that make first-order methods decompose along the game tree; this structure is pivotal for the paper’s Balanced FTRL design and for the adaptive weighting strategy. Farina, Kroer, and Sandholm subsequently brought optimistic/FTRL-style methods to extensive-form games under full-information feedback; the present work extends these techniques to trajectory feedback and closes the gap to problem-independent lower bounds. Finally, CFR+ exemplifies the prevailing regret-matching-based practice, whose limitations under trajectory sampling are precisely what the proposed balanced/adaptive FTRL approach overcomes.

---
*Generated: 2026-01-06T23:09:26.548487*
