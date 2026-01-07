# Prior Work Analysis Report

## Target Paper
**Title:** zQTi3pziFp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Sounding Bodies’ key contribution—a pose-conditioned neural model that reconstructs a full 3D sound field around a speaking human from headset microphones—sits at the intersection of neural implicit representations, human pose modeling, and spatial audio theory/measurement. NeRF established the coordinate-based implicit field paradigm for continuous scene queries, and D-NeRF extended it to dynamic subjects via conditioning on time or deformation. Building on these ideas, Sounding Bodies conditions a neural acoustic field on human pose to capture pose-dependent scattering and diffraction created by limbs and torso during speech. SMPL provides the practical parameterization of human body pose/shape that makes such conditioning tractable.

On the acoustics side, Higher-Order Ambisonics (Daniel, Moreau, Nicol) and spherical harmonic theory define how 3D sound fields can be represented and rendered at arbitrary listener positions. Rafaely’s work on spherical microphone arrays underpins how to sample and reconstruct these fields in practice, directly informing the paper’s unique dataset built with a dense spherical array surrounding the talker. Prior learning-based spatialization efforts such as Mono2Binaural demonstrated that spatial cues can be inferred from limited audio plus auxiliary context; Sounding Bodies generalizes this concept from binaural outputs to a full volumetric sound field using pose instead of image cues. Finally, the CIPIC HRTF database anchored the community’s understanding of head-related filtering; the present work extends this line from head-only HRTFs to full-body acoustic effects, replacing exhaustive measurements with a learned, pose-aware field.

---
*Generated: 2026-01-07T00:02:04.838655*
