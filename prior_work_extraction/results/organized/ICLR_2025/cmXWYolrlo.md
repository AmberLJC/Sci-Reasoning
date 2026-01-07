# Prior Work Analysis Report

## Target Paper
**Title:** cmXWYolrlo
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Connection:* Introduced the linearized training dynamics governed by an architecture-dependent kernel, directly enabling this paper’s "average geometry" notion and its result that early geometry evolution is the data covariance projected onto an architecture-defined kernel.

**Bayesian Deep Convolutional Networks with Many Channels are Gaussian Processes** (2019)
- *Authors:* Roman Novak et al.
- *Connection:* Established architecture-specific function-space priors (NNGP/NTK) for CNNs and related architectures, grounding the paper’s use of an architecture-dependent, initialization-time "average geometry" to summarize input–output geometry.

**Exact Solutions to the Nonlinear Dynamics of Learning in Deep Linear Neural Networks** (2013)
- *Authors:* Andrew M. Saxe et al.
- *Connection:* Provided closed-form training dynamics showing evolution along data covariance modes, a precursor to this paper’s result that early geometry changes follow data covariance projected onto an architecture-defined geometry.

### 💡 Inspiration

**On the Inductive Bias of Neural Tangent Kernels** (2019)
- *Authors:* Adrien Bietti et al.
- *Connection:* Analyzed how architectural choices imprint anisotropic spectral/geometric biases in NTKs; this directly motivates the paper’s architecture-dependent invariance directions and its orientation-dependent generalization phenomena.

**Universal Adversarial Perturbations** (2017)
- *Authors:* Seyed-Mohsen Moosavi-Dezfooli et al.
- *Connection:* Revealed shared, low-dimensional input directions that consistently alter network outputs, inspiring this paper’s geometric invariance hypothesis and its claim that architecture determines subspaces where input-space curvature is invariant or evolves.

### 🔧 Extension

**Wide Neural Networks of Any Depth Evolve as Linear Models Under Gradient Descent** (2019)
- *Authors:* Jaehoon Lee et al.
- *Connection:* Generalized NTK dynamics to deep architectures (including ResNets), which this work leverages to analyze architecture-dependent geometry evolution and to explain why MLPs vs. ResNets differ with respect to plane orientation.

**Spectral Bias and Task-Model Alignment in Kernel Regression** (2021)
- *Authors:* Mehmet Canatar et al.
- *Connection:* Showed that learning dynamics and generalization are governed by alignment between data/task spectra and the kernel’s eigenfunctions; this paper recasts that alignment as data-covariance projections onto an architecture-driven "average geometry" and uses it to predict where geometry can or cannot change.

---

## Synthesis

The paper’s core idea—that a network’s input-space geometry evolves only along architecture-determined directions and, at initialization, according to data covariance projected onto an architecture-defined average geometry—emerges from the kernel-view of training dynamics. Jacot et al. introduced the Neural Tangent Kernel (NTK), establishing that early training follows linearized dynamics determined by an architecture-dependent kernel. Lee et al. extended this to deep networks, including ResNets, enabling a head-to-head architectural comparison central to the paper’s orientation-dependent generalization findings. Canatar et al. showed that learning and generalization depend on alignment between data spectra and kernel eigenfunctions; the present work reframes this as data-covariance projections onto an average geometry, predicting where geometry can change (and where it remains invariant). Bietti and Mairal analyzed how architectural choices induce anisotropic spectral biases in NTKs, directly motivating the paper’s architecture-specific invariance directions and explaining why MLPs (near rotationally invariant kernels) and ResNets (anisotropic kernels) behave differently. Novak et al. grounded these ideas by deriving architecture-specific Gaussian process/NTK priors, legitimizing an architecture-only summary of input–output geometry at initialization. Beyond the kernel lens, Saxe et al. showed in deep linear nets that training progresses along data covariance modes, foreshadowing the paper’s projection result. Finally, Moosavi-Dezfooli et al.’s universal adversarial perturbations highlighted low-dimensional, shared input directions with outsized effect, inspiring the geometric invariance hypothesis that certain architecture-dependent directions preserve curvature while others drive its evolution.

---
*Generated: 2026-01-06T23:08:23.926446*
