# Prior Work Analysis Report

## Target Paper

**Title:** When do GFlowNets learn the right distribution?

**Conference:** ICLR 2025 (spotlight)

**Authors:** Tiago Silva, Rodrigo Barreto Alves, Eliezer de Souza da Silva, Amauri H Souza, Vikas Garg, Samuel Kaski, Diego Mesquita

**Keywords:** GFlowNets

**Abstract:** 
> Generative Flow Networks (GFlowNets) are an emerging class of sampling methods for distributions over discrete and compositional objects, e.g., graphs. In spite of their remarkable success in problems such as drug discovery and phylogenetic inference, the question of when and whether GFlowNets learn to sample from the target distribution remains underexplored. To tackle this issue, we first assess the extent to which a violation of the detailed balance of the underlying flow network might hamper...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation** (2021)
- *Authors:* Emmanuel Bengio et al.
- *Direct Connection:* This paper introduced GFlowNets, the flow conservation and edge-level detailed balance constraints that define when sampling matches a target reward-proportional distribution—the exact correctness criterion whose violations this work analyzes.

**Trajectory Balance: Improved Credit Assignment in GFlowNets** (2022)
- *Authors:* Akhilesh K. Madan et al.
- *Direct Connection:* Trajectory Balance provides the global equality whose satisfaction guarantees correct sampling, and this work directly studies how deviations from the implied per-edge balances affect the learned distribution.

**Bayesian Structure Learning with Generative Flow Networks** (2022)
- *Authors:* Tristan Deleu et al.
- *Direct Connection:* This work established GFlowNets for graph-structured distributions (e.g., DAGs) with GNN-parameterized policies, the exact setting in which this paper analyzes when correctness holds and why imbalance may be inevitable.

### 💡 Inspiration

**Subtrajectory Balance for Compositional Generation** (2023)
- *Authors:* Anton Malkin et al.
- *Direct Connection:* By enforcing local consistency along subpaths, Subtrajectory Balance focused attention on localized balance constraints, motivating this paper’s edge-level analysis of how local imbalances propagate and unevenly impact correctness.

### 🔍 Gap Identification

**How Powerful are Graph Neural Networks?** (2019)
- *Authors:* Keyulu Xu et al.
- *Direct Connection:* Its characterization of message-passing GNNs’ expressivity limits (via 1-WL) underpins this paper’s claim that GNN-parameterized GFlowNets cannot distinguish certain transitions, making exact detailed balance unattainable in some graph families.

### 🔗 Related Problem

**Weisfeiler and Leman Go Neural: Higher-order Graph Neural Networks** (2019)
- *Authors:* Christopher Morris et al.
- *Direct Connection:* By formalizing when MPNNs collapse distinct structures, this work provides the theoretical lens used here to argue that unavoidable symmetries induce persistent edge imbalances in GNN-parameterized GFlowNets.

---

## Synthesis: How Prior Work Led to This Paper

GFlowNets were introduced with a flow conservation framework that enforces detailed balance across edges to ensure sampling matches a reward-proportional target distribution, precisely articulating when a learned policy is correct. Trajectory Balance subsequently provided a global equality whose satisfaction guarantees correctness, connecting trajectory-level credit assignment to per-edge balance constraints. Subtrajectory Balance emphasized local consistency along subpaths, suggesting that the locus of constraint enforcement matters and implicitly raising the question of how local violations influence global sampling accuracy. GFlowNets were then applied to graph-structured distributions such as DAGs using GNN-parameterized forward/backward policies, demonstrating practical success while exposing a setting where the correctness guarantees hinge on the representational capacity of the parameterization. In parallel, results on GNN expressivity showed that message-passing architectures cannot distinguish structures beyond 1-WL, and that symmetries cause different transitions or edges to be indistinguishable, limiting the realizability of exact balance.
Together, these works revealed a tension: correctness objectives require exact (local or trajectory-level) balance, yet common GNN parameterizations on graphs cannot separate all necessary transitions, making some violations inevitable. This paper takes the natural next step by quantifying how imbalance at specific edges affects the learned distribution as a function of the flow traversing those edges, showing the effect is unevenly distributed, and by formalizing inevitability under GNN expressivity limits in graph sampling settings.

---

*Analysis generated on: 2026-01-06T13:17:27.398679*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
