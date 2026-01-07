# Prior Work Analysis Report

## Target Paper
**Title:** bhSfbjS6j9
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Han, Zickler, and Nishino’s key contribution—recovering a multimodal distribution over shapes from a single shading image—emerges at the intersection of diffusion modeling, patch-based priors, and classical shape constraints. DDPM provides the practical mechanism for learning and sampling from a rich, multi-peaked prior; the authors instantiate this as a compact denoising diffusion trained on 16×16 normal patches. Song and Ermon’s score-based perspective underpins how such a denoiser can be guided by additional energies, enabling principled conditioning of the patch sampler with inter-patch consistency during generation.

The architectural choice to model local patches and reconcile them globally is a direct descendant of EPLL, which showed that powerful patch priors combined with overlapping-patch consistency can yield globally coherent reconstructions. Plug-and-Play further legitimizes the decoupled design: a learned denoiser (here, diffusion) acts as a prior while separate constraints steer inference, avoiding monolithic end-to-end training. For normals, the most salient consistency is integrability; the Frankot–Chellappa formulation offers the classic mathematical apparatus to fuse locally ambiguous normal predictions into a coherent surface.

On the problem side, Belhumeur–Kriegman–Yuille’s analysis of generalized bas-relief and related ambiguities frames why point estimates are insufficient, while SIRFS typifies strong-prior, single-mode SFS that cannot express multistability. Combining these strands yields a patch-diffusion SFS model that naturally samples multiple perceptually plausible shapes, aligning computational inference with human multistable perception.

---
*Generated: 2026-01-06T23:33:35.554780*
