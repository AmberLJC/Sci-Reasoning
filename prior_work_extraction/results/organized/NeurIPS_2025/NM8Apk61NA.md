# Prior Work Analysis Report

## Target Paper
**Title:** NM8Apk61NA
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

HyperET’s core idea—achieving efficient multi-granularity alignment by training in hyperbolic space with dynamically adjusted radii—sits at the intersection of hyperbolic representation theory and multimodal training practice. Nickel and Kiela’s Poincaré Embeddings established that hyperbolic geometry intrinsically encodes hierarchies, where distance from the origin reflects depth; their Lorentz-model work further stabilized training and clarified radius–hierarchy semantics. Building on this geometric foundation, Ganea et al.’s Hyperbolic Neural Networks supplied the practical apparatus (exp/log maps, gyrovector arithmetic) to operate neural computations on manifolds, while Bécigneul and Ganea’s Riemannian adaptive optimizers made such training computationally feasible at scale—key for HyperET’s efficiency target. On the language side, Tifrea et al. showed that lexical semantics are naturally hierarchical and better captured in hyperbolic space, directly motivating HyperET to align visual representations to text within a shared hyperbolic geometry.
In parallel, CLIP popularized global image–text alignment but exposed limitations in capturing fine- to coarse-grained correspondences central to MLLMs. BLIP-2 emphasized efficiency by freezing encoders, yet still inherited limited granularity alignment. HyperET synthesizes these threads: it replaces Euclidean/global alignment with a hyperbolic formulation where dynamic radius controls granularity, enabling the visual encoder to align to text across arbitrary levels while leveraging Riemannian optimization for compute-efficient training.

---
*Generated: 2026-01-07T00:05:12.550622*
