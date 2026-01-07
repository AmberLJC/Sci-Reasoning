# Prior Work Analysis Report

## Target Paper
**Title:** oRLwyayrh1
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DRCT’s central idea—improving generalization of AI-generated image detectors by training on ‘hard’ diffusion-reconstructed samples and using contrastive learning to focus on generator artifacts—rests on two pillars: faithful diffusion-based reconstruction and artifact-centric representation learning. Foundational diffusion works (DDPM) formalize the forward/reverse noising process that induces characteristic traces in generated images, while DDIM enables deterministic sampling and practical inversion, making it feasible to reconstruct real images with minimal semantic drift. Building on this, methods like SDEdit and Null-text Inversion demonstrate that diffusion models can produce reconstructions nearly indistinguishable from the originals, yet still imbued with subtle diffusion priors; DRCT leverages precisely this property to create hard negatives that closely mimic real images while embedding detectable diffusion artifacts.

On the representation side, Supervised Contrastive Learning provides an objective to explicitly separate such hard negatives from real images while preserving content-invariant, artifact-focused features. This aligns with the forensics literature on generator fingerprints, notably the GAN fingerprinting line of work, which established that generative processes leave identifiable, learnable traces that can generalize across content. DRCT extends this fingerprinting intuition to diffusion models and operationalizes it by synthesizing especially challenging training pairs via high-quality reconstruction. By uniting high-fidelity diffusion inversion with supervised contrastive learning, DRCT turns the most confounding, near-real reconstructions into a training signal, yielding detectors that better transfer to unseen diffusion models.

---
*Generated: 2026-01-06T23:42:48.053055*
