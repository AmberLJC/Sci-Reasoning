# Prior Work Analysis Report

## Target Paper
**Title:** Zd6VyjmN1S
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ElasticMM’s core contribution—Elastic Multimodal Parallelism (EMP) for efficient MLLM serving—rests on two pillars: the modular multimodal model design and the systems techniques that exploit stage heterogeneity. LLaVA and BLIP-2 crystallized the modern MLLM architecture: heavy modality-specific feature extractors and projection/bridging modules feeding a frozen or shared LLM. This separation exposes distinct inference stages with divergent compute and memory profiles, motivating ElasticMM’s modality-aware load balancer and explicit decoupling of encoders/bridges from the LLM decoder. On the systems side, Megatron-LM and PipeDream provide the foundational vocabulary of tensor and pipeline parallelism and the need for stage-aware throughput balancing. ElasticMM translates these training-centric ideas to serving-time elasticity, choosing and resizing parallelism per stage (and per modality) to reduce time-to-first-token and improve utilization under mixed workloads. Alpa’s automatic placement and parallelism search further inform ElasticMM’s dynamic reconfiguration across heterogeneous resources, enabling rapid adaptation as the request mix shifts between images, video, audio, and text-only. Finally, vLLM and FlashAttention supply crucial runtime enablers at the decode stage—paged KV caching, efficient batching, and IO-aware attention kernels—freeing memory and compute that ElasticMM can reallocate elastically to upstream modality pipelines. Together, these works directly shape ElasticMM’s design: a decoupled, stage-specialized, and elastically scheduled serving stack tuned to the unique heterogeneity of multimodal LLM inference.

---
*Generated: 2026-01-07T00:05:12.536573*
