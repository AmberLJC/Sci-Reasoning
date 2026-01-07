# Prior Work Analysis Report

## Target Paper
**Title:** qPx3i9sMxv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**SoundSpaces 2.0: A Simulation Platform for Audio-Visual Navigation in Complex 3D Environments** (2022)
- *Authors:* Changan Chen et al.
- *Connection:* The BEWO-1M simulation pipeline draws on SoundSpaces 2.0’s principles of controllable, physics-based spatial rendering with moving and multiple sources, which we repurpose at scale for stereo training data.

**Self-Supervised Generation of Spatial Audio for 360° Video** (2018)
- *Authors:* Pedro Morgado et al.
- *Connection:* This work formulated data-driven spatial audio generation (ambisonics/binaural) but relied on video; we generalize the problem to language (and optional images) and scale to multi-source, moving soundscapes.

### 💡 Inspiration

**WavCaps: A ChatGPT-Assisted Weakly-Labelled Audio Captioning Dataset and Benchmark for Audio-Language Learning** (2023)
- *Authors:* Xinhao Mei et al.
- *Connection:* BEWO-1M explicitly builds on WavCaps’ GPT-assisted curation paradigm, extending it to generate rich spatial and motion-aware descriptions that supervise stereo/spatial audio generation.

**Learning to Binauralize in the Wild** (2019)
- *Authors:* Ruohan Gao et al.
- *Connection:* Mono2Binaural established learning-based binauralization and highlighted the centrality of interaural cues and azimuth; SpatialSonic internalizes these cues via spatial-aware encoders and azimuth-state guidance within a generative diffusion model.

### 🔍 Gap Identification

**AudioGen: Textually Guided Audio Generation** (2022)
- *Authors:* Felix Kreuk et al.
- *Connection:* As a leading text-to-audio system producing mono waveforms without controllable spatial placement, AudioGen exemplifies the gap this work targets—accurate, language-driven stereo spatialization.

### 📊 Baseline

**AudioLDM: Text-to-Audio Generation with Latent Diffusion Models** (2023)
- *Authors:* Haohe Liu et al.
- *Connection:* SpatialSonic adopts AudioLDM’s latent diffusion pipeline for text-to-audio and directly augments it with spatial-aware encoders plus explicit azimuth-state conditioning to overcome AudioLDM’s mono-only, spatially-indistinct outputs.

### 🔧 Extension

**LAION-CLAP: Open Large-Scale Contrastive Language-Audio Pretraining** (2023)
- *Authors:* Yusong Wu et al.
- *Connection:* We start from CLAP-style audio–text contrastive encoders for semantic conditioning and extend them with spatial-aware representations so that conditioning preserves azimuth/interaural cues that vanilla CLAP discards.

---

## Synthesis

Both Ears Wide Open’s core innovation—language-driven, controllable stereo spatial audio generation—emerges from fusing latent diffusion with explicit spatial conditioning and a scalable, simulation-based, GPT-assisted corpus. AudioLDM provides the immediate generative backbone and conditioning paradigm for text-to-audio diffusion, but its mono outputs and lack of spatial control define a clear gap that the authors directly address. AudioGen further crystallizes this limitation among strong baselines: mono waveforms without controllable spatial placement. To make spatial control feasible at scale, the dataset contribution BEWO-1M follows WavCaps’ ChatGPT-assisted curation strategy, extending it to encode spatial attributes (azimuth, motion, multiplicity) critical for supervising spatial generation. On the rendering side, SoundSpaces 2.0 offers the conceptual and practical foundation for large-scale, controllable simulation with moving and multiple sources, which BEWO adapts to mass-produce stereo training data. Methodologically, classic spatialization works—Mono2Binaural and Morgado et al.’s 360° spatial audio generation—demonstrate how interaural cues and azimuth/ambisonics structure enable learning-based spatial audio; the present work transposes those insights into a generative diffusion setting and removes the reliance on video inputs. Finally, CLAP-style audio–text encoders enable semantic conditioning but are spatially agnostic; SpatialSonic explicitly extends them with spatial-aware encoders and azimuth-state modeling, yielding precise spatial guidance that turns previously random, indistinct stereo outputs into controlled, language-aligned spatial soundscapes.

---
*Generated: 2026-01-06T23:08:23.934443*
