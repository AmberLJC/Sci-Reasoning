# Prior Work Analysis Report

## Target Paper
**Title:** WvIHbQhrTq
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Asymptotically efficient adaptive allocation rules** (1985)
- *Authors:* Tze Leung Lai et al.
- *Connection:* Lai–Robbins introduced the stochastic MAB formulation and instance-dependent lower bounds that MIN-UCB is proven to match, grounding the paper’s claims of tight instance-dependent regret.

### 🔍 Gap Identification

**Stochastic Multi-Armed Bandits in the Presence of Adversarial Corruptions** (2018)
- *Authors:* Thodoris Lykouris et al.
- *Connection:* They showed that without a bound on corruption one cannot improve over standard stochastic-bandit guarantees, motivating this paper’s core insight that a non-trivial upper bound on offline–online discrepancy is necessary to beat UCB.

### 📊 Baseline

**Finite-Time Analysis of the Multiarmed Bandit Problem** (2002)
- *Authors:* Peter Auer et al.
- *Connection:* UCB is the canonical baseline whose regret is the benchmark in this paper’s impossibility result and the starting point from which MIN-UCB is constructed and to which it reduces when offline data are uninformative.

### 🔧 Extension

**The KL-UCB Algorithm for Bounded Stochastic Bandits** (2011)
- *Authors:* Aurélien Garivier et al.
- *Connection:* This work established the modern UCB-index framework for instance-dependent optimality via confidence bounds; MIN-UCB directly extends the UCB-index paradigm by incorporating a bounded bias term to safely exploit offline samples.

**Better Algorithms for Stochastic Bandits with Adversarial Corruptions** (2019)
- *Authors:* Anupam Gupta et al.
- *Connection:* Their corruption-robust UCB variants formalized how to adjust confidence indices using a known/controlled corruption budget; MIN-UCB adapts this bias-aware indexing idea to the offline–online mismatch setting with provably tight regret.

### 🔗 Related Problem

**Conservative Q-Learning for Offline Reinforcement Learning** (2020)
- *Authors:* Aviral Kumar et al.
- *Connection:* CQL’s pessimism principle—use offline data only when it can be trusted under distribution shift—directly informs MIN-UCB’s design that adaptively leverages offline samples only when a known discrepancy bound certifies informativeness.

---

## Synthesis

The paper builds squarely on the stochastic bandit canon and the robustness insights from corruption-robust and offline-learning lines of work. Lai and Robbins (1985) provide the foundational problem formulation and instance-dependent lower bounds that underpin the paper’s tight-regret claims. Auer et al. (2002) introduced UCB, the baseline both theoretically and algorithmically: the paper’s impossibility theorem explicitly states that, without a non-trivial bound on distribution shift between offline and online data, no non-anticipatory policy can outperform UCB’s guarantees. Garivier and Cappé (2011) further established the UCB-index methodology for attaining instance-dependent optimality via concentration inequalities; MIN-UCB is a direct extension of this index-based approach, augmenting the confidence bounds with a bounded-bias term derived from the offline–online discrepancy. The necessity of a discrepancy bound is foreshadowed by Lykouris and Sridharan (2018), who showed in corrupted-feedback bandits that improvement over clean-bandit rates is impossible without bounding corruption—precisely the gap this paper formalizes for offline data. Gupta, Koren, and Talwar (2019) refined how to incorporate a corruption budget into UCB-style indices, a technique MIN-UCB adapts to the bias between offline and online reward distributions. Finally, the conservative/pessimistic principle from offline RL (Kumar et al., 2020) directly inspires MIN-UCB’s adaptive behavior: exploit offline data when certified informative by the bound, otherwise ignore it—yielding provably tight instance-independent and dependent regret.

---
*Generated: 2026-01-06T23:09:26.430893*
