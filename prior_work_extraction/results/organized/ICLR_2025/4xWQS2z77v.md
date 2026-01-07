# Prior Work Analysis Report

## Target Paper

**Title:** Exploring The Loss Landscape Of Regularized Neural Networks Via Convex Duality

**Conference:** ICLR 2025 (oral)

**Authors:** Sungyoon Kim, Aaron Mishkin, Mert Pilanci

**Keywords:** Convex duality, Machine Learning Theory, Loss Landscape, Optimal Sets

**Abstract:** 
> We discuss several aspects of the loss landscape of regularized neural networks: the structure of stationary points, connectivity of optimal solutions, path with non-increasing loss to arbitrary global optimum, and the nonuniqueness of optimal solutions, by casting the problem into an equivalent convex problem and considering its dual. Starting from two-layer neural networks with scalar output, we first characterize the solution set of the convex problem using its dual and further characterize a...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Breaking the Curse of Dimensionality with Convex Neural Networks** (2017)
- *Authors:* Francis Bach
- *Direct Connection:* This work introduced the convex (variation-norm/atomic-norm) formulation of two-layer networks that underlies casting regularized network training as a convex program whose dual can be analyzed to characterize solutions.

### 💡 Inspiration

**Global Optimality in Tensor Factorization, Deep Learning, and Beyond** (2015)
- *Authors:* Benjamin Haeffele et al.
- *Direct Connection:* By exploiting positive homogeneity to link nonconvex factorizations with convex programs and global-optimality certificates, this paper provided the key homogeneity/atomic-norm insight leveraged to map ReLU networks with regularization to a convex dual framework.

**Mode Connectivity in Loss Landscapes of Neural Networks** (2018)
- *Authors:* Timur Garipov et al.
- *Direct Connection:* The empirical observation of non-increasing-loss paths connecting minima directly inspired the construction of certified non-increasing-loss paths to arbitrary global optima using the convex program’s dual structure.

### 🔍 Gap Identification

**Spurious Valleys in Two-Layer Neural Networks** (2019)
- *Authors:* Luca Venturi et al.
- *Direct Connection:* Their identification of spurious valleys and disconnected low-loss regions in shallow networks motivates resolving when and why such pathologies occur, which is addressed here via dual certificates that delineate topology and phase transitions of global optima with width.

### 🔧 Extension

**Convex Formulations for Two-Layer Neural Networks** (2021)
- *Authors:* Ergen et al.
- *Direct Connection:* The present work directly builds on this convex-duality characterization of L2-regularized two-layer ReLU training, extending it to a full loss-landscape analysis that classifies stationary points and proves connectivity of optimal sets (and to vector outputs and parallel three-layer architectures).

### 🔗 Related Problem

**Gradient Descent Finds Global Minima of Over-parameterized Deep Neural Networks** (2019)
- *Authors:* Simon S. Du et al.
- *Direct Connection:* Results showing global convergence under sufficient width motivated the dual-based analysis that pinpoints a phase transition in the topology of global optima as width varies and explains when connectivity emerges.

---

## Synthesis: How Prior Work Led to This Paper

Bach established that two-layer networks admit a convex representation via variation/atomic norms, enabling training perspectives grounded in convex geometry and duality. Haeffele and Vidal leveraged positive homogeneity to relate nonconvex factorizations to convex programs with global-optimality guarantees, clarifying how appropriate regularization induces convex atomic norms over network outputs. Building on these convex viewpoints, Ergen and Pilanci formulated L2-regularized two-layer ReLU training as an equivalent convex problem via duality, providing a precise bridge from parameter-space nonconvexity to function-space convexity. In contrast, Venturi, Bandeira, and Bruna highlighted that shallow ReLU networks can exhibit spurious valleys and disconnected low-loss regions, pinpointing structural pitfalls in the landscape. Garipov and colleagues empirically demonstrated mode connectivity, exhibiting non-increasing-loss paths between minima that suggested hidden geometric regularity. Du and coauthors showed that sufficient overparameterization yields global convergence of gradient descent, suggesting that width governs qualitative changes in optimization topology.
Together, these works revealed an opportunity: convex function-space formulations and dual certificates could resolve open questions about nonconvex landscapes—stationary-point structure, connectivity, and multiplicity—beyond empirical observations and width-asymptotic results. The present paper synthesizes the convex duality program (from Bach and Ergen–Pilanci) with the landscape phenomena (from Venturi and Garipov) and the width-driven guarantees (from Du), to rigorously characterize all stationary points, certify non-increasing-loss paths to arbitrary global optima, expose nonuniqueness of optimal solutions, and reveal a phase transition in the topology of global optima as width increases, extending the analysis to vector outputs and parallel three-layer networks.

---

*Analysis generated on: 2026-01-06T12:18:08.942221*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
