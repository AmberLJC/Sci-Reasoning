# Prior Work Analysis Report

## Target Paper

**Title:** Scaling and evaluating sparse autoencoders

**Conference:** ICLR 2025 (oral)

**Authors:** Leo Gao, Tom Dupre la Tour, Henk Tillman, Gabriel Goh, Rajan Troll, Alec Radford, Ilya Sutskever, Jan Leike, Jeffrey Wu

**Keywords:** interpretability, sparse autoencoders, superposition, scaling laws

**Abstract:** 
> Sparse autoencoders provide a promising unsupervised approach for extracting interpretable features from a language model by reconstructing activations from a sparse bottleneck layer. Since language models learn many concepts, autoencoders need to be very large to recover all relevant features. However, studying the properties of autoencoder scaling is difficult due to the need to balance reconstruction and sparsity objectives and the presence of dead latents. We propose using k-sparse autoencod...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Toy Models of Superposition** (2022)
- *Authors:* Nicholas Elhage et al.
- *Direct Connection:* By formalizing superposition and showing that sparse coding can disentangle superposed features, it provided the core motivation to use sparse autoencoders to recover interpretable features from language model activations.

### 💡 Inspiration

**Winner-Take-All Autoencoders** (2014)
- *Authors:* Alireza Makhzani et al.
- *Direct Connection:* The winner-take-all/lifetime sparsity mechanisms motivated design choices for preventing dead latents under fixed-sparsity activations, informing the modifications that yield few dead latents at large scale.

**Network Dissection: Quantifying Interpretability of Deep Visual Representations** (2017)
- *Authors:* David Bau et al.
- *Direct Connection:* Its concept-level alignment metrics inspired creating quantitative feature-quality evaluations (e.g., hypothesized feature recovery and explainability of activation patterns) tailored to SAEs on LM activations.

### 🔍 Gap Identification

**Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet** (2024)
- *Authors:* Tom Lieberum et al.
- *Direct Connection:* Scaling SAEs in production LMs exposed worsening dead-latent rates and hyperparameter fragility, motivating the need for methods (like k-sparsity) that maintain feature quality and stability at large scales.

### 📊 Baseline

**Towards Monosemanticity: Decomposing Language Models with Sparse Autoencoders** (2023)
- *Authors:* Ethan Bricken et al.
- *Direct Connection:* This work established L1-regularized SAEs as the main approach for extracting interpretable features from LMs and highlighted practical issues—balancing sparsity vs. reconstruction and pervasive dead latents—that the current paper explicitly addresses.

### 🔧 Extension

**k-Sparse Autoencoders** (2013)
- *Authors:* Alireza Makhzani et al.
- *Direct Connection:* The paper directly adopts and modifies the top-k sparsity projection from k-sparse autoencoders to control latent sparsity, which simplifies tuning and improves the reconstruction–sparsity frontier relative to L1-penalized SAEs.

### 🔗 Related Problem

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Jared Kaplan et al.
- *Direct Connection:* Their methodology for measuring and fitting clean scaling relationships informed the analysis framework for deriving scaling laws with respect to autoencoder size and sparsity.

---

## Synthesis: How Prior Work Led to This Paper

k-sparse autoencoders introduced enforcing a fixed top‑k activation pattern to directly control sparsity, showing that projection-based sparsity can avoid the tuning instability of penalty-based methods while preserving reconstruction quality. Winner‑take‑all autoencoders extended this idea by emphasizing k‑winners and lifetime sparsity mechanisms that mitigate unit collapse, offering concrete practices for reducing dead units under strict sparsity constraints. Toy Models of Superposition framed why sparse codes matter in neural representations, arguing that features are superposed and that sparse dictionary recovery can disentangle them—pointing directly to SAEs as a tool for interpretability. Towards Monosemanticity operationalized this in language models with L1‑regularized SAEs, demonstrating interpretable features but documenting hard tradeoffs between sparsity and reconstruction and the prevalence of dead latents. Scaling Monosemanticity pushed SAEs to modern models and layers, revealing that dead-latent rates and hyperparameter fragility worsen with scale, and motivating more robust sparsity control. Network Dissection provided a template for quantitative, concept-based evaluations of interpretability that could be adapted from vision to LM feature dictionaries. Finally, scaling laws for LMs offered a methodology for fitting and interpreting clean power-law trends.
These threads jointly suggested an approach: use projection-based k‑sparsity to directly set activity levels, incorporate design choices from winner‑take‑all to keep latents alive at scale, and evaluate with concept-aligned metrics while analyzing performance through scaling-law methodology. The resulting synthesis naturally targets the core gaps identified by L1‑SAE work—unstable tuning and dead latents—enabling large‑scale, well‑behaved SAEs and revealing clean scaling laws over autoencoder size and sparsity.

---

*Analysis generated on: 2026-01-06T12:57:30.014480*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
