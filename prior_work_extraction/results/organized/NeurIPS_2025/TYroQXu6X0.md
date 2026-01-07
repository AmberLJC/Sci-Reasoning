# Prior Work Analysis Report

## Target Paper
**Title:** TYroQXu6X0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s key contribution—a principled explanation of shortcut learning via the eigenspectrum of the Neural Tangent Kernel (NTK)—rests on three pillars from prior work. First, Jacot et al. introduced the NTK framework and its Mercer decomposition, enabling the present authors to define a neural network’s “features” as NTK eigenfunctions and to analyze learning through spectral components. Second, linearization results for wide networks (Lee et al.) validate treating gradient descent training as kernel regression in the NTK, which implies that predictions evolve along eigenfunctions at rates governed by eigenvalues. Third, spectral analyses of kernel learning (Canatar, Bordelon, Pehlevan) established that high-eigenvalue modes are learned faster and dominate generalization, providing the mathematical lens through which data structure maps to learning dynamics.
Anchored by Geirhos et al.’s formulation of shortcut learning, the present work connects imbalanced, clustered data to an NTK spectrum in which shortcut-related eigenfunctions acquire larger eigenvalues, thereby explaining their preferential learning and persistent influence after training. Finally, implicit-bias results (Soudry et al.; Gunasekar et al.) offer a competing max-margin account. By showing that preference for large-eigenvalue features survives even when network margin is controlled, the authors argue that max-margin bias alone cannot explain shortcut learning in this setting. Collectively, these works directly enable the paper’s core insight: shortcut features emerge as top NTK eigenfunctions shaped by data imbalance, and their dominance is a spectral—not merely margin-based—effect.

---
*Generated: 2026-01-07T00:21:32.297191*
