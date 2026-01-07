# Prior Work Analysis Report

## Target Paper
**Title:** qQbvLU34F1
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

AnaCP sits at the intersection of two influential lines in class-incremental learning: analytic, prototype-based classification over frozen features, and contrastive representation learning for class separation. The CIL foundations laid by iCaRL defined the evaluation protocol and popularized prototype-based prediction, while Mensink et al. provided the nearest-class-mean formulation that underpins efficient analytic classifiers. Methods like CWR* and ScaIL showed that freezing a pre-trained encoder and updating only the classifier with simple, closed-form or calibration steps can be highly competitive—yet they also exposed a key limitation: without adapting representations to the evolving set of classes, performance saturates below the joint-training upper bound. SimpleShot further reinforced that, with the right normalization and metric, analytic prototype classifiers over fixed embeddings are remarkably strong, sharpening the question of how to add feature plasticity without costly gradient-based training. Supervised Contrastive Learning introduced a powerful separation objective that, if harnessed without backpropagation, could endow CIL with adaptable yet stable features. AnaCP leverages this idea by recasting contrastive separation into an analytic projection update, drawing on the spirit of incremental LDA to achieve closed-form, streaming-compatible adaptation of the feature space. By marrying analytic prototype classification with an incrementally computable, contrastive-inspired projection, AnaCP preserves efficiency and stability while recovering much of the performance gap to the upper bound.

---
*Generated: 2026-01-06T23:42:48.130559*
