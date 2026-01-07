# Prior Work Analysis Report

## Target Paper

**Title:** Faithful and Efficient Explanations for Neural Networks via Neural Tangent Kernel Surrogate Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Andrew William Engel, Zhichao Wang, Natalie Frank, Ioana Dumitriu, Sutanay Choudhury, Anand Sarwate, Tony Chiang

**Keywords:** Explainability, Surrogate Models, Neural Tangent Kernel, Deep Learning, Attribution

**Abstract:** 
> A recent trend in explainable AI research has focused on surrogate modeling, where neural networks are approximated as simpler ML algorithms such as kernel machines. A second trend has been to utilize kernel functions in various explain-by-example or data attribution tasks. In this work, we combine these two trends to analyze approximate empirical neural tangent kernels (eNTK) for data attribution. Approximation is critical for eNTK analysis due to the high computational cost to compute the eNTK...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Direct Connection:* This work formalized the NTK K(x,x') = ∇θf(x)·∇θf(x'), which is the exact kernel the paper adopts (and approximates) to build kernel-machine surrogates for neural networks.

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* It introduced the modern data attribution problem—quantifying each training point’s influence on a prediction—whose computational and stability limitations this work addresses via NTK-based surrogate attribution.

### 💡 Inspiration

**Wide Neural Networks of Any Depth Evolve as Linear Models Under Gradient Descent** (2019)
- *Authors:* Jaehoon Lee et al.
- *Direct Connection:* By showing trained wide networks are well-approximated by their NTK linearization (i.e., kernel regression with the NTK), this paper directly motivates using eNTK kernel machines as faithful global surrogates of trained models.

### 📊 Baseline

**Estimating Training Data Influence by Tracing Gradient Descent** (2020)
- *Authors:* Garima Pruthi et al.
- *Direct Connection:* TracIn estimates influence via gradient inner products across checkpoints, which this work generalizes by using the eNTK gradient kernel with new random-projection approximations to compute example attributions without storing training trajectories.

### 🔧 Extension

**Database-friendly random projections: Johnson–Lindenstrauss with binary coins** (2003)
- *Authors:* Dimitris Achlioptas
- *Direct Connection:* Its sparse Johnson–Lindenstrauss projections that preserve inner products are adapted here to compress parameter gradients, yielding the paper’s tunable random-projection eNTK approximations for time/memory-efficient surrogate computation.

### 🔗 Related Problem

**Representer Point Selection for Explaining Deep Neural Networks** (2018)
- *Authors:* Chih-Kuan Yeh et al.
- *Direct Connection:* This paper showed predictions can be expressed as weighted sums over training examples through a kernelized representer view, directly informing the use of kernel machines for explain-by-example with an NTK kernel.

---

## Synthesis: How Prior Work Led to This Paper

The neural tangent kernel was formalized as the inner product of parameter gradients, providing a concrete kernel that encodes a network’s infinitesimal function geometry. Subsequent work established that wide networks trained by gradient descent evolve as their linearized counterparts, effectively performing kernel regression in the NTK, which legitimized using NTK-based kernel machines to emulate trained networks. Example-based explanations advanced in parallel: representer-point selection derived predictions as weighted sums over training examples via a kernelized view of deep models, showing that explain-by-example can be cast in a kernel surrogate framework. In data attribution, influence functions posed the core problem—quantifying each training point’s effect on predictions—but incurred heavy Hessian inversions and stability issues; TracIn mitigated cost by replacing second-order terms with gradient inner products along training trajectories, revealing gradient similarity as a practical attribution signal. Orthogonally, random projection theory (e.g., sparse Johnson–Lindenstrauss transforms) offered a principled way to compress high-dimensional vectors while preserving inner products, suggesting scalable paths for gradient-kernel computation.
Synthesizing these threads, the opportunity emerged to unify kernel surrogates and example attribution by directly using the empirical NTK as the kernel while overcoming its prohibitive computation. The paper operationalizes this by treating gradient features as the surrogate embedding, introducing random-projection variants that provably preserve gradient inner products to approximate the eNTK efficiently, and analyzing when the resulting kernel machine aligns with the underlying network. This closes the loop between NTK-theoretic faithfulness, example-based interpretability, and scalable computation, making kernel surrogates a practical and reliable vehicle for data attribution.

---

*Analysis generated on: 2026-01-06T19:04:46.875333*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
