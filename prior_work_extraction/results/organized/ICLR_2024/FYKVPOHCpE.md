# Prior Work Analysis Report

## Target Paper

**Title:** Improving Non-Transferable Representation Learning by Harnessing Content and Style

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ziming Hong, Zhenyi Wang, Li Shen, Yu Yao, Zhuo Huang, Shiming Chen, Chuanwu Yang, Mingming Gong, Tongliang Liu

**Keywords:** non-transferable representation learning, domain adaptation, transfer learning

**Abstract:** 
> Non-transferable learning (NTL) aims to restrict the generalization of models toward the target domain(s). To this end, existing works learn non-transferable representations by reducing statistical dependence between the source and target domain. However, such statistical methods essentially neglect to distinguish between *styles* and *contents*, leading them to inadvertently fit (i) spurious correlation between *styles* and *labels*, and (ii) fake independence between *contents* and *labels*. C...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Non-Transferable Learning for Unsupervised Domain Adaptation** (2022)
- *Authors:* Yao et al.
- *Direct Connection:* This paper formalized the NTL objective as restricting generalization to specified target domains by reducing source–target statistical dependence, which H-NTL rethinks by introducing content/style causal separation to overcome its blind dependence reduction.

### 💡 Inspiration

**Invariant Risk Minimization** (2020)
- *Authors:* Arjovsky et al.
- *Direct Connection:* IRM’s causal view that predictive signals decompose into invariant (content) and spurious environment-dependent (style) factors directly motivates H-NTL’s explicit causal model that separates and harnesses content and style to control transferability.

**Multimodal Unsupervised Image-to-Image Translation** (2018)
- *Authors:* Huang et al.
- *Direct Connection:* MUNIT’s explicit factorization of images into a shared content code and a domain-specific style code provides the concrete latent-factor design that H-NTL repurposes to disentangle and guide content/style for non-transferable representation learning.

### 🔍 Gap Identification

**ImageNet-trained CNNs are biased towards texture; increasing shape bias in CNNs using stylized ImageNet** (2019)
- *Authors:* Geirhos et al.
- *Direct Connection:* This work exposes texture (style) bias and its brittleness under distribution shift, directly motivating H-NTL to avoid fitting spurious style–label correlations when enforcing non-transferability.

### 📊 Baseline

**Learning Non-Transferable Representations via Mutual Information Regularization** (2023)
- *Authors:* Huang et al.
- *Direct Connection:* As a primary NTL baseline that minimizes source–target dependence via MI, it is directly improved by H-NTL, which shows MI-only objectives can induce fake content–label independence and instead leverages disentangled content/style guidance.

### 🔗 Related Problem

**Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization** (2017)
- *Authors:* Huang and Belongie
- *Direct Connection:* AdaIN’s finding that channel-wise feature statistics encode style informs H-NTL’s style guidance mechanism for isolating style signals from content and preventing spurious style–label coupling.

---

## Synthesis: How Prior Work Led to This Paper

Invariant Risk Minimization (IRM) crystallized a causal perspective on generalization, positing that predictive signals decompose into invariant causal factors and spurious environment-linked factors, and that learning should target invariants. In computer vision, AdaIN demonstrated that channel-wise statistics capture style and can be manipulated to control it, while MUNIT operationalized a two-latent-factor model with content and style codes that can be disentangled and recombined. Geirhos et al. provided empirical evidence that CNNs over-rely on texture (a form of style), revealing how style–label correlations can drive brittleness under distribution shifts. Within this backdrop, early Non-Transferable Learning (NTL) efforts formalized the goal of restricting generalization to specified target domains by reducing source–target statistical dependence (e.g., via discrepancy or mutual information penalties), and subsequent work instantiated MI-based regularization to learn non-transferable representations. These NTL methods, however, treated all cross-domain signals uniformly, without distinguishing causal content from incidental style.

Taken together, these works highlight both the need to separate content and style and the pitfalls of undifferentiated dependence reduction. The causal framing from IRM and the concrete content–style factorization mechanisms from AdaIN/MUNIT suggested a natural next step: explicitly model and harness content and style as distinct latent factors while learning non-transferable features. H-NTL synthesizes these insights by introducing a causal model that disentangles content and style, using content guidance to preserve causal predictiveness and style guidance to avoid spurious correlations—thereby overcoming the fake content–label independence and style–label spuriosity that limit prior dependence-based NTL.

---

*Analysis generated on: 2026-01-06T12:08:34.247178*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
