# Prior Work Analysis Report

## Target Paper

**Title:** DMV3D: Denoising Multi-view Diffusion Using 3D Large Reconstruction Model

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yinghao Xu, Hao Tan, Fujun Luan, Sai Bi, Peng Wang, Jiahao Li, Zifan Shi, Kalyan Sunkavalli, Gordon Wetzstein, Zexiang Xu, Kai Zhang

**Keywords:** 3D Generation; Single-view 3D Reconstruction; text-to-3D

**Abstract:** 
> We propose DMV3D, a novel 3D generation approach that uses a transformer-based 3D large reconstruction model to denoise multi-view diffusion. Our reconstruction model incorporates a triplane NeRF representation and, functioning as a denoiser, can denoise noisy multi-view images via 3D NeRF reconstruction and rendering, achieving single-stage 3D generation in the 2D diffusion denoising process. We train DMV3D on large-scale multi-view image datasets of extremely diverse objects using only image r...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**EG3D: Efficient Geometry-aware 3D Generative Adversarial Networks** (2022)
- *Authors:* Eric R. Chan et al.
- *Direct Connection:* DMV3D adopts EG3D’s tri-plane representation as the core 3D backbone for reconstruction and rendering inside the denoising loop to maintain geometry-aware multi-view consistency.

**Zero-1-to-3: Zero-shot One Image to 3D** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* Zero-1-to-3 established single-image–conditioned diffusion for novel-view synthesis, which DMV3D generalizes by performing multi-view denoising through an explicit 3D reconstructor for stronger geometric coherence.

**DreamFusion: Text-to-3D using 2D Diffusion** (2022)
- *Authors:* Ben Poole et al.
- *Direct Connection:* DreamFusion showed how 2D diffusion priors can drive 3D generation, a paradigm DMV3D operationalizes in a single denoising stage by embedding a 3D reconstruction model into the diffusion process for text-to-3D.

### 🔍 Gap Identification

**SyncDreamer: Generating Multiview-Consistent Images from a Single-View** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* By relying on cross-view attention in a 2D diffusion model, SyncDreamer exposes the limitation of lacking explicit 3D structure, which DMV3D resolves by reconstructing and rendering a NeRF during denoising.

### 📊 Baseline

**MVDream: Multi-view Diffusion for 3D Generation** (2023)
- *Authors:* Zifan Shi et al.
- *Direct Connection:* DMV3D targets the same multi-view diffusion setting as MVDream but replaces the 2D image denoiser with a 3D reconstruction denoiser to address MVDream’s cross-view inconsistency.

### 🔧 Extension

**LRM: Large Reconstruction Model for Single-View 3D Reconstruction** (2023)
- *Authors:* Hong-Xing Yu et al.
- *Direct Connection:* DMV3D directly extends LRM’s transformer-based tri-plane NeRF reconstructor by repurposing it as the diffusion denoiser, enabling single-stage 3D generation during multi-view denoising.

---

## Synthesis: How Prior Work Led to This Paper

A transformer-based large reconstruction model demonstrated that a single image can be lifted to a tri-plane NeRF by predicting geometry-aware features and rendering them differentiably, establishing a scalable recipe for image-supervised 3D reconstruction without requiring explicit 3D assets. The tri-plane representation popularized by EG3D made this efficient by factoring 3D fields into three orthogonal feature planes that render quickly while preserving geometry, making it a practical backbone for large-scale training. Multi-view diffusion models such as MVDream showed that generating multiple views jointly improves cross-view consistency, yet their denoisers operate purely in 2D image space and still suffer from geometric drift. SyncDreamer improved synchronization across views via cross-view attention, but without an explicit 3D representation its consistency is fundamentally limited. Zero-1-to-3 introduced single-image–conditioned diffusion for novel view synthesis, revealing the power of diffusion priors for view completion but without enforcing a global 3D shape. DreamFusion established that 2D diffusion priors can supervise 3D via rendering, kickstarting diffusion-guided 3D generation.
Synthesizing these threads, a clear opportunity emerges: marry the efficiency and scalability of tri-plane reconstruction with the cross-view modeling of multi-view diffusion, but inject explicit 3D structure into the denoiser itself. By turning a large tri-plane reconstructor into the denoising operator, the method performs single-stage 3D generation during diffusion, trained with image reconstruction alone, thereby overcoming 2D denoiser limitations and naturally extending to text-to-3D with stronger geometric fidelity.

---

*Analysis generated on: 2026-01-07T00:09:22.663907*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
