# Prior Work Analysis Report

## Target Paper
**Title:** paRLw86ONU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DANCE’s core innovation—ante-hoc, disentangled concept-based reasoning for video actions—sits at the intersection of concept supervision, motion–appearance separation, and language-driven semantics. Concept Bottleneck Models provided the central blueprint for enforcing predictions through human-aligned concepts, which DANCE extends to the video domain by explicitly partitioning the bottleneck into motion dynamics, objects, and scenes. The longstanding two-stream paradigm crystallized the need to separate motion from spatial context; DANCE pushes this further by elevating the separation from feature streams to interpretable concept types. For motion, the skeleton-action literature, epitomized by ST-GCN, demonstrated that pose sequences effectively capture human dynamics. DANCE adopts this representation directly as its motion concepts, operationalized in practice by robust keypoint extraction methods such as OpenPose.
At the same time, DANCE recognizes that spatial context—objects and scenes—is best structured via language priors. Inspired by language-supervised vision like CLIP and the broader trend of LLM-guided semantic structuring, DANCE uses an LLM to automatically enumerate object and scene concepts tied to each action class. This stands in contrast to prior explanatory paradigms: saliency methods such as Grad-CAM provide post-hoc, entangled heatmaps, while textual justification methods show that language alone often struggles to express tacit motion. By unifying these threads, DANCE converts the two-stream intuition into a concept bottleneck with explicit motion (pose), object, and scene concepts, yielding faithful, disentangled explanations and competitive recognition performance.

---
*Generated: 2026-01-07T00:21:32.313200*
