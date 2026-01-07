# Prior Work Analysis Report

## Target Paper

**Title:** Input-gradient space particle inference for neural network ensembles

**Conference:** ICLR 2024 (spotlight)

**Authors:** Trung Trinh, Markus Heinonen, Luigi Acerbi, Samuel Kaski

**Keywords:** deep ensembles, diversity, input gradient, robustness, covariate shift, particle variational inference

**Abstract:** 
> Deep Ensembles (DEs) demonstrate improved accuracy, calibration and robustness to perturbations over single neural networks partly due to their functional diversity. Particle-based variational inference (ParVI) methods enhance diversity by formalizing a repulsion term based on a network similarity kernel. However, weight-space repulsion is inefficient due to over-parameterization, while direct function-space repulsion has been found to produce little improvement over DEs. To sidestep these diffi...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Stein Variational Gradient Descent: A General Purpose Bayesian Inference Algorithm** (2016)
- *Authors:* Qiang Liu and Dilin Wang
- *Direct Connection:* Supplies the particle-based variational inference framework and repulsive kernel mechanism that the method directly adopts and redefines in input-gradient space.

### 💡 Inspiration

**Sobolev Training for Neural Networks** (2017)
- *Authors:* Wojciech M. Czarnecki et al.
- *Direct Connection:* Demonstrates that supervising or matching first-order input derivatives effectively constrains the learned function, motivating the idea that input gradients can serve as a compact, discriminative space for enforcing functional diversity.

**Improving the Adversarial Robustness and Interpretability of Deep Neural Networks by Regularizing Their Input Gradients** (2018)
- *Authors:* Andrew Ross and Finale Doshi-Velez
- *Direct Connection:* Shows that controlling input gradients shapes predictive behavior and robustness, directly supporting the choice to operate the diversity-inducing repulsion in gradient space.

### 📊 Baseline

**Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles** (2017)
- *Authors:* Balaji Lakshminarayanan et al.
- *Direct Connection:* Provides the primary ensemble baseline whose functional diversity benefits are targeted and systematically amplified via explicit repulsion in the proposed method.

### 🔧 Extension

**Stein Variational Gradient Descent in Function Space** (2019)
- *Authors:* Qiang Liu et al.
- *Direct Connection:* Shifts SVGD from parameter to function space, a move the new method extends by relocating the repulsion to input-gradient space to avoid weight-space over-parameterization and weak function-space gains.

### 🔗 Related Problem

**Improving Adversarial Robustness via Promoting Ensemble Diversity** (2019)
- *Authors:* Tiantian Pang et al.
- *Direct Connection:* Provides evidence and a concrete regularizer that diversity among ensemble members improves robustness, motivating explicit diversity promotion as a core training objective that the new method realizes via ParVI in gradient space.

---

## Synthesis: How Prior Work Led to This Paper

Deep ensembles were shown to deliver strong accuracy, calibration, and robustness, with benefits attributed to functional diversity among members (Lakshminarayanan et al., 2017). Stein Variational Gradient Descent (SVGD) formalized particle-based variational inference with an explicit repulsive kernel that encourages diversity among particles while following a variational objective (Liu & Wang, 2016). Subsequent work moved SVGD from parameter to function space to avoid pathologies of over-parameterized weight-space similarity, instantiating repulsion directly between predictive functions (Liu et al., 2019). In parallel, Sobolev Training established that supervising first-order input derivatives tightly constrains the learned function, highlighting gradients as a succinct and informative representation of model behavior (Czarnecki et al., 2017). Complementarily, input-gradient regularization demonstrated that manipulating gradients directly influences interpretability and adversarial robustness, underscoring their causal role in predictive behavior (Ross & Doshi-Velez, 2018). Finally, diversity-promoting ensemble training showed that explicitly encouraging diversity improves robustness, motivating principled diversity objectives during training (Pang et al., 2019). Building on these insights, a natural opportunity emerged: ParVI’s repulsion is principled but suffers when defined in weight space, and direct function-space repulsion has limited gains; meanwhile, first-order input gradients compactly and uniquely characterize functions up to translation and are linked to robustness. Synthesizing these pieces, the method relocates ParVI’s repulsion into input-gradient space, guaranteeing functional distinctness at far lower dimensionality than weights and more targeted than outputs, thereby operationalizing ensemble diversity where it most directly shapes learned features and robustness.

---

*Analysis generated on: 2026-01-06T18:08:43.125930*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
