# Prior Work Analysis Report

## Target Paper
**Title:** LwQGRGJTHw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Sampling algorithms for l2 regression and applications** (2006)
- *Authors:* Petros Drineas et al.
- *Connection:* This work introduced and analyzed row/column sampling sketches (including leverage-score sampling) that define the random sampling matrices whose inverses the current paper studies and corrects for inversion bias.

**Newton Sketch: A Linear-Time Optimization Algorithm with Linear-Quadratic Convergence** (2015)
- *Authors:* Mert Pilanci et al.
- *Connection:* It formalized second-order optimization via sketched Hessians, making the inverse of sketched matrices central; the present paper addresses the fundamental inversion bias that arises in such inverse Hessian approximations.

**Aspects of Multivariate Statistical Theory** (1982)
- *Authors:* R. J. Muirhead
- *Connection:* Classical Wishart/inverse-Wishart results from this monograph imply the simple scalar correction that removes inversion bias for Gaussian projections; the present paper generalizes beyond this special case to random sampling sketches.

### 💡 Inspiration

**Correcting inversion bias for sparse sub-Gaussian projections** (2024)
- *Authors:* Zhenyu Liao et al.
- *Connection:* This recent work identified and corrected inversion bias for sparse sub-Gaussian projection sketches; the current paper extends the bias-correction paradigm to the different and widely used class of random sampling matrices.

### 📊 Baseline

**Sub-sampled Newton Methods I: Globally Convergent Algorithms** (2016)
- *Authors:* Farbod Roosta-Khorasani et al.
- *Connection:* This paper established subsampled (row-sampled) Newton methods using random sampling of Hessian information; the current work directly targets the bias in inverting these sampled Hessians and provides corrections that improve SSN.

### 🔗 Related Problem

**Randomized Sketches of Convex Programs with Sharp Guarantees** (2016)
- *Authors:* Mert Pilanci et al.
- *Connection:* By introducing the (Iterative) Hessian Sketch framework and analyzing inverses of sketched normal matrices, it highlighted the centrality of sketched matrix inversion; the current paper explains and corrects the systematic inversion bias that those frameworks implicitly incur.

---

## Synthesis

The core of this paper is a principled characterization and correction of inversion bias for random sampling matrices, with concrete impact on sub-sampled Newton (SSN) methods. The lineage begins with the development of sampling-based sketches for least-squares and subspace embeddings by Drineas et al. (2006), which established leverage-score and related random sampling matrices now ubiquitous in RandNLA and optimization. In second-order optimization, Pilanci and Wainwright’s Newton Sketch (2015) and their broader convex-program sketching framework (2016) made the inverse of sketched Hessians a central computational primitive, creating a direct setting where inversion bias matters. Roosta-Khorasani and Mahoney’s SSN (2016) instantiated these ideas with explicit row-sampled Hessian approximations; the current paper treats SSN as a primary baseline and targets the bias that arises when inverting those sampled Hessians. On the theoretical side, Muirhead’s classic multivariate statistics results provide the exact inverse-Wishart expectation, explaining why Gaussian projections admit a simple scalar debiasing—an important special case that motivates searching for analogous corrections beyond Gaussian sketches. Most recently, Liao et al. (2024) showed how to correct inversion bias for sparse sub-Gaussian projection sketches; this identified the phenomenon and supplied a modern debiasing blueprint. The present paper directly extends that blueprint to the structurally different class of random sampling matrices, filling a key gap for methods like SSN that rely on sampling rather than projection.

---
*Generated: 2026-01-06T23:07:19.632884*
