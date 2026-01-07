# Prior Work Analysis Report

## Target Paper
**Title:** VCTt5DXiBe
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The core contribution of CompDiffuser—learning to compositionally stitch overlapping trajectory chunks with a single bidirectional diffusion model—emerges from two converging lines of work. First, trajectory-level generative planning showed that sequence models can plan by modeling entire behavior distributions. Trajectory Transformer established the feasibility of modeling long-horizon behaviors as sequences, and Diffuser reframed decision making as trajectory sampling with diffusion, offering strong planning performance but largely within-task generalization. Second, advances in compositional and conditional diffusion demonstrated how to integrate multiple constraints within a single generative process. Compositional diffusion (Du et al.) provided the mechanism to combine conditions via shared score functions, while RePaint’s inpainting highlighted how diffusion can condition on observed regions and iteratively resample to maintain boundary consistency.
In parallel, diffusion for motion generation (MDM) validated that transitions between segments can be synthesized to be physically consistent, foreshadowing trajectory “stitching” in control domains. Complementing these generative advances, CompILE showed that decomposing demonstrations into sub-trajectories enables reusable building blocks for long-horizon tasks. CompDiffuser synthesizes these ideas: it decomposes trajectories into overlapping chunks (CompILE-style segmentation), then uses a single diffusion model to jointly denoise chunks under mutual conditioning (compositional diffusion/inpainting), allowing information to propagate bidirectionally across overlaps. This yields robust, physically consistent stitching that generalizes to novel task compositions beyond the training distribution.

---
*Generated: 2026-01-07T00:05:12.551476*
