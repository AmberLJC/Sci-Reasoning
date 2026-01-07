# Prior Work Analysis Report

## Target Paper

**Title:** Dictionary Contrastive Learning for Efficient Local Supervision without Auxiliary Networks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Suhwan Choi, Myeongho Jeon, Yeonjung Hwang, Jeonglyul Oh, Sungjun Lim, Joonseok Lee, Myungjoo Kang

**Keywords:** Contrastive learning, Forward learning, Local learning, Image classification, Efficient learning

**Abstract:** 
> While backpropagation (BP) has achieved widespread success in deep learning, it
faces two prominent challenges: computational inefficiency and biological implausibility.
In response to these challenges, local supervision, encompassing Local
Learning (LL) and Forward Learning (FL), has emerged as a promising research
direction. LL employs module-wise BP to achieve competitive results yet relies on
module-wise auxiliary networks, which increase memory and parameter demands.
Conversely, FL updates ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Deeply-Supervised Nets** (2015)
- *Authors:* Chen-Yu Lee et al.
- *Direct Connection:* Introduced the core local supervision formulation via auxiliary classifiers attached to intermediate layers, establishing the module-wise supervised training setup that this work seeks to retain without auxiliary networks.

### 💡 Inspiration

**Supervised Contrastive Learning** (2020)
- *Authors:* Prannay Khosla et al.
- *Direct Connection:* Provided the label-aware contrastive objective of pulling same-class representations together and pushing others apart, which this work adapts to layer-local features as the core supervision signal.

### 🔍 Gap Identification

**Training Neural Networks with Local Errors** (2019)
- *Authors:* Arild Nøkland et al.
- *Direct Connection:* Showed that local classifiers (even random ones) can drive layer-wise learning but still require auxiliary networks, motivating a local objective that eliminates such heads while preserving performance.

**The Forward-Forward Algorithm: Some Preliminary Investigations** (2022)
- *Authors:* Geoffrey Hinton
- *Direct Connection:* Proposed forward-only local learning without backprop or auxiliary heads but with a notable accuracy gap, highlighting the need for a more discriminative local objective to close performance to BP.

### 📊 Baseline

**Greedy Layerwise Learning Can Scale to Many Layers** (2019)
- *Authors:* Eugene Belilovsky et al.
- *Direct Connection:* Demonstrated competitive module-wise backpropagation using local losses and per-layer auxiliary heads, serving as the primary local-learning baseline whose memory/parameter overhead this work aims to remove.

### 🔧 Extension

**Momentum Contrast for Unsupervised Visual Representation Learning** (2020)
- *Authors:* Kaiming He et al.
- *Direct Connection:* Introduced the dictionary/queue mechanism that supplies large, consistent sets of keys for contrastive learning, which this work repurposes into label-structured dictionaries to stabilize local supervision without auxiliary networks.

---

## Synthesis: How Prior Work Led to This Paper

Deeply-Supervised Nets established that attaching auxiliary classifiers to intermediate layers can provide effective local supervision, formalizing a module-wise training setup that decouples layers via explicit heads. Building on that premise, greedy layerwise methods showed that module-wise backpropagation with local losses and auxiliary heads can scale and achieve strong accuracy, confirming the practical viability of local learning while inheriting the memory and parameter overhead of per-layer heads. Complementing this, local error approaches trained layers using local classifiers—including fixed random ones—proving local signals suffice but still depending on auxiliary mappings to labels. A forward-only alternative removed both backprop and auxiliary heads by leveraging local goodness objectives, but the resulting representations typically lagged in discriminativeness versus BP-trained models. In parallel, supervised contrastive learning demonstrated that label-aware contrastive objectives are especially effective at class-separating representations, and momentum contrast introduced dictionary/queue mechanisms that provide large, stable key sets crucial for robust contrastive optimization.
Together, these works revealed a clear opportunity: retain the efficiency and decoupling of local supervision while eliminating auxiliary heads, and replace weak local objectives with label-aware contrastive signals supported by stable dictionaries. By marrying the local-training formulation with supervised contrastive objectives and a dictionary mechanism adapted to labels at each layer, the current work naturally synthesizes these insights into a head-free, contrastive local supervision scheme that is both efficient and competitive.

---

*Analysis generated on: 2026-01-06T12:33:49.130045*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
