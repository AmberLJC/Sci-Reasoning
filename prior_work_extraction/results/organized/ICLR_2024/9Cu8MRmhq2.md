# Prior Work Analysis Report

## Target Paper
**Title:** 9Cu8MRmhq2
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Norton tackles long-video temporal learning under multi-granularity noisy correspondences by combining contrastive objectives with a principled optimal transport backbone. Two lines of prior work directly shaped this core idea. First, the emergence of large-scale, weakly aligned video–text pretraining—HowTo100M and its MIL-NCE objective—demonstrated both the promise and the pitfalls of learning from noisy ASR-aligned long videos. VideoCLIP further solidified the use of video–paragraph and clip–caption contrastive formulations on such data, yet relied on heuristics to cope with misalignment. Norton inherits these contrastive structures but replaces heuristic selection with OT-driven matching that can capture long-term dependencies while being robust to noise.
Second, optimal transport theory provided the enabling machinery. Cuturi’s Sinkhorn algorithm made OT practical at scale, while unbalanced OT from Chizat et al. offered a mathematically grounded way to ignore or downweight unmatched mass—precisely what is needed to filter irrelevant clips/captions and handle frame–word mismatches. On the fine-grained side, SCAN showed the effectiveness of token-level cross-modal alignment, which Norton reinterprets through OT to provide softer, noise-aware correspondences. Finally, ALBEF’s align-before-fuse paradigm for noisy web supervision inspired Norton’s alignable-bucket filtering concept, now instantiated with OT rather than momentum distillation. Together, these works converge into Norton’s unified OT framework that jointly addresses coarse (clip–caption) and fine (frame–word) misalignments for efficient long-term video–language learning.

---
*Generated: 2026-01-06T23:42:49.024255*
