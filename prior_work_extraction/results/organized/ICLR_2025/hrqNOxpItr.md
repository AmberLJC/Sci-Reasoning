# Prior Work Analysis Report

## Target Paper

**Title:** Cross-Entropy Is All You Need To Invert the Data Generating Process

**Conference:** ICLR 2025 (oral)

**Authors:** Patrik Reizinger, Alice Bizeul, Attila Juhos, Julia E Vogt, Randall Balestriero, Wieland Brendel, David Klindt

**Keywords:** supervised learning, representation learning, identifiability, linear representation hypothesis

**Abstract:** 
> Supervised learning has become a cornerstone of modern machine learning, yet a comprehensive theory explaining its effectiveness remains elusive. Empirical phenomena, such as neural analogy-making and the linear representation hypothesis, suggest that supervised models can learn interpretable factors of variation in a linear fashion. Recent advances in self-supervised learning, particularly nonlinear Independent Component Analysis, have shown that these methods can recover latent structures by i...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Noise-Contrastive Estimation: A New Estimation Principle for Unnormalized Statistical Models** (2010)
- *Authors:* Michael U. Gutmann et al.
- *Direct Connection:* NCE established that a simple cross-entropy (logistic) classifier can recover parameters of a data-generating density via discrimination against noise, a core insight this paper leverages to show cross-entropy can invert a latent generative process in supervised settings.

**Unsupervised Feature Extraction by Time-Contrastive Learning and Nonlinear ICA** (2016)
- *Authors:* Aapo Hyvärinen et al.
- *Direct Connection:* This work proved identifiability of nonlinear ICA using auxiliary variables through a contrastive (classification) objective, providing the identifiability blueprint that the present paper extends to instance discrimination and then to supervised cross-entropy.

**Unsupervised Feature Learning via Non-Parametric Instance Discrimination** (2018)
- *Authors:* Zhirong Wu et al.
- *Direct Connection:* This paper introduced the instance discrimination formulation that the present work analyzes in a parametric setting as the intermediate step enabling identifiability results to transfer from nonlinear ICA to supervised cross-entropy.

### 💡 Inspiration

**Prevalence of Neural Collapse During the Terminal Phase of Training** (2020)
- *Authors:* Vardan Papyan et al.
- *Direct Connection:* Neural collapse revealed the linear geometric structure induced by cross-entropy training, inspiring the present paper's claim and proof that cross-entropy can learn latent factors up to a linear transform.

### 🔍 Gap Identification

**Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations** (2019)
- *Authors:* Francesco Locatello et al.
- *Direct Connection:* Their impossibility result for unsupervised disentanglement without inductive biases explicitly motivates seeking identifiability via side information, a gap this work addresses by using labels/cross-entropy to guarantee factor recovery.

### 🔧 Extension

**Variational Autoencoders and Nonlinear ICA: A Unifying Framework** (2020)
- *Authors:* Ilyes Khemakhem et al.
- *Direct Connection:* iVAE showed identifiability under conditional exponential-family assumptions with observed auxiliaries; the current paper adapts these conditional/auxiliary-variable identifiability conditions and extends them to parametric instance discrimination and supervised classification.

### 🔗 Related Problem

**Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere** (2020)
- *Authors:* Tongzhou Wang et al.
- *Direct Connection:* The alignment–uniformity decomposition clarified the geometric effects of contrastive losses, informing the present analysis of how instance discrimination geometry supports recovery of latent generative factors.

---

## Synthesis: How Prior Work Led to This Paper

Noise-contrastive estimation revealed that discriminative training with cross-entropy can recover parameters of a generative model by classifying real data against noise, establishing a bridge between density estimation and classification. Time-Contrastive Learning and subsequent nonlinear ICA theory showed that introducing auxiliary variables—such as temporal segmentation—renders latent sources identifiable using a contrastive classifier, grounding identifiability in discriminative objectives. Identifiable VAEs further unified this view by proving identifiability of nonlinear generative models under conditional exponential-family assumptions when conditioning on observed auxiliaries. In parallel, instance discrimination framed self-supervised learning as classifying instances, catalyzing rigorous analyses of contrastive formulations. The alignment–uniformity perspective clarified how contrastive losses shape representation geometry, linking objective design to the emergence of structured embeddings. Meanwhile, impossibility results for unsupervised disentanglement emphasized that identifiability requires side information or inductive biases. Finally, neural collapse demonstrated that cross-entropy training produces highly structured, near-linear feature geometry, hinting at deeper connections between supervised objectives and latent factor structure. Together, these works suggested a path: if contrastive, auxiliary-variable-based objectives can identify latent factors, and cross-entropy induces disciplined geometry, then identifiability might extend beyond self-supervision. This paper synthesizes those insights by first formalizing identifiability for parametric instance discrimination under conditional generative assumptions, then showing that the same cross-entropy machinery suffices in standard supervised classification. By treating labels as the auxiliary signal and leveraging contrastive-to-classification equivalences, it proves representations recover ground-truth factors up to a linear transform, resolving the gap highlighted by disentanglement impossibility and aligning with observed linear feature phenomena.

---

*Analysis generated on: 2026-01-06T10:22:55.833958*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
