# Prior Work Analysis Report

## Target Paper

**Title:** Towards Marginal Fairness Sliced Wasserstein Barycenter

**Conference:** ICLR 2025 (spotlight)

**Authors:** Khai Nguyen, Hai Nguyen, Nhat Ho

**Keywords:** Sliced Wasserstein Barycenter, Optimal Transport, Sliced Wasserstein, Averaging Measures.

**Abstract:** 
> The Sliced Wasserstein barycenter (SWB) is a widely acknowledged method for efficiently generalizing the averaging operation within probability measure spaces. However, achieving marginal fairness SWB, ensuring approximately equal distances from the barycenter to marginals, remains unexplored. The uniform weighted SWB is not necessarily the optimal choice to obtain the desired marginal fairness barycenter due to the heterogeneous structure of marginals and the non-optimality of the optimization....

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Barycenters in the Wasserstein space** (2011)
- *Authors:* M. Agueh et al.
- *Direct Connection:* This paper formalized Wasserstein barycenters as minimizers of weighted sums of W2 distances, which the present work constrains (in the sliced setting) to equalize barycenter-to-marginal distances for marginal fairness.

### 💡 Inspiration

**Max-Sliced Wasserstein Distance** (2019)
- *Authors:* I. Deshpande et al.
- *Direct Connection:* Their maximization over projection directions demonstrates that learned slicing directions enhance discriminative power and sample efficiency, directly inspiring the paper’s slicing distribution selection to speed up fairness-aware SW barycenter computation.

### 🔍 Gap Identification

**Trimmed Barycenters of Probability Measures** (2016)
- *Authors:* J. Álvarez-Esteban et al.
- *Direct Connection:* By revealing that heterogeneity and outliers bias barycenters and proposing trimming (with a tuning parameter) for robustness, this paper highlights the gap that the current work fills with hyperparameter-free surrogates targeting equalized barycenter-to-marginal distances.

### 📊 Baseline

**Sliced and Radon Wasserstein Barycenters of Measures** (2015)
- *Authors:* N. Bonneel et al.
- *Direct Connection:* They introduced the practical computation of sliced Wasserstein barycenters via averaging 1D barycenters over random projections, the very baseline whose uniform weighting is revisited here to enforce approximately equal distances to all marginals.

### 🔧 Extension

**Distributional Sliced Wasserstein** (2022)
- *Authors:* K. Nguyen et al.
- *Direct Connection:* This work proposes learning a distribution over projections rather than using fixed random slices, an idea the current paper extends by selecting slicing distributions to accelerate its surrogate marginal-fairness SW barycenter objectives.

### 🔗 Related Problem

**Generalized Sliced Wasserstein Distances** (2019)
- *Authors:* S. Kolouri et al.
- *Direct Connection:* By showing that altering the slicing transform (generalized Radon) changes the induced geometry and performance, this work motivates the idea that selecting appropriate slicing distributions can improve efficiency and fidelity of sliced OT-based barycenter objectives.

---

## Synthesis: How Prior Work Led to This Paper

Wasserstein barycenters were formalized as minimizers of weighted sums of Wasserstein distances, establishing the geometric notion of an average measure in optimal transport (Agueh and Carlier). To make this tractable, sliced variants compute barycenters by projecting measures onto lines, solving 1D problems, and averaging over projections, yielding an efficient computational baseline (Bonneel et al.). Subsequent advances showed that the slicing mechanism itself shapes behavior: generalized slicing via alternative Radon transforms alters the geometry and quality of sliced OT estimates (Kolouri et al.). Beyond fixed random projections, optimizing projection directions can markedly improve discrimination and sample efficiency, as evidenced by max-sliced Wasserstein distances (Deshpande et al.). Pushing this further, learning a distribution over projections reduces variance and accelerates sliced OT computations (Nguyen et al.), indicating that projection selection is a powerful lever. Parallel work on robustness exposed that heterogeneous marginals can skew barycenters and proposed trimming to mitigate outliers, albeit at the cost of tuning hyperparameters (Álvarez-Esteban et al.). Together, these strands surfaced a gap: the standard (uniform-weight) sliced barycenter can be inefficient and can yield uneven barycenter-to-marginal distances under heterogeneity. The natural next step is to explicitly target marginal-distance fairness within the sliced framework and to leverage learned slicing distributions for efficiency. The paper synthesizes these insights by casting fairness as a constrained SWB problem and introducing hyperparameter-free surrogate objectives, while adopting slicing distribution selection to achieve practical, efficient computation.

---

*Analysis generated on: 2026-01-06T20:05:36.629956*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
