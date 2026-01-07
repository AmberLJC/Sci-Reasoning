# Prior Work Analysis Report

## Target Paper

**Title:** Unleashing the Potential of Fractional Calculus in Graph Neural Networks with FROND

**Conference:** ICLR 2024 (spotlight)

**Authors:** Qiyu Kang, Kai Zhao, Qinxu Ding, Feng Ji, Xuhao Li, Wenfei Liang, Yang Song, Wee Peng Tay

**Keywords:** graph neural network

**Abstract:** 
> We introduce the FRactional-Order graph Neural Dynamical network (FROND), a new continuous graph neural network (GNN) framework. Unlike traditional continuous GNNs that rely on integer-order differential equations, FROND employs the Caputo fractional derivative to leverage the non-local properties of fractional calculus. This approach enables the capture of long-term dependencies in feature updates, moving beyond the Markovian update mechanisms in conventional integer-order models and offering e...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Neural Ordinary Differential Equations** (2018)
- *Authors:* Ricky T. Q. Chen et al.
- *Direct Connection:* FROND adopts the continuous-depth dynamical systems view of Neural ODEs but replaces the integer-order time derivative with a Caputo fractional derivative to model history-dependent dynamics on graphs.

**Fractional Differential Equations** (1999)
- *Authors:* Igor Podlubny
- *Direct Connection:* FROND’s modeling and analysis hinge on Caputo derivative definitions and properties from Podlubny, including treatment of initial conditions and memory kernels in fractional-order dynamical systems.

### 💡 Inspiration

**The Random Walk’s Guide to Anomalous Diffusion: A Fractional Dynamics Approach** (2000)
- *Authors:* Ralf Metzler et al.
- *Direct Connection:* The established equivalence between time-fractional diffusion (with Caputo derivatives) and non-Markovian continuous-time random walks directly motivates FROND’s non-Markovian random-walk interpretation of feature updates.

### 🔍 Gap Identification

**Graph Neural Networks Exponentially Lose Expressive Power for Node Classification** (2020)
- *Authors:* Kenta Oono et al.
- *Direct Connection:* This work’s contraction analysis of deep GNNs formalizes the oversmoothing problem that FROND explicitly addresses by weakening the contraction via time-fractional dynamics.

**Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning** (2018)
- *Authors:* Qimai Li et al.
- *Direct Connection:* By identifying GCN propagation as Laplacian smoothing that homogenizes features, this paper motivates FROND’s shift from integer-time diffusion to fractional-time diffusion to retain discriminative signals.

### 🔧 Extension

**GRAND: Graph Neural Diffusion** (2021)
- *Authors:* Benjamin P. Chamberlain et al.
- *Direct Connection:* FROND directly generalizes GRAND’s Laplacian-driven diffusion ODE ẋ = −Lx by formulating a Caputo time-fractional diffusion d^αx/dt^α = −Lx, yielding non-Markovian feature evolution with provable oversmoothing mitigation.

---

## Synthesis: How Prior Work Led to This Paper

Neural Ordinary Differential Equations introduced a continuous-depth viewpoint where hidden states evolve under time-parameterized dynamics, providing the formal machinery to treat layer-wise propagation as the solution of a differential equation. GRAND specialized this idea to graphs by casting node feature propagation as a graph-Laplacian-driven diffusion ODE, tightly linking representation learning to the heat equation on networks. Parallel to these developments, fractional calculus established by Podlubny codified Caputo derivatives and their memory kernels, enabling well-posed fractional-order dynamical systems with natural initial conditions. Metzler and Klafter connected time-fractional diffusion equations to non-Markovian continuous-time random walks with heavy-tailed waiting times, showing how history-dependent dynamics slow mixing and preserve heterogeneity relative to Markovian diffusion. In graph learning, Li, Han, and Wu characterized standard GCN propagation as Laplacian smoothing, explaining feature homogenization through diffusion. Oono and Suzuki further proved that deep GNNs contract exponentially, formalizing oversmoothing as an inherent limitation of repeated diffusion-like updates.
Bringing these strands together suggested a natural opportunity: retain the powerful continuous-depth and diffusion formalisms of GRAND/Neural ODEs while replacing the integer-order time derivative by a Caputo fractional derivative to inject explicit memory into graph propagation. This synthesis yields a non-Markovian, time-fractional diffusion on graphs that analytically weakens the contraction underpinning oversmoothing and admits a random-walk interpretation grounded in anomalous diffusion theory, while remaining a drop-in generalization of established continuous GNN baselines.

---

*Analysis generated on: 2026-01-06T14:23:46.127971*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
