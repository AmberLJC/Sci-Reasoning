# Prior Work Analysis Report

## Target Paper

**Title:** OPTIMAL ROBUST MEMORIZATION WITH RELU NEURAL NETWORKS

**Conference:** ICLR 2024 (spotlight)

**Authors:** Lijia Yu, Xiao-Shan Gao, Lijun Zhang

**Keywords:** Memorization, expressive power of network, optimal robust memorization, computation complexity, Lipschitz constant

**Abstract:** 
> Memorization with neural networks is to study the expressive power of neural networks to interpolate a finite classification data set, which is closely related to the generalizability of deep learning. However, the important problem of robust memorization has not been thoroughly studied. In this paper, several basic problems about robust memorization are solved. First, we prove that it is NP-hard to compute neural networks with certain simple structures, which are robust memorization. A network ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Expressive Power of Neural Networks: A View from the Width** (2017)
- *Authors:* Zhou Lu et al.
- *Direct Connection:* Its width-based expressivity results (e.g., minimal width n+1 phenomena for nontrivial functions) underpin the paper’s lower-bound arguments on the network width required for optimal robust memorization in n dimensions.

**Approximating Continuous Functions by ReLU Nets of Minimal Width** (2017)
- *Authors:* Boris Hanin et al.
- *Direct Connection:* The minimal-width and topological constraints identified here are used as technical building blocks to derive the paper’s width lower bounds when robustness constraints are imposed.

**Training a 3-Node Neural Network is NP-Complete** (1993)
- *Authors:* Avrim Blum et al.
- *Direct Connection:* This classic NP-completeness template for training small neural networks is adapted to establish the paper’s NP-hardness results for computing ReLU networks that achieve robust memorization under structural constraints.

### 💡 Inspiration

**Spectrally-Normalized Margin Bounds for Neural Networks** (2017)
- *Authors:* Peter L. Bartlett et al.
- *Direct Connection:* By explicitly linking classifier margins and Lipschitz/spectral norms, this work motivates the paper’s use of Lipschitz control to certify robustness up to budgets tied to the data’s separation bound.

### 🔧 Extension

**Optimal Memorization with ReLU Neural Networks** (2023)
- *Authors:* Lijia Yu et al.
- *Direct Connection:* This prior work gave an explicit O(Nn)-parameter ReLU construction for exact (non-robust) memorization of any finite dataset, which the current paper directly extends by redesigning the construction to control Lipschitz constants and achieve optimal robust memorization.

### 🔗 Related Problem

**Certified Adversarial Robustness via Randomized Smoothing** (2019)
- *Authors:* Jeremy M. Cohen et al.
- *Direct Connection:* As a leading certification approach that formalizes robustness radii, it frames the robustness objective and highlights the gap that the paper fills by giving worst-case, constructive robust memorization up to half the separation bound without stochastic smoothing.

---

## Synthesis: How Prior Work Led to This Paper

Yu, Gao, and Zhang previously provided an explicit two-layer ReLU design with O(Nn) parameters that exactly interpolates any finite dataset, establishing constructive, size-optimal memorization without robustness guarantees. Lu et al. showed that width governs expressivity and identified fundamental minimal-width thresholds (on the order of the input dimension), while Hanin and Sellke refined minimal-width constraints and topological limitations for ReLU networks; together these width results delineate hard limits any construction must respect. Bartlett, Foster, and Telgarsky connected margins to Lipschitz/spectral control, formalizing how Lipschitz constants certify stability around data and paving the way to tie robust radii to geometric separation. Blum and Rivest’s NP-completeness proof for training small neural networks offers a reduction template demonstrating intrinsic computational intractability of certain training targets. Cohen, Rosenfeld, and Kolter’s randomized smoothing crystallized the notion of certified radii, highlighting certification goals but through stochastic means rather than exact worst-case constructions.

Against this backdrop, the synthesis was natural: explicit, size-optimal memorization constructions could, in principle, be upgraded to guarantee robustness if their Lipschitz properties were controlled relative to the dataset’s separation. The width limitations clarified what architectures could possibly achieve such guarantees, and classic NP-hardness templates suggested the right reductions to capture the computational barrier of robust memorization. The result is a constructive, parameter-efficient ReLU architecture that achieves robustness up to half the separation bound, alongside matching width lower bounds and NP-hardness results, closing the gap between memorization expressivity and certified robustness.

---

*Analysis generated on: 2026-01-06T12:18:59.226758*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
