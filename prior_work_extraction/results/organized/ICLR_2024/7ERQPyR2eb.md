# Prior Work Analysis Report

## Target Paper

**Title:** Real3D-Portrait: One-shot Realistic 3D Talking Portrait Synthesis

**Conference:** ICLR 2024 (spotlight)

**Authors:** Zhenhui Ye, Tianyun Zhong, Yi Ren, Jiaqi Yang, Weichuang Li, Jiawei Huang, Ziyue Jiang, Jinzheng He, Rongjie Huang, Jinglin Liu, Chen Zhang, Xiang Yin, Zejun MA, Zhou Zhao

**Keywords:** One-shot Talking Face Generation, Neural Radiance Field

**Abstract:** 
> One-shot 3D talking portrait generation aims to reconstruct a 3D avatar from an unseen image, and then animate it with a reference video or audio to generate a talking portrait video. The existing methods fail to simultaneously achieve the goals of accurate 3D avatar reconstruction and stable talking face animation. Besides, while the existing works mainly focus on synthesizing the head part, it is also vital to generate natural torso and background segments to obtain a realistic talking portrai...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**EG3D: Efficient Geometry-aware 3D Generative Adversarial Networks** (2022)
- *Authors:* Eric R. Chan et al.
- *Direct Connection:* Real3D-Portrait’s large image-to-plane module directly regresses tri-plane features by distilling geometry and appearance priors from a pretrained EG3D-like 3D face generator, making one-shot 3D avatar reconstruction feasible.

**AD-NeRF: Audio Driven Neural Radiance Fields for Talking Head Synthesis** (2021)
- *Authors:* Yudong Chen et al.
- *Direct Connection:* AD-NeRF established the audio-to-expression conditioning of a radiance field that Real3D-Portrait generalizes via an efficient motion adapter to support robust, one-shot audio-driven animation.

**NeRFace: Dynamic Neural Radiance Fields for Modeling Face Expressions** (2021)
- *Authors:* Guy Gafni et al.
- *Direct Connection:* NeRFace’s pose- and expression-conditioned NeRF provides the motion-control formulation that Real3D-Portrait adapts, using an explicit adapter to fuse video-/audio-derived motion signals for stable driving.

**DECA: Detailed Expression Capture and Animation** (2021)
- *Authors:* Yao Feng et al.
- *Direct Connection:* Real3D-Portrait relies on DECA-style 3DMM codes for estimating and representing facial pose/expression, which the motion adapter consumes to produce accurate motion-conditioned animation from one shot.

### 🔍 Gap Identification

**GeneFace++: Improving Audio-Driven 3D Talking Head Synthesis** (2023)
- *Authors:* Yi Ren et al.
- *Direct Connection:* Although enhancing lip articulation and quality, GeneFace++ remains head-focused and exhibits residual jitter, gaps that Real3D-Portrait targets with motion-adapter stabilization and explicit torso/background synthesis.

### 📊 Baseline

**GeneFace: Generalizable and Efficient NeRF-based Audio-Driven Talking Head Synthesis** (2023)
- *Authors:* Yi Ren et al.
- *Direct Connection:* GeneFace is the primary baseline for one-shot, generalizable NeRF-based talking heads that Real3D-Portrait improves upon by addressing GeneFace’s weaker single-image 3D reconstruction and animation stability.

---

## Synthesis: How Prior Work Led to This Paper

EG3D introduced a 3D-aware GAN with a tri-plane scene representation, enabling high-fidelity, 3D-consistent faces and making it practical to regress 3D features from a single image by leveraging strong generative priors. AD-NeRF demonstrated that audio features can drive a radiance field to synthesize talking heads, establishing the core audio-to-expression conditioning pathway for 3D neural rendering. NeRFace formalized conditioning a dynamic NeRF on pose and expression codes, providing a clear motion-control interface that separates identity from driving signals. DECA provided a robust route to recover 3DMM-based pose and expression parameters from images or video, yielding reliable motion representations widely used to drive 3D face models. Building on these, GeneFace showed that a generalizable NeRF conditioned on identity and motion could achieve one-shot audio-driven talking head synthesis, while GeneFace++ further improved lip articulation and quality but remained primarily head-focused and prone to residual jitter in challenging scenarios.
Taken together, these works exposed a gap: generalizable talking heads lacked accurate one-shot 3D reconstruction and stable long-horizon animation, and most pipelines ignored realistic torso dynamics and background control. Real3D-Portrait naturally synthesizes these threads by distilling EG3D-style 3D face priors into a large image-to-plane encoder for precise single-image 3D reconstruction; adopting a motion-control interface inspired by NeRFace/AD-NeRF but inserting an efficient adapter that robustly maps audio/video-derived 3DMM motion into stable NeRF dynamics; and extending beyond the head with a head–torso–background super-resolution module to deliver coherent upper-body motion and switchable backgrounds, directly addressing the limitations revealed by GeneFace/GeneFace++.

---

*Analysis generated on: 2026-01-07T00:30:28.713842*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
