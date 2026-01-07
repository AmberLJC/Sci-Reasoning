# Prior Work Analysis Report

## Target Paper

**Title:** SGD Finds then Tunes Features in Two-Layer Neural Networks with near-Optimal Sample Complexity: A Case Study in the XOR problem

**Conference:** ICLR 2024 (spotlight)

**Authors:** Margalit Glasgow

**Keywords:** optimization, stochastic gradient descent, two-layer neural network, sample complexity

**Abstract:** 
> In this work, we consider the optimization process of minibatch stochastic gradient descent (SGD) on a 2-layer neural network with data separated by a quadratic ground truth function. We prove that with data drawn from the Boolean hypercube labeled by the quadratic ``XOR'' function $y = -x_ix_j$ , it is possible to train to a population error $o(1)$
 with $\Theta(d\text{polylog}(d))$ samples. Our result considers simultaneously training both layers of the two-layer-neural network with ReLU activ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Implicit Bias of Gradient Descent on Separable Data** (2018)
- *Authors:* Daniel Soudry et al.
- *Direct Connection:* This establishes that gradient descent on logistic loss converges directionally to max-margin classifiers on separable data, providing the foundational tool to characterize the tuning/balancing dynamics once XOR features render the problem separable.

### 💡 Inspiration

**On Lazy Training in Differentiable Programming** (2019)
- *Authors:* Lénaïc Chizat et al.
- *Direct Connection:* This work formalizes the lazy vs feature-learning regimes and conditions for significant parameter movement, inspiring the paper’s two-phase view where neurons first move non-lazily to find features before entering a tuning phase.

**Kernel and Rich Regimes in Overparameterized Models** (2020)
- *Authors:* Blake Woodworth et al.
- *Direct Connection:* By delineating kernel (lazy) versus rich (feature-learning) regimes and their learnability implications, this work motivates operating in (and analyzing) a rich regime necessary to capture XOR beyond NTK limitations.

### 🔍 Gap Identification

**On the Power and Limitations of Random Features for Learning** (2019)
- *Authors:* Sivan Yehudai et al.
- *Direct Connection:* They prove that random-features/NTK-style training cannot learn parity/XOR under isotropic distributions with polynomial resources, directly motivating a feature-learning (non-lazy) analysis to overcome this barrier.

### 🔧 Extension

**Gradient Descent Maximizes the Margin of Homogeneous Neural Networks** (2019)
- *Authors:* Kaifeng Lyu et al.
- *Direct Connection:* Their directional convergence and layer-balancing results for homogeneous networks under logistic loss are extended to the signal-heavy phase to show SGD maintains and balances the discovered XOR features.

### 🔗 Related Problem

**Gradient Descent Learns One-Hidden-Layer Convolutional Neural Networks** (2018)
- *Authors:* Simon S. Du et al.
- *Direct Connection:* Their analysis showing neurons specialize and evolve (approximately) independently from random initialization informs the signal-finding phase where many neurons independently align to the quadratic (pairwise) XOR features.

---

## Synthesis: How Prior Work Led to This Paper

Random-features and NTK analyses have shown stark limits for learning simple but non-linear interactions like parity/XOR: Yehudai and Shamir proved that with isotropic inputs, such kernelized approaches cannot succeed with polynomial resources, making explicit that learning must rely on feature movement rather than fixed features. Chizat, Oyallon, and Bach formalized the lazy versus feature-learning dichotomy, identifying when parameters undergo significant motion and thus can create new features, laying conceptual groundwork for a phase-based view of training dynamics. In parallel, the implicit-bias literature for logistic loss provides precise descriptions of the tuning dynamics once data become separable: Soudry et al. established directional convergence to max-margin classifiers, and Lyu and Li extended this to deep homogeneous networks, showing margin maximization accompanied by inter-layer weight balancing. Complementing these, Woodworth et al. delineated kernel versus rich regimes in overparameterized models, underscoring that rich (feature-learning) dynamics are essential for tasks beyond kernels. Finally, Du et al. demonstrated in a related shallow setting that neurons can specialize and evolve largely independently from random initialization, a mechanism that supports feature discovery.

Taken together, these works expose both the necessity and the mechanism of feature learning to overcome NTK barriers on XOR, and they provide the tools to analyze what happens after features are found. The rich/lazy dichotomy and neuron specialization insights suggest an initial feature-finding phase where many units independently latch onto pairwise interactions, while the implicit-bias results for logistic loss naturally describe a subsequent signal-heavy phase that tunes and balances those features. This synthesis enables a rigorous two-phase analysis showing that standard minibatch SGD on a standard two-layer ReLU network can learn XOR with near-optimal sample complexity.

---

*Analysis generated on: 2026-01-06T15:48:23.393402*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
