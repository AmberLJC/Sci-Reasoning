# Prior Work Analysis Report

## Target Paper

**Title:** Generalization of Scaled Deep ResNets in the Mean-Field Regime

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yihang Chen, Fanghui Liu, Yiping Lu, Grigorios Chrysos, Volkan Cevher

**Keywords:** ResNet, mean field, generalization, Rademacher complexity

**Abstract:** 
> Despite the widespread empirical success of ResNet, the generalization properties of deep ResNet are rarely explored beyond the lazy training regime. In this work, we investigate scaled ResNet in the limit of infinitely deep and wide neural networks, of which the gradient flow is described by a partial differential equation in the large-neural network limit, i.e., the mean-field regime. To derive the generalization bounds under this setting, our analysis necessitates a shift from the conventiona...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport** (2018)
- *Authors:* Lénaïc Chizat et al.
- *Direct Connection:* It formulates training as a Wasserstein gradient flow over parameter distributions and clarifies the mean-field (feature-learning) scaling, which we adopt to model scaled-ResNet dynamics beyond the lazy regime.

**Mean Field Analysis of Neural Networks: A Law of Large Numbers** (2020)
- *Authors:* Justin Sirignano et al.
- *Direct Connection:* This paper derives the PDE governing the evolution of the parameter distribution under gradient flow, which we leverage to characterize the infinite-width/depth scaled-ResNet training dynamics in the mean-field limit.

**Tensor Programs V: Tuning Wide Neural Networks via μ-Parametrization** (2021)
- *Authors:* Greg Yang
- *Direct Connection:* This work formalizes parameter scalings that interpolate between NTK and mean-field regimes (including for ResNets), providing the precise scaled-ResNet parameterization under which our mean-field generalization analysis operates.

### 🔍 Gap Identification

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Direct Connection:* By establishing a time-invariant Gram/NTK in the lazy regime, this work exposes the limitation that motivates our shift to a time-varying, distribution-dependent Gram needed to analyze feature-learning in the mean-field regime.

**A Convergence Theory for Deep Learning via Over-Parameterization** (2019)
- *Authors:* Zeyuan Allen-Zhu et al.
- *Direct Connection:* By proving lower bounds on the minimum eigenvalue of a time-invariant Gram matrix for deep ResNets in the lazy regime, this work highlights the gap we close with a global eigenvalue lower bound for a time-varying, distribution-dependent Gram in the mean-field setting.

### 🔧 Extension

**Mean-field theory of two-layer neural networks: global convergence and generalization** (2018)
- *Authors:* Song Mei et al.
- *Direct Connection:* Their distribution-dependent kernel and convergence analysis in the two-layer mean-field regime directly seed our extension to deep ResNets, including linear empirical-error decay and KL-divergence control along training.

---

## Synthesis: How Prior Work Led to This Paper

A central thread begins with the neural tangent kernel, which shows that in the lazy regime the Gram matrix becomes time-invariant and training behaves like kernel regression. While powerful, this viewpoint freezes features and relies on a fixed kernel. In contrast, optimal-transport mean-field analyses recast training as a Wasserstein gradient flow over parameter distributions and delineate scalings that enable genuine feature learning. Building on this, a law-of-large-numbers limit characterizes the evolution of parameter distributions via a PDE, furnishing the analytic machinery to track dynamics in infinite-width limits. For shallow networks, mean-field theory further introduces a distribution-dependent, time-varying kernel and establishes convergence and generalization behavior, offering templates for controlling empirical error and measure dynamics. Complementing these, over-parameterization results for deep ResNets prove lower bounds on the minimum eigenvalue of a time-invariant Gram, guaranteeing optimization but only in the lazy regime. Finally, μ-parameterization prescribes precise scalings that interpolate between NTK and mean-field and apply to ResNets, ensuring well-posed wide-and-deep feature-learning dynamics.
Together, these works expose a gap: deep ResNets lack generalization guarantees in the mean-field regime where features evolve and the Gram matrix becomes distribution- and time-dependent. The combination of PDE-based measure dynamics, distribution-dependent kernels, and scaling prescriptions for ResNets naturally leads to analyzing scaled ResNets under mean-field gradient flow, proving global lower bounds for the evolving Gram, tracking KL divergence to control measure drift, and deriving uniform convergence via Rademacher complexity—thereby extending kernel-era optimization guarantees to feature-learning, infinitely deep and wide residual networks.

---

*Analysis generated on: 2026-01-06T11:57:26.674639*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
