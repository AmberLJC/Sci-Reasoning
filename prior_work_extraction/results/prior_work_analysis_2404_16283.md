# Prior Work Analysis Report

## Target Paper

**Title:** Andes: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services

**arXiv ID:** [2404.16283](https://arxiv.org/abs/2404.16283)

**Abstract:** 
> Large language models (LLMs) are now at the core of conversational AI services such as real-time translation and chatbots, which provide live user interaction by incrementally streaming text to the user. However, existing LLM serving systems fail to provide good user experience because their optimization metrics are not always aligned with user experience.   In this paper, we first introduce and define the notion of Quality-of-Experience (QoE) for text streaming services by considering each user's end-to-end interaction timeline. Based on this, we propose Andes, a QoE-aware LLM serving system that enhances user experience by ensuring that users receive the first token promptly and subsequent tokens at a smooth, digestible pace, even during surge periods. This is enabled by Andes's preemptive request scheduler that dynamically prioritizes requests at the token granularity based on each request's expected QoE gain and GPU resource usage. Our evaluations demonstrate that, compared to state-of-the-art LLM serving systems, Andes improves the average QoE by up to $4.7\times$ given the same GPU resource, or saves up to 61% GPU resources while maintaining the same high QoE.

---

## Key Prior Works (6 papers with direct influence)

### 🏷️ Inspiration

**Neural Adaptive Video Streaming with Pensieve** (2017)
- *Authors:* Hongzi Mao et al.
- *Direct Connection:* Pensieve’s explicit QoE formulation balancing startup delay, rebuffering, and smoothness directly inspired Andes’s analogous QoE definition for text streaming (first-token promptness and digestible, smooth token pace).

**BOLA: Near-Optimal Bitrate Adaptation for Online Videos** (2016)
- *Authors:* Stefano Petrangeli Spiteri et al.
- *Direct Connection:* BOLA’s marginal-utility view of segment choices and emphasis on smoothness informed Andes’s notion of per-token marginal QoE gain and the need to avoid bursty, hard-to-digest output rates.

### 🏷️ Gap Identification

**InferLine: ML Inference Pipeline Composition with End-to-End Latency SLOs** (2020)
- *Authors:* Isaac Crankshaw et al.
- *Direct Connection:* InferLine’s SLO-centric scheduling underscored the limitation of meeting latency targets without modeling user-perceived utility over the full interaction timeline, a gap Andes addresses with an explicit QoE objective.

### 🏷️ Baseline

**Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM)** (2023)
- *Authors:* Kwon et al.
- *Direct Connection:* This system’s continuous batching and throughput-oriented scheduling provide the dominant serving baseline that Andes directly departs from by replacing throughput/latency proxies with token-granular prioritization based on expected QoE gain.

**SGLang: Efficient Execution Engine for Structured Language Model Programs** (2024)
- *Authors:* Lianmin Zheng et al.
- *Direct Connection:* SGLang’s optimized prefill/decode execution and batching policies serve as a high-performance baseline that focuses on system efficiency rather than user-perceived smoothness, motivating Andes’s shift to QoE-aware token-level scheduling.

### 🏷️ Related Problem

**Size-Based Scheduling to Improve Web Performance** (2003)
- *Authors:* Mor Harchol-Balter et al.
- *Direct Connection:* This work’s preemptive, size-aware scheduling insights (e.g., SRPT-style prioritization) informed Andes’s token-granularity preemption policy that favors actions with the highest immediate QoE gain per unit of GPU time.

---

## Synthesis: How Prior Work Led to This Paper

Throughput-oriented LLM serving systems like vLLM introduced continuous batching and memory-efficient PagedAttention to maximize tokens-per-second, and SGLang further streamlined prefill/decode execution with high-performance batching and caching policies. These systems excel at raw efficiency but optimize proxy metrics rather than modeling how users experience streamed text. In contrast, the adaptive bitrate (ABR) literature explicitly defined and optimized user-centric Quality-of-Experience (QoE): Pensieve formalized a QoE function combining startup delay, rebuffering, and smoothness, and learned policies that trade off early start versus consistent playback; BOLA framed bitrate selection via marginal utility and emphasized avoiding burstiness that harms perception. Meanwhile, inference pipeline schedulers such as InferLine focused on meeting end-to-end latency SLOs across models, revealing a gap between hitting deadlines and optimizing perceived utility over an interaction. Finally, size-based, preemptive scheduling work in web systems (e.g., SRPT-style insights) demonstrated the benefits of preemption and prioritizing high-payoff work units to minimize perceived wait. Taken together, these strands highlighted an opportunity: import ABR-style QoE modeling into token-streamed LLM interactions and couple it with preemptive, fine-grained scheduling. Building on high-throughput batching engines, a natural next step is to prioritize tokens by expected marginal QoE gain per unit GPU time, ensuring fast first tokens and smooth, digestible pacing under load rather than solely maximizing aggregate throughput.

---

*Analysis generated on: 2026-01-06T05:37:56.260221*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
