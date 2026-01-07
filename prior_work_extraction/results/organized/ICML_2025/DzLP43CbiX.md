# Prior Work Analysis Report

## Target Paper
**Title:** DzLP43CbiX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution of Flopping for FLOPs is to achieve horizontal mirror (Z2) equivariance without the usual group-size computational penalty by parameterizing feature spaces using irreducible representations—mirror-even and mirror-odd channels—which makes linear layers block-diagonal and halves FLOPs. This builds directly on the group-equivariant lineage inaugurated by Group Equivariant Convolutional Networks and the practical flip/rotation lifting of Dieleman et al., both of which demonstrated accuracy and parameter efficiency but incurred a compute blowup proportional to the group. Ravanbakhsh et al.’s characterization of equivariant linear maps via parameter sharing provides the precise algebraic underpinning: for Z2, the regular representation decomposes into trivial and sign irreps, implying a block structure the authors exploit for computational savings. Steerable CNNs introduced irrep-typed feature spaces and type-preserving nonlinearities; the present work adopts this representation-theoretic view and specializes it to parity types tied to horizontal reflection. Weiler and Cesa’s E(2)-equivariant framework further clarified parity channels and mixing rules for 2D images with reflections, offering a practical template that the paper refines to target FLOP efficiency. Finally, Fourier/irrep-based approaches on non-Euclidean domains (e.g., Spherical CNNs) showed that working in an irrep basis can induce block-diagonal operators with efficiency benefits; here, that insight is translated to the simplest nontrivial group, Z2, yielding symmetry-aware layers with near-standard FLOPs per parameter and reduced wall-clock time.

---
*Generated: 2026-01-07T00:04:09.149002*
