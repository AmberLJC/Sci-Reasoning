# Prior Work Analysis Report

## Target Paper

**Title:** Global Convergence in Neural ODEs: Impact of Activation Functions

**Conference:** ICLR 2025 (oral)

**Authors:** Tianxiang Gao, Siyuan Sun, Hailiang Liu, Hongyang Gao

**Keywords:** Neural ODEs, Gradient Descent, Neural Tangent Kernel (NTK)

**Abstract:** 
> Neural Ordinary Differential Equations (ODEs) have been successful in various applications due to their continuous nature and parameter-sharing efficiency. However, these unique characteristics also introduce challenges in training, particularly with respect to gradient computation accuracy and convergence analysis. In this paper, we address these challenges by investigating the impact of activation functions. We demonstrate that the properties of activation functions—specifically smoothness and...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Neural Ordinary Differential Equations** (2018)
- *Authors:* Ricky T. Q. Chen et al.
- *Direct Connection:* This work introduced the Neural ODE formulation and the continuous-time adjoint method, directly motivating the need to ensure well-posed forward and backward ODEs during training that this paper secures via activation smoothness.

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Direct Connection:* The NTK framework underpins the paper’s convergence analysis by linking gradient descent dynamics to a kernel whose spectral properties must be preserved during training.

### 💡 Inspiration

**Gradient Descent Finds Global Minima of Over-parameterized Neural Networks** (2019)
- *Authors:* Simon S. Du et al.
- *Direct Connection:* Their proof that global convergence follows when the NTK Gram matrix has a uniform spectral lower bound—achieved under sufficiently nonlinear (non-polynomial) activations—inspires this work’s requirement on activation nonlinearity to maintain NTK spectrum for Neural ODEs.

### 🔍 Gap Identification

**ANODE: Unconditionally Accurate Memory-Efficient Gradients for Neural ODEs** (2019)
- *Authors:* Amir Gholami et al.
- *Direct Connection:* By showing that the continuous adjoint can yield inaccurate gradients when dynamics are non-invertible or non-smooth, this paper exposed a concrete failure mode that the present work addresses by imposing smooth activations to guarantee globally unique forward/backward ODEs.

**Dissecting Neural ODEs** (2020)
- *Authors:* Stefano Massaroli et al.
- *Direct Connection:* This analysis highlighted well-posedness, stiffness, and gradient pathologies in Neural ODEs, motivating the present activation-based conditions that ensure stable dynamics and reliable gradient computation.

### 🔧 Extension

**A Convergence Theory for Deep Learning via Over-Parameterization** (2019)
- *Authors:* Zeyuan Allen-Zhu et al.
- *Direct Connection:* Their analysis showing that wide networks converge because the NTK stays close to initialization is directly extended here to the continuous-depth setting by enforcing activation-driven conditions that keep the NTK’s spectrum stable during training.

---

## Synthesis: How Prior Work Led to This Paper

Neural Ordinary Differential Equations introduced continuous-depth parameterizations and the adjoint method for training, making the correctness of both forward and backward ODE solutions central to learning dynamics. Subsequent work demonstrated that, in practice, the continuous adjoint can produce inaccurate gradients when the flow is not smooth or reversible, and exposed broader well-posedness and gradient pathologies in Neural ODEs, highlighting the need for structural conditions that ensure stable dynamics. In parallel, the Neural Tangent Kernel (NTK) offered a precise view of gradient descent in overparameterized networks, reducing training to kernel regression whose success depends on maintaining a favorable kernel spectrum. Global convergence results then established that if the NTK Gram matrix has a uniform spectral lower bound—often guaranteed by sufficiently nonlinear (non-polynomial) activations—and if the kernel remains near its initialization during training, gradient descent reaches global minima efficiently.
Together, these insights suggested a path for continuous-depth models: ensure the ODE vector field is smooth enough to guarantee unique forward and adjoint trajectories, while enforcing activation nonlinearity to secure and preserve the NTK’s spectral properties. The present work synthesizes these strands by tying smooth activations to global well-posedness of the forward/backward flows and tying sufficient nonlinearity to the NTK spectrum’s stability in the overparameterized regime, thereby extending finite-depth NTK convergence theory to Neural ODEs and closing the training-accuracy gap identified by prior analyses.

---

*Analysis generated on: 2026-01-06T12:21:11.295657*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
