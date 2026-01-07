# Prior Work Analysis Report

## Target Paper
**Title:** OJximyClit
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Frolic advances zero-shot vision-language recognition by unifying three influential lines of work: prompt learning for CLIP, fusion of adapted and base models, and principled bias correction. CLIP demonstrated that carefully crafted textual templates and prompt ensembling can unlock strong zero-shot generalization, while CoOp and CoCoOp established that continuous and image-conditional prompts, learned with labels, yield sizable gains. Frolic internalizes these insights but removes the reliance on labeled data by learning a distribution over prompt prototypes from unlabeled samples, capturing diverse visual-text correspondences beyond fixed templates or a single learned prompt.
To translate distributional prompt gains into robust predictions, Frolic adaptively fuses its learned prompt-distribution model with the original CLIP, guided by confidence matching. This draws on ideas from Tip-Adapter and WiSE-FT, which show that combining adapted and base CLIP predictions or weights improves robustness; Frolic operationalizes a label-free, confidence-driven fusion tailored to zero-shot use.
Finally, Frolic addresses a key failure mode—label-frequency bias inherited from web-scale pretraining—by performing label-free logit adjustment. This component is theoretically anchored in long-tail logit adjustment and classical prior-shift recalibration that estimate target class priors without labels. Together, these priors directly shape Frolic’s core contribution: a label-free framework that learns and fuses prompt distributions while correcting label bias, thereby boosting zero-shot performance without annotations.

---
*Generated: 2026-01-06T23:33:36.293006*
