# Prior Work Analysis Report

## Target Paper
**Title:** Vj56Z9yNCr
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Shallow Diffuse’s key contribution—robust and invisible watermarking by decoupling payload embedding from the diffusion generation process via a low-dimensional subspace—sits at the intersection of diffusion modeling, generative priors, and classical/learned watermarking. Latent Diffusion Models (Rombach et al., 2022) crystallized the practical importance of low-dimensional latent spaces for high-fidelity synthesis, motivating the view that generation concentrates within a compact subspace. Score-based SDEs (Song et al., 2021) formalized how signals evolve under diffusion dynamics, enabling the identification of components minimally affected by the score flow. Conceptually, Shallow Diffuse borrows from generative priors for inverse problems (Bora et al., 2017), which decompose signals into the range of a generator and its orthogonal complement; here, the watermark is purposefully placed in the complement (a null space relative to the generative subspace) to avoid interfering with synthesis.
Classical watermarking theory—spread-spectrum (Cox et al., 1997) and QIM (Chen & Wornell, 2001)—provides the robustness–invisibility blueprint: embed where the host process is least likely to corrupt the payload and structure the embedding for reliable detection at low distortion. Shallow Diffuse repurposes this, treating the “channel” as the diffusion-induced subspace geometry rather than a fixed frequency or perceptual band. Finally, learned watermarking systems (HiDDeN, 2018) and practical diffusion watermarks (SynthID, 2023) supply training methodology and baselines, highlighting limitations of embedding throughout sampling. By unifying these strands, Shallow Diffuse introduces a projection-based, subspace-null embedding that preserves generative fidelity while strengthening watermark detectability under post-processing.

---
*Generated: 2026-01-07T00:21:32.323429*
