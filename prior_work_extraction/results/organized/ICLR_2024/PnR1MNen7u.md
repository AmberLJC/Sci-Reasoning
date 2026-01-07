# Prior Work Analysis Report

## Target Paper

**Title:** Deep Geodesic Canonical Correlation Analysis for Covariance-Based Neuroimaging Data

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ce Ju, Reinmar J Kobler, Liyao Tang, Cuntai Guan, Motoaki Kawanabe

**Keywords:** Geometric Deep Learning, Self-Supervised Learning, Brain-Computer Interfaces, Neuroimaging, Neuroscience

**Abstract:** 
> In human neuroimaging, multi-modal imaging techniques are frequently combined to enhance our comprehension of whole-brain dynamics and improve diagnosis in clinical practice. Modalities like electroencephalography and functional magnetic resonance imaging provide distinct views to the brain dynamics due to diametral spatiotemporal sensitivities and underlying neurophysiological coupling mechanisms. These distinct views pose a considerable challenge to learning a shared representation space, espe...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Deep Canonical Correlation Analysis** (2013)
- *Authors:* Galen Andrew et al.
- *Direct Connection:* This work formalized maximizing canonical correlations between nonlinear projections as a learning objective, which the present paper generalizes from Euclidean correlation to an intrinsic geodesic correlation tailored to SPD-valued covariance data.

**A Riemannian framework for tensor computing** (2006)
- *Authors:* Xavier Pennec et al.
- *Direct Connection:* This paper introduced the affine-invariant Riemannian metric and geodesic structure on SPD manifolds, providing the mathematical basis for defining and computing the proposed geodesic correlation between covariance representations.

### 💡 Inspiration

**Deep Canonically Correlated Autoencoders** (2015)
- *Authors:* Weiran Wang et al.
- *Direct Connection:* By coupling a CCA-style alignment loss with self-supervised reconstruction, this paper established correlation consistency as a powerful self-supervision signal that directly motivates adopting a CCA-derived (here, geodesic) correlation for multi-view covariance data.

**A Riemannian Network for SPD Matrices** (2017)
- *Authors:* Zhiwu Huang and Luc Van Gool
- *Direct Connection:* By showing that deep models can operate natively on SPD manifolds with geometry-preserving layers, this work inspired the paper’s geometry-aware treatment of covariance data and the need for manifold-consistent alignment objectives.

### 🔍 Gap Identification

**Log-Euclidean metrics for fast and simple calculus on diffusion tensors** (2006)
- *Authors:* Vincent Arsigny et al.
- *Direct Connection:* The common practice of flattening SPD data via log-Euclidean/tangent-space mapping highlighted here motivates the present work’s intrinsic geodesic formulation by exposing the distortion and locality limits of Euclideanized correlation on manifold-valued covariances.

**Barlow Twins: Self-Supervised Learning via Redundancy Reduction** (2021)
- *Authors:* Jure Zbontar et al.
- *Direct Connection:* This method popularized correlation-based alignment for self-supervision in Euclidean spaces, whose limitation on manifold-valued covariances directly motivates replacing Euclidean cross-correlation with a geodesic correlation consistent with SPD geometry.

### 📊 Baseline

**Deep Generalized Canonical Correlation Analysis** (2017)
- *Authors:* Adrian Benton et al.
- *Direct Connection:* As the standard deep multiview extension of CCA, this method provides the primary Euclidean-space baseline that the paper extends by replacing Euclidean correlation with a geodesic correlation on the SPD manifold for multi-view neuroimaging covariances.

---

## Synthesis: How Prior Work Led to This Paper

Deep Canonical Correlation Analysis established learning by maximizing canonical correlations between nonlinear projections of paired views, and Deep Generalized CCA extended this to multiple views, cementing correlation consistency as a central multiview objective. Deep Canonically Correlated Autoencoders further showed that CCA-style alignment can serve as a self-supervised signal when combined with representation learning, strengthening the case for correlation-driven objectives beyond supervised settings. Parallelly, the Riemannian framework for tensor computing introduced the affine-invariant geometry and geodesics on the symmetric positive definite manifold, offering intrinsic tools to compare and align covariance representations. Log-Euclidean metrics provided a practical tangent-space alternative but also revealed the drawbacks of flattening SPD data, including distortions and locality, when one needs global, geometry-faithful comparisons. A Riemannian Network for SPD Matrices demonstrated that deep architectures can honor manifold structure end-to-end, underscoring the importance of geometry-aware objectives for SPD inputs. Finally, Barlow Twins highlighted the strength of correlation-based redundancy reduction in self-supervised learning, yet it operates strictly in Euclidean feature spaces. Together these works expose a clear opportunity: combine the proven multiview power of CCA-style correlation with the intrinsic geometry of SPD covariance data. The natural next step is to replace Euclidean correlation with a geodesic, CCA-derived measure that evaluates cross-view consistency directly on the SPD manifold, enabling multi-view self-supervised representation learning that respects covariance geometry without resorting to distorting tangent-space embeddings.

---

*Analysis generated on: 2026-01-06T12:41:19.567674*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
