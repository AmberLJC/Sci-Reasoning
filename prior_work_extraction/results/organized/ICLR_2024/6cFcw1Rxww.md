# Prior Work Analysis Report

## Target Paper

**Title:** Local Search GFlowNets

**Conference:** ICLR 2024 (spotlight)

**Authors:** Minsu Kim, Taeyoung Yun, Emmanuel Bengio, Dinghuai Zhang, Yoshua Bengio, Sungsoo Ahn, Jinkyoo Park

**Keywords:** GFlowNet, molecule optimization, biological sequence design, local search, reinforcement learning

**Abstract:** 
> Generative Flow Networks (GFlowNets) are amortized sampling methods that learn a distribution over discrete objects proportional to their rewards. GFlowNets exhibit a remarkable ability to generate diverse samples, yet occasionally struggle to consistently produce samples with high rewards due to over-exploration on wide sample space. 
This paper proposes to train GFlowNets with local search, which focuses on exploiting high-rewarded sample space to resolve this issue. Our main idea is to explor...

---

## Key Prior Works (5 papers with direct influence)

### 🏗️ Foundation

**Generative Flow Networks** (2021)
- *Authors:* Yoshua Bengio et al.
- *Direct Connection:* This work introduced the core GFlowNet framework of coupled forward and backward policies that sample objects proportional to reward, which LS-GFN directly repurposes to backtrack (via the backward policy) and reconstruct (via the forward policy) during local search.

### 💡 Inspiration

**Go-Explore: a New Approach for Hard-Exploration Problems** (2019)
- *Authors:* Adrien Ecoffet et al.
- *Direct Connection:* LS-GFN’s backtrack-then-reexplore procedure mirrors Go-Explore’s “return to promising states then explore,” but instantiates it within GFlowNets by using the learned backward policy for returning and the forward policy for local neighborhood exploration.

### 📊 Baseline

**Trajectory Balance: Improved Credit Assignment in GFlowNets** (2022)
- *Authors:* Nikolay Malkin et al.
- *Direct Connection:* LS-GFN departs from the standard TB training/generation regime that samples complete trajectories from scratch with the forward policy, addressing TB’s tendency to over-explore by interleaving exploitative local-search episodes guided by learned backward/forward policies.

### 🔧 Extension

**Training GFlowNets by Subtrajectory Balance** (2023)
- *Authors:* Kushal Madan et al.
- *Direct Connection:* Subtrajectory Balance formalizes consistency over partial trajectories, and LS-GFN directly leverages this idea by performing backtracking-and-reconstruction edits on subtrajectories around high-reward states while retaining flow consistency.

### 🔗 Related Problem

**Bayesian Structure Learning with GFlowNets** (2022)
- *Authors:* Tristan Deleu et al.
- *Direct Connection:* This paper operationalized bidirectional moves (adding/removing edges) on discrete DAGs with GFlowNets, informing LS-GFN’s use of backward actions to reliably return to promising intermediate states before locally reconstructing forward.

---

## Synthesis: How Prior Work Led to This Paper

Generative Flow Networks established a bidirectional sampling framework that learns forward and backward policies so that terminal objects are sampled proportional to their reward; this bidirectionality made it natural to manipulate trajectories both toward and away from terminal states. Trajectory Balance then standardized training and generation by sampling complete trajectories from scratch via the forward policy, providing a stable objective but implicitly biasing the procedure toward broad exploration over targeted exploitation. Subtrajectory Balance extended the framework to enforce flow consistency over partial paths, concretizing how edits to subsegments can remain distributionally correct—an essential ingredient for any method that modifies only part of a trajectory. In parallel, Bayesian Structure Learning with GFlowNets demonstrated practical bidirectional edits on combinatorial objects (e.g., adding/removing edges in DAGs), showing that backward moves can reliably return to earlier states within complex discrete spaces. Outside the GFlowNet literature, Go-Explore introduced the simple but powerful principle of returning to promising states and then exploring locally to reliably improve solution quality in vast search spaces.
Taken together, these works suggested a clear opportunity: use GFlowNets’ learned backward policy to return to promising states and their forward policy to reconstruct locally consistent partial trajectories, exploiting high-reward neighborhoods while preserving reward-proportional sampling. Local Search GFlowNets synthesizes TB’s stable training, SB’s subtrajectory consistency, and Go-Explore’s return-and-explore intuition to bias sampling toward high-reward solutions without sacrificing the mode coverage that defines GFlowNets.

---

*Analysis generated on: 2026-01-06T20:03:55.434762*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
