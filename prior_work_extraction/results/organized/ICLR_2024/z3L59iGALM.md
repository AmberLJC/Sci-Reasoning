# Prior Work Analysis Report

## Target Paper

**Title:** Massively Scalable Inverse Reinforcement Learning in Google Maps

**Conference:** ICLR 2024 (spotlight)

**Authors:** Matt Barnes, Matthew Abueg, Oliver F. Lange, Matt Deeds, Jason Trader, Denali Molitor, Markus Wulfmeier, Shawn O'Banion

**Keywords:** Inverse reinforcement learning, route optimization

**Abstract:** 
> Inverse reinforcement learning (IRL) offers a powerful and general framework for learning humans' latent preferences in route recommendation, yet no approach has successfully addressed planetary-scale problems with hundreds of millions of states and demonstration trajectories. In this paper, we introduce scaling techniques based on graph compression, spatial parallelization, and improved initialization conditions inspired by a connection to eigenvector algorithms. We revisit classic IRL methods ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Maximum Entropy Inverse Reinforcement Learning** (2008)
- *Authors:* Andrew Y. Ng and Pieter Abbeel and Andrew B. Ziebart
- *Direct Connection:* The MaxEnt IRL formulation that learns rewards by inducing a soft-optimal stochastic policy is the algorithmic template RHIP generalizes via a finite planning horizon to trade robustness for computational efficiency on massive graphs.

### 💡 Inspiration

**Linearly-Solvable Markov Decision Processes** (2007)
- *Authors:* Emanuel Todorov
- *Direct Connection:* The exponential transformation that linearizes control and yields principal-eigenvector solutions motivates the paper’s eigenvector/power-iteration view and eigenvector-based initialization for scalable IRL updates.

### 🔍 Gap Identification

**Maximum Entropy Deep Inverse Reinforcement Learning** (2016)
- *Authors:* Markus Wulfmeier et al.
- *Direct Connection:* Deep MaxEnt IRL demonstrated effective reward learning for navigation but exposed the prohibitive cost of full soft planning at scale, a limitation addressed here via graph compression, spatial parallelization, and RHIP’s controllable horizon.

### 📊 Baseline

**Maximum Margin Planning** (2006)
- *Authors:* Nathan D. Ratliff et al.
- *Direct Connection:* MMP exemplifies the cheap deterministic shortest-path learner that forms the opposite endpoint of RHIP’s trade-off, which RHIP approaches as the planning horizon shrinks toward purely deterministic planning.

### 🔧 Extension

**Modeling Purposeful Behavior with the Principle of Maximum Causal Entropy** (2010)
- *Authors:* Andrew B. Ziebart
- *Direct Connection:* The maximum causal entropy inverse optimal control recursion provides the stochastic Bellman backups that RHIP truncates into a receding-horizon operator, with the infinite-horizon limit recovering the standard MCE-IOC solution.

### 🔗 Related Problem

**Contraction Hierarchies: Faster and Simpler Hierarchical Routing in Road Networks** (2008)
- *Authors:* Robert Geisberger et al.
- *Direct Connection:* Contraction Hierarchies’ graph compression and fast shortest-path queries directly underpin the scalable deterministic planning primitives that RHIP repeatedly invokes across a planetary-scale road graph.

---

## Synthesis: How Prior Work Led to This Paper

Maximum entropy inverse reinforcement learning introduced a probabilistic formulation that fits rewards by inducing a soft-optimal policy, realized via entropy-regularized Bellman backups that are robust to suboptimal demonstrations. The maximum causal entropy refinement cast this as a causal, dynamic-programming-friendly recursion over MDPs, clarifying the stochastic policy structure and the temperature/horizon effects that govern robustness versus determinism. In contrast, maximum margin planning framed reward learning as structured prediction over deterministic shortest paths, enabling fast learning with Dijkstra-like planners but at the cost of brittleness to demonstration noise. Linearly-solvable MDPs showed that an exponential transform linearizes control, reducing planning to principal-eigenvector computation and suggesting power-iteration-style algorithms and eigenfunction initializations that can dramatically affect convergence. Deep maximum entropy IRL established that expressive neural features can learn navigation rewards, while simultaneously revealing the heavy computational burden of full soft planning on large graphs. Finally, contraction hierarchies demonstrated that hierarchical graph compression yields planet-scale shortest-path queries and naturally supports spatial partitioning and parallelization. Together, these works expose a gap between cheap deterministic planning and robust but expensive stochastic IRL, suggest that horizon/temperature mediates this gap, and hint that eigenvector perspectives and graph compression can stabilize and scale learning. The present work synthesizes these insights by introducing a receding-horizon generalization of classic entropy-based IRL that interpolates between deterministic and stochastic regimes, while leveraging hierarchical graph compression and eigenvector-inspired initialization to make reward inference tractable at global scale.

---

*Analysis generated on: 2026-01-06T10:09:55.780931*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
