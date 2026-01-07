# Prior Work Analysis Report

## Target Paper
**Title:** PBjCTeDL6o
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Axiomatic Attribution for Deep Networks** (2017)
- *Authors:* Mukund Sundararajan et al.
- *Connection:* Introduced Integrated Gradients, formalizing gradient-based attribution as a path integral from a baseline and highlighting saturation issues; UNI keeps this baseline-based formulation but replaces hand-chosen baselines with an adaptive, unlearning-derived baseline to directly address IG’s baseline dependence.

**Learning Important Features Through Propagating Activation Differences** (2017)
- *Authors:* Avanti Shrikumar et al.
- *Connection:* DeepLIFT established reference (baseline) inputs for attribution via activation differences; UNI targets the same reference-choice bottleneck by computing the reference adaptively through an unlearning direction rather than a static function.

### 💡 Inspiration

**Interpretable Explanations of Black Boxes by Meaningful Perturbation** (2017)
- *Authors:* Ruth Fong et al.
- *Connection:* Framed explanations as optimizing input deletions that remove class evidence; UNI adopts this deletion/unlearning perspective but computes the perturbation via the steepest-ascent unlearning direction to automatically discover a faithful baseline.

**Explaining and Harnessing Adversarial Examples** (2015)
- *Authors:* Ian J. Goodfellow et al.
- *Connection:* Introduced the fast gradient sign method for moving inputs in the loss’s steepest-ascent direction; UNI leverages this principle to compute an unlearning direction that defines a data- and model-adaptive attribution baseline.

### 🔍 Gap Identification

**XRAI: Better Attributions Through Regions** (2019)
- *Authors:* Nick Kapishnikov et al.
- *Connection:* XRAI popularized Blur Integrated Gradients (a blur-path baseline) and region-based attributions; UNI explicitly critiques blur/average baselines for injecting frequency and texture priors and replaces them with a debiased, input-adaptive unlearning baseline.

**Sanity Checks for Saliency Maps** (2018)
- *Authors:* Julius Adebayo et al.
- *Connection:* Showed many saliency methods are insensitive to model parameters, revealing brittleness partly exacerbated by heuristic baselines; UNI’s adaptive unlearning baseline is designed to avoid such model-insensitive artifacts.

**Adversarial Attacks on Neural Network Interpretations** (2019)
- *Authors:* Amirata Ghorbani et al.
- *Connection:* Demonstrated that explanations can be adversarially manipulated without altering predictions; UNI counters this manipulability by erasing salient features via unlearning, which locally smooths decision boundaries and stabilizes attributions.

---

## Synthesis

UNI emerges at the intersection of baseline-based attribution and perturbation-driven reasoning. Integrated Gradients and DeepLIFT established the core attribution paradigm that compares an input to a reference baseline to mitigate saturation, but they left open the crucial question of how to choose that baseline. Practical variants such as XRAI’s Blur Integrated Gradients operationalized this choice with static priors (blur/averages), which inject frequency and texture assumptions that can bias saliency. At the same time, the field recognized reliability gaps: sanity checks revealed methods that are insensitive to model parameters, and adversarial attacks showed explanations can be manipulated without changing predictions. In parallel, the perturbation perspective—exemplified by Meaningful Perturbation—demonstrated that effective explanations can be obtained by deleting evidence that supports a prediction. UNI synthesizes these threads: rather than handcrafting a static baseline, it computes an adaptive baseline by perturbing the input along the loss’s steepest-ascent direction (inspired by the FGSM view of steepest ascent), effectively unlearning salient class evidence. This unlearning-derived reference both erases features that drive the model and locally smooths high-curvature decision boundaries, directly addressing saturation, bias from static baselines, and manipulability. Thus, UNI can be seen as a principled, debiased replacement for baseline selection that preserves the axiomatic benefits of path-based attributions while inheriting the robustness and faithfulness of perturbation-based deletion.

---
*Generated: 2026-01-06T23:08:23.932280*
