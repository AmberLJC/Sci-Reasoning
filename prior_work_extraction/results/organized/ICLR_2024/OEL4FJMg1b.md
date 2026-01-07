# Prior Work Analysis Report

## Target Paper

**Title:** DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Chong Mou, Xintao Wang, Jiechong Song, Ying Shan, Jian Zhang

**Keywords:** Diffusion model, Image editing, Image generation

**Abstract:** 
> Despite the ability of text-to-image (T2I) diffusion models to generate high-quality images, transferring this ability to accurate image editing remains a challenge. In this paper, we propose a novel image editing method, DragonDiffusion, enabling Drag-style manipulation on Diffusion models. Specifically, we treat image editing as the change of feature correspondence in a pre-trained diffusion model. By leveraging feature correspondence, we develop energy functions that align with the editing ta...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold** (2023)
- *Authors:* Xingang Pan et al.
- *Direct Connection:* It established the drag-style handle–target formulation and energy-based point alignment that DragonDiffusion adapts from GAN latent optimization to diffusion sampling via correspondence-driven gradient guidance.

**DIFT: Diffusion Features for Dense Visual Correspondence** (2023)
- *Authors:* Chen et al.
- *Direct Connection:* It showed that multi-scale Stable Diffusion features provide robust dense correspondences, directly enabling DragonDiffusion’s correspondence-centric energy functions and its semantic–geometric multi-scale guidance design.

### 💡 Inspiration

**Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models** (2023)
- *Authors:* Hila Chefer et al.
- *Direct Connection:* By demonstrating that manipulating attention can steer diffusion toward desired semantics, it inspires DragonDiffusion’s use of a memory-backed cross-attention mechanism to couple semantic consistency with drag-driven geometric changes.

### 📊 Baseline

**DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing** (2023)
- *Authors:* Shi et al.
- *Direct Connection:* As the primary diffusion-based drag baseline, it motivates DragonDiffusion’s shift from pixel/latent constraints to diffusion-feature correspondence and multi-scale guidance to mitigate geometry distortions and identity drift observed in DragDiffusion.

### 🔧 Extension

**Prompt-to-Prompt Image Editing with Cross-Attention Control** (2022)
- *Authors:* Amir Hertz et al.
- *Direct Connection:* Its cross-attention control mechanism for preserving layout/content is extended by DragonDiffusion into a visual cross-attention memory bank that enforces consistency with the source image during drag edits.

### 🔗 Related Problem

**Pix2Pix-Zero: Zero-shot Image-to-Image Translation** (2023)
- *Authors:* Huang et al.
- *Direct Connection:* Its training-free attention injection to preserve subject/layout informs DragonDiffusion’s strategy of caching and reusing attention information to maintain fidelity while applying drag guidance.

---

## Synthesis: How Prior Work Led to This Paper

Drag-style interactive manipulation was crystallized by Drag Your GAN, which framed editing as moving user-specified handles to targets by minimizing an energy defined on internal features and updating the generator with gradients. DragDiffusion transferred this idea to diffusion models, but its point constraints in pixel or latent space often yielded identity drift and geometric artifacts under large or semantic motions. In parallel, DIFT established that Stable Diffusion’s internal features encode strong dense correspondences at multiple layers—early layers capturing geometry and later layers capturing semantics—suggesting a principled space for alignment-based control. Prompt-to-Prompt revealed that reusing or constraining cross‑attention maps can preserve scene layout and content during editing, while Pix2Pix‑Zero generalized this training‑free attention injection to maintain identity and structure across denoising steps. Attend‑and‑Excite further showed that targeted attention modulation can enforce semantic focus, underscoring attention as a lightweight, effective control knob.

Together, these works expose a clear opportunity: marry drag-style energy minimization with diffusion’s rich, multi-scale correspondences, and stabilize edits by explicitly preserving attention patterns tied to the source image. DragonDiffusion synthesizes this by defining correspondence-driven energy functions over diffusion features and injecting their gradients into sampling, scaling guidance from geometric to semantic layers, and introducing a memory‑banked visual cross‑attention to anchor content fidelity during drag operations—achieving precise, training‑free, drag-style editing on diffusion models.

---

*Analysis generated on: 2026-01-06T22:34:19.894735*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
