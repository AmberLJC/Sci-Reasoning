# Prior Work Analysis Report

## Target Paper

**Title:** Geometry of Neural Reinforcement Learning in Continuous State and Action Spaces

**Conference:** ICLR 2025 (oral)

**Authors:** Saket Tiwari, Omer Gottesman, George Konidaris

**Keywords:** reinforcement learning, deep learning, geometry

**Abstract:** 
> Advances in reinforcement learning (RL) have led to its successful application in complex tasks with continuous state and action spaces. Despite these advances in practice, most theoretical work pertains to finite state and action spaces. We propose building a theoretical understanding of continuous state and action spaces by employing a geometric lens to understand the locally attained set of states. The set of all parametrised policies learnt through a semi-gradient based approach induce a set...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Deterministic Policy Gradient Algorithms** (2014)
- *Authors:* David Silver et al.
- *Direct Connection:* The analysis assumes a continuous-action actor–critic with deterministic policy updates, directly adopting the deterministic policy gradient framework to define the semi-gradient training dynamics that induce the attainable-state set.

**Controllability of Nonlinear Systems** (1972)
- *Authors:* Velimir Jurdjevic et al.
- *Direct Connection:* Geometric control results on local reachability and the rank of control-induced vector fields underpin the argument that the tangent space of attainable states is spanned by action-direction fields, linking manifold dimension to action dimension.

### 💡 Inspiration

**Proto-Value Functions: A Laplacian Framework for Learning Representation** (2005)
- *Authors:* Sridhar Mahadevan
- *Direct Connection:* The Laplacian view that MDP state spaces possess exploitable geometric structure inspired adopting a geometric lens on state space, here focused on the subset of states attainable under policy learning.

### 🔍 Gap Identification

**Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator** (2018)
- *Authors:* Maryam Fazel et al.
- *Direct Connection:* By restricting to linear dynamics and quadratic costs, this work highlighted the lack of theory for general continuous-state/action RL, motivating a geometric analysis for nonlinear systems with neural policies.

### 🔧 Extension

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Direct Connection:* The proof strategy leverages NTK-style linearization of two-layer networks to characterize the gradient-flow subspace of policy updates, enabling a dimension bound on the induced manifold of attainable states.

### 🔗 Related Problem

**Eigenoption Discovery through the Deep Successor Representation** (2018)
- *Authors:* Marlos C. Machado et al.
- *Direct Connection:* By using spectral structure of dynamics to define behaviors, this work informed the idea that policy-induced dynamics carve specific low-dimensional structures in state space, motivating analysis of the attainable-state manifold under learning.

---

## Synthesis: How Prior Work Led to This Paper

Deterministic Policy Gradient established a precise actor–critic framework for continuous actions in which policy updates deterministically shape the state visitation distribution, grounding subsequent analyses of how learning transforms reachable sets in continuous spaces. Neural Tangent Kernel theory showed that two-layer networks trained by gradient flow evolve within a linearized function space, effectively constraining updates to a low-dimensional subspace determined by the network’s tangent features. Classical geometric control, epitomized by Jurdjevic and Sussmann, characterized local reachability via the span of control-induced vector fields and Lie algebraic conditions, linking the dimension of reachable sets to the number and structure of control inputs. In the continuous-control theory track, policy gradient analyses for LQR demonstrated how gradient dynamics couple to system trajectories, but only in linear-quadratic regimes. Meanwhile, representation-learning works like Proto-Value Functions and eigenoption discovery revealed that MDP dynamics impart geometric structure on state spaces, in practice yielding low-dimensional spectral structure that shapes behavior and exploration. Together these streams exposed a gap: while control theory ties reachability geometry to input dimensions and deep-learning theory constrains gradient dynamics via tangent features, RL lacked a unifying account of how semi-gradient actor–critic training with neural policies sculpts the subset of states actually reached. The present synthesis marries NTK linearization with geometric control insights in the deterministic policy-gradient setting, yielding a precise characterization: training a two-layer policy induces a locally low-dimensional manifold of attainable states whose dimension scales with the action space, bridging continuous-control theory and representation geometry under neural training dynamics.

---

*Analysis generated on: 2026-01-06T13:50:18.702165*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
