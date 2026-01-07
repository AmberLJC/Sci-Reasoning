# Prior Work Analysis Report

## Target Paper
**Title:** Y2RW9EVwhT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Eagle’s core contribution is to systematically explore the mixture-of-encoders design space for multimodal LLMs and distill simple, general principles for expert selection and fusion—most notably, that concatenating tokens from complementary visual experts and resolutions can match more complex routers/resamplers. This builds on two foundational strands. First, Flamingo and BLIP-2 shaped how visual tokens are formed and injected into LLMs—via Perceiver-style resamplers or Q-Former bridges—establishing baselines for token compression and cross-attention. Eagle explicitly probes whether such heavy bridging remains necessary when multiple vision experts are present, and finds minimal projection plus concatenation is often sufficient.
Second, the AnyRes lineage (Qwen-VL, InternVL) demonstrated that multi-resolution tiling and simple token concatenation preserve fine details crucial for OCR and document analysis. Eagle generalizes this beyond multi-scale inputs to heterogeneous experts (e.g., general-purpose vs text-focused), articulating when and how to select complementary encoders and how many tokens to allocate per expert.
Concurrently, models like DeepSeek-VL2 and TextHawk explored multi-granularity cropping and specialized text-reading branches with selective routing. Eagle’s ablations show that much of the reported gains can be captured by careful expert pairing and straightforward token concatenation, simplifying engineering costs. Methodologically, Eagle’s broad, MM1-style analysis provides the missing, principled comparison across expert selection and integration strategies, yielding a streamlined recipe for robust, high-resolution visual perception in MLLMs.

---
*Generated: 2026-01-07T00:02:04.905470*
