# Prior Work Analysis Report

## Target Paper
**Title:** eNM94i7R3A
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Kunin et al. build directly on the exact-gradient-dynamics tradition inaugurated by Saxe, McClelland, and Ganguli, who solved learning trajectories in deep linear nets via singular-mode dynamics. Against this backdrop, Jacot et al.’s NTK formalized the lazy regime in which features remain fixed, while Chizat, Oyallon, and Bach clarified that whether training is lazy or rich depends critically on parameterization—specifically how initialization scales with width and how learning rates are set. The present paper sharpens this dependence by deriving exact solutions for a minimal model where layer-specific initialization variances and learning rates jointly determine the regime, revealing conserved quantities that reshape trajectories in parameter and function space.

Two complementary lines further shaped this advance. First, mean-field analyses (Mei, Montanari, Nguyen) established a rich regime at infinite width, demonstrating genuine feature learning beyond NTK; Kunin et al. analytically interpolate between these extremes and pinpoint when rapid feature learning occurs. Second, results on balancedness and invariants in deep linear networks (Ji and Telgarsky) suggested that conservation laws constrain gradient flow; this paper identifies the precise conserved quantities that encode the effect of unbalanced layer scales. Finally, practical scaling insights from μP (Yang and Hu) underscored the importance of layer-wise learning-rate and initialization choices for feature evolution; the new exact solutions explain, mechanistically, how such unbalanced choices accelerate feature learning. The lineage thus integrates exact linear dynamics, kernel vs mean-field regimes, and layer-wise scaling theory into a unified, solvable account of the lazy–rich transition.

---
*Generated: 2026-01-06T23:33:35.543910*
