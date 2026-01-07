# Prior Work Analysis Report

## Target Paper

**Title:** Leveraging augmented-Lagrangian techniques for differentiating over infeasible quadratic programs in machine learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Antoine Bambade, Fabian Schramm, Adrien Taylor, Justin Carpentier

**Keywords:** Machine Learning, Optimization, Differentiable Optimization, Optimization layers

**Abstract:** 
> Optimization layers within neural network architectures have become increasingly popular for their ability to solve a wide range of machine learning tasks and to model domain-specific knowledge. However, designing optimization layers requires careful consideration as the underlying optimization problems might be infeasible during training. 
Motivated by applications in learning, control and robotics, this work focuses on convex quadratic programming (QP) layers. The specific structure of this ty...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**A Dual Approach to Solving Nonlinear Programming Problems Using Augmented Lagrangians** (1973)
- *Authors:* R. Tyrrell Rockafellar
- *Direct Connection:* Established the augmented-Lagrangian method’s exact-penalty and feasibility-restoration properties, which this paper leverages to construct a differentiable map to the closest feasible QP solution and to derive unified derivatives across feasible and infeasible regimes.

### 💡 Inspiration

**OSQP: An Operator Splitting Solver for Quadratic Programs** (2020)
- *Authors:* Bartolomeo Stellato et al.
- *Direct Connection:* Demonstrated that primal–dual operator-splitting (augmented-Lagrangian/ADMM) methods exploit QP structure and provide infeasibility certificates, directly inspiring the use of a primal–dual augmented-Lagrangian backbone to define and differentiate meaningful solution maps even when the QP is infeasible.

### 🔍 Gap Identification

**Differentiable MPC for End-to-end Planning and Control** (2018)
- *Authors:* Brandon Amos et al.
- *Direct Connection:* Showed QP-based control layers in practice can become infeasible and resort to ad hoc softening, highlighting the need for principled gradients in infeasible regimes that this work directly provides via augmented-Lagrangian differentiation.

### 📊 Baseline

**OptNet: Differentiable Optimization as a Layer in Neural Networks** (2017)
- *Authors:* Brandon Amos et al.
- *Direct Connection:* Introduced QP layers with implicit differentiation through KKT conditions, establishing the standard differentiable-QP formulation that this work directly generalizes to handle infeasible cases and provide gradients via an augmented-Lagrangian view.

**Differentiable Convex Optimization Layers** (2019)
- *Authors:* Akshay Agrawal et al.
- *Direct Connection:* Generalized differentiable convex layers via cone-program implicit differentiation but assumed well-posed, feasible problems, whose limitation (lack of a principled treatment of infeasibility) this work addresses by defining and differentiating the closest feasible QP through a primal–dual augmented-Lagrangian framework.

### 🔧 Extension

**Deep Declarative Networks** (2019)
- *Authors:* Stephen Gould et al.
- *Direct Connection:* Provided a general implicit-differentiation calculus for optimization layers under regularity and feasibility, which this work extends by redefining the layer via an augmented-Lagrangian ‘closest feasible’ surrogate to obtain well-defined gradients when the original QP is infeasible.

---

## Synthesis: How Prior Work Led to This Paper

Early differentiable optimization layers treated quadratic programs as implicit functions, with OptNet formalizing KKT-based differentiation for QP layers and showing how to embed them in neural networks. Differentiable Convex Optimization Layers broadened this to generic cone programs via implicit differentiation, but their sensitivity analysis presupposed well-posed feasible problems. Operator-splitting via OSQP exploited the special structure of convex QPs with a primal–dual augmented-Lagrangian scheme that yields residuals and certificates for infeasibility, illustrating how augmented-Lagrangian mechanisms can remain informative even when constraints cannot be satisfied. The classical augmented-Lagrangian theory of Rockafellar established exact-penalty and feasibility-restoration properties, suggesting a principled way to regularize constraint violations while maintaining meaningful dual information. In application domains like model-predictive control, Differentiable MPC highlighted that QP subproblems can become infeasible in practice, leading to heuristic softening and unreliable gradients. Deep Declarative Networks provided a general calculus for differentiating through argmin layers under regularity, clarifying where standard approaches break when feasibility and smoothness fail. Together, these works exposed both the promise and the fragility of differentiable QP layers: powerful when feasible and regular, but brittle at infeasibility. The present work synthesizes OSQP’s primal–dual augmented-Lagrangian structure with Rockafellar’s feasibility-restoring insights to define a ‘closest feasible’ surrogate for QPs and to derive unified, stable derivatives across feasible and infeasible regimes, thereby extending declarative-layer differentiation and overcoming the practical gap surfaced by differentiable MPC and prior QP-layer frameworks.

---

*Analysis generated on: 2026-01-06T17:49:57.672557*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
