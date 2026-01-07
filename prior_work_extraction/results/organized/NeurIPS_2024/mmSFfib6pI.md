# Prior Work Analysis Report

## Target Paper
**Title:** mmSFfib6pI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—defining a spherical convolutional Wasserstein distance for validating global climate models—sits at the intersection of optimal transport and spherical signal processing. Rubner, Tomasi, and Guibas (2000) established the Earth Mover’s Distance as a practical metric to compare distributions, which is the conceptual bedrock for quantifying discrepancies between climate fields. Cuturi’s (2013) Sinkhorn distances enabled scalable computation of OT, a prerequisite for repeatedly evaluating local distributional differences across the globe. To further improve efficiency and robustness, the approach draws from projection-based OT: Bonneel et al. (2015) introduced sliced/Radon Wasserstein distances via 1D projections, and Deshpande et al. (2018) showed that Wasserstein-type discrepancies computed on convolutional features can be highly effective, motivating the use of learned or fixed filters as projections rather than purely linear ones.

Because the data live on the sphere, the method must respect spherical geometry. Esteves et al. (2018) provide an SO(3)-equivariant framework for spherical convolutions, ensuring rotationally consistent features, while Driscoll and Healy (1994) supply the harmonic-analysis foundation for efficient and mathematically sound spherical convolutions. Finally, Peyré and Cuturi’s (2019) monograph consolidates the theoretical and algorithmic landscape of OT—including regularization and computation on geometric domains—guiding practical choices in the proposed metric. Together, these works directly inform the design of a geometry-aware, convolutionally projected Wasserstein distance tailored to evaluating CMIP climate model outputs against reanalysis data.

---
*Generated: 2026-01-06T23:33:35.557721*
