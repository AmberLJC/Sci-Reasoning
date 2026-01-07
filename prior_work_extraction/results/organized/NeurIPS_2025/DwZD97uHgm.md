# Prior Work Analysis Report

## Target Paper
**Title:** DwZD97uHgm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ZS-NCD’s core contribution—zero-shot denoising by optimizing an untrained neural compression model on patches from a single noisy image and using the compressor’s entropy model as an implicit regularizer—emerges from two converging lines of work. From the internal-learning/zero-shot side, Deep Image Prior and Zero-Shot Super-Resolution established that a network’s architecture and intra-image patch recurrence can serve as powerful priors when optimized on the test image alone. Self2Self then demonstrated that truly single-image denoising is feasible, while highlighting the risk of overfitting noise and the need for principled regularization. Classical BM3D provided the patch-overlap aggregation blueprint and showed the enduring strength of intra-image self-similarity without external training.

From the compression side, Ballé et al.’s hyperprior model and Minnen et al.’s joint autoregressive–hierarchical priors introduced end-to-end neural compression with accurate entropy models and an explicit rate–distortion trade-off. These architectures embed a learnable code-length (entropy) constraint that naturally penalizes overly complex representations. ZS-NCD fuses these strands: it replaces ad-hoc early stopping or masking with the compressor’s rate term as an MDL-like regularizer during single-image optimization, and it applies internal learning over overlapping patches with aggregation to exploit self-similarity. The broader concept of using model structure as a prior for inverse problems, exemplified by Bora et al., supports ZS-NCD’s view that constraining reconstructions to a model family—in this case, a neural compressor with an entropy model—yields robust, data-free denoising across noise types.

---
*Generated: 2026-01-07T00:02:04.971756*
