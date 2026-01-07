# Prior Work Analysis Report

## Target Paper

**Title:** Learning Energy Decompositions for Partial Inference in GFlowNets

**Conference:** ICLR 2024 (oral)

**Authors:** Hyosoon Jang, Minsu Kim, Sungsoo Ahn

**Keywords:** Generative flow networks, reinforcement learning, generative models

**Abstract:** 
> This paper studies generative flow networks (GFlowNets) to sample objects from the Boltzmann energy distribution via a sequence of actions. In particular, we focus on improving GFlowNet with partial inference: training flow functions with the evaluation of the intermediate states or transitions. To this end, the recently developed forward-looking GFlowNet reparameterizes the flow functions based on evaluating the energy of intermediate states. However, such an evaluation of intermediate energies...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**GFlowNet Foundations** (2021)
- *Authors:* Yoshua Bengio et al.
- *Direct Connection:* This work formalized sampling from unnormalized Boltzmann rewards via flows over sequential construction graphs, providing the state/action/terminal-reward framework that LED-GFN adopts when learning transition-level energy potentials.

### 💡 Inspiration

**Policy Invariance under Reward Transformations: Theory and Application to Reward Shaping** (1999)
- *Authors:* Andrew Y. Ng et al.
- *Direct Connection:* The potential-based shaping principle (using differences of a scalar potential across transitions) directly inspires LED-GFN’s energy decomposition into transition potentials that reparameterize flows while preserving the target Boltzmann distribution.

**RUDDER: Return Decomposition for Delayed Rewards** (2019)
- *Authors:* Marc G. Bellemare (Arjona-Medina) et al.
- *Direct Connection:* RUDDER’s idea of learning a decomposition of delayed returns to provide informative local credit signals informs LED-GFN’s strategy of learning transition-level energy contributions for partial inference training.

### 🔍 Gap Identification

**Forward-Looking GFlowNets** (2023)
- *Authors:* Unknown et al.
- *Direct Connection:* This method reparameterizes flow functions using evaluated intermediate-state energies, and LED-GFN directly addresses its stated limitations by replacing expensive and potentially misleading intermediate energy evaluations with learned transition-level energy decompositions.

### 📊 Baseline

**A Trajectory Balance Objective for Generative Flow Networks** (2022)
- *Authors:* Mikhail Malkin et al.
- *Direct Connection:* Trajectory Balance is the principal training objective/baseline that LED-GFN reparameterizes with learned transition potentials to enable partial inference without relying on exact intermediate energy evaluations.

### 🔗 Related Problem

**Subtrajectory Balance for Credit Assignment in Generative Flow Networks** (2023)
- *Authors:* Unknown et al.
- *Direct Connection:* By enforcing balance on subpaths to improve credit assignment, this work motivates LED-GFN’s design of informative local training signals, which it achieves via learned transition potentials consistent with the global energy.

---

## Synthesis: How Prior Work Led to This Paper

Generative Flow Networks were grounded by GFlowNet Foundations, which framed the problem of sampling from unnormalized Boltzmann rewards through flows over a directed construction graph, tying terminal energies to path-wise flows. Building on this, the Trajectory Balance objective established a practical, stable global consistency constraint—equating products of forward policies and backward flows along complete trajectories to terminal rewards—that became the standard training baseline. Subtrajectory Balance moved beyond purely terminal credit by enforcing consistency on subpaths, highlighting the importance of local signals for long horizons. A complementary direction, Forward-Looking GFlowNets, reparameterized flows with evaluated intermediate-state energies to inject more informative local guidance, but revealed critical limitations: intermediate energies can be expensive or infeasible to compute and may mislead training when energies fluctuate sharply along sequences. Independently, the reinforcement learning literature provided two key insights: potential-based reward shaping (Ng et al.) showed that differences of a learned scalar potential across transitions can redistribute credit without changing the target optimum, and RUDDER demonstrated that learning return decompositions can transform delayed rewards into informative local signals. Together, these strands suggested an opportunity to replace brittle intermediate energy evaluations with learnable, transition-level surrogates. LED-GFN synthesizes these ideas by learning a potential whose differences decompose terminal energy across transitions, then reparameterizing the GFlowNet flow functions with these potentials to enable partial inference. This preserves the global Boltzmann target while supplying robust, informative local credit—naturally addressing forward-looking GFlowNets’ limitations and integrating smoothly with trajectory-balance style training.

---

*Analysis generated on: 2026-01-06T15:41:24.473521*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
