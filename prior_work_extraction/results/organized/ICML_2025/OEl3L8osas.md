# Prior Work Analysis Report

## Target Paper
**Title:** OEl3L8osas
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper interrogates a growing trend in atomistic machine learning: training models to predict forces directly without guaranteeing they derive from a potential energy. This trajectory can be traced back to the force-matching paradigm of Ercolessi and Adams, which legitimized learning from forces but did not enforce integrability, and to sGDML, which demonstrated that explicitly conservative force fields are both feasible and data-efficient. The Open Catalyst 2020 benchmark and its GemNet-OC models then shifted community focus to force-centric training and geometry relaxations at scale, where many high-performing models were deployed without a provable energy functional, implicitly suggesting that conservativity might be unnecessary. Concurrently, architectures such as TorchMD-Net made force-only, SE(3)-equivariant predictors practical for molecular dynamics, further normalizing non-conservative usage in simulation settings. Against this backdrop, conservative, energy-based standards like NequIP and DeePMD consistently delivered accurate and stable MD, providing a robust baseline for comparison. The present work synthesizes these streams by systematically stress-testing non-conservative force models in core simulation tasks—geometry optimization and various molecular dynamics protocols—revealing ill-posed convergence and instabilities that conservative models avoid. In doing so, it challenges the emerging narrative that energy conservation can be ‘learned implicitly,’ arguing instead for explicit conservativity or principled constraints when the goal is reliable microscopic simulation.

---
*Generated: 2026-01-07T00:04:09.139953*
