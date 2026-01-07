# Prior Work Analysis Report

## Target Paper
**Title:** plXXbXjvQ9
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

Gerken and Kessel’s key contribution—showing that deep-ensemble predictions become exactly equivariant under data augmentation for all inputs and at all training times in the infinite-width limit—sits at the intersection of ensemble methodology, symmetry-aware learning, and NTK/GP theory. The deep-ensemble framework of Lakshminarayanan et al. provides the operational mechanism: averaging the outputs of independently trained networks. Jacot et al.’s neural tangent kernel establishes that wide networks trained by gradient descent behave as kernel machines, enabling precise analysis of augmentation effects at the function level. Lee et al. further extend this to training dynamics, which the present work leverages to argue that equivariance is not only a property of the terminal solution but holds across the full training trajectory. The GP perspective of Lee et al. (2018) supports taking expectations over initializations/ensembles, clarifying how the ensemble predictor becomes the object of analysis rather than any single network. Conceptually, Cohen and Welling’s group-equivariant CNNs define the desired symmetry property, but the present paper shows it can emerge without specialized architectures—through augmentation and ensembling alone. Finally, classical kernel-method results by Schölkopf et al. demonstrate that augmentation acts as a group-averaging operator projecting predictors onto symmetry-respecting subspaces. Gerken and Kessel fuse these strands to prove that, in the NTK regime, the ensemble-averaged predictor trained with augmentation is the group-averaged (hence equivariant) solution globally in input space, explaining emergent equivariance even when individual ensemble members are not.

---
*Generated: 2026-01-06T23:42:48.059801*
