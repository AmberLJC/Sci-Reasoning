# Prior Work Analysis Report

## Target Paper
**Title:** dEypApI1MZ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Connection:* Introduced the NTK and its RKHS, providing the kernel-limit baseline that this paper explicitly contrasts with by defining easy/super-easy (in-RKHS) vs. hard (out-of-RKHS) tasks and then moving beyond the NTK regime.

**A Mean Field View of the Landscape of Two-Layer Neural Networks** (2018)
- *Authors:* Song Mei et al.
- *Connection:* Established the mean-field feature-learning framework beyond the NTK limit; this paper draws on that beyond-kernel perspective to analytically study scaling when features evolve during training.

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Jared Kaplan et al.
- *Connection:* Introduced empirical power-law scaling with model size, data, and compute; this work targets a theoretical account of such laws and refines them by predicting when feature learning changes exponents for hard tasks.

### 💡 Inspiration

**Exact solutions to the nonlinear dynamics of learning in deep linear neural networks** (2013)
- *Authors:* Andrew M. Saxe et al.
- *Connection:* Showed mode-wise learning dynamics and timescales in deep linear networks; the present paper leverages this solvable dynamics perspective to derive training-time and compute scaling exponents in the feature-learning regime.

### 🔍 Gap Identification

**On Lazy Training in Differentiable Programming** (2019)
- *Authors:* Lénaïc Chizat et al.
- *Connection:* Formalized the distinction between lazy (kernel) and rich (feature-learning) regimes, highlighting the limitations of the lazy/NTK approximation that this work addresses by developing a solvable feature-learning model for scaling laws.

### 📊 Baseline

**Spectral bias and task-model alignment explain generalization in kernel regression** (2021)
- *Authors:* Benjamin Canatar et al.
- *Connection:* Provided spectral learning-curve theory for kernel regression and a task-hardness notion via target coefficients in the NTK eigenbasis; this paper directly adopts that formulation and extends the scaling predictions to feature-learning models.

### 🔗 Related Problem

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Jordan Hoffmann et al.
- *Connection:* Presented compute-optimal tradeoffs under empirical scaling; the current paper derives a new compute-optimal scaling law specifically for hard tasks in the feature-learning regime, explaining when optimal exponents differ from Chinchilla-style prescriptions.

---

## Synthesis

The paper’s core idea—deriving solvable scaling laws beyond the kernel limit and showing that feature learning improves exponents for hard (out-of-RKHS) tasks—rests on three pillars. First, the NTK framework of Jacot et al. defined the kernel-limit baseline and its RKHS, which this work uses to categorize tasks as easy/super-easy (in-RKHS) versus hard (out-of-RKHS). Canatar, Bordelon, and Pehlevan supplied the spectral learning-curve analysis for kernel regression, tying generalization and scaling exponents to target coefficients in the NTK eigenspectrum; this new paper directly extends those kernel-only predictions into the feature-learning regime. Second, moving beyond the lazy/NTK approximation is motivated by Chizat and Bach’s formulation of lazy versus rich training, and enabled analytically by the solvable dynamics tradition of Saxe et al., whose deep linear network results on mode-wise learning times underpin the paper’s training-time and compute scaling derivations. Mean-field perspectives on feature learning, crystallized by Mei, Montanari, and Nguyen, provide the conceptual framework for evolving features at large width. Third, the broader scaling-law agenda set by Kaplan et al. and compute-optimal tradeoffs advanced by Hoffmann et al. form the empirical and practical backdrop: the present work explains when and why exponents should change once features learn, and it delivers a new compute-optimal law for hard tasks in the feature-learning regime. Together, these works directly enable and motivate the paper’s main theoretical contribution.

---
*Generated: 2026-01-06T23:09:26.625705*
