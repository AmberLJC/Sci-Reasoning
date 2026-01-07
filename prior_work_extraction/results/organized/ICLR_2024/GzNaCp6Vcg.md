# Prior Work Analysis Report

## Target Paper

**Title:** PINNACLE: PINN Adaptive ColLocation and Experimental points selection

**Conference:** ICLR 2024 (spotlight)

**Authors:** Gregory Kang Ruey Lau, Apivich Hemachandra, See-Kiong Ng, Bryan Kian Hsiang Low

**Keywords:** Physics-informed Neural Networks, PINNs, adaptive training points selection

**Abstract:** 
> Physics-Informed Neural Networks (PINNs), which incorporate PDEs as soft constraints, train with a composite loss function that contains multiple training point types: different types of collocation points chosen during training to enforce each PDE and initial/boundary conditions, and experimental points which are usually costly to obtain via experiments or simulations. Training PINNs using this loss function is challenging as it typically requires selecting large numbers of points of different ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations** (2019)
- *Authors:* M. Raissi et al.
- *Direct Connection:* Established the composite PINN loss over PDE, initial/boundary, and data terms defined on distinct point sets—precisely the multi–point-type training formulation that PINNACLE optimizes over.

### 💡 Inspiration

**Self-Adaptive Physics-Informed Neural Networks** (2020)
- *Authors:* L. McClenny et al.
- *Direct Connection:* Proposed learning the relative weights of different PINN loss terms during training, directly inspiring PINNACLE’s idea of dynamically adjusting the emphasis across different training point types (via selection/proportion) rather than static weighting.

### 🔍 Gap Identification

**When and why PINNs fail to train: A neural tangent kernel perspective** (2022)
- *Authors:* S. Wang et al.
- *Direct Connection:* Diagnosed gradient and loss-imbalance pathologies among PDE, boundary, and data terms, motivating PINNACLE’s use of interactions among point types to rebalance training via adaptive point selection and type proportioning.

### 📊 Baseline

**DeepXDE: A Deep Learning Library for Solving Differential Equations** (2021)
- *Authors:* L. Lu et al.
- *Direct Connection:* Introduced residual-based adaptive refinement (RAR) for collocation point selection, providing the primary collocation-only adaptive sampling baseline that PINNACLE generalizes to jointly handle collocation and experimental points.

### 🔗 Related Problem

**B-PINNs: Bayesian physics-informed neural networks for forward and inverse PDE problems** (2021)
- *Authors:* L. Yang et al.
- *Direct Connection:* Enabled uncertainty-aware use of experimental/data points and suggested active acquisition strategies, informing PINNACLE’s information-driven selection of costly experimental points alongside collocation points.

**hp-VPINNs: Variational physics-informed neural networks with adaptivity** (2021)
- *Authors:* M. Kharazmi et al.
- *Direct Connection:* Developed adaptive refinement guided by a-priori/a-posteriori indicators for PDE enforcement, highlighting the effectiveness of adaptive point placement for collocation-only settings that PINNACLE extends to all point types.

---

## Synthesis: How Prior Work Led to This Paper

Physics-informed neural networks were formalized with a composite loss over PDE residuals, initial/boundary conditions, and data-driven terms defined on separate point sets, establishing the central training paradigm and point taxonomy for subsequent work (Raissi et al., 2019). Building on this, adaptive collocation strategies such as residual-based adaptive refinement (RAR) focused on reallocating interior points toward high-residual regions to accelerate convergence and improve accuracy, but operated solely on collocation points (Lu et al., 2021). Complementarily, self-adaptive PINNs learned loss weights among PDE, boundary, and data terms, demonstrating that rebalancing emphasis among training components can markedly improve optimization (McClenny et al., 2020). NTK-based analyses then exposed that competing gradients across these terms cause optimization pathologies and imbalance, underscoring the need to account for interactions among point types during training (Wang et al., 2022). In parallel, Bayesian PINNs introduced uncertainty-aware usage and active acquisition of scarce experimental points, showing that data placement can be principled but treating it separately from collocation mechanisms (Yang et al., 2021). Finally, hp-VPINNs demonstrated the power of adaptive refinement guided by error indicators in variational settings, again primarily for collocation/test points (Kharazmi et al., 2021).
Taken together, these works revealed that (i) different point types drive distinct dynamics, (ii) adaptive refinement and uncertainty-aware acquisition are effective but siloed, and (iii) loss/gradient interactions across terms must be managed. The natural next step is to unify these insights by jointly selecting all training point types while adaptively rebalancing their proportions using interaction-aware signals—precisely the gap PINNACLE addresses by integrating information-driven collocation and experimental point selection with automatic type proportion adjustment.

---

*Analysis generated on: 2026-01-06T06:20:18.301224*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
