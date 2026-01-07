# Prior Work Analysis Report

## Target Paper
**Title:** AuXd54odxm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ERDiff’s core contribution—aligning neural population activity across domains while preserving spatio-temporal latent structure—stands at the intersection of latent neural dynamics modeling and modern diffusion-based generative modeling. Foundational latent dynamics methods such as GPFA (Yu et al., 2009) and LFADS (Pandarinath et al., 2018) established that neural activity can be represented by low-dimensional trajectories with temporal coherence, motivating ERDiff’s focus on latent dynamics as the substrate for alignment. rSLDS (Linderman et al., 2017) further emphasized explicit temporal structure and state-dependent dynamics, underscoring the need to respect temporal dependencies rather than aligning static embeddings.

On the alignment side, Degenhart et al. (2020) and Gallego et al. (2020) demonstrated that behaviorally relevant latent manifolds are stable across days and that subspace alignment can stabilize decoding. However, these approaches typically treat alignment as a geometric mapping that underweights temporal structure. ERDiff addresses this gap by replacing purely geometric criteria with a generative prior that encodes spatio-temporal structure learned from the source domain.

This is operationalized via diffusion models: DDPM (Ho et al., 2020) provides a powerful training framework to learn complex data distributions, while score-based modeling (Song & Ermon, 2019) offers gradients of the log-density that can guide optimization. ERDiff extracts the source domain’s latent dynamics distribution with a diffusion/score model and then performs maximum-likelihood alignment of target data under this learned prior, ensuring the recovered latents conform to the source’s spatio-temporal manifold. In doing so, ERDiff unifies latent dynamics extraction with alignment under an explicit, expressive generative prior, directly extending both the neural dynamics and diffusion modeling lines of work.

---
*Generated: 2026-01-07T00:02:04.836429*
