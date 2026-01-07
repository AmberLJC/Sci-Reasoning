# Prior Work Analysis Report

## Target Paper
**Title:** Z764QxwETf
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

PuzzleFusion’s key contribution is to recast spatial puzzle solving—estimating 2D translations and rotations for jigsaw or room-layout pieces—as conditional generative modeling with diffusion. This reframing stands on the methodological foundations of diffusion models: DDPM provides the denoising objective and sampling mechanics, while score-based SDEs offer a continuous-time perspective that facilitates stable training and flexible conditioning in continuous pose spaces. To condition generation on observed piece shapes and puzzle context, the work draws on classifier-free guidance, enabling controllable sampling without a separate classifier.
A second pillar is the adaptation of diffusion to rigid-body transformations. Equivariant diffusion for molecules established how to model rotations and translations with appropriate symmetries, and DiffDock concretely demonstrated that diffusion can solve complex spatial arrangement tasks by predicting SE(3) poses; PuzzleFusion mirrors these ideas in SE(2), using diffusion to place parts coherently in 2D.
Finally, classical jigsaw literature shaped the task’s formulation and constraints. Pomeranz et al. provided compatibility-based assembly and evaluation protocols for large-scale puzzles, while Gallagher’s unknown-orientation setting directly motivates PuzzleFusion’s joint rotation-translation estimation. Together, these works converge to the insight that diffusion can replace combinatorial search with end-to-end conditional generation over piece poses, enabling robust spatial puzzle solving and guiding the dataset design and evaluation choices in PuzzleFusion.

---
*Generated: 2026-01-07T00:02:04.869801*
