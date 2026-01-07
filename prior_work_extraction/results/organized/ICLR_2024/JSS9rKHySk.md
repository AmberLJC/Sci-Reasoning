# Prior Work Analysis Report

## Target Paper

**Title:** On the Role of General Function Approximation in Offline Reinforcement Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Chenjie Mao, Qiaosheng Zhang, Zhen Wang, Xuelong Li

**Keywords:** reinforcement learning theory, offline reinforcement learning, general function approximation, learnability, minimax lower bounds

**Abstract:** 
> We study offline reinforcement learning (RL) with general function approximation. General function approximation is a powerful tool for algorithm design and analysis, but its adaptation to offline RL encounters several challenges due to varying approximation targets and assumptions that blur the real meanings of function assumptions. In this paper, we try to formulate and clarify the treatment of general function approximation in offline RL in two aspects: (1) analyzing different types of assump...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Contextual Decision Processes with Low Bellman Rank are PAC-Learnable** (2017)
- *Authors:* Nan Jiang et al.
- *Direct Connection:* By introducing Bellman rank and framing function approximation assumptions as structural restrictions on the admissible MDP class, this work provides the foundational lens that the paper formalizes and analyzes for offline RL.

### 💡 Inspiration

**Model-Based Reinforcement Learning in Contextual Decision Processes** (2019)
- *Authors:* Wen Sun et al.
- *Direct Connection:* This paper’s model-realizability framework and witness-based analysis directly motivate using model classes to characterize MDP restrictions, which the paper exploits to construct generic lower bounds transferable across function classes.

**Statistical Complexity of Interactive Decision Making** (2021)
- *Authors:* Dylan J. Foster et al.
- *Direct Connection:* Its decision-estimation coefficient and information-theoretic lower-bound techniques inform the paper’s perspective of treating function approximation assumptions as constraints on MDP families and deriving minimax lower bounds.

### 🔍 Gap Identification

**Is Pessimism Provably Efficient for Offline Reinforcement Learning?** (2021)
- *Authors:* Tengyang Xie et al.
- *Direct Connection:* By establishing guarantees under heterogeneous realizability and coverage assumptions, this work exposed ambiguity in approximation targets that the paper explicitly disentangles and systematizes for offline RL.

### 🔧 Extension

**A Minimax Theory for Offline Reinforcement Learning with Linear Function Approximation** (2022)
- *Authors:* Yin et al.
- *Direct Connection:* Their representation-specific lower-bound constructions for linear function classes are generalized by the paper via model-realizability to yield class-agnostic, reusable lower bounds.

### 🔗 Related Problem

**Statistically Efficient Off-Policy Policy Evaluation for Reinforcement Learning with Finite Horizons** (2020)
- *Authors:* Nathan Kallus et al.
- *Direct Connection:* Its minimax lower bounds for off-policy evaluation under model-based assumptions provide technical tools and a reduction viewpoint that underpin the paper’s model-realizability-driven lower-bound methodology for policy learning.

---

## Synthesis: How Prior Work Led to This Paper

Bellman-rank theory established that function approximation assumptions can be formalized as structural constraints on the environment by requiring low-complexity Bellman factorization, thereby tying statistical learnability to restrictions on the underlying MDPs. Model-based analysis in contextual decision processes further operationalized this idea through model-realizability and witness-based diagnostics, clarifying how specifying a model class both enables learning guarantees and implicitly narrows the admissible MDP family. Complementing these, information-theoretic work on the statistical complexity of interactive decision making introduced the decision-estimation coefficient and hypothesis-testing lower bounds, offering general tools to convert such structural constraints into minimax limits. In offline RL, pessimism-based theory delivered sharp guarantees but under a patchwork of realizability targets and coverage assumptions, revealing ambiguity about precisely what is being approximated. For linear representations, minimax upper and lower bounds were derived via class-specific hard instances, while off-policy evaluation attained tight minimax characterizations under model-based assumptions, illuminating how model realism can anchor lower-bound constructions.
Together these strands expose both an opportunity and a gap: powerful general frameworks existed to view function classes as MDP restrictions and to derive information-theoretic lower bounds, yet offline RL lacked a unified clarification of approximation targets and generic lower bounds beyond specific representations. By synthesizing the model-realizability lens with the DEC-style information-theoretic machinery, it is natural to formalize general function approximation as an MDP restriction in offline RL and to leverage model-realizability to craft generic, portable lower bounds—leading directly to the paper’s clarified assumption taxonomy and its two general-purpose minimax lower bounds.

---

*Analysis generated on: 2026-01-06T08:54:04.311748*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
