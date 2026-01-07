# Prior Work Analysis Report

## Target Paper
**Title:** 4HQaMUYWAT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Connection:* The paper’s theory explicitly leverages the small-initialization (linearized/NTK) training dynamics to explain why tiny scales bias models toward structured, algorithmic solutions rather than rote memorization.

**Training Behavior of Deep Neural Networks: The Frequency Principle (F-Principle)** (2019)
- *Authors:* Zhi-Qin John Xu et al.
- *Connection:* The frequency-principle framework underpins the paper’s training-dynamics explanation, connecting small-norm initialization to early learning of low-frequency/global structure that manifests as reasoning behavior.

### 💡 Inspiration

**On the Spectral Bias of Neural Networks** (2019)
- *Authors:* Nazmul Karim Rahaman et al.
- *Connection:* By showing that neural nets learn low-frequency components before high-frequency ones, this work directly motivates the paper’s use of controlled ‘anchor’ target functions to probe reasoning versus memorization under different init scales.

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Mor Geva et al.
- *Connection:* Identifying FFNs as a learned associative memory directly informs the paper’s claim that larger initializations favor memorization pathways (FFN/embedding-driven) over reasoning.

**In-Context Learning and Induction Heads** (2022)
- *Authors:* Catherine Olsson et al.
- *Connection:* The discovery of induction-head circuits provides the mechanism the paper tests for: small initialization expedites the emergence of attention-based algorithmic reasoning relative to memory-based solutions.

### 🔍 Gap Identification

**Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets** (2022)
- *Authors:* A. Power et al.
- *Connection:* Grokking exposed a memorization-to-reasoning transition but did not explain the role of initialization; the present work fills this gap by showing initialization scale systematically controls that preference and dynamics in LLMs.

### 🔧 Extension

**On the Global Convergence of Gradient Descent for Over-Parameterized Models: A Dynamical System Viewpoint** (2018)
- *Authors:* Lénaïc Chizat et al.
- *Connection:* This work formalized the lazy-vs-feature-learning regimes governed by initialization scale; the current paper extends this lens to transformers, linking small-scale (lazy-like) training to reasoning bias and large-scale to memorization.

---

## Synthesis

The core innovation—showing that initialization scale steers LLMs toward reasoning versus memorization and explaining it via early training dynamics—rests on two intertwined theoretical lineages and a mechanistic account of transformer internals. From the theory side, the NTK framework (Jacot et al.) and the lazy/feature-learning dichotomy governed by initialization (Chizat & Bach) provide the central lens: small initialization keeps training near the linearized regime, whereas larger scales encourage stronger feature evolution. This connects directly to frequency-based accounts of learning (Xu’s F-Principle and Rahaman’s spectral bias), which predict that networks initialized with small norms preferentially learn low-frequency, global structure before high-frequency details, mirroring the paper’s definition of “reasoning” versus “memorization.” On the mechanistic side, transformer interpretability works anchor the pathways: Geva et al. show FFNs and embeddings act as key–value memories, while Olsson et al. identify induction heads as attention circuits for algorithmic pattern-following. These map naturally onto the paper’s component-wise analysis, attributing memorization to FFN/embedding mechanisms and reasoning to self-attention circuits. Finally, the grokking literature (Power et al.) highlighted a memorization-to-generalization transition but left the role of initialization unresolved; this paper resolves that gap by demonstrating, with anchor functions and real tasks, that initialization scale is a primary control knob and by giving a training-dynamics theory that ties component behavior to the observed bias.

---
*Generated: 2026-01-06T23:07:19.633772*
