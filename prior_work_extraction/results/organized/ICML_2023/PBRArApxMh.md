# Prior Work Analysis Report

## Target Paper
**Title:** PBRArApxMh
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Connection:* TRAK targets the same core objective—attributing a test prediction to training points—as influence functions, but replaces the brittle Hessian-inversion–based formulation with an after-training kernel view that remains tractable and reliable for deep, non-convex models.

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Connection:* TRAK’s "after kernel" is the NTK evaluated at the trained parameters; the method operationalizes this kernel to score train–test influence, and uses random projections plus a small ensemble of trained models to compute these NTK-based similarities at scale.

**Exploiting Generative Models in Discriminative Classifiers (Fisher Kernels)** (1999)
- *Authors:* Tommi Jaakkola et al.
- *Connection:* TRAK leverages the Fisher-kernel idea of using parameter gradients as features to define similarities between examples, instantiating it for modern deep nets by computing gradient-based kernels after training.

### 🔍 Gap Identification

**Data Shapley: Equitable Valuation of Data for Machine Learning** (2019)
- *Authors:* Amirata Ghorbani et al.
- *Connection:* Data Shapley provides a high-fidelity notion of data value but requires training thousands of models; TRAK is explicitly designed to match such high-quality attributions while eliminating this prohibitive computational cost.

### 📊 Baseline

**Estimating Training Data Influence by Tracing Gradient Descent** (2020)
- *Authors:* Garima Pruthi et al.
- *Connection:* TracIn’s gradient-similarity along the training trajectory is a primary scalable baseline that TRAK improves upon, achieving higher-quality attributions with only a handful of trained models instead of many checkpoints over the entire trajectory.

### 🔧 Extension

**Representer Point Selection for Explaining Deep Neural Networks** (2018)
- *Authors:* Chih-Kuan Yeh et al.
- *Connection:* TRAK extends the representer-point perspective—decomposing predictions into contributions from training examples—by replacing the L2-regularized representer theorem with an after-training gradient kernel that works broadly for deep networks and can be efficiently approximated via random projections.

---

## Synthesis

TRAK’s core innovation—accurate, scalable data attribution for deep networks via an after-training kernel—emerges from unifying three lines of prior work. First, influence functions (Koh & Liang) formalized the modern data-attribution problem: quantify how each training point affects a specific prediction. However, their reliance on Hessian inversion and local convexity limits reliability for deep nets, motivating a more stable formulation. Second, representer-point selection (Yeh et al.) demonstrated that predictions can be decomposed into contributions from training examples, but required restrictive regularization. TRAK generalizes this representer viewpoint by adopting a kernel built from parameter gradients after training—connecting directly to the Neural Tangent Kernel (Jacot et al.), but evaluated at the learned parameters rather than at initialization. This yields a principled, model-agnostic similarity between train and test points. Third, practical scalability lessons come from TracIn (Pruthi et al.), which uses gradient similarity along the training trajectory; TRAK preserves the gradient-based intuition but dispenses with full-trajectory dependence, using random projections and only a handful of trained models to approximate the after-training kernel efficiently. Finally, TRAK positions itself against the computationally intensive gold standard of data valuation (Data Shapley), aiming to match its attribution fidelity without thousands of retrainings. The Fisher kernel provides the historical foundation for gradient-feature kernels that TRAK operationalizes at scale for modern deep learning, completing the direct intellectual lineage.

---
*Generated: 2026-01-06T23:09:26.559961*
