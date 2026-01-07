# Prior Work Analysis Report

## Target Paper
**Title:** zWIS8I9G9B
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Online Control with Adversarial Disturbances** (2018)
- *Authors:* Y. Cohen et al.
- *Connection:* This paper established the now-standard reduction from online LQR with adversarial disturbances to online convex optimization with memory and introduced the stability term our work reanalyzes and controls via a with-history reduction.

**Online Learning with Composite Loss Functions** (2015)
- *Authors:* O. Anava et al.
- *Connection:* This work formalized online convex optimization with memory (composite losses depending on recent actions), the precise framework our LQR-to-BCO reduction targets and builds upon with a with-history construction.

**Online Convex Optimization in the Bandit Setting** (2005)
- *Authors:* A. Flaxman et al.
- *Connection:* It introduced the core bandit gradient-estimation machinery that our reduction to bandit convex optimization with memory leverages to obtain regret bounds under bandit feedback.

### 💡 Inspiration

**Interior-Point Polynomial Methods in Convex Programming** (1994)
- *Authors:* Y. Nesterov et al.
- *Connection:* We adopt the Newton decrement from interior-point methods developed in this monograph to analyze and control the LQR stability term under heterogeneous curvatures.

### 🔍 Gap Identification

**Efficient Regret Minimization in Nonstochastic Control Using Improper Learning** (2020)
- *Authors:* E. Hazan et al.
- *Connection:* This line introduced disturbance-action (improper) policies for nonstochastic control but relied on impulse-response truncation that creates hard-to-control errors, a limitation our with-history reduction is designed to avoid.

### 📊 Baseline

**Nonstochastic Control with Bandit Feedback** (2020)
- *Authors:* E. Hazan et al.
- *Connection:* It set up the bandit-feedback formulation for nonstochastic control (including LQR) and obtained regret via bandit gradient estimators under uniform strong convexity, a homogeneous-curvature assumption our paper explicitly relaxes.

---

## Synthesis

The core of this paper is a principled path from online LQR with bandit feedback and semi-adversarial disturbances to bandit convex optimization with memory, and a new curvature-adaptive stability analysis. The lineage begins with Online Control with Adversarial Disturbances, which crystallized the reduction of LQR to online convex optimization with memory and identified the central stability term that governs regret. Nonstochastic Control with Bandit Feedback then placed this reduction in the bandit setting, obtaining regret bounds via gradient-free estimators but under a uniform strong-convexity (homogeneous curvature) assumption. On the optimization side, Online Learning with Composite Loss Functions provided the formal OCO-with-memory framework our reduction targets, while Online Convex Optimization in the Bandit Setting supplied the foundational one-point smoothing/gradient-estimation techniques that enable bandit feedback learning after the reduction. A key technical limitation in the nonstochastic control literature is reliance on truncating infinite impulse responses in disturbance-action (improper) policies, creating hard-to-quantify truncation errors; this gap, highlighted in work on efficient regret minimization via improper learning, motivates our with-history reduction that preserves the full memory and sidesteps truncation. Finally, to handle heterogeneous curvatures and control the shared stability term in both regret and memory, we import the Newton decrement from interior-point methods (Nesterov–Nemirovski), enabling curvature-adaptive bounds and a simplified analysis that extends beyond the homogeneous strong-convexity regime.

---
*Generated: 2026-01-06T23:09:26.439202*
