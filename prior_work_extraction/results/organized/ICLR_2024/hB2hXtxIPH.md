# Prior Work Analysis Report

## Target Paper

**Title:** Solving Homogeneous and Heterogeneous Cooperative Tasks with Greedy Sequential Execution

**Conference:** ICLR 2024 (spotlight)

**Authors:** Shanqi Liu, Dong Xing, Pengjie Gu, Xinrun Wang, Bo An, Yong Liu

**Keywords:** Multi-Agent Cooperation, Credit Assignment, Homogeneous and Heterogeneous Cooperative Tasks

**Abstract:** 
> Cooperative multi-agent reinforcement learning (MARL) is extensively used for solving complex cooperative tasks, and value decomposition methods are a prevalent approach for this domain. However, these methods have not been successful in addressing both homogeneous and heterogeneous tasks simultaneously which is a crucial aspect for the practical application of cooperative agents. 
On one hand, value decomposition methods demonstrate superior performance in homogeneous tasks. Nevertheless, they ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Value-Decomposition Networks For Cooperative Multi-Agent Learning** (2018)
- *Authors:* Sunehag et al.
- *Direct Connection:* Introduced the value-decomposition/IGM framework for centralized training with decentralized execution that this paper retains while rethinking the joint action selection mechanism via greedy sequential execution.

**The StarCraft Multi-Agent Challenge** (2019)
- *Authors:* Samvelyan et al.
- *Direct Connection:* Defines the heterogeneous cooperative benchmark and problem protocol that the paper explicitly targets to demonstrate unified performance across homogeneous and heterogeneous tasks.

### 💡 Inspiration

**Action Branching Architectures for Deep Reinforcement Learning** (2018)
- *Authors:* Tavakoli et al.
- *Direct Connection:* Provides the key insight that greedy per-dimension selection over a factored Q can make large discrete decisions tractable, which this paper adapts to multi-agent settings by selecting agents’ actions sequentially and greedily.

### 🔍 Gap Identification

**ROMA: Multi-Agent Reinforcement Learning with Emergent Roles** (2020)
- *Authors:* Wang et al.
- *Direct Connection:* Shows that role/personalization mechanisms suit heterogeneous cooperation but degrade performance in homogeneous settings, directly motivating the search for a unified approach that avoids this trade-off.

**RODE: Learning Roles to Decompose Multi-Agent Tasks** (2021)
- *Authors:* Wang et al.
- *Direct Connection:* Reinforces that role-based policy aggregation aids heterogeneous tasks yet compromises homogeneous performance, a limitation the proposed greedy sequential execution is designed to address.

### 📊 Baseline

**QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning** (2018)
- *Authors:* Rashid et al.
- *Direct Connection:* Serves as the principal value-decomposition baseline whose monotonic mixing and simultaneous greedy execution work well on homogeneous tasks but encourage near-identical agent policies that this paper explicitly aims to overcome.

### 🔧 Extension

**QPLEX: Duplex Dueling Multi-Agent Q-Learning** (2021)
- *Authors:* Wang et al.
- *Direct Connection:* Demonstrates that more expressive value factorisation (duplex dueling) can improve credit assignment, which this paper preserves while changing the decision process to agent-wise greedy sequential execution to better handle heterogeneity.

---

## Synthesis: How Prior Work Led to This Paper

Value-Decomposition Networks (VDN) established the core centralized-training/decentralized-execution paradigm by factorizing a joint action-value into agent-wise utilities under the IGM principle, enabling scalable cooperative learning. QMIX advanced this with a monotonic mixing network so that the joint argmax aligned with individual argmaxes, a design that excelled on homogeneous coordination but tended to homogenize agent policies. QPLEX increased factorisation expressiveness via duplex dueling advantage decomposition, improving credit assignment while still relying on simultaneous action selection. In parallel, ROMA showed that emergent roles and personalized observations can induce specialization suited for heterogeneous teams, and RODE further decomposed tasks through learned roles, but both lines revealed a consistent trade-off: role-induced diversity often undermined performance on homogeneous tasks. Outside MARL, the Branching Dueling Q-network demonstrated that greedy, per-dimension action selection over a factored Q can scale to high-dimensional discrete action spaces, highlighting the power of sequential greedy choice in structured decisions. The StarCraft Multi-Agent Challenge provided the canonical heterogeneous cooperative testbed shaping evaluation protocols.
Taken together, these works left a clear opportunity: maintain the strengths of value factorisation and credit assignment while avoiding the homogeneity bias of simultaneous argmax and the homogeneity–heterogeneity trade-off of role aggregation. The paper synthesizes these insights by preserving factorised value learning yet replacing simultaneous selection with agent-wise greedy sequential execution, leveraging the branching-style greedy principle to induce flexible, specialized behaviors without sacrificing coordinated performance on homogeneous tasks, and validating the unified capability on SMAC and other cooperative settings.

---

*Analysis generated on: 2026-01-06T08:27:12.250796*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
