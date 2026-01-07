# Prior Work Analysis Report

## Target Paper
**Title:** aTBwCSkPxv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Exact solutions to the nonlinear dynamics of learning in deep linear neural networks** (2013)
- *Authors:* Saxe et al.
- *Connection:* This paper established the gradient-flow viewpoint and core conserved quantities in deep linear networks, providing the template the present work generalizes to convolutional blocks, residual blocks, and attention.

**Deep Residual Learning for Image Recognition** (2016)
- *Authors:* He et al.
- *Connection:* Introduced residual blocks and skip connections; the current paper’s key finding—that residual blocks share the same conservation laws as their non-residual counterparts—relies on this architectural formulation.

**Attention Is All You Need** (2017)
- *Authors:* Vaswani et al.
- *Connection:* Defines the single attention layer architecture whose gradient-flow conservation laws are completely characterized in the present work.

### 💡 Inspiration

**Path-SGD: Path-Normalized Optimization in Deep Neural Networks** (2015)
- *Authors:* Neyshabur et al.
- *Connection:* By exploiting rescaling symmetries in positively homogeneous ReLU networks, this work highlighted invariants tied to paths/units, directly inspiring the present paper’s systematic characterization of all conservation laws for shallow ReLU blocks and their blockwise generalization.

### 🔍 Gap Identification

**On the Global Convergence of Gradient Descent for Over-parameterized Models: Beyond Neural Tangent Kernel** (2018)
- *Authors:* Chizat and Bach
- *Connection:* This work formalized positive homogeneity and scaling symmetries that underlie conservation laws in ReLU networks but did not address convolution, residual connections, or attention, motivating the present paper’s extension of conservation principles to practical architectures.

### 📊 Baseline

**Implicit Regularization in Matrix Factorization** (2017)
- *Authors:* Gunasekar et al.
- *Connection:* By identifying conserved Gram-difference quantities (e.g., UᵀU − V Vᵀ) under gradient flow in (deep) matrix factorization, it serves as the baseline conservation-law characterization that this work extends to convolutions and modern blocks and reframes at the block/subset-of-parameters level.

---

## Synthesis

The core innovation of this paper—systematically deriving and classifying conservation laws for practical deep architectures (convolutional blocks, residual blocks, and attention), and introducing conservation laws that depend only on subsets of parameters—rests on a clear lineage. Saxe et al. provided the foundational gradient-flow framing and explicit invariants for deep linear networks, establishing the analytical paradigm the present work generalizes. Gunasekar et al. then crystallized conservation laws in matrix factorization via preserved Gram-difference quantities under gradient flow; these serve as the baseline invariant structures that this paper extends to convolutional operators and leverages in multi-layer settings. Chizat and Bach formalized the role of positive homogeneity and rescaling symmetries in ReLU models, making explicit the structural reasons invariants arise—yet stopping short of treating modern blocks like convolution, residual connections, or attention; that gap directly motivates this paper’s architectural generality. Neyshabur et al.’s Path-SGD operationalized rescaling invariances in ReLU networks, inspiring the present work’s precise, exhaustive characterization of all conservation laws for shallow ReLU blocks and the notion of blockwise (subset-of-parameters) invariants. Finally, the architectural formulations of residual networks (He et al.) and transformers (Vaswani et al.) provide the concrete blocks the paper analyzes: it shows residual skips do not alter the conservation laws of their underlying blocks and gives a complete description of conservation laws for a single attention layer. Together, these works directly enable and motivate the paper’s unified conservation-law framework for modern deep architectures.

---
*Generated: 2026-01-06T23:07:19.580642*
