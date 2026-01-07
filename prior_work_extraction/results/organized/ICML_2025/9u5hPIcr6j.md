# Prior Work Analysis Report

## Target Paper
**Title:** 9u5hPIcr6j
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LotteryCodec reframes single-image compression as the problem of discovering an image-specific subnetwork within a shared, randomly initialized backbone and transmitting only the binary mask. This synthesis builds on two converging lines of work. From the sparsity-in-networks literature, the Lottery Ticket Hypothesis posited that performant sparse subnetworks exist within dense models, while follow-ups showed that such subnetworks can be identified even in randomly initialized networks by optimizing only masks. Supermasks further demonstrated that different masks can encode different functionalities within a single backbone, directly motivating the idea of using the mask itself as the compact code that carries image statistics. Stabilizing techniques such as weight rewinding informed LotteryCodec’s rewind modulation, an analogue that regularizes subnetwork search to improve rate–distortion trade-offs.

Concurrently, untrained-network image modeling established that network structure alone provides a strong prior. Deep Image Prior and Deep Decoder showed that optimizing an untrained generator per image can yield high-quality reconstructions and compact representations—core precedents for overfitted, single-image neural codecs. Implicit neural representation advances like SIREN validated the expressivity of over-parameterized coordinate networks, supporting the premise that a randomly initialized, shared backbone contains subnetworks capable of high-fidelity synthesis. By uniting these strands, LotteryCodec replaces weight optimization and transmission with mask discovery and coding, enabling competitive RD performance and adaptive decoding complexity via controllable mask ratios.

---
*Generated: 2026-01-07T00:21:32.379841*
