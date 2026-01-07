# Prior Work Analysis Report

## Target Paper

**Title:** Towards Optimal Regret in Adversarial Linear MDPs with Bandit Feedback

**Conference:** ICLR 2024 (spotlight)

**Authors:** Haolin Liu, Chen-Yu Wei, Julian Zimmert

**Keywords:** adversarial MDPs, policy optimization, bandit feedback

**Abstract:** 
> We study online reinforcement learning in linear Markov decision processes with adversarial losses and bandit feedback. We introduce two algorithms that achieve improved regret performance compared to existing approaches. The first algorithm, although computationally inefficient, achieves a regret of $\widetilde{O}(\sqrt{K})$ without relying on simulators, where $K$ is the number of episodes. This is the first rate-optimal result in the considered setting. The second algorithm is computationally...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Provably Efficient Reinforcement Learning with Linear Function Approximation** (2020)
- *Authors:* Jin et al.
- *Direct Connection:* The linear MDP factorization and occupancy-measure viewpoint introduced here provide the structural model and analytical tools that this paper assumes and operates within when deriving adversarial bandit-regret guarantees.

**Online Markov Decision Processes** (2009)
- *Authors:* Even-Dar et al.
- *Direct Connection:* This work formalized the online/adversarial MDP setting and regret against the best policy, establishing the problem template that the current paper tackles under linear function approximation and bandit feedback.

### 🔍 Gap Identification

**Adversarial Linear MDPs with Bandit Feedback: Improved Regret via Variance-Aware Analysis** (2023)
- *Authors:* Kong et al.
- *Direct Connection:* Their simulator-free but computationally inefficient algorithm achieved ~O(K^{4/5} + 1/λ_min) regret in adversarial linear MDPs with bandit feedback, and this paper directly addresses both the suboptimal K-exponent and the undesired dependence on λ_min by attaining the first ~O(√K) rate without a simulator.

### 📊 Baseline

**Efficient Adversarial Reinforcement Learning in Linear MDPs with Bandit Feedback** (2023)
- *Authors:* Sherman et al.
- *Direct Connection:* Their computationally efficient policy-optimization framework achieved ~O(K^{6/7}) regret, and this paper builds on and tightens that approach with a refined loss estimator and exploration schedule to obtain ~O(K^{3/4}) while preserving efficiency.

### 🔧 Extension

**Online Learning in Markov Decision Processes with Bandit Feedback** (2010)
- *Authors:* Neu et al.
- *Direct Connection:* The paper’s bandit occupancy-measure loss estimator and OMD-style policy updates are adapted and refined here to the linear-MDP setting, with variance control that is crucial for the improved K-dependence achieved by this work.

### 🔗 Related Problem

**Online Learning in Episodic Markov Decision Processes by Mixing Past Policies** (2013)
- *Authors:* Zimin et al.
- *Direct Connection:* Their policy-mixing strategy for adversarial episodic MDPs informs the stability and bias-variance tradeoffs of the policy optimization schemes that the present paper tailors to the linear-function-approximation and bandit-feedback regime.

---

## Synthesis: How Prior Work Led to This Paper

Online Markov Decision Processes established the adversarial RL template, defining regret against the best policy and clarifying the episodic structure of nonstochastic losses. Online Learning in Markov Decision Processes with Bandit Feedback extended this to bandit feedback, introducing importance-weighted occupancy-measure estimators and mirror-descent style updates that balance exploration with adversarial loss estimation under high variance. Online Learning in Episodic Markov Decision Processes by Mixing Past Policies further developed policy-mixing techniques that stabilize updates in adversarial episodic control, highlighting how to temper estimator bias and variance over trajectories. Provably Efficient Reinforcement Learning with Linear Function Approximation introduced the linear MDP model, factorizing transition dynamics and enabling low-dimensional occupancy representations and analyses that became the standard structural assumption for function approximation in RL.
Building on these foundations, Efficient Adversarial Reinforcement Learning in Linear MDPs with Bandit Feedback provided the first computationally efficient framework for adversarial linear MDPs with bandit feedback but achieved only ~O(K^{6/7}) regret, revealing remaining variance and exploration inefficiencies. Adversarial Linear MDPs with Bandit Feedback: Improved Regret via Variance-Aware Analysis obtained ~O(K^{4/5}) with an inefficient procedure and incurred an undesirable 1/λ_min dependence, underscoring both statistical and structural bottlenecks. The current paper synthesizes these insights: it adapts bandit occupancy-measure estimation to the linear MDP structure with sharper variance control, yielding a simulator-free, rate-optimal ~O(√K) (albeit inefficient) algorithm, and, by tightening the efficient policy-optimization pipeline of Sherman et al., achieves a computationally efficient ~O(K^{3/4}) regret bound—closing key gaps highlighted by prior work.

---

*Analysis generated on: 2026-01-06T08:09:17.614147*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
