# Prior Work Analysis Report

## Target Paper
**Title:** 0uUHfhXdnH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Attention Is All You Need** (2017)
- *Authors:* Vaswani et al.
- *Connection:* DiJiang starts from pre-trained vanilla Transformers and explicitly targets converting this standard self-attention architecture into a linear-complexity form with minimal retraining.

**Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention** (2020)
- *Authors:* Katharopoulos et al.
- *Connection:* DiJiang adopts the kernel-feature reformulation of attention introduced here to achieve O(n) complexity and then improves the feature approximation and implementation via QMC sampling and DCT.

**Random Features for Large-Scale Kernel Machines** (2007)
- *Authors:* Rahimi et al.
- *Connection:* DiJiang’s kernelization of attention is rooted in the random-feature paradigm of approximating kernels via sampled feature maps introduced by Rahimi and Recht.

### 💡 Inspiration

**FNet: Mixing Tokens with Fourier Transforms** (2021)
- *Authors:* Lee-Thorp et al.
- *Connection:* FNet demonstrated that frequency-domain transforms can replace or approximate attention while retaining accuracy, motivating DiJiang’s frequency-domain (DCT) realization of attention kernelization for low training cost.

### 📊 Baseline

**Rethinking Attention with Performers (Fast Attention via Positive Orthogonal Random Features)** (2021)
- *Authors:* Choromanski et al.
- *Connection:* Performer’s FAVOR+ random-feature approximation of softmax is the primary linear-attention baseline that DiJiang directly improves upon by replacing Monte Carlo random features with weighted Quasi-Monte Carlo and using DCT-based computation.

### 🔧 Extension

**Quasi-Monte Carlo Feature Maps for Shift-Invariant Kernels** (2014)
- *Authors:* Yang et al.
- *Connection:* Building on the idea that QMC yields lower-variance kernel feature maps than plain Monte Carlo, DiJiang extends this line by designing weighted QMC sampling tailored to softmax-kernelization for attention.

### 🔗 Related Problem

**Fastfood: Approximating Kernel Expansions in Loglinear Time** (2013)
- *Authors:* Le et al.
- *Connection:* Fastfood’s use of fast orthogonal transforms to accelerate kernel feature computations directly informs DiJiang’s choice to realize kernelization with efficient frequency-domain operations, here instantiated with DCT.

---

## Synthesis

DiJiang’s core innovation—turning a pre-trained vanilla Transformer into a linear-complexity model via frequency-domain kernelization—stands on two intertwined foundations: kernel-based linear attention and variance-reduced kernel feature approximation. The problem setting and target architecture derive from the original Transformer, while the linearization mechanism follows the kernel-feature reformulation of attention introduced by Katharopoulos et al. and advanced by Performer’s FAVOR+, which approximates softmax with nonnegative random features. However, Performer’s reliance on standard Monte Carlo sampling leaves variance and sample-efficiency limitations that can require substantial retraining to match accuracy.

To address this, DiJiang draws directly from the random-features lineage inaugurated by Rahimi and Recht and specifically extends Yang et al.’s Quasi-Monte Carlo feature maps: it introduces weighted QMC sampling tailored to attention’s kernel, improving approximation efficiency over plain Monte Carlo and orthogonal-feature variants. Complementing the sampling advance, DiJiang realizes the kernelization with fast frequency-domain primitives, inspired by Fastfood’s insight that structured orthogonal transforms accelerate kernel features and by FNet’s evidence that frequency-domain operators can replace attention while preserving quality. Concretely, DiJiang employs DCT-based operations to reduce compute and enable a post-hoc conversion of pre-trained Transformers, thus avoiding large-scale retraining. Together, these threads—linear attention via kernel features, QMC-driven variance reduction, and efficient frequency-domain transforms—directly shape DiJiang’s frequency-domain kernelization with weighted QMC and DCT, yielding linear-complexity inference with minimal fine-tuning.

---
*Generated: 2026-01-06T23:09:26.503106*
