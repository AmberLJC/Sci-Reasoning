# Prior Work Analysis Report

## Target Paper
**Title:** 4QVLKwgg3S
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

SpecEdge’s key contribution—an edge-assisted serving framework that splits LLM inference via speculative decoding while exchanging only tokens—emerges at the intersection of speculative decoding algorithms and high-throughput serving systems. The foundational catalyst is speculative decoding, which introduced drafting by a cheap model and verification by a strong model; SpecEdge translates this primitive into a cross-device protocol, placing the drafter on consumer-grade edge GPUs and constraining communication to token streams for WAN efficiency. Advances like Medusa and EAGLE refined drafting efficiency and acceptance rates; SpecEdge leverages these insights to design proactive edge drafting depths that maximize accepted tokens given network latency and server load, overlapping edge generation with server verification to reduce per-token latency. On the systems side, vLLM established continuous batching and KV-aware scheduling to keep accelerators saturated; SpecEdge adapts these ideas to a two-tier pipeline, interleaving server-side verification across many users while edge devices independently draft future tokens. DistServe showed that disaggregation and token-centric interfaces can unlock utilization gains; SpecEdge applies a similar philosophy across the edge–cloud boundary, avoiding bulky activation transfers. Finally, classic split-computing from Neurosurgeon provides the architectural precedent for collaborative edge–cloud intelligence, which SpecEdge tailors to the autoregressive, token-stepped nature of LLM serving. Together, these works directly inform SpecEdge’s proactive drafting, token-only communication, and pipeline-aware scheduling that yield higher server throughput and better cost efficiency.

---
*Generated: 2026-01-07T00:21:32.260191*
