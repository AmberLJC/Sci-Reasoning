# Prior Work Analysis Report

## Target Paper
**Title:** AVd7DpiooC
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

QKFormer fuses three intellectual streams to close the SNN–ANN performance gap while retaining neuromorphic efficiency. From the vision-transformer lineage, ViT provides the token/patch-embedding blueprint, while Swin introduces a hierarchical, multi-scale token design. QKFormer adopts both: it keeps a ViT-like tokenization but varies token counts across blocks in Swin’s spirit to realize scalable, multi-resolution spiking representations.
From efficient attention, linear-attention work demonstrated that moving away from quadratic dot-product attention is pivotal for scalability. QKFormer’s spike-form Q–K attention follows this trajectory but reframes it for SNNs: queries and keys are binary spike vectors, enabling linear-time computations and memory savings tailored to event-driven hardware.
From neuromorphic learning, surrogate-gradient training provides the mechanism for direct optimization of spiking modules, and residual SNN designs (e.g., SEW-ResNet) highlight the importance of carefully engineered shortcuts to preserve and mix temporal-spatial information. QKFormer’s SPEDS extends these ideas with a deformed shortcut to stabilize and enrich spiking patch embeddings.
Finally, early spiking transformers established the feasibility of attention within SNNs; QKFormer advances that paradigm with a binary Q–K mechanism that exploits XNOR/popcount-style efficiency from binary networks, translating proven bitwise compute gains into the attention core. Together, these prior works converge to enable QKFormer’s linear-complexity, hierarchical spiking transformer with improved energy efficiency and accuracy.

---
*Generated: 2026-01-06T23:33:36.278508*
