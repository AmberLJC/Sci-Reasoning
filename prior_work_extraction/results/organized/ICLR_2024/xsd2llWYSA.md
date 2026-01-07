# Prior Work Analysis Report

## Target Paper

**Title:** FLD: Fourier Latent Dynamics for Structured Motion Representation and Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Chenhao Li, Elijah Stanger-Jones, Steve Heim, Sang bae Kim

**Keywords:** latent dynamics, motion representation and generation, representation learning, reinforcement learning

**Abstract:** 
> Motion trajectories offer reliable references for physics-based motion learning but suffer from sparsity, particularly in regions that lack sufficient data coverage. To address this challenge, we introduce a self-supervised, structured representation and generation method that extracts spatial-temporal relationships in periodic or quasi-periodic motions. The motion dynamics in a continuously parameterized latent space enable our method to enhance the interpolation and generalization capabilities...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors** (2013)
- *Authors:* Auke Ijspeert et al.
- *Direct Connection:* FLD replaces the hand-crafted phase-driven basis of rhythmic DMPs with a learned Fourier latent dynamical system that preserves periodic structure while capturing spatial–temporal coupling for interpolation across motions.

**Probabilistic Movement Primitives** (2013)
- *Authors:* Anastasios Paraschos et al.
- *Direct Connection:* Adopting the idea of low-dimensional distributions over trajectories, FLD directly addresses ProMPs’ limited expressivity for complex periodic/quasi-periodic behaviors by learning a continuous Fourier-parameterized latent dynamics that generalizes across sparse demonstrations.

### 💡 Inspiration

**Phase-Functioned Neural Networks for Character Control** (2017)
- *Authors:* Daniel Holden et al.
- *Direct Connection:* Building on the phase-conditioning insight of PFNNs, FLD generalizes phase to a learned latent with Fourier dynamics, decoupling phase from pose and enabling smooth interpolation to unseen targets.

**Implicit Neural Representations with Periodic Activation Functions (SIREN)** (2020)
- *Authors:* Vincent Sitzmann et al.
- *Direct Connection:* Leveraging SIREN’s insight that sinusoidal bases efficiently encode periodic signals, FLD parameterizes motion in a Fourier latent space to stably learn and reconstruct periodic and quasi-periodic dynamics.

### 🔍 Gap Identification

**AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control** (2021)
- *Authors:* Xue Bin Peng et al.
- *Direct Connection:* FLD addresses AMP’s lack of explicit temporal structure and dependence on dense motion priors by introducing an explicit Fourier latent dynamics that generalizes from sparse data while preserving motion periodicities.

### 📊 Baseline

**DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills** (2018)
- *Authors:* Xue Bin Peng et al.
- *Direct Connection:* Targeting the same physics-based tracking setting as DeepMimic, FLD replaces per-clip reference tracking with a structured Fourier latent motion model to overcome coverage sparsity and enable continuous interpolation.

### 🔧 Extension

**Deep learning for universal linear embeddings of nonlinear dynamics** (2018)
- *Authors:* Nathaniel Lusch et al.
- *Direct Connection:* FLD extends Koopman-style autoencoding by constraining the latent evolution to harmonic (Fourier) dynamics, yielding a simple, linearizable latent that better captures periodic/quasi-periodic motion structure.

---

## Synthesis: How Prior Work Led to This Paper

Rhythmic dynamic movement primitives established that periodic motions can be encoded with a phase-driven dynamical system, but relied on hand-crafted bases that do not capture rich spatial–temporal coupling. Probabilistic Movement Primitives extended this line with distributions over trajectories, enabling variability and interpolation, though expressivity and scalability to complex periodic/quasi-periodic behaviors remained limited. Phase-Functioned Neural Networks showed that conditioning on a continuous phase variable can drive high-fidelity locomotion controllers, highlighting phase as a powerful motion coordinate. In physics-based character control, DeepMimic demonstrated robust RL tracking from motion clips, while its clip-centric design struggled when reference coverage is sparse. Adversarial Motion Priors improved generalization via learned motion priors, yet lacked explicit temporal structure to guarantee coherent interpolation across styles and frequencies. Parallel advances in Koopman autoencoders revealed that nonlinear dynamics can be encoded into latent spaces with simple, often linear evolution, and SIREN showed that sinusoidal parameterizations are especially effective for representing periodic signals. Together, these works point to a gap: controllers need an explicit, low-dimensional, temporally structured latent that both respects periodic/quasi-periodic dynamics and supports interpolation under sparse data. The natural synthesis is to learn a Koopman-inspired latent where dynamics are constrained to harmonic/Fourier evolution, using sinusoidal structure to encode spatial–temporal relations while providing a continuous parameterization for control. This yields a motion model that bridges PFNN-style phase conditioning with DeepMimic/AMP tracking, enabling robust online tracking and generalization to unseen targets from limited demonstrations.

---

*Analysis generated on: 2026-01-06T18:17:27.441529*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
