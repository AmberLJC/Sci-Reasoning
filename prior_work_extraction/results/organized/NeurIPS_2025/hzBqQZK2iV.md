# Prior Work Analysis Report

## Target Paper
**Title:** hzBqQZK2iV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Uni-LoRA’s key contribution is to unify and extend parameter-efficient LoRA variants by recasting their trainable spaces as projections from a compact subspace. This builds directly on LoRA’s core idea of constraining updates to a low-rank manifold, but reframes all LoRA parameters across layers as a single flattened vector recoverable via a projection P from R^d to R^D. Works like Tied-LoRA and VeRA provided the immediate predecessors: Tied-LoRA’s cross-layer tying becomes a specific structural constraint on P, while VeRA explicitly parameterizes updates as projecting a task vector through a fixed/random basis, an exact instance of the Uni-LoRA projection view. VB-LoRA contributes the latent-variable perspective, which in Uni-LoRA corresponds to choosing a low-dimensional latent and its associated projection into the LoRA space. This projection-based lens is theoretically motivated by intrinsic-dimension results showing that effective fine-tuning lives in surprisingly low-dimensional subspaces, indicating that d << D can suffice. Methodologically, it resonates with HyperNetworks and Compacter, which generate many weights from compact representations and shared low-rank components, respectively—both interpretable as learned or structured projections shared across layers. Uni-LoRA crystallizes these threads by identifying the choice of P as the fundamental differentiator among methods and pushes efficiency further by enabling extreme cross-layer sharing—up to a single vector—without sacrificing expressivity.

---
*Generated: 2026-01-07T00:05:12.545763*
