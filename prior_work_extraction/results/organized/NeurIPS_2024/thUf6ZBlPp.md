# Prior Work Analysis Report

## Target Paper
**Title:** thUf6ZBlPp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EigenVI’s key contribution—score-based variational inference with orthogonal function expansions—sits at the intersection of three lines of work: operator/score-based objectives for inference, black-box stochastic optimization, and orthogonal spectral representations. Hyvärinen’s score matching established Fisher divergence as a principled objective that depends only on the score, not the intractable normalizer, which EigenVI adopts to align the variational and target score fields. Black Box Variational Inference provided the stochastic optimization machinery to estimate such objectives and their gradients from samples, enabling EigenVI to remain black-box despite using higher-order function families. Operator Variational Inference further legitimized replacing KL with operator-based criteria (including score/Fisher- and Stein-type objectives), conceptually grounding EigenVI’s choice of Fisher divergence.

On the representation side, the Wiener–Askey polynomial chaos literature supplies families of orthogonal functions tailored to the support (Hermite for R^D, Laguerre for R_+^D, Jacobi for bounded domains), directly informing EigenVI’s design so that sampling and moments remain tractable. The lowest-order truncation reproduces the classical variational Gaussian approximation, while higher-order terms systematically capture skewness, kurtosis, and multimodality. Finally, recent score-based generative modeling showed that matching scores can model complex distributions; EigenVI brings this philosophy to VI with a compact, orthogonal basis rather than neural networks. In contrast to Stein variational methods that transport particles, EigenVI’s Fisher objective and orthogonal expansion reduce optimization to structured linear-algebraic problems, yielding an expressive yet analytically manageable family for black-box inference across diverse variable domains.

---
*Generated: 2026-01-06T23:33:36.273685*
