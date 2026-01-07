# Prior Work Analysis Report

## Target Paper

**Title:** Implicit Bias of Mirror Flow for Shallow Neural Networks in Univariate Regression

**Conference:** ICLR 2025 (spotlight)

**Authors:** Shuang Liang, Guido Montufar

**Keywords:** implicit bias, overparametrized neural network, mirror descent, univariate regression, lazy training

**Abstract:** 
> We examine the implicit bias of mirror flow in least squares error regression with wide and shallow neural networks. For a broad class of potential functions, we show that mirror flow exhibits lazy training and has the same implicit bias as ordinary gradient flow when the network width tends to infinity. For univariate ReLU networks, we characterize this bias through a variational problem in function space. Our analysis includes prior results for ordinary gradient flow as a special case and lift...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**A Variational Perspective on Accelerated Methods** (2016)
- *Authors:* Wibisono et al.
- *Direct Connection:* This work formalized mirror flow via Bregman geometry induced by a potential, providing the continuous-time mirror-descent framework the paper adopts to analyze implicit bias under general potentials and to define the new class of scaled potentials.

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Jacot et al.
- *Direct Connection:* The NTK linearization yields the RKHS bias of infinite-width gradient flow, which the paper extends by proving that mirror flow has the same infinite-width implicit bias and by pinpointing when scaled potentials depart from the NTK regime.

**Breaking the Curse of Dimensionality with Convex Neural Networks** (2017)
- *Authors:* Bach
- *Direct Connection:* The measure/variation-norm representation for two-layer ReLU networks underlies the paper’s function-space variational characterization of the implicit bias for univariate networks (including absolute value activations).

**A Function Space View of Bounded Variation Regularization in Deep Learning** (2019)
- *Authors:* Ongie et al.
- *Direct Connection:* By linking shallow ReLU networks to linear splines and BV-type seminorms, this work provides the specific spline/variational machinery the paper leverages to characterize the implicit bias of univariate ReLU networks trained by mirror flow.

### 🔍 Gap Identification

**On Lazy Training in Differentiable Programming** (2019)
- *Authors:* Chizat and Bach
- *Direct Connection:* By identifying the lazy (kernel) regime and its scaling conditions for gradient flow, this work motivates the paper’s extension showing mirror flow is also lazy for broad potentials and highlights the gap the paper fills with a lazy-but-non-kernel regime via scaled potentials.

**Near-Interpolating Splines via Two-Layer ReLU Networks: Trend Filtering Connections** (2019)
- *Authors:* Parhi and Nowak
- *Direct Connection:* Their characterization of univariate ReLU fits through trend-filtering–style variational problems required data adjustments or architectural tweaks (e.g., skip connections), a limitation the paper explicitly removes by giving a direct variational bias characterization for standard univariate networks.

### 🔧 Extension

**Wide Neural Networks of Any Depth Evolve as Linear Models Under Gradient Descent** (2019)
- *Authors:* Lee et al.
- *Direct Connection:* Their function-space equivalence between infinite-width gradient descent and kernel gradient flow is the baseline equivalence the paper generalizes to mirror flow to establish identical implicit bias at infinite width.

---

## Synthesis: How Prior Work Led to This Paper

Mirror flow arises as the continuous-time limit of mirror descent defined by Bregman geometry from a potential, as formalized by Wibisono et al., making it natural to study optimization-induced bias through the choice of potential. The neural tangent kernel framework of Jacot et al. established that infinite-width gradient flow linearizes dynamics and induces an RKHS bias, while Lee et al. showed this equivalently as kernel gradient flow in function space for wide networks. Chizat and Bach identified the lazy regime and the scaling conditions that keep training near initialization, delineating when such kernel dynamics prevail. On the function-space side, Bach’s measure-based representation of two-layer ReLU networks and the associated variation norms, together with Ongie et al.’s linear-spline/BV perspective, supplied precise variational tools linking shallow ReLU networks to spline minimization. Parallel work connecting univariate ReLU regression to trend filtering (e.g., Parhi and Nowak) offered variational characterizations but often relied on data adjustments or skip connections to make the analysis tractable. Taken together, these strands suggested that both the optimization geometry (mirror maps/potentials) and width scaling govern whether training is lazy and which function-space norm is implicitly minimized. The paper synthesizes these ideas by proving that mirror flow—across broad potentials—exhibits lazy training and shares gradient flow’s RKHS bias at infinite width, then introducing scaled potentials that retain laziness yet move beyond NTK. Leveraging spline/BV representations, it gives a direct variational characterization for univariate ReLU and shows absolute-value activations yield implicit biases not captured by any RKHS, thereby resolving prior limitations and expanding the controllable bias landscape via potentials.

---

*Analysis generated on: 2026-01-06T08:05:27.830671*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
