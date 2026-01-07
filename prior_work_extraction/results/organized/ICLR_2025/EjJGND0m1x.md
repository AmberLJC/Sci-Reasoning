# Prior Work Analysis Report

## Target Paper

**Title:** MIND over Body: Adaptive Thinking using Dynamic Computation

**Conference:** ICLR 2025 (oral)

**Authors:** Mrinal Mathur, Barak A. Pearlmutter, Sergey M. Plis

**Keywords:** Interpretability, Fixed points, Dynamic routing, Dynamic input processing, Deep Learning Framework

**Abstract:** 
> While the human brain efficiently handles various computations with a limited number of neurons, traditional deep learning networks require a significant increase in parameters to improve performance.
  Yet, these parameters are used inefficiently as the networks employ the same amount of computation for inputs of the same size, regardless of the input's complexity.
  We address this inefficiency by introducing self-introspection capabilities to the network, enabling it to adjust the number of u...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Deep Equilibrium Models** (2019)
- *Authors:* Shaojie Bai et al.
- *Direct Connection:* Introduced the fixed-point (equilibrium) formulation with weight tying and implicit differentiation, which MIND adopts to reuse a compact parameter set while allocating compute via convergence-based, input-dependent iterations.

### 💡 Inspiration

**Adaptive Computation Time for Recurrent Neural Networks** (2016)
- *Authors:* Alex Graves
- *Direct Connection:* Pioneered halting units that let models dynamically choose the number of computation steps per input, directly inspiring MIND’s introspective mechanism for per-input adaptive compute.

**Routing Networks: Adaptive Selection of Non-Linear Functions for Multi-Task Learning** (2017)
- *Authors:* Clemens Rosenbaum et al.
- *Direct Connection:* Proposed a controller that routes inputs to function blocks for parameter reuse across tasks, which MIND generalizes with introspective, iterative routing that adapts effective depth until consistency is reached.

### 🔍 Gap Identification

**PonderNet: Learning to Ponder** (2021)
- *Authors:* Andrea Banino et al.
- *Direct Connection:* Exposed training instabilities of ACT and proposed probabilistic halting with a ponder loss, whose limitations (discrete halting and architecture specificity) motivate MIND’s differentiable, fixed-point–based introspective stopping.

### 📊 Baseline

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Direct Connection:* Established input-dependent routing to sparsely activate experts; MIND contrasts and improves on this by not only routing parameters but also varying computation time via state-dependent iteration and convergence.

### 🔗 Related Problem

**Universal Transformers** (2019)
- *Authors:* Mostafa Dehghani et al.
- *Direct Connection:* Showed how weight sharing across depth combined with ACT yields per-position adaptive computation, informing MIND’s coupling of parameter reuse with dynamic, input-conditioned computation beyond Transformers.

**Dynamic Routing Between Capsules** (2017)
- *Authors:* Sara Sabour et al.
- *Direct Connection:* Introduced iterative, agreement-based dynamic routing, providing the iterative, input-driven routing principle that MIND extends to general networks with a learned convergence/halting signal.

---

## Synthesis: How Prior Work Led to This Paper

Deep Equilibrium Models introduced the idea that deep networks can be cast as fixed-point solvers with tied parameters, trained via implicit differentiation; crucially, their convergence tolerance offers a natural, state-dependent stopping signal. Adaptive Computation Time showed that networks can learn to halt computation per input through a halting unit, trading accuracy for speed on the fly. Universal Transformers coupled depth-wise weight sharing with per-position ACT, demonstrating that adaptive steps and parameter reuse can coexist within a single architecture. PonderNet addressed ACT’s training pathologies via a probabilistic halting distribution and ponder loss, clarifying both the promise of adaptive steps and the limitations of discrete/stochastic halting. Sparsely-gated Mixture-of-Experts made input-dependent routing practical, activating only a subset of experts to scale capacity efficiently. Routing Networks extended routing to multi-task learning, using a controller to select function blocks and thus reuse parameters conditioned on task identity. Dynamic routing in Capsule Networks further established iterative, input-driven routing as a powerful mechanism for refining internal representations.
Collectively, these works revealed a gap: methods either reused parameters without varying compute time (e.g., MoE) or varied compute time without a principled, architecture-agnostic introspection signal (e.g., ACT/PonderNet), while fixed-point models lacked explicit routing across modules. MIND synthesizes these threads by using fixed-point convergence as an introspective criterion to adapt the number of iterations per input, while dynamically routing through a compact set of shared modules, enabling both parameter reuse across tasks and computation commensurate with input complexity.

---

*Analysis generated on: 2026-01-06T12:37:53.788737*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
