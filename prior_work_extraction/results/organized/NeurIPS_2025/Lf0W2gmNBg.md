# Prior Work Analysis Report

## Target Paper
**Title:** Lf0W2gmNBg
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EAG3R fuses two influential lines of work: pointmap-based, pose-free 3D reconstruction and event-based perception under challenging imaging conditions. DUSt3R established dense pointmaps from image pairs as a powerful representation for fast, accurate geometry without explicit poses. MonST3R extended this family to better handle dynamics, providing the architectural foundation and training protocol that EAG3R adopts and augments. On the event side, E2VID showed that events complement frames with HDR, low-latency edge information, while EV-FlowNet encoded events into motion-aware features—together motivating EAG3R’s lightweight event encoder and its SNR-aware fusion that selectively trusts events or RGB depending on local reliability.
Crucially, EAG3R introduces an event-based photometric consistency loss to enforce spatiotemporal coherence during global optimization. This objective is conceptually rooted in Gallego et al.’s contrast maximization principles for event cameras, but is tailored to supervise pointmap predictions and cross-time consistency in a differentiable reconstruction pipeline. The overall optimization design echoes the photometric bundle-adjustment paradigm popularized by DROID-SLAM, now adapted to asynchronous event streams. Finally, EAG3R’s retinex-inspired enhancement module draws from Deep Retinex-Net, stabilizing RGB appearance under extreme illumination so that fusion with events is more effective. Together, these works directly inform EAG3R’s core innovations: an event-augmented pointmap framework, reliability-aware RGB-event fusion, and an event-based photometric loss for globally consistent geometry in dynamic, extreme-lighting scenes.

---
*Generated: 2026-01-07T00:21:32.319712*
