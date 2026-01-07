# Prior Work Analysis Report

## Target Paper
**Title:** zprMrpiLgT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CURE’s core idea—orthogonal, training-free removal of a concept by projecting out a discriminative subspace—sits at the intersection of three lines of work. First, debiasing and concept erasure in representation learning established that concepts live in linear subspaces that can be identified and removed. Bolukbasi et al. introduced hard debiasing by projecting off a concept direction in word embeddings, while INLP and Amnesic Probing refined this into a principled, often SVD-informed, projection that removes linearly predictable concept information while preserving other capabilities. CURE generalizes these projection-based ideas to the token embedding and cross-attention representations used in diffusion models, explicitly contrasting ‘forget’ and ‘retain’ sets to derive a discriminative subspace with a closed-form SVD.
Second, weight-space editing methods like ROME demonstrated that localized, closed-form edits can precisely and efficiently steer large models without full fine-tuning. CURE adopts this philosophy, applying a spectral, rank-controlled edit directly to diffusion weights for speed, interpretability, and minimal collateral damage.
Third, advances specific to text-to-image diffusion—Latent Diffusion (the underlying architecture), Textual Inversion (concept encoding in token embeddings), and Prompt-to-Prompt (cross-attention control)—show where and how concepts are represented and can be manipulated. CURE synthesizes these insights, moving from inference-time guidance or costly fine-tuning to a fast, interpretable, SVD-driven weight-space projection that selectively suppresses undesired concepts while preserving unrelated capabilities.

---
*Generated: 2026-01-07T00:21:32.288371*
