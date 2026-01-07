# Prior Work Analysis Report

## Target Paper
**Title:** ZdqTePSV1K
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—RAM-APL, a multi-foundation-model, pseudo-label-accuracy-based one-shot subset selection method tailored to fine-grained datasets—emerges from two lines of prior work. First, classic one-shot/coreset selection approaches such as GLISTER and CRAIG established that a small, well-chosen subset can approximate full-dataset training, but they depend on dataset-specific information extractors or gradients from a target model. These methods motivate the paper’s Question (1) and serve as the primary baseline paradigm that the authors replace with foundation-model (FM) extractors. Second, recent progress with FMs shows their utility for data curation and transfer. CLIP provides zero-shot classification and robust embeddings, while DataComp demonstrates that CLIP-based scoring can curate datasets effectively at scale and that model choice matters—directly motivating Question (2). To design a selection criterion that exploits FMs while being robust, the authors draw on pseudo-labeling (Lee), using FM predictions as pseudo-class labels, and on multi-model agreement ideas from Query by Committee and DivideMix. Instead of relying on a single model’s confidence, RAM-APL aggregates signals across multiple FMs to estimate the mean accuracy of pseudo-class labels and rank examples accordingly. This synthesis replaces dataset-dependent IEs with transferable FMs and leverages committee-style agreement to excel on fine-grained data, while also explaining diminished gains on noisy, coarse-grained settings.

---
*Generated: 2026-01-07T00:21:32.397581*
