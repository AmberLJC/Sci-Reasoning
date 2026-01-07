# Prior Work Analysis Report

## Target Paper
**Title:** QIXdI207nq
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LeMiCa’s core idea—formulating cache scheduling for diffusion-based video generation as a graph problem with error-weighted edges and solving it via a lexicographic minimax path objective—sits at the intersection of three threads of prior work. First, training-free acceleration of diffusion models (DDIM; EDM) established that significant speedups are possible without retraining, but primarily targeted single-image/single-trajectory samplers. LeMiCa complements these by accelerating the per-frame forward pass through cache reuse, targeting temporal sequences where cumulative errors—not just local sampling error—dominate quality.
Second, the architectural substrate enabling reusable features comes from latent diffusion (LDM), which standardized attention- and U-Net-based backbones. Building on this, video-specific works showed the promise and pitfalls of reusing features over time: Deep Feature Flow introduced keyframe caching and highlighted error accumulation when propagating features to save compute; in diffusion, Prompt-to-Prompt and TokenFlow demonstrated that cross-attention and intermediate tokens encode content/style and can be propagated for temporal consistency, yet typically relied on local heuristics that left global drift unchecked.
Third, LeMiCa’s scheduling engine is grounded in multicriteria shortest path theory (Martins), adopting a lexicographic minimax objective to explicitly cap worst-case path error while optimizing secondary costs. This reframing converts heuristic cache decisions into a principled global optimization, delivering both speed and improved global consistency across frames—precisely where earlier caching and propagation approaches struggled.

---
*Generated: 2026-01-07T00:21:32.337719*
