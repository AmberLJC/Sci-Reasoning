# Prior Work Analysis Report

## Target Paper
**Title:** BC1IJdsuYB
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Selective Amnesia’s core idea—targeted forgetting in deep generative models—sits at the intersection of continual learning regularization and modern variational generative modeling. The continual learning lineage (EWC and Synaptic Intelligence) provides the key mechanism: estimate parameter importance and regularize updates to avoid unwanted drift. Selective Amnesia inverts this retention-centric objective, constraining parameters critical to non-target knowledge while allowing modifications that specifically degrade a chosen concept. Variational Continual Learning contributes a complementary perspective by treating learning (and here, unlearning) through a variational lens, aligning naturally with the paper’s derivation for conditional variational likelihood models.

On the generative side, Auto-Encoding Variational Bayes supplies the ELBO-based foundation that enables a principled formulation of forgetting as operating on conditional likelihoods. Denoising Diffusion Probabilistic Models and Latent Diffusion Models ground the method in the dominant text-to-image architectures and objectives, making it practical to apply selective forgetting to prompts such as nudity and celebrity names. Finally, recent attempts at diffusion concept erasure, exemplified by Erasing Concepts from Diffusion Models, crystallize the problem setting and baseline strategies (fine-tuning to suppress specific concepts). Against this backdrop, Selective Amnesia’s contribution is to replace ad hoc erasure procedures with a continual-learning–inspired, controllable regularization that generalizes across VAEs and diffusion while maintaining non-target capabilities.

---
*Generated: 2026-01-07T00:02:04.833120*
