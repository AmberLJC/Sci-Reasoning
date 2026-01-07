# Prior Work Analysis Report

## Target Paper

**Title:** How I Warped Your Noise: a Temporally-Correlated Noise Prior for Diffusion Models

**Conference:** ICLR 2024 (oral)

**Authors:** Pascal Chang, Jingwei Tang, Markus Gross, Vinicius C. Azevedo

**Keywords:** diffusion models; temporal coherency; Gaussian noise field; continuous white noise; noise transport

**Abstract:** 
> Video editing and generation methods often rely on pre-trained image-based diffusion models. During the diffusion process, however, the reliance on rudimentary noise sampling techniques that do not preserve correlations present in subsequent frames of a video is detrimental to the quality of the results. This either produces high-frequency flickering, or texture-sticking artifacts that are not amenable to post-processing. With this in mind, we propose a novel method for preserving temporal corre...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**SDEdit: Image Synthesis and Editing with Stochastic Differential Equations** (2021)
- *Authors:* Chenlin Meng et al.
- *Direct Connection:* By casting editing as adding Gaussian noise and then denoising with a pre-trained image diffusion model, SDEdit made the initial noise sample the pivotal control variable—this paper replaces that i.i.d. noise prior with a temporally correlated, transportable ∫-noise.

### 💡 Inspiration

**Wavelet Noise** (2005)
- *Authors:* Robert L. Cook et al.
- *Direct Connection:* Wavelet Noise introduced a continuous, band-limited Gaussian noise with exact filtering over pixel footprints, inspiring the paper’s core idea to treat per-pixel noise as the integral of an underlying continuous noise field.

**Procedural Noise using Sparse Gabor Convolution** (2009)
- *Authors:* Ares Lagae et al.
- *Direct Connection:* Gabor noise formalized stationary continuous noise fields and their exact filtering properties, informing the paper’s ∫-noise representation and its ability to preserve statistics under warping and integration over pixel areas.

### 🔍 Gap Identification

**Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation** (2023)
- *Authors:* Jay Zhangjie Wu et al.
- *Direct Connection:* Tune-A-Video reduces flicker by reusing the same noise/seed across frames but suffers from texture-sticking, directly motivating this paper’s ∫-noise and transport scheme that preserves temporal correlation without locking textures to the frame.

**Text2Video-Zero: Text-to-Image Diffusion Models are Zero-Shot Video Generators** (2023)
- *Authors:* Hrayr Khachatryan et al.
- *Direct Connection:* Text2Video-Zero showed that zero-shot video generation with image diffusion and simple noise reuse/warping yields either flicker or over-locked textures, highlighting the need for a principled temporally correlated noise prior provided by ∫-noise.

### 📊 Baseline

**TokenFlow: Consistent Diffusion Features for Consistent Video Editing** (2023)
- *Authors:* First author et al.
- *Direct Connection:* TokenFlow enforces temporal consistency by flow-warping diffusion features while still relying on per-frame Gaussian noise, and this paper complements/improves such pipelines by transporting the noise itself via a continuous ∫-noise field.

---

## Synthesis: How Prior Work Led to This Paper

SDEdit established that image editing with diffusion models can be framed as injecting Gaussian noise and denoising with a fixed pre-trained model, making the initial noise field a primary lever over results. Tune-A-Video extended image diffusion to video by reusing the same seed across frames to mitigate flicker, but its reliance on fixed noise led to texture-sticking artifacts, showing that naïvely correlating noise is insufficient. Text2Video-Zero similarly demonstrated zero-shot video generation/editing from image models using simple noise reuse or flow-based heuristics, revealing a persistent trade-off between flicker and over-constrained textures. TokenFlow improved temporal coherence by warping and aggregating diffusion features along optical flow, yet it retained per-frame i.i.d. noise assumptions, leaving noise as an unmodeled source of inconsistency. In parallel, graphics works such as Wavelet Noise and Gabor Noise treated noise as continuous random fields and emphasized exact filtering/integration over pixel footprints, providing the key insight that noise should be defined and manipulated in a continuous domain and then integrated to pixels. Taken together, these threads exposed a gap: video diffusion pipelines needed a principled noise prior that is continuous, transportable, and correctly filtered under warps. The present work synthesizes these ideas by redefining the pixel noise as the integral of an infinite-resolution white-noise field and by transporting this ∫-noise with carefully designed advection, naturally resolving flicker versus texture-sticking while fitting seamlessly into image-to-video diffusion workflows.

---

*Analysis generated on: 2026-01-06T15:04:54.421227*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
