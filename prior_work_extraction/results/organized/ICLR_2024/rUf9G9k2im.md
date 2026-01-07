# Prior Work Analysis Report

## Target Paper

**Title:** Image Inpainting via Iteratively Decoupled Probabilistic Modeling

**Conference:** ICLR 2024 (spotlight)

**Authors:** Wenbo Li, Xin Yu, Kun Zhou, Yibing Song, Zhe Lin

**Keywords:** Inpainting, Decoupled Probabilistic Modeling, Pixel Spread Model

**Abstract:** 
> Generative adversarial networks (GANs) have made great success in image inpainting yet still have difficulties tackling large missing regions. In contrast, iterative probabilistic algorithms, such as autoregressive and denoising diffusion models, have to be deployed with massive computing resources for decent effect. To achieve high-quality results with low computational cost, we present a novel pixel spread model (PSM) that iteratively employs decoupled probabilistic modeling, combining the opt...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Free-Form Image Inpainting with Gated Convolution** (2019)
- *Authors:* Jiahui Yu et al.
- *Direct Connection:* Gated Convolution introduced mask-aware free-form inpainting with efficient feed-forward generators, establishing the efficiency paradigm that PSM retains while replacing deterministic one-pass prediction with explicit probabilistic, iterative commitments.

### 💡 Inspiration

**MaskGIT: Masked Generative Image Transformer** (2022)
- *Authors:* Huiwen Chang et al.
- *Direct Connection:* MaskGIT’s confidence‑guided, iterative masked prediction directly inspires PSM’s pixel‑spread mechanism, where the model selects and commits informative pixels across iterations while deferring uncertain regions.

### 🔍 Gap Identification

**RePaint: Inpainting using Denoising Diffusion Probabilistic Models** (2022)
- *Authors:* Andreas Lugmayr et al.
- *Direct Connection:* RePaint established iterative probabilistic inpainting with strong fidelity but at the cost of hundreds of denoising steps, directly motivating PSM’s few-iteration decoupled updates that preserve tractable predictions while slashing sampling cost.

### 📊 Baseline

**Resolution-robust Large Mask Inpainting with Fourier Convolutions (LaMa)** (2022)
- *Authors:* Konstantin Suvorov et al.
- *Direct Connection:* LaMa represents the fast GAN-based large‑mask inpainting baseline whose struggles with very large missing regions PSM targets by injecting probabilistic, iterative updates without sacrificing efficiency.

### 🔗 Related Problem

**High-Resolution Image Synthesis with Latent Diffusion Models** (2022)
- *Authors:* Robin Rombach et al.
- *Direct Connection:* Latent Diffusion’s inpainting variant showed that iterative denoising in a compressed space improves quality but still requires many steps, informing PSM’s design choice to avoid long diffusion trajectories by committing only high-certainty pixels per iteration.

**Palette: Image-to-Image Diffusion Models** (2022)
- *Authors:* Chitwan Saharia et al.
- *Direct Connection:* Palette demonstrated diffusion-based inpainting with supervised conditioning and high visual quality but substantial sampling cost, highlighting the quality–efficiency tension that PSM resolves via decoupled, few-step pixel selection and prediction.

---

## Synthesis: How Prior Work Led to This Paper

Diffusion-based inpainting advanced fidelity by iteratively sampling conditional distributions; RePaint formalized this for holes by repeatedly denoising while enforcing known-pixel consistency, achieving strong realism but requiring hundreds of steps. Palette generalized supervised image-to-image diffusion (including inpainting), again highlighting the quality but heavy sampling budgets in iterative probabilistic approaches. Latent Diffusion reduced cost by operating in a compressed latent space and offered an inpainting variant, yet still needed dozens of iterations. In contrast, GAN-style methods emphasized speed: Gated Convolution introduced mask-aware, free-form inpainting with efficient feed-forward generators, and LaMa pushed large-mask performance via very wide receptive fields and frequency-domain convolutions. However, these fast methods remained deterministic and struggled to reliably hallucinate semantics in large regions. Separately, MaskGIT showed that iterative, confidence-guided masked prediction enables parallel commitments to high-certainty tokens while deferring uncertain ones, yielding efficient yet probabilistic generation.
Bringing these strands together, the gap was clear: diffusion and related probabilistic methods provide tractable conditional predictions but are slow; GAN approaches are fast but brittle on large holes. By adopting MaskGIT’s confidence-driven, iterative masked commitment principle and applying it at the pixel level, while targeting the diffusion family’s tractable conditional estimation, the new work decouples selection (which pixels to commit) from prediction (how to sample them). This synthesis yields a few-step, pixel-spread procedure that retains probabilistic rigor and constraint handling like RePaint/Palette/LDM but runs with GAN-like efficiency, directly addressing the long-standing quality–efficiency trade-off in large-mask inpainting.

---

*Analysis generated on: 2026-01-06T17:43:26.244944*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
