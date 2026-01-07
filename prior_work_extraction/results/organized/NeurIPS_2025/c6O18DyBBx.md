# Prior Work Analysis Report

## Target Paper
**Title:** c6O18DyBBx
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LD3M’s core contribution—learning gradient-based distilled latents and class embeddings end-to-end through a frozen latent diffusion model while preserving gradients across many denoising steps—sits at the intersection of dataset distillation and diffusion modeling. The problem framing descends from classic dataset distillation (Wang et al., 2018) and its powerful gradient-based objectives (Zhao et al., 2020), which established that synthetic data can be optimized to induce real-like training dynamics. Generative Teaching Networks (Such et al., 2020) then showed the efficacy of using a generator to emit such synthetic data, foreshadowing LD3M’s decision to rely on a strong generative prior rather than optimize pixels directly.

On the generative side, LD3M is enabled by the diffusion family. DDPM (Ho et al., 2020) provides the reverse denoising chain that makes diffusion models state-of-the-art yet introduces severe gradient attenuation when naively backpropagated, directly motivating LD3M’s linearly decaying skip from the initial noise to every reverse step. DDIM (Song et al., 2021) contributes the deterministic, reduced-step perspective that makes differentiable multi-step sampling more tractable and amenable to explicit gradient flow control. Crucially, Latent Diffusion (Rombach et al., 2022) furnishes an efficient latent space and conditioning interface, allowing LD3M to scale to 128–256 px and to optimize class embeddings without fine-tuning the diffusion weights. Finally, Textual Inversion (Gal et al., 2022) demonstrates that learnable embeddings can steer a frozen diffusion model, a principle LD3M generalizes to class-conditional dataset distillation by jointly optimizing distilled latents and class embeddings under a fixed diffusion prior.

---
*Generated: 2026-01-07T00:29:42.063775*
