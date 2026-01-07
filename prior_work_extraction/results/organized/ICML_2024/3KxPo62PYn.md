# Prior Work Analysis Report

## Target Paper
**Title:** 3KxPo62PYn
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Deep Learning Scaling is Predictable, Empirically** (2017)
- *Authors:* Joel Hestness et al.
- *Connection:* Hestness et al. provided the cross-domain empirical scaling-law framework that underpins the paper’s premise of navigating between scaling regimes across modalities.

### 💡 Inspiration

**Net2Net: Accelerating Learning via Knowledge Transfer** (2016)
- *Authors:* Tianqi Chen et al.
- *Connection:* Net2Net introduced function-preserving depth/width expansions, demonstrating that changing a model’s shape mid-training can retain learned capabilities—an operational enabler for the paper’s adaptive model growth along a compute-optimal trajectory.

**Progressive Growing of GANs for Improved Quality, Stability, and Variation** (2018)
- *Authors:* Tero Karras et al.
- *Connection:* Karras et al. showed that progressively increasing model capacity during training can improve efficiency and outcomes, directly motivating the paper’s idea of traversing training with capacity growth rather than fixing architecture.

### 🔍 Gap Identification

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Jared Kaplan et al.
- *Connection:* Kaplan et al. established predictive compute–performance scaling and a compute-optimal regime but assumed a static model shape; this static assumption is the explicit limitation the present work removes by allowing the model to change shape during training.

### 📊 Baseline

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Jordan Hoffmann et al.
- *Connection:* The paper’s adaptive schedules are explicitly designed to beat the static compute-optimal frontier defined by Hoffmann et al., which formalized how to allocate compute between model size and data under fixed (non-adaptive) architectures.

### 🔗 Related Problem

**Once-for-All: Train One Network and Specialize it for Efficient Deployment** (2020)
- *Authors:* Han Cai et al.
- *Connection:* Once-for-All demonstrates a single training process supporting multiple model shapes (width/depth/resolution), informing the paper’s assertion that one can move across architectures during training; the present work reframes this adaptivity through compute-optimal scaling laws.

---

## Synthesis

The core innovation—compute-optimal training with an architecture that adapts its shape during learning—sits at the intersection of two lines of work: scaling-law based compute optimality and techniques that enable mid-training architecture changes. Foundational scaling-law studies by Hestness et al. established predictable power-law behavior across modalities, while Kaplan et al. formalized compute-driven performance prediction and a compute-optimal regime under the key assumption of a static model. Hoffmann et al. refined this into the widely used Chinchilla-style static compute-optimal baseline that balances parameters and data at fixed architecture. The present paper directly targets the central limitation in these baselines—the static-shape assumption—by proposing adaptive models that traverse between scaling regimes during training to reduce the compute required for a target performance.

Operationally, prior methods have shown that models can change shape without losing learned knowledge: Net2Net introduced function-preserving depth/width growth, and progressive growing of GANs demonstrated that staged capacity increases can improve training efficiency and quality. Complementing these, Once-for-All validated that a single training run can support many architectural instantiations, reinforcing the feasibility of moving across model shapes. Building on these ideas, the paper provides a principled framework that marries scaling-law compute optimality with adaptive capacity, deriving trajectories that strategically reallocate compute over training. In doing so, it establishes adaptive training as a superior path to the static compute-optimal frontier across modalities.

---
*Generated: 2026-01-06T23:09:26.418730*
