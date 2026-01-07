# Prior Work Analysis Report

## Target Paper

**Title:** Decentralized Sporadic Federated Learning: A Unified Algorithmic Framework with Convergence Guarantees

**Conference:** ICLR 2025 (spotlight)

**Authors:** Shahryar Zehtabi, Dong-Jun Han, Rohit Parasnis, Seyyedali Hosseinalipour, Christopher Brinton

**Keywords:** Decentralized Federated Learning, Sporadicity, Unified Algorithmic Framework, Convergence Analysis

**Abstract:** 
> Decentralized federated learning (DFL) captures FL settings where both (i) model updates and (ii) model aggregations are exclusively carried out by the clients without a central server. Existing DFL works have mostly focused on settings where clients conduct a fixed number of local updates between local model exchanges, overlooking heterogeneity and dynamics in communication and computation capabilities. In this work, we propose Decentralized Sporadic Federated Learning ($\texttt{DSpodFL}$), a D...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Can decentralized algorithms outperform centralized algorithms? A case study for decentralized parallel stochastic gradient descent** (2017)
- *Authors:* Xiangru Lian et al.
- *Direct Connection:* DSpodFL generalizes the D-PSGD formulation by replacing its fixed, synchronous update-and-mix rule with per-iteration indicator random variables for both local gradient steps and neighbor exchanges, recovering D-PSGD as a special case.

**Randomized Gossip Algorithms** (2006)
- *Authors:* Stephen Boyd et al.
- *Direct Connection:* DSpodFL’s representation of pairwise model exchanges as Bernoulli indicator activations directly adopts the randomized gossip abstraction originating from Boyd et al.’s framework.

### 💡 Inspiration

**Local SGD Converges Fast and Communicates Little** (2019)
- *Authors:* Sebastian U. Stich
- *Direct Connection:* The idea of performing multiple local steps between aggregations in Local SGD motivates DSpodFL’s stochastic modeling of whether a client executes a local gradient step at each iteration, generalizing periodic local computation to sporadic participation.

### 🔍 Gap Identification

**Asynchronous Decentralized Parallel Stochastic Gradient Descent** (2018)
- *Authors:* Xiangru Lian et al.
- *Direct Connection:* AD-PSGD highlights heterogeneity and uncoordinated client activity but assumes a specific asynchronous protocol; DSpodFL addresses this gap by providing a unified stochastic-indicator model and convergence guarantees that cover arbitrary, time-varying sporadic computation and communication.

### 📊 Baseline

**Gossip Learning as a Decentralized Alternative to Federated Learning** (2021)
- *Authors:* István Hegedűs et al.
- *Direct Connection:* GossipFL operationalizes peer-to-peer model averaging in FL, and DSpodFL formalizes and analyzes this decentralized FL regime under heterogeneous, sporadic participation, showing it as a special case of the unified framework.

### 🔧 Extension

**Stochastic Gradient Push for Distributed Deep Learning** (2019)
- *Authors:* Mohamed B. Assran et al.
- *Direct Connection:* DSpodFL subsumes SGP by modeling directed/time-varying link activations via random edge indicators, thereby recovering push-sum style decentralized training as a specific instantiation of its unified framework.

---

## Synthesis: How Prior Work Led to This Paper

Decentralized parallel SGD established a canonical formulation for serverless training over networks using mixing matrices, typically assuming a fixed, synchronous cadence of local gradient updates and neighbor averaging. Randomized gossip introduced the notion that pairwise exchanges occur randomly, with edge activations modeled probabilistically, enabling analysis over time-varying connectivity. Building on gossip, push-sum based stochastic gradient methods extended decentralized training to directed and lossy networks, where mixing weights evolve with the communication pattern. Asynchrony-focused decentralized SGD further exposed the reality of heterogeneous client speeds and uncoordinated progress but analyzed convergence under specific asynchronous protocols. In federated learning, gossip-style peer-to-peer model averaging demonstrated that decentralized learning can replace the central server, though typically with heuristic participation and fixed or scenario-specific exchange patterns. Meanwhile, local SGD showed that allowing multiple local steps between aggregations can drastically reduce communication, but under periodic and centrally coordinated schedules. Together, these works revealed that both computation and communication in decentralized FL are inherently irregular, yet prior analyses treated only fixed or protocol-specific schedules. The natural next step was to unify these strands by explicitly modeling per-iteration sporadicity in both local updates and edge activations via indicator random variables, thereby capturing heterogeneous and time-varying participation. By doing so, one can recover gossip-FL, D-PSGD, push-sum methods, and periodic local-update schemes as special cases, while deriving convergence guarantees that hold across this broader, realistic spectrum of decentralized federated learning behaviors.

---

*Analysis generated on: 2026-01-06T18:46:21.749792*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
