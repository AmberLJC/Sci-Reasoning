# Prior Work Analysis Report

## Target Paper
**Title:** RnfyqrkOxD
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

GeoRemover’s key contribution is to treat object removal as a causal geometry-to-appearance problem: first remove the object in geometry space, then render RGB so that shadows and reflections—effects caused by the object’s presence—disappear coherently. This stance arises from two observed limitations in prior art. On one side, mask-aligned inpainting methods like LaMa excel at reconstructing only the masked region, but by design they do not alter unmasked pixels, leaving behind causal artifacts (e.g., shadows, reflections) that lie outside the mask. On the other side, loosely mask-aligned diffusion editors such as InstructPix2Pix can modify broader context but often lack controllability, risking over-erasure of unrelated content.
To overcome this, GeoRemover builds on a lineage of structure-conditioned synthesis. MiDaS popularized robust monocular depth as a geometry proxy, making depth a practical canvas for structure-aware edits. Geometry-first completion, as in 3D Photography using Context-aware Layered Depth Inpainting, showed that operating in layered/depth space yields coherent spatial reasoning before rendering appearance. SPADE/GauGAN established the general paradigm of synthesizing photorealistic images conditioned on structural maps, while ControlNet demonstrated that modern diffusion can faithfully follow depth and other controls at high fidelity. Finally, inverse rendering advances like NeRFactor explicitly connect geometry, materials, and illumination to shadows/specularities, providing the theoretical underpinning for GeoRemover’s causal claim: if the object is removed in geometry, its visual effects should be re-rendered away. Collectively, these works directly inform GeoRemover’s two-stage, geometry-aware design that achieves controllable object removal along with principled elimination of causal visual artifacts.

---
*Generated: 2026-01-07T00:05:12.553364*
