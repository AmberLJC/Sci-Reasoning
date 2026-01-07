# Prior Work Analysis Report

## Target Paper

**Title:** Beyond Worst-case Attacks: Robust RL with Adaptive Defense via Non-dominated Policies

**Conference:** ICLR 2024 (spotlight)

**Authors:** Xiangyu Liu, Chenghao Deng, Yanchao Sun, Yongyuan Liang, Furong Huang

**Keywords:** robust reinforcement learning; beyond worse-case

**Abstract:** 
> In light of the burgeoning success of reinforcement learning (RL) in diverse real-world applications, considerable focus has been directed towards ensuring RL policies are robust to adversarial attacks during test time. Current approaches largely revolve around solving a minimax problem to prepare for potential worst-case scenarios. While effective against strong attacks, these methods often compromise performance in the absence of attacks or the presence of only weak attacks. To address this, w...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Adversarial Attacks on Neural Network Policies** (2017)
- *Authors:* Sandy Huang et al.
- *Direct Connection:* This paper introduced the now-standard state-adversarial, Lp-bounded test-time perturbation model that the paper adopts to define performance across varying attack strengths.

**The Nonstochastic Multiarmed Bandit Problem** (2002)
- *Authors:* Peter Auer et al.
- *Direct Connection:* The adversarial bandit regret framework (e.g., EXP3) underpins the paper’s test-time regret minimization and its guarantee of sublinear regret when selecting among a finite compact set of baseline policies.

### 💡 Inspiration

**A Survey of Multi-Objective Sequential Decision-Making** (2013)
- *Authors:* Diederik M. Roijers et al.
- *Direct Connection:* This survey formalizes non-dominated (Pareto) policy sets and coverage concepts, which the paper repurposes to construct a compact set of non-dominated policies spanning attack strengths for adaptive defense.

### 🔍 Gap Identification

**Action Robust Reinforcement Learning** (2019)
- *Authors:* Chen Tessler et al.
- *Direct Connection:* By showing that PR-MDP/NR-MDP minimax formulations against action disturbances yield conservative policies, this work crystallizes the key limitation of worst-case robustification that the paper tackles under state-adversarial attacks via a set of non-dominated policies.

**Theoretically Principled Trade-off Between Robustness and Accuracy** (2019)
- *Authors:* Hongyang Zhang et al.
- *Direct Connection:* By formalizing the inherent robustness–accuracy trade-off in adversarial training, this work motivates the paper’s beyond-worst-case stance to cover multiple robustness levels and preserve clean performance via adaptive selection.

### 📊 Baseline

**Robust Adversarial Reinforcement Learning** (2017)
- *Authors:* Lerrel Pinto et al.
- *Direct Connection:* This minimax adversarial-training approach is the primary worst-case robust RL baseline whose over-conservatism the paper addresses by adaptively selecting among a non-dominated set instead of committing to a single worst-case policy.

---

## Synthesis: How Prior Work Led to This Paper

Minimax robust RL methods such as Robust Adversarial Reinforcement Learning train policies against a worst-case adversary, yielding robustness but often at the cost of overly conservative behavior. Action Robust Reinforcement Learning sharpened this point in the PR-MDP/NR-MDP setting, showing that worst-case formulations aimed at action disturbances can significantly degrade nominal performance. Concurrently, the adversarial test-time threat model for reinforcement learning was crystallized by Adversarial Attacks on Neural Network Policies, which established the now-standard Lp-bounded state-perturbation framework used to evaluate and design defenses. Beyond the RL domain, Theoretically Principled Trade-off Between Robustness and Accuracy formalized the inherent trade-off between clean and robust performance, introducing the idea of tuning across robustness levels rather than optimizing only for the worst case. For online decision-making under adversarial feedback, The Nonstochastic Multiarmed Bandit Problem provided the core regret-minimization machinery (e.g., EXP3) to adaptively choose among a finite set of experts with sublinear regret. Finally, the multi-objective decision-making literature, summarized in A Survey of Multi-Objective Sequential Decision-Making, introduced non-dominated (Pareto) policy sets to cover trade-offs across competing objectives. Taken together, these works reveal a gap: worst-case robust RL secures robustness but sacrifices clean performance, even though the attack strength at test time can vary. The natural next step is to precompute policies spanning the robustness–performance trade-off (leveraging Pareto/non-dominated ideas) and then use adversarial bandit-style selection to adapt online to the realized attack strength under the standard state-attack model, thereby going beyond worst-case defenses with principled regret guarantees.

---

*Analysis generated on: 2026-01-06T09:19:08.926499*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
