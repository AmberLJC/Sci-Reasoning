# Prior Work Analysis Report

## Target Paper
**Title:** zDCwJQY3eI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core idea—realizing Brenier’s polar factorization F = ∇u ∘ M with neural networks—rests squarely on Brenier’s 1991 theorem, which guarantees a decomposition of any suitable vector field into a monotone gradient map and a measure-preserving rearrangement. To make this constructive, the authors adopt input convex neural networks (ICNNs) to parameterize the convex potential u, following Amos, Xu, and Kolter’s architecture that enforces convexity in the input. Building on neural optimal transport advances, particularly Makkuva et al.’s demonstration that ICNNs can learn Monge maps as gradients of convex potentials, the paper trains ∇u as the monotone factor of the decomposition.
Convex analysis is essential to the implementation: Rockafellar’s conjugacy theory justifies retrieving the measure-preserving component via M = ∇u* ∘ F, linking the learned u to its convex conjugate u*. Practical neural OT techniques also influence the pipeline. Seguy et al. introduced scalable neural parameterizations and training for OT maps and dual potentials, while Cuturi’s Sinkhorn regularization enabled computationally tractable OT objectives that often serve as training signals or regularizers in such settings. The broader algorithmic and theoretical framing from Peyré and Cuturi’s monograph informs choices around potentials, gradients, and measure-preserving properties.
Together, these works directly scaffold the paper’s contribution: a practical neural mechanism to factor a vector field into a gradient of a convex potential and a measure-preserving map, with the conjugate-based route to M and ICNN-based parameterization of u providing the key operational pieces.

---
*Generated: 2026-01-07T00:02:04.902392*
