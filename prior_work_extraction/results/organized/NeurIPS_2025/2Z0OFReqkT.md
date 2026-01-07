# Prior Work Analysis Report

## Target Paper
**Title:** 2Z0OFReqkT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

UMoE’s core contribution—unifying attention and FFN under a single MoE design with shared experts—stands on two converging lines of prior work. First, sparse conditional computation matured through MoE research in Transformers. The seminal MoE layer of Shazeer et al. introduced sparse expert routing, later operationalized at scale in Transformers by GShard. Switch Transformers simplified routing to top-1, improving stability and efficiency, while Expert Choice refined routing and load balancing. These works established FFN-MoE as the standard scalable path but left attention largely outside the MoE umbrella, in part due to specialized implementations and poorer performance of attention-MoE variants.

Second, a stream of results reframed attention as structures closer to feed-forward mixing. Linear attention factored softmax attention into kernelized linear maps and associative contractions, and Synthesizer showed that learned parametric mixing can substitute for dot-product attention. Together they imply that attention can be expressed with FFN-like operations, opening the door to reuse MoE machinery. Finally, ALBERT’s success with parameter sharing provided a blueprint for compressing models without sacrificing quality.

UMoE synthesizes these trajectories: it reformulates attention to expose an FFN-like computational path, applies proven MoE routing and balancing uniformly to both attention and FFN, and enables expert sharing across the two. This yields attention-based MoE layers that are competitive with FFN-MoE while reducing implementation divergence and improving parameter efficiency.

---
*Generated: 2026-01-07T00:21:32.263323*
