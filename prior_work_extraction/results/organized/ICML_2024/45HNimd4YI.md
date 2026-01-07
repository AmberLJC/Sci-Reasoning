# Prior Work Analysis Report

## Target Paper
**Title:** 45HNimd4YI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Perturb-and-Project builds on two converging threads: objective/input perturbation for DP optimization and geometry-driven analyses of noise and denoising. Chaudhuri–Monteleoni–Sarwate introduced objective perturbation for ERM, establishing that carefully structured randomness in optimization objectives can deliver privacy with strong utility. Hardt–Talwar’s geometric program explained how error is governed by Gaussian width/complexity, inspiring both projection-based denoising and the analysis lens adopted here. Nikolov–Talwar–Zhang’s projection mechanism concretized this idea for linear queries by projecting noisy answers onto a feasible polytope, a principle the present paper generalizes to the space of admissible datasets S via input perturbation followed by projection.

For workloads, k-way marginals and similarity structures are central. The Matrix Mechanism provided a principled baseline for large linear query workloads, including marginals, but leaves room for specialized algorithms. Barak et al. showed early that enforcing consistency via projection enables high-quality release of contingency tables, foreshadowing the present paper’s perturb-and-project approach to marginals. For pairwise similarities, DP PCA by Chaudhuri–Sarwate–Sinha offered techniques for privately handling covariance/Gram matrices, which directly relate to cosine similarities; the new algorithms tailor these ideas to achieve efficient, accurate similarity release. Finally, MWEM stands as a practical baseline for marginals; the current work advances theory and efficiency, notably providing guarantees for odd k and improved bounds in sparse regimes. The novel technical step—tight sum-of-squares certificates that upper bound Gaussian complexity—pushes the geometry-of-DP agenda forward, explaining why fast input perturbation plus projection works and enabling new guarantees for similarities and marginals.

---
*Generated: 2026-01-07T00:02:04.904090*
