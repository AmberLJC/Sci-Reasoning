# Prior Work Analysis Report

## Target Paper
**Title:** zwCb9cKHpd
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

SAVVY’s core contribution—a training-free, two-stage pipeline that unifies spatial audio and visual cues for egocentric 3D spatial reasoning, coupled with a benchmark for dynamic scenes—emerges at the intersection of three lines of prior work. First, audio-visual correspondence and spatial audio localization laid the sensing foundations. Look, Listen and Learn demonstrated that synchronized audio and vision can localize sounding objects, while SELDnet established reliable direction-of-arrival estimation from ambisonic inputs, the precise primitive SAVVY exploits to stabilize egocentric tracks with directional cues. SoundSpaces further validated that physically grounded, spatialized audio in 3D environments enables stronger embodied spatial reasoning, motivating SAVVY-Bench’s synchronized spatial audio. Second, egocentric mapping methods, epitomized by ORB-SLAM2, showed how to build consistent global frames without task-specific training; SAVVY’s Dynamic Global Map Construction echoes these ideas to fuse multi-object trajectories over time into a coherent global map. Third, instruction-following multimodal LLMs catalyzed controllable reasoning over rich inputs: LLaVA established visual instruction tuning, and AudioGPT extended LLMs to audio, together informing SAVVY’s use of AV-LLMs to parse queries and guide track selection and temporal grounding. Finally, Ego4D highlighted the demands of egocentric, dynamic, temporally grounded queries, shaping SAVVY-Bench’s focus on moving objects and fine-grained temporal reasoning. Combined, these works directly scaffold SAVVY’s sensing primitives, mapping strategy, and instruction-driven, training-free reasoning design.

---
*Generated: 2026-01-07T00:21:32.324579*
