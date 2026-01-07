# Prior Work Analysis Report

## Target Paper
**Title:** 36cKp4tsHF
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Deno-IF’s core innovation—unsupervised noisy IR–visible fusion via a convolutional low-rank decomposition and a unified denoising–fusion network—rests on two intertwined lines of prior work. First, classic low-rank modeling (RPCA and LRR) established that clean structure can be isolated from corruption by enforcing low-rankness. Deno-IF adapts this principle to the convolutional/feature domain, aligning with Hankel/ALOHA-style insights that convolutionally lifted representations become low rank for structured signals. This directly motivates both the optimization module that extracts clean components from only noisy inputs and the explicit convolutional low-rankness loss that stabilizes training.
Second, unsupervised learning for restoration and fusion demonstrated that paired clean/fused targets are unnecessary. Noise2Noise showed denoising can be learned from noisy observations alone, while DenseFuse and U2Fusion pioneered unsupervised IR–visible fusion with reconstruction/structure constraints. Deno-IF synthesizes these by learning from noisy sources, but unlike prior fusion networks, it couples intra-modal recovery (denoising) and inter-modal fusion within a single architecture, guided by a principled low-rank prior. Finally, the Plug-and-Play paradigm informs the systemic integration of denoising as a regularizer inside a larger inverse task, mirroring Deno-IF’s joint design where denoising and fusion mutually reinforce each other. Together, these works directly scaffold Deno-IF’s two key modules: convolutional low-rank decomposition without supervision, and an efficient unified network that simultaneously denoises and fuses under a low-rankness constraint.

---
*Generated: 2026-01-07T00:05:12.526355*
