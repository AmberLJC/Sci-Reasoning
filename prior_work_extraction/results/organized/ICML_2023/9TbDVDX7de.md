# Prior Work Analysis Report

## Target Paper
**Title:** 9TbDVDX7de
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Adversarial Examples Are Not Bugs, They Are Features** (2019)
- *Authors:* Andrew Ilyas et al.
- *Connection:* Ilyas et al. established the robust vs. non-robust feature framework, providing the conceptual basis that robustness is tied to human-perceptible (robust) features—directly motivating the hypothesis that enforcing perceptually aligned gradients could induce robustness.

**On the Connection Between Adversarial Robustness and Saliency Map Interpretability** (2019)
- *Authors:* Tobias Etmann et al.
- *Connection:* Etmann et al. theoretically and empirically linked robustness to more interpretable, human-aligned gradient-based saliency, a specific linkage this work operationalizes by explicitly promoting gradient–perception alignment during training.

**The Unreasonable Effectiveness of Deep Features as a Perceptual Metric** (2018)
- *Authors:* Richard Zhang et al.
- *Connection:* LPIPS from Zhang et al. provides the perceptual similarity metric that this paper relies on to define and quantify perceptual alignment of gradients and to construct a training objective that promotes such alignment.

### 💡 Inspiration

**Image Synthesis with a Single (Robust) Classifier** (2019)
- *Authors:* Surya Santurkar et al.
- *Connection:* Santurkar et al. showed that robust classifiers have gradients aligned well enough with semantic content to synthesize realistic class images, directly inspiring the idea to treat perceptually aligned gradients as a target property rather than a byproduct.

### 📊 Baseline

**Towards Deep Learning Models Resistant to Adversarial Attacks** (2018)
- *Authors:* Aleksander Madry et al.
- *Connection:* Adversarial training from Madry et al. is the primary robustness baseline and the source of the well-documented phenomenon that robust models exhibit perceptually aligned input gradients, which this paper inverts by directly training for such alignment to test whether it implies robustness.

**Theoretically Principled Trade-off between Robustness and Accuracy (TRADES)** (2019)
- *Authors:* Hongyang Zhang et al.
- *Connection:* TRADES is a core adversarial training baseline against which the proposed perceptual-gradient alignment objective is compared and with which it is combined to demonstrate robustness gains attributable to improved gradient alignment.

### 🔧 Extension

**Improving the Adversarial Robustness and Interpretability of Deep Neural Networks by Regularizing their Input Gradients** (2018)
- *Authors:* Andrew Ross et al.
- *Connection:* Ross and Doshi-Velez demonstrated that constraining input gradients can simultaneously improve interpretability and robustness; this paper extends that paradigm by aligning gradients to a perceptual target (rather than merely shrinking or masking them) and showing the alignment itself yields robustness.

---

## Synthesis

The paper’s core contribution—directly training classifiers to have perceptually aligned input gradients and testing whether this property itself implies robustness—stands on a lineage that first established a robust–interpretability link and then hinted that manipulating input gradients can affect robustness. Madry et al. introduced adversarial training, the dominant robustness baseline and the empirical source of the observation that robust models exhibit perceptually aligned gradients. Ilyas et al.’s robust vs. non-robust feature framework provided the conceptual foundation: robustness correlates with human-perceptible features, suggesting that encouraging gradients to point along perceptual directions may induce robustness. Etmann et al. formally connected adversarial robustness to more interpretable saliency, reinforcing the specific target—human-aligned gradients—that this work operationalizes.

Two lines of prior work then enable the method design. Santurkar et al. demonstrated that robust classifiers’ gradients align so well with semantics that gradient ascent can synthesize class images, directly inspiring the idea to treat perceptually aligned gradients as a trainable goal. Ross and Doshi-Velez showed that regularizing input gradients can improve both interpretability and robustness, a technique this paper extends by aligning to a perceptual target rather than merely shrinking gradients. Finally, Zhang et al.’s LPIPS supplies the perceptual metric needed to define and measure alignment, while TRADES (alongside Madry’s PGD training) serves as a principal baseline and integration point, enabling controlled tests that reveal a bidirectional link: improving perceptual gradient alignment causally improves adversarial robustness.

---
*Generated: 2026-01-06T23:09:26.539083*
