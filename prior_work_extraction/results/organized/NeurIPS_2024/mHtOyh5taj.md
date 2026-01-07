# Prior Work Analysis Report

## Target Paper
**Title:** mHtOyh5taj
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core idea—teaching a large multimodal model to make relative image-quality comparisons and then translating those into continuous scores—sits at the intersection of instruction-tuned LMMs, preference learning, and IQA. InstructBLIP established that vision-language models can be reliably guided by carefully designed instructions; this work extends that recipe to comparative IQA by scaling instruction data through within-dataset pairings. From the perceptual side, LPIPS showed that pairwise human judgments (2AFC) yield robust supervision for perceptual metrics, encouraging a shift from noisy absolute MOS labels to relative comparisons. The statistical backbone for turning comparisons into continuous quality arises from the Bradley–Terry model and Bayesian extensions like TrueSkill, which formalize win probabilities and aggregation across multiple references—mirroring the paper’s soft-comparison inference that estimates how often a test image would be preferred. Finally, traditional NR-IQA methods such as BRISQUE and modern deep approaches like NIMA exemplify the absolute-rating paradigm that this paper seeks to overcome, motivating the need for a more adaptable, cross-dataset strategy. Collectively, these works enable the study’s two-step innovation: instruction-tuning an LMM as a human-like quality comparator and principled aggregation of relative preferences into a stable continuous quality score.

---
*Generated: 2026-01-06T23:42:49.047569*
