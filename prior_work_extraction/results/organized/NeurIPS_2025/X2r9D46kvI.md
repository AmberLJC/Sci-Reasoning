# Prior Work Analysis Report

## Target Paper
**Title:** X2r9D46kvI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

MOSPA’s core contribution—generating human motion driven by spatial audio and introducing a spatial audio–motion dataset—emerges from unifying three research threads: diffusion-based motion synthesis, audio-conditioned motion generation, and machine learning with spatial audio representations. On the generative side, the Human Motion Diffusion Model (MDM) provides the denoising diffusion framework and conditioning mechanics that MOSPA extends to audio-conditioned, sequence-level motion. Prior audio-to-motion works, notably Ginosar et al., showed that raw audio carries useful prosodic structure for gesture synthesis and established evaluation practices; dance generation lines (AIST++, EDGE) demonstrated how to pair high-fidelity motion capture with temporally aligned audio and how to leverage beat/rhythm features to assess synchronization and realism. MOSPA generalizes these insights from monaural/music signals to spatial audio by conditioning on features that encode direction and distance so the body orients, attends, and moves relative to sound sources.
Concurrently, spatial audio ML (SoundSpaces; SELD with ambisonics) standardized FOA/binaural renderings and DOA estimation, offering learnable representations of interaural cues and room acoustics. MOSPA operationalizes these cues as conditioning features, tying acoustic directionality to kinematic responses (e.g., head yaw, torso turn, stepping toward/away from sources). The SAM dataset design follows the audio–motion alignment and benchmarking practices of music/gesture datasets while capturing spatial metadata, enabling new spatial-consistency metrics. Together, these works directly shaped MOSPA’s dataset construction, spatial-audio feature design, and diffusion-based conditioning to realize spatially faithful human motion generation.

---
*Generated: 2026-01-07T00:21:32.314712*
