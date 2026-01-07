# Prior Work Analysis Report

## Target Paper

**Title:** Analyzing Neural Scaling Laws in Two-Layer Networks with Power-Law Data Spectra

**Conference:** ICLR 2025 (spotlight)

**Authors:** Roman Worschech, Bernd Rosenow

**Keywords:** Statistical mechanics, neural scaling laws

**Abstract:** 
> Neural scaling laws describe how the performance of deep neural networks scales with key factors such as training data size, model complexity, and training time, often following power-law behaviors over multiple orders of magnitude. Despite their empirical observation, the theoretical understanding of these scaling laws remains limited. In this work, we employ techniques from statistical mechanics to analyze one-pass stochastic gradient descent within a student-teacher framework, where both the ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**On-line learning in Soft Committee Machines** (1995)
- *Authors:* David Saad and Sara A. Solla
- *Direct Connection:* This work established the student–teacher framework and order-parameter dynamics for one-pass SGD in two-layer (committee) networks, the analytical template that the current paper directly extends to structured (power-law) data spectra and nonlinear feature learning.

**Gaussian Processes for Regression: Learning Curves** (2002)
- *Authors:* Peter Sollich
- *Direct Connection:* Sollich’s learning-curve theory linked eigenvalue spectra of data (or kernels) to power-law generalization rates, an insight the present work translates from kernel/GP settings to SGD-trained two-layer neural networks.

**Deep learning scaling is predictable, empirically** (2017)
- *Authors:* Joel Hestness et al.
- *Direct Connection:* It documented robust power-law scaling with data and model size across tasks, defining the empirical phenomenon that motivates deriving exact scaling conditions from first principles in two-layer networks.

### 💡 Inspiration

**High-dimensional dynamics of generalization error in neural networks** (2017)
- *Authors:* M. S. Advani and Andrew M. Saxe
- *Direct Connection:* By showing how data covariance anisotropy controls learning dynamics and generalization in linear models, this paper provided the specific spectral perspective that is adopted and pushed to the power-law regime for two-layer networks trained by one-pass SGD.

### 🔍 Gap Identification

**Spectrum-dependent learning curves in kernel regression** (2020)
- *Authors:* Blake Bordelon, Kerem Canatar, and Cengiz Pehlevan
- *Direct Connection:* This paper quantified how power-law eigenvalue decay yields power-law learning curves in kernel regression, highlighting a gap—the absence of analogous spectral–scaling theory for feature-learning networks trained with SGD—that the current work fills.

**Explaining Neural Scaling Laws** (2021)
- *Authors:* Yasaman Bahri et al.
- *Direct Connection:* Offering a phenomenological account that ties power-law performance to broad difficulty spectra, this work underscored the need for a mechanistic SGD-based derivation—precisely what the present analysis provides in a student–teacher two-layer setting.

---

## Synthesis: How Prior Work Led to This Paper

Empirical studies first established that performance often follows power laws with data and model size, with Hestness et al. showing predictable scaling across deep learning benchmarks. Bahri et al. proposed a phenomenological explanation grounded in broad distributions of task difficulty, suggesting that heavy-tailed spectra can induce power-law learning curves. In parallel, theory from kernel and Gaussian process regression connected data or kernel eigenspectra to learning curves: Sollich demonstrated that eigenvalue decay controls generalization rates, and Bordelon, Canatar, and Pehlevan derived spectrum-dependent formulas that yield power-law regimes under power-law eigenvalue decay. Complementing these, Advani and Saxe analyzed gradient-based learning in high dimensions, revealing how anisotropic data covariance shapes generalization dynamics in linear models. Crucially, Saad and Solla introduced the student–teacher framework and order-parameter dynamics for one-pass SGD in two-layer (soft committee) networks, enabling exact analytical tracking of generalization through statistical mechanics.
Together, these works exposed a clear opportunity: while spectral theories predict power-law learning in kernelized or linear settings, and empirical works document scaling in neural networks, there lacked a mechanistic derivation for feature-learning two-layer networks trained with one-pass SGD under structured (power-law) data. By fusing the student–teacher dynamical machinery with the spectral lens from kernel/GP theory and high-dimensional linear dynamics, the present study naturally advances the field—deriving explicit generalization curves, identifying when power laws emerge from power-law covariances, and extending the analysis from linear to nonlinear activation regimes.

---

*Analysis generated on: 2026-01-06T08:29:59.839654*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
