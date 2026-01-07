# Prior Work Analysis Report

## Target Paper

**Title:** Adaptive Rational Activations to Boost Deep Reinforcement Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Quentin Delfosse, Patrick Schramowski, Martin Mundt, Alejandro Molina, Kristian Kersting

**Keywords:** Deep Reinforcement Learning, Neural Plasticity, Activation Functions, Rational Functions

**Abstract:** 
> Latest insights from biology show that intelligence not only emerges from the connections between neurons, but that individual neurons shoulder more computational responsibility than previously anticipated. Specifically, neural plasticity should be critical in the context of constantly changing reinforcement learning (RL) environments, yet current approaches still primarily employ static activation functions. In this work, we motivate the use of adaptable activation functions in RL and show that...

---

## Key Prior Works (7 papers with direct influence)

### 💡 Inspiration

**Padé Activation Units: End-to-end Learning of Activation Functions for Deep Networks** (2019)
- *Authors:* M. G. Apicella et al.
- *Direct Connection:* This work established trainable rational-form activations (Padé units), directly inspiring the choice of rational parameterizations that the current paper regularizes via joint sharing and adapts for residual architectures.

**Deep Residual Learning for Image Recognition** (2016)
- *Authors:* Kaiming He et al.
- *Direct Connection:* Residual connections in ResNets motivated the authors to derive the specific closure condition ensuring that rational activation units remain well-formed under residual compositions.

**Activate or Not: Learning Customized Activation** (2021)
- *Authors:* Ningning Ma et al.
- *Direct Connection:* The idea of globally or channel-wise shared, learnable activation parameters here informed the decision to tie rational activation coefficients across layers as a natural regularizer.

### 🔍 Gap Identification

**Differentiable Plasticity: Training Plastic Neural Networks with Backpropagation** (2018)
- *Authors:* Thomas Miconi et al.
- *Direct Connection:* This work demonstrated the importance of neural plasticity for RL but implemented it via synaptic rules, highlighting a gap that the current paper fills by realizing plasticity through adaptive activation functions instead.

### 📊 Baseline

**Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification** (2015)
- *Authors:* Kaiming He et al.
- *Direct Connection:* Parametric ReLU from this paper serves as a principal learnable-activation baseline that the proposed joint-rational activations aim to surpass in flexibility and stability for RL.

### 🔧 Extension

**Rational Neural Networks** (2020)
- *Authors:* Nicolas Boullé and Alex Townsend
- *Direct Connection:* The paper adopts learnable rational activation units introduced here and extends them by sharing coefficients across layers and deriving conditions for closure under residual connections to control plasticity in RL.

### 🔗 Related Problem

**Learning Activation Functions to Improve Deep Neural Networks** (2014)
- *Authors:* Forest Agostinelli et al.
- *Direct Connection:* By showing that learnable activations can boost performance but risk overfitting when overly flexible, this paper motivated the current work’s regularized, jointly-parameterized rational activations to balance flexibility and control.

---

## Synthesis: How Prior Work Led to This Paper

Rational activation research established that activations parameterized as ratios of polynomials can flexibly approximate diverse nonlinearities, with Boullé and Townsend showing learnable rational units achieve strong function approximation properties and stability, while Padé Activation Units demonstrated practical end-to-end training of such rational forms. Earlier work on learnable activations, such as Adaptive Piecewise Linear units, validated that making activation shapes task-adaptive improves learning but also revealed the tendency to overfit when flexibility is unconstrained. Meta-ACON further explored customization and parameter sharing of activation behavior across channels or layers, indicating that tying activation parameters can regularize expressivity while preserving adaptability. In parallel, the importance of neural plasticity for nonstationary reinforcement learning was highlighted by Differentiable Plasticity, which introduced trainable, Hebbian-like synaptic updates to enable rapid adaptation. Finally, residual networks formalized the utility of residual connections, motivating analysis of how activation classes behave under residual compositions. Together, these works revealed a clear opportunity: rational activations offer the right expressive family for adaptive neurons, but they require principled regularization and compatibility with residual architectures to avoid instability and overfitting. The current paper synthesizes these insights by introducing jointly-parameterized rational activations that share coefficients across layers for natural regularization, and by deriving specific closure conditions under residual connections, thereby operationalizing neuron-level plasticity in deep RL without the complexity of explicit synaptic plasticity rules.

---

*Analysis generated on: 2026-01-07T00:12:47.812590*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
