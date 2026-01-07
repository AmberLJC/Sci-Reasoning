# Prior Work Analysis Report

## Target Paper
**Title:** dg3tI3c2B1
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The Latent Prompt Transformer (LPT) fuses three influential lines of work into a unified framework for property-conditional molecular generation. First, latent-space molecular design from Gómez-Bombarelli et al. and JTVAE established that molecules can be generated and optimized by manipulating a learned latent representation tied to properties. LPT retains this latent-control paradigm but replaces downstream optimization with a principled Bayesian mechanism: a property predictor p(y|z) defines a posterior p(z|y) from which latent prompts are sampled to meet target properties. This Bayesian factorization directly echoes the semi-supervised VAE formulation (p(x|z), p(y|z), p(z)), providing a likelihood-based training objective on molecule–property pairs and a clear inference route for conditional design.
Second, LPT’s use of a continuous prompt to condition a causal Transformer draws on Prefix-Tuning, extending continuous prompting beyond NLP to molecular generation. Rather than tuning prompt vectors per-task, LPT learns a generative prior over prompts and uses posterior-inferred prompts to guide the decoder at sample time. This prompts-as-latents view is further connected to controllable generation methods like PPLM: LPT’s property predictor plays the role of an attribute model, but guidance occurs in the latent prompt space, yielding more stable and scalable control.
Finally, the learnable prior over latent prompts follows the VAE literature on flexible priors (e.g., VampPrior), improving expressivity over fixed Gaussians. Coupled with an autoregressive SMILES Transformer as popularized by MolGPT, these components collectively enable LPT’s key contribution: likelihood-trained, posterior-guided, prompt-conditioned molecule generation with explicit property control.

---
*Generated: 2026-01-06T23:33:35.535440*
