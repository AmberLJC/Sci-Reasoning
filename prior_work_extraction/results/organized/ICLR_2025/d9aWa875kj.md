# Prior Work Analysis Report

## Target Paper

**Title:** Exact Certification of (Graph) Neural Networks Against Label Poisoning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Mahalakshmi Sabanayagam, Lukas Gosch, Stephan Günnemann, Debarghya Ghoshdastidar

**Keywords:** graph neural networks, robustness, certificates, provable robustness, neural networks, label poisoning, label flipping, poisoning, mixed-integer linear programming, neural tangent kernel, support vector machines

**Abstract:** 
> Machine learning models are highly vulnerable to label flipping, i.e., the adversarial modification (poisoning) of training labels to compromise performance. Thus, deriving robustness certificates is important to guarantee that test predictions remain unaffected and to understand worst-case robustness behavior. However, for Graph Neural Networks (GNNs), the problem of certifying label flipping has so far been unsolved. We change this by introducing an exact certification method, deriving both sa...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Direct Connection:* This work established that gradient descent training of wide networks is equivalent to kernel regression under the NTK, a core modeling step the paper uses to linearize GNN training dynamics for exact certification.

**Poisoning Attacks against Support Vector Machines** (2012)
- *Authors:* Battista Biggio et al.
- *Direct Connection:* This paper formulated data poisoning as a bilevel optimization problem for margin-based learners, a formulation the current work adopts and then exactly reformulates (under NTK) into a mixed-integer linear program for label flipping.

### 🔍 Gap Identification

**Poisoning Attacks with Back-gradient Optimization** (2017)
- *Authors:* Luis Muñoz-González et al.
- *Direct Connection:* By demonstrating effective bilevel poisoning of deep models via back-gradient methods yet without guarantees, this work highlights the need for provable, exact certification that the current paper provides.

**Certified Defenses for Data Poisoning Attacks** (2017)
- *Authors:* Jacob Steinhardt et al.
- *Direct Connection:* This paper introduced the idea of certifying worst-case poisoning effects for convex learners but does not handle neural networks or label flipping in GNNs, a key limitation the current work overcomes using NTK and MILP.

### 🔧 Extension

**Graph Neural Tangent Kernel: Fusing Graph Neural Networks with Graph Kernels** (2019)
- *Authors:* Qinliang (Edward) Du et al.
- *Direct Connection:* By providing a concrete NTK for GNN architectures (GNTK), this paper supplies the graph-specific kernel machinery that the current work leverages to represent wide GNN training in its MILP-based certification framework.

### 🔗 Related Problem

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* Influence functions provide an approximate sensitivity analysis of predictions to training labels, a perspective the current paper replaces with exact, worst-case certificates derived via an NTK-based MILP.

---

## Synthesis: How Prior Work Led to This Paper

The neural tangent kernel (NTK) formalism showed that gradient descent on wide neural networks is equivalent to kernel regression, making training dynamics tractable through linearization. Building on this, the graph neural tangent kernel (GNTK) instantiated NTK for message-passing architectures, giving a concrete kernel representation that reflects GNN inductive biases. In parallel, early data poisoning research cast training-time attacks as bilevel optimization, with poisoning against SVMs providing a precise margin-based formulation and demonstrating the centrality of discrete label and training-set decisions. Subsequent work introduced back-gradient techniques to carry bilevel attacks to deep networks, underscoring the practical vulnerability of complex models but stopping short of provable guarantees. Complementing these attacks, certified defenses framed worst-case guarantees for poisoning in convex settings, highlighting what can be certified but not addressing neural-network or graph-specific learners. Influence functions further quantified how small label perturbations affect predictions, offering a sensitivity lens that, while insightful, remained approximate and local.
Together, these strands pointed to a natural path: represent GNN training in the wide-limit via (G)NTK to obtain a convex, kernelized view; express adversarial label flips within the bilevel poisoning paradigm; and then replace approximation with exactness by encoding the resulting problem as a mixed-integer linear program. This synthesis closes the gap between empirical poisoning attacks and limited convex certifications by delivering exact, sample-wise and collective certificates for GNNs under label flipping, enabling principled robustness comparisons across architectures.

---

*Analysis generated on: 2026-01-06T09:50:59.318225*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
