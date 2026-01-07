# Prior Work Analysis Report

## Target Paper
**Title:** aYRNINhNGV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Meta CLIP 2’s core innovation—a practical, from-scratch recipe for training CLIP on worldwide web-scale data that avoids the common English performance drop—sits at the intersection of three idea streams. First, CLIP and ALIGN established the dual-encoder contrastive framework and demonstrated that massive, noisy web data can yield strong zero-shot transfer. Second, LAION-5B operationalized open, multilingual-scale data collection and filtering, showing how language detection, deduplication, and quality scoring can make web corpora trainable. Third, DataComp proved that data curation and sampling policies are the dominant levers for CLIP quality, motivating Meta CLIP 2’s rigorous ablations and minimal-change philosophy.

MetaCLIP, the direct predecessor, provided an English-centric recipe tying together data filtering, sampling, and training choices. Meta CLIP 2 extends this recipe to the global setting by introducing multilingual-aware filtering and balancing that let non-English data improve English and cross-lingual transfer simultaneously. Insights from SigLIP’s objective design guide robust optimization under noisy, heterogeneous sources, an important factor when mixing many languages and domains. Finally, early multilingual adaptations like M-CLIP both motivated the need and exposed the pitfall: naïvely adding multilingual supervision often harms English performance. Meta CLIP 2 directly tackles this with data-centric strategies—cross-lingual quality control, balanced sampling, and careful loss/training choices—delivering a simple scaling recipe where English and non-English data are mutually beneficial.

---
*Generated: 2026-01-07T00:21:32.241923*
