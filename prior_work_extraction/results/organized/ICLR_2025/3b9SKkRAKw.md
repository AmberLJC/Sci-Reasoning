# Prior Work Analysis Report

## Target Paper
**Title:** 3b9SKkRAKw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LeFusion’s core contribution—controllable pathology synthesis that preserves background fidelity while focusing learning and sampling on lesion regions—sits squarely on diffusion-model advances in masked, conditional, and structure-preserving editing. DDPM provides the training objective and sampling backbone that LeFusion reweights over lesion masks to concentrate capacity on pathology. The SDE perspective formalized by Song et al. enables principled coupling between forward noising and reverse denoising; SDEdit operationalizes this by partially noising an input and then denoising to retain its structure. LeFusion adapts this mechanism to medical images by forward-diffusing the background and injecting it into the reverse process so that backgrounds remain faithful while only lesions are synthesized.
RePaint shows that repeated re-noising and masked inpainting can maintain contextual consistency; LeFusion internalizes this idea by baking locality into the objective rather than relying solely on sampling heuristics. Palette demonstrates effective image-to-image conditioning for tasks such as inpainting, guiding LeFusion’s setup of transforming lesion-free inputs into lesion-containing outputs under explicit conditioning. Blended Diffusion contributes the principle of localized, mask-driven edits and seamless blending with original content, mirroring LeFusion’s separation of lesion and background streams. Finally, ControlNet exemplifies how explicit structural signals (e.g., segmentation maps) can steer diffusion, informing LeFusion’s controllability over lesion location, category, and texture modes (multi-class, multi-peak). Together, these works directly shape LeFusion’s lesion-focused loss, background-context integration, and controllable synthesis pipeline.

---
*Generated: 2026-01-06T23:42:48.099565*
