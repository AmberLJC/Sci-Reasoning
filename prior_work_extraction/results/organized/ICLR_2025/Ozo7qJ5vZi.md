# Prior Work Analysis Report

## Target Paper

**Title:** KAN: Kolmogorov–Arnold Networks

**Conference:** ICLR 2025 (oral)

**Authors:** Ziming Liu, Yixuan Wang, Sachin Vaidya, Fabian Ruehle, James Halverson, Marin Soljacic, Thomas Y. Hou, Max Tegmark

**Keywords:** Kolmogorov-Arnold networks, Kolmogorov-Arnold representation theorem, learnable activation functions, interpretability, AI + Science

**Abstract:** 
> Inspired by the Kolmogorov-Arnold representation theorem, we propose Kolmogorov-Arnold Networks (KANs) as promising alternatives to Multi-Layer Perceptrons (MLPs). While MLPs have fixed activation functions on nodes ("neurons''), KANs have learnable activation functions on edges ("weights''). KANs have no linear weights at all -- every weight parameter is replaced by a univariate function parametrized as a spline. We show that this seemingly simple change makes KANs outperform MLPs in terms of a...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**On the representation of continuous functions of several variables by superposition of continuous functions of one variable and addition** (1957)
- *Authors:* Andrey N. Kolmogorov
- *Direct Connection:* KAN’s edge-wise learnable univariate functions are a direct architectural instantiation of Kolmogorov’s superposition theorem, which guarantees that any multivariate continuous function can be expressed via sums and compositions of univariate functions.

**On functions of three variables** (1957)
- *Authors:* Vladimir I. Arnold
- *Direct Connection:* Arnold’s strengthening of Kolmogorov’s result into a concrete two-stage superposition (sums of univariate functions of affine combinations of univariate functions) informs KAN’s repeating motif of summation plus univariate transformation across layers.

### 💡 Inspiration

**Kolmogorov's mapping neural network existence theorem** (1987)
- *Authors:* Robert Hecht-Nielsen
- *Direct Connection:* By explicitly mapping the Kolmogorov–Arnold representation to a three-layer neural network with univariate nonlinearities, this work provided the blueprint that KAN realizes by making those univariate components trainable spline functions on edges rather than fixed node activations.

**Neural Additive Models: Interpretable Machine Learning with Neural Nets** (2021)
- *Authors:* Agarwal et al.
- *Direct Connection:* NAMs operationalized learnable univariate shape functions with neural networks; KAN borrows this learnable shape-function paradigm and extends it to every edge in a deep architecture to implement the Kolmogorov–Arnold superposition with enhanced interpretability.

### 🔍 Gap Identification

**AI Feynman: A physics-inspired method for symbolic regression** (2020)
- *Authors:* Silviu-Marian Udrescu et al.
- *Direct Connection:* AI Feynman showed the value of interpretable functional structure for scientific discovery but relies on combinatorial symbolic search, motivating KAN’s gradient-based, human-interpretable univariate components that can aid equation rediscovery without explicit symbolic enumeration.

### 🔧 Extension

**Neural Spline Flows** (2019)
- *Authors:* Conor Durkan et al.
- *Direct Connection:* This work demonstrated stable, backprop-trainable spline parameterizations for expressive univariate transformations, which KAN leverages by parameterizing each edge function as a spline to obtain smooth, flexible, and interpretable 1D mappings.

### 🔗 Related Problem

**Generalized Additive Models** (1986)
- *Authors:* Trevor Hastie et al.
- *Direct Connection:* GAMs introduced interpretable feature-wise univariate “shape functions” combined additively, an idea KAN generalizes from shallow additive models to deep compositions of per-edge shape functions to preserve interpretability while increasing expressivity.

---

## Synthesis: How Prior Work Led to This Paper

Kolmogorov demonstrated that any continuous multivariate function can be represented via sums and compositions of univariate functions, and Arnold’s companion result sharpened this into a concrete two-stage superposition involving sums of univariate functions of affine combinations of univariate functions. Hecht-Nielsen then mapped these representation-theoretic insights onto a neural architecture, showing that a small number of layers with univariate nonlinearities suffice in principle to realize Kolmogorov–Arnold superpositions. In parallel, generalized additive models introduced interpretable modeling through feature-wise univariate “shape functions” summed additively, and Neural Additive Models updated this idea by learning flexible shape functions with neural networks while preserving interpretability. On the parametrization side, Neural Spline Flows provided a practical recipe to represent and train expressive univariate functions using splines via backpropagation, yielding smooth and stable transformations. Finally, AI Feynman highlighted the scientific value of explicit functional structure and interpretability for rediscovering equations, while exposing the brittleness and search costs of symbolic approaches.
Together, these works suggested a path: instantiate the Kolmogorov–Arnold superposition within a trainable neural architecture by replacing linear weights with learnable univariate shape functions, parameterized with splines for stability, and arranged across layers to move beyond shallow additivity toward deep compositions. This synthesis preserves GAM/NAM-style interpretability, leverages spline-based trainability, and answers AI Feynman’s search burden with continuous, gradient-based learning—yielding a natural next step: a network whose edges are univariate functions embodying the Kolmogorov–Arnold idea.

---

*Analysis generated on: 2026-01-06T17:56:29.133271*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
