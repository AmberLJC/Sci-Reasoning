# Prior Work Analysis Report

## Target Paper

**Title:** Bayesian Optimization via Continual Variational Last Layer Training

**Conference:** ICLR 2025 (spotlight)

**Authors:** Paul Brunzema, Mikkel Jordahn, John Willes, Sebastian Trimpe, Jasper Snoek, James Harrison

**Keywords:** Bayesian deep learning, bayesian optimization, uncertainty

**Abstract:** 
> Gaussian Processes (GPs) are widely seen as the state-of-the-art surrogate models for Bayesian optimization (BO) due to their ability to model uncertainty and their performance on tasks where correlations are easily captured (such as those defined by Euclidean metrics) and their ability to be efficiently updated online. However, the performance of GPs depends on the choice of kernel, and kernel selection for complex correlation structures is often difficult or must be made bespoke. While Bayesia...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Practical Bayesian Optimization of Machine Learning Algorithms** (2012)
- *Authors:* Jasper Snoek et al.
- *Direct Connection:* Established GP-based BO with exact conditioning and online updates—the surrogate/baseline and update behavior that the proposed continual VBLL explicitly emulates.

### 💡 Inspiration

**Deep Bayesian Bandits Showdown: An Empirical Comparison of Bayesian Deep Networks for Thompson Sampling** (2018)
- *Authors:* Carlos Riquelme et al.
- *Direct Connection:* Showed that a neural feature extractor with a Bayesian linear last layer (neural-linear) yields calibrated uncertainty and efficient sequential updates, the architectural template the proposed method adopts for BO.

**Laplace Redux: Effortless Bayesian Deep Learning** (2021)
- *Authors:* Christoph Immer et al.
- *Direct Connection:* Established that Bayesianizing only the last layer (e.g., via Laplace) yields GP-like predictions over learned features; the proposed work generalizes this insight to a variational last layer and makes the GP-conditioning equivalence explicit for online training.

### 🔍 Gap Identification

**Bayesian Optimization with Robust Bayesian Neural Networks** (2016)
- *Authors:* Jost Tobias Springenberg et al.
- *Direct Connection:* Demonstrated BO with BNN surrogates yet reported unreliable performance and calibration on some tasks, a limitation directly addressed by tying VBLL training to exact GP conditioning.

### 🔧 Extension

**Variational Continual Learning** (2018)
- *Authors:* Cuong V. Nguyen et al.
- *Direct Connection:* Introduced an online variational update that projects prior posteriors as new data arrive; the proposed approach applies this continual VI recipe to the Bayesian last layer to enable fast per-iteration BO updates.

### 🔗 Related Problem

**Deep Kernel Learning** (2016)
- *Authors:* Andrew Gordon Wilson et al.
- *Direct Connection:* Showed that learning deep feature maps for GPs captures complex correlations; the proposed method adopts the same deep-feature surrogate idea but replaces GP inference with a variational Bayesian last layer trained via GP-like conditioning.

---

## Synthesis: How Prior Work Led to This Paper

Gaussian process surrogates for Bayesian optimization were popularized with exact conditioning and efficient online updates, enabling principled acquisition-driven search over expensive black-box functions. Deep kernel learning subsequently showed that learning feature maps before a GP can model complex, non-Euclidean correlations by letting a neural network parameterize the kernel, retaining GP conditioning while gaining representational power. In parallel, robust Bayesian neural network surrogates were explored for BO, but empirical studies reported poor calibration and inconsistent performance on some tasks. A complementary insight emerged from neural-linear methods in sequential decision making: coupling a neural feature extractor with a Bayesian linear last layer yields calibrated uncertainty and cheap posterior updates, suggesting that only the final layer needs to be Bayesian for effective uncertainty. This was reinforced by last-layer Laplace approaches, which demonstrated that Bayesianizing just the final layer produces GP-like predictions over deep features, hinting at a tight equivalence between last-layer Bayesian inference and GP conditioning. Finally, variational continual learning introduced a practical recipe for streaming variational updates by projecting the previous posterior as new data arrive, providing a template for online Bayesian updates. Together, these works expose an opportunity: marry deep feature flexibility with GP-style exact conditioning and streaming updates by Bayesianizing only the last layer. The resulting step is to cast the last layer’s variational training so it is algebraically equivalent to GP conditioning, and then leverage continual variational updates to deliver efficient online BO training while overcoming BNN calibration weaknesses and GP kernel-selection brittleness.

---

*Analysis generated on: 2026-01-06T08:43:27.244890*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
