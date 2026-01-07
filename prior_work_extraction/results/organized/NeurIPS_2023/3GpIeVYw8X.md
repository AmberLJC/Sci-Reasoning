# Prior Work Analysis Report

## Target Paper
**Title:** 3GpIeVYw8X
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

HUME’s central contribution is an unsupervised, model-agnostic procedure that infers human labeling by searching for labelings that are linearly separable across many fixed representation spaces. This idea stands on two pillars: the robustness of semantic structure to representation choice and the use of simple linear probes to expose that structure. SimCLR and DINO established that self-supervised representations encode semantics that are reliably extractable by linear classifiers, legitimizing HUME’s decision to keep representations frozen and evaluate candidate labelings purely via linear separability. Complementing this, work on transferability by Kornblith et al. showed that linear probes succeed across architectures and datasets, suggesting that human-aligned class geometry persists across diverse feature spaces—an assumption HUME explicitly operationalizes.

On the unsupervised labeling side, DeepCluster, IIC, and SCAN demonstrated that, without labels, one can recover categories that closely track human annotations by leveraging clustering, mutual-information-based view consistency, and simple classifiers on frozen features. HUME synthesizes these insights but replaces instance- or view-level objectives with a global search over labelings guided by an across-representation separability score. Finally, the multi-view agreement principle from co-training provides the theoretical template: the correct labeling is the one that is simultaneously simple and consistent in multiple independent views. HUME instantiates this by treating different pretrained encoders as views and selecting the labeling that is linearly separable in all of them, thereby aligning unsupervised discovery with human labeling.

---
*Generated: 2026-01-07T00:02:04.820651*
