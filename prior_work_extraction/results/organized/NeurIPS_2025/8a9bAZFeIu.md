# Prior Work Analysis Report

## Target Paper
**Title:** 8a9bAZFeIu
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Cue3D’s core innovation—a model-agnostic framework that quantifies how individual image cues drive single-image 3D generation—stands on three pillars of prior work. First, classical vision established the cue taxonomy and its geometric import: Horn and Brooks formalized shading as a primary route from image intensities to shape, while Laurentini’s visual hull theory articulated how silhouettes constrain 3D geometry. These works motivate treating shading and silhouette as distinct, testable factors and underpin Cue3D’s finding that geometric cues—especially shading—are decisive, whereas texture contributes less to generalization. Second, the methodology of perturbation-based auditing comes from robustness and cue-conflict analyses in 2D vision. Geirhos et al. demonstrated that controlled manipulations (stylization) can expose texture versus shape reliance; Hendrycks and Dietterich showed that standardized corruptions enable model-agnostic, quantitative comparisons of performance drops. Cue3D generalizes these ideas to the 3D setting with cue-specific perturbations (shading, texture, silhouette, perspective, edges, continuity) and evaluates their impact on 3D quality. Third, differentiable rendering and modern 3D generative paradigms provide the technical context and targets for analysis. Kato et al. and Niemeyer et al. made 3D learning from 2D cues practical, which explains silhouette and photometric dependencies that Cue3D measures and critiques. Finally, native 3D generative models like Shap-E motivated a cross-paradigm benchmark, enabling Cue3D to show how cue reliance varies across regression, multi-view, and native 3D generators, culminating in the central insight that shape meaningfulness, not texture, dictates generalization.

---
*Generated: 2026-01-07T00:05:12.555710*
