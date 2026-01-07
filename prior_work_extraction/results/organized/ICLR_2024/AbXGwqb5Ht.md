# Prior Work Analysis Report

## Target Paper

**Title:** Implicit regularization of deep residual networks towards neural ODEs

**Conference:** ICLR 2024 (spotlight)

**Authors:** Pierre Marion, Yu-Han Wu, Michael Eli Sander, Gérard Biau

**Keywords:** deep learning theory, residual networks, neural ODEs, optimization, implicit regularization, gradient flow

**Abstract:** 
> Residual neural networks are state-of-the-art deep learning models. Their continuous-depth analog, neural ordinary differential equations (ODEs), are also widely used. Despite their success, the link between the discrete and continuous models still lacks a solid mathematical foundation. In this article, we take a step in this direction by establishing an implicit regularization of deep residual networks towards neural ODEs, for nonlinear networks trained with gradient flow. We prove that if the ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Neural Ordinary Differential Equations** (2018)
- *Authors:* Chen et al.
- *Direct Connection:* This paper formalized continuous-depth neural networks via ODE flows, providing the continuous-time model and forward-Euler discretization target that the present work proves gradient flow implicitly regularizes ResNets toward and preserves throughout training.

**A Proposal on Machine Learning via Dynamical Systems** (2017)
- *Authors:* E
- *Direct Connection:* This work introduced the dynamical-systems viewpoint that casts deep networks, and in particular residual connections, as discretizations of continuous dynamics, directly motivating the problem of rigorously linking ResNet training to an underlying ODE.

**Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak–Łojasiewicz Condition** (2016)
- *Authors:* Karimi et al.
- *Direct Connection:* This paper established convergence guarantees under the PL condition, which the current work leverages to extend preservation and convergence results to infinite training time when residual blocks satisfy a PL inequality.

### 💡 Inspiration

**Stable Architectures for Deep Neural Networks** (2017)
- *Authors:* Haber et al.
- *Direct Connection:* By interpreting ResNets explicitly as forward-Euler discretizations of ODEs and analyzing stability, this work supplied the precise discretization structure whose invariance under gradient flow the current paper establishes mathematically.

**The Implicit Bias of Gradient Descent on Separable Data** (2018)
- *Authors:* Soudry et al.
- *Direct Connection:* By proving that gradient descent/flow converges to structurally biased solutions (max-margin) without explicit regularization, this paper provided the template for analyzing implicit regularization that is extended here to the structural constraint of remaining an ODE discretization.

### 🔍 Gap Identification

**Gradient Descent Finds Global Minima of Over-parameterized Nonlinear Neural Networks** (2019)
- *Authors:* Du et al.
- *Direct Connection:* By proving convergence under large overparameterization (typically polynomially large width), this work exposed the limitation that the present paper addresses by proving a PL condition and convergence for residual blocks with only linear overparameterization in width.

### 🔗 Related Problem

**Implicit Bias of Gradient Descent on Linear Convolutional Networks** (2018)
- *Authors:* Gunasekar et al.
- *Direct Connection:* This work showed that gradient descent preserves architectural structure and induces specific norms in the limit, informing the present analysis that gradient flow preserves the ODE-discretization manifold of ResNets initialized from a neural ODE.

---

## Synthesis: How Prior Work Led to This Paper

Neural Ordinary Differential Equations introduced a continuous-depth formulation in which a learnable vector field generates network transformations via an ODE, with forward-Euler steps serving as a natural discretization. Building on a similar perspective, Stable Architectures for Deep Neural Networks formalized residual networks as explicit Euler discretizations of dynamical systems and examined stability, providing a precise discretization template. A Proposal on Machine Learning via Dynamical Systems advanced the broader dynamical-systems viewpoint, explicitly motivating rigorous connections between deep residual architectures and underlying continuous flows. In parallel, the implicit regularization literature demonstrated that gradient-based dynamics bias solutions in structured ways: The Implicit Bias of Gradient Descent on Separable Data proved gradient flow converges to max-margin solutions without explicit regularizers, while Implicit Bias of Gradient Descent on Linear Convolutional Networks showed architecture-specific structural norms emerge from pure optimization dynamics. Complementing these, Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak–Łojasiewicz Condition provided the analytical machinery to translate PL inequalities into convergence guarantees. Finally, Gradient Descent Finds Global Minima of Over-parameterized Nonlinear Neural Networks established convergence for highly overparameterized models, highlighting the width requirements typical of prior guarantees. Together, these works reveal a gap: while ResNets are understood as ODE discretizations and gradient flow exhibits implicit structural bias, there lacked a proof that training preserves the ODE-discretization structure and converges under realistic width. Synthesizing these insights, the current paper shows gradient flow implicitly regularizes deep ResNets to remain consistent with a neural ODE discretization and achieves convergence under a PL condition that holds for residual two-layer perceptrons with only linear overparameterization.

---

*Analysis generated on: 2026-01-06T23:22:08.723818*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
