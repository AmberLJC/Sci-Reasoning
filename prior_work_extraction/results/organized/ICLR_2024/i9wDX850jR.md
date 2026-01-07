# Prior Work Analysis Report

## Target Paper

**Title:** Feature emergence via margin maximization: case studies in algebraic tasks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Depen Morwani, Benjamin L. Edelman, Costin-Andrei Oncescu, Rosie Zhao, Sham M. Kakade

**Keywords:** inductive bias, margin maximization, feature learning, mechanistic interpretability

**Abstract:** 
> Understanding the internal representations learned by neural networks is a cornerstone challenge in the science of machine learning. While there have been significant recent strides in some cases towards understanding *how* neural networks implement specific target functions, this paper explores a complementary question -- *why* do networks arrive at particular computational strategies? 
Our inquiry focuses on the algebraic learning tasks of modular addition, sparse parities, and finite group op...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Implicit Bias of Gradient Descent on Separable Data** (2018)
- *Authors:* Soudry et al.
- *Direct Connection:* This work established that gradient descent on logistic loss converges in direction to the max-margin classifier, providing the core margin-maximization principle the present paper leverages to characterize learned features.

**Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets** (2022)
- *Authors:* Power et al.
- *Direct Connection:* This work introduced modular addition as a canonical algorithmic task and highlighted puzzling circuit choices during grokking, setting the problem context the present paper analyzes normatively.

### 💡 Inspiration

**Implicit Bias of Gradient Descent on Linear Convolutional Networks** (2018)
- *Authors:* Gunasekar et al.
- *Direct Connection:* This paper connects implicit bias to Fourier-domain structure in linear conv nets, directly motivating the present work’s use of Fourier features as the max-margin-selected representation for modular addition.

### 🔍 Gap Identification

**Progress Measures for Grokking via Mechanistic Interpretability** (2023)
- *Authors:* Nanda et al.
- *Direct Connection:* By empirically showing that networks implement modular addition via Fourier-phase features while lacking a principled ‘why,’ this work posed the gap the present paper fills with a margin-based explanation.

### 🔧 Extension

**Gradient Descent Maximizes the Margin of Homogeneous Neural Networks** (2019)
- *Authors:* Lyu and Li
- *Direct Connection:* By extending max-margin implicit bias to deep homogeneous networks trained with exponential-tailed losses, this paper enables the present work to apply margin-based feature selection arguments to the stylized neural architectures it analyzes.

### 🔗 Related Problem

**Group Equivariant Convolutional Networks** (2016)
- *Authors:* Cohen and Welling
- *Direct Connection:* This paper established irreducible group representations as the natural feature basis for group-structured data, which the present work shows emerge even without built-in equivariance via margin maximization.

---

## Synthesis: How Prior Work Led to This Paper

Soudry et al. formalized that, on separable data, gradient descent with logistic loss converges to the maximum-margin direction, identifying margin maximization as the operative inductive bias of training. Lyu and Li extended this principle to deep homogeneous networks trained with exponential-tailed losses, ensuring that margin arguments apply beyond linear models to the kinds of neural architectures typically used for feature learning. Gunasekar et al. connected implicit bias to analysis in the Fourier domain for linear convolutional networks, demonstrating that gradient descent prefers margin-maximizing solutions structured in frequency space. Power et al. introduced modular addition as a compact algorithmic task central to grokking studies, making it a standard benchmark for probing how networks implement algebraic computations. Nanda et al. then provided mechanistic evidence that trained models solve modular addition via Fourier-phase features, but left open a normative account of why those features are chosen among many possibilities. Complementarily, Cohen and Welling showed that irreducible representations form the canonical feature basis for group-structured problems, linking group theory to neural representations. Taken together, these works suggest a natural synthesis: if gradient-based training implicitly maximizes margin, and algebraic tasks admit canonical Fourier/irrep bases, then margin considerations should select those bases even without built-in equivariance or hand-crafted features. The present paper operationalizes this insight by proving that margin maximization alone fully specifies the emergent features on modular addition, sparse parities, and finite group operations—recovering Fourier features and irreps as the margin-optimal representations.

---

*Analysis generated on: 2026-01-06T17:07:54.686051*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
