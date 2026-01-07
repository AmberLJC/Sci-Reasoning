# Prior Work Analysis Report

## Target Paper
**Title:** 73mDARqOtQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

RAPID’s core contribution—using a retrieval-augmented drafter to accelerate and enhance long-context decoding—rests on two pillars: speculative decoding and retrieval conditioning. The speculative decoding framework of Leviathan et al. provides the acceptance–rejection mechanism and the drafter–verifier architecture that RAPID reuses; the twist is to supply the drafter with a short, high-signal context built via retrieval. Works in retrieval-augmented generation (Lewis et al.) and retrieval-conditioned language modeling at scale (RETRO) validate that targeted retrieval can substitute for wide in-context windows, suggesting a short retrieved context can approximate the predictive distribution of a long-context model well enough to yield high acceptance rates. Concurrently, systems work (vLLM/PagedAttention) establishes that long-context inference is often memory bound due to KV-cache operations, motivating RAPID’s design to relocate most context processing to a small retrieval window for the drafter, alleviating the KV bottleneck. Empirical evidence that models often underutilize long contexts (Lost in the Middle) further supports selecting compact, salient spans for drafting. Finally, dynamic retrieval during generation (Self-RAG) informs how retrieval can be interleaved with token proposal to improve factuality and guidance. Together, these strands directly shape RAPID’s insight: a RAG-powered drafter can be same-scale—or even larger—than the target yet remain efficient by operating on a short retrieved context, achieving both acceleration and quality gains in long-context inference.

---
*Generated: 2026-01-07T00:21:32.389145*
