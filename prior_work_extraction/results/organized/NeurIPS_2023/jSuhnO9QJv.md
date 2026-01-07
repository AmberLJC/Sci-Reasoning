# Prior Work Analysis Report

## Target Paper
**Title:** jSuhnO9QJv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Spuriosity Rankings advances a practical path to measure and mitigate spurious-cue bias by ranking images within a class according to the strength of human-understandable cues and then training on the least spurious subset. This contribution fuses two lines of prior work: concept-based interpretability and group-robust learning. On the interpretability side, Network Dissection operationalized unit-to-concept mapping and soft segmentation, giving a tool to estimate per-image concept presence; TCAV showed that model behavior can be quantified along human concepts, legitimizing concept-centric bias measurement. Empirical studies on ImageNet’s spurious cues—textures and backgrounds—by Geirhos et al. and Xiao et al. established which cues are problematic and why per-example cue measurement is meaningful. On the robustness side, IRM and Group DRO formalized avoiding spurious correlations via invariance and worst-group performance, but typically require environment or group labels. Methods like Learning from Failure (LfF) demonstrated that emphasizing bias-conflicting samples can improve robustness without group annotations. Spuriosity Rankings synthesizes these strands by constructing a concept-driven spuriosity score that implicitly induces subpopulations (low vs high spuriosity), enabling both an informative bias metric (accuracy gap) and a simple mitigation (head finetuning on low-spuriosity images) that mirrors the benefits of group-aware methods without needing group labels or costly retraining. The result is a lightweight, data-sorting approach that leverages interpretable features to directly target spurious correlations at scale.

---
*Generated: 2026-01-07T00:02:04.806845*
