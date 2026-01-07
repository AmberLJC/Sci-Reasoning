# Prior Work Analysis Report

## Target Paper
**Title:** bg6fVPVs3s
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The core insight—steering a strong diffusion model with a smaller or less-trained version of itself to raise perceptual quality without sacrificing sample diversity—emerges directly from the evolution of guidance in diffusion models. DDPM provided the foundational denoising framework where sample trajectories can be altered by modifying the score estimate. Building on this, Improved DDPM and subsequent high-quality ImageNet models supplied strong conditional predictors and training practices that make guidance effective and measurable at scale. Dhariwal and Nichol’s classifier guidance first exposed a practical fidelity–diversity trade-off via external gradients, while Ho and Salimans’ classifier-free guidance replaced the classifier with an unconditional branch, making the trade-off accessible but still entangled: stronger guidance improved alignment/quality yet reduced variation. Large-scale text-to-image systems like GLIDE amplified this observation, showing that tuning CFG scales predictably sacrifices diversity for fidelity. Karras et al.’s EDM then clarified how architectural, loss, and sampling choices influence perceptual quality, providing a stable platform to test new guidance mechanisms.
Within this trajectory, the present work’s leap is to reinterpret the auxiliary model in CFG: rather than using an unconditional predictor, use a deliberately weaker conditional model as the auxiliary. Because the weaker model underfits visual detail while preserving the conditioning signal, its difference from the strong model provides a direction that selectively boosts image quality without collapsing modes. This reframing preserves variation yet improves fidelity, resolving the long-standing entanglement exposed by prior guidance methods.

---
*Generated: 2026-01-06T23:33:35.553808*
