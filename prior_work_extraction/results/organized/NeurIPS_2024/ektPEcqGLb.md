# Prior Work Analysis Report

## Target Paper
**Title:** ektPEcqGLb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Poisson VAE (P‑VAE) integrates three strands of prior work: variational autoencoders, predictive coding, and sparse/efficient neural codes. Auto‑Encoding Variational Bayes supplied the ELBO and amortized inference template that P‑VAE preserves while changing the latent family to discrete Poisson spike counts. β‑VAE crystallized how the KL term acts as an information pressure shaping representations; P‑VAE reframes this pressure as a metabolically grounded spike‑rate cost that naturally arises from Poisson latents integrated with predictive coding, thereby tying representation quality to energetic efficiency. The predictive coding lineage—initiated by Rao & Ballard and formalized algorithmically by Whittington & Bogacz—provides the architectural and theoretical scaffolding for P‑VAE’s error‑correcting dynamics and its equivalence to variational free‑energy minimization, justifying a predictive‑coding interpretation of VAE training.

On the latent‑variable side, Deep Exponential Families demonstrated that deep generative models can be trained with count distributions via variational inference, legitimizing P‑VAE’s move from continuous Gaussians to count‑valued latents. Training discrete latents at scale draws on techniques like NVIL, which introduced practical low‑variance gradient estimators for non‑reparameterizable variables, informing how to optimize Poisson spike counts with amortized inference. Finally, Olshausen & Field’s sparse coding objective connects directly to P‑VAE’s emergent metabolic cost: the Poisson‑driven regularization mirrors classic sparsity penalties and explains the empirically observed sparse, high‑dimensional, linearly separable representations. Together, these works directly enable P‑VAE’s core contribution: a biologically grounded, predictive‑coding VAE with Poisson spike‑count latents that couples metabolic efficiency with modern variational learning.

---
*Generated: 2026-01-06T23:39:42.955566*
