# Prior Work Analysis Report

## Target Paper
**Title:** i5WnXNjwbR
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution—revisiting the texture-bias hypothesis by replacing forced-choice cue conflicts with a domain-agnostic, controlled suppression framework—builds directly on and responds to several key threads in the literature. Geirhos et al. (2019) established the prevailing claim that ImageNet CNNs are texture-biased using cue-conflict stimuli constructed with neural style transfer (Gatys et al., 2016). While pivotal, that methodology entangles multiple cues and forces a discrete choice; the present paper addresses these limitations by isolating and systematically suppressing shape, texture, and color cues, inspired by the principled use of controlled corruptions popularized by ImageNet-C (Hendrycks & Dietterich, 2019).

A second line of influence comes from evidence that CNNs can succeed using strictly local evidence, notably BagNets (Brendel & Bethge, 2019). This directly motivates the paper’s key empirical finding: ImageNet CNNs are not inherently texture-biased but predominantly rely on local shape features. The authors further probe how architectural inductive biases and training strategies affect reliance, leveraging modern baselines such as Vision Transformers (Dosovitskiy et al., 2021), whose global attention can favor more holistic shape processing, and ConvNeXt (Liu et al., 2022), a strong contemporary ConvNet, to show such reliance can be mitigated.

Finally, the decision to extend analyses across computer vision, medical imaging, and remote sensing reflects the broader insight that models often exploit whichever cues are most accessible, sometimes spurious—highlighted by explainability-driven revelations of "Clever Hans" behavior (Lapuschkin et al., 2019). Together, these works shape a unified, cue-suppression methodology that reinterprets prior texture-bias claims, quantifies feature reliance rigorously, and demonstrates its dependence on architecture, training, and domain.

---
*Generated: 2026-01-07T00:29:42.056937*
