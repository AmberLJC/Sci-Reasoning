# Prior Work Analysis Report

## Target Paper
**Title:** 0KnZasL9nA
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

DERD-Net’s core innovation is to encode event streams into disparity-space images (DSIs) that measure spatial ray densities from back-projected events and to learn depth with a hybrid 3D-convolutional and recurrent architecture operating locally on these volumes. This design fuses two lines of prior work. On the geometric side, Collins’ plane-sweep stereo established the DSI as a powerful representation for multi-view depth reasoning, later adapted to events by EMVS, which back-projected events with known poses to accumulate volumetric evidence and extract depth at peaks. The contrast maximization framework for event cameras provided the unifying principle that correct geometric hypotheses align events to yield high-contrast, high-density accumulations—precisely the signal DERD-Net learns to parse in ray-density DSIs.
On the learning side, GC-Net demonstrated that 3D CNNs can regularize and infer disparity directly from cost volumes, while R-MVSNet introduced recurrent processing to scale volume inference efficiently without sacrificing detail. DERD-Net borrows these architectural insights, tailoring them to the sparser, asynchronous statistics of event-derived DSIs and enabling local, parallelizable subregion inference. Finally, EST evidenced that event data can be structured into tensors amenable to 3D convolutional learning, motivating DERD-Net’s learned processing of an event-specific volumetric representation. Together, these works directly shape DERD-Net’s formulation: event-driven DSI construction from geometric back-projection, and deep 3D/recurrent aggregation for fast, accurate, monocular and stereo depth from events.

---
*Generated: 2026-01-06T23:42:48.161382*
