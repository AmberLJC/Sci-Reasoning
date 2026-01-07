# Prior Work Analysis Report

## Target Paper
**Title:** 3dnG7LcKxT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper targets the expressive limits of spectrally-enhanced GNNs (SGNNs)—models that exploit Laplacian eigenvectors and spectra—now common through Laplacian positional encodings in MPNNs and Graph Transformers. This trend was catalyzed by the spectral GNN foundations of Bruna et al. and operationalized in practice by Dwivedi and Bresson, whose LapPE popularized injecting eigenvectors as positional signals. Yet, the dominant lenses for expressivity—1-WL and its higher-order variants (Xu et al.; Morris et al.) and the homomorphism-count viewpoint (Keriven & Peyré)—do not align with the algebraic structure of graph spectra. These frameworks, while central benchmarks, overlook the symmetries and degeneracies created by eigenvalue multiplicities. The present work fills this gap by proposing an expressivity hierarchy keyed to the multiplicity of the largest eigenvalue and proving that many SGNNs remain incomplete even on graphs with simple spectrum, revealing a fundamental shortfall of current spectral positional encodings. To address the root cause—orthogonal gauge freedom within eigenspaces—the authors adapt the group-equivariant design principle of Cohen & Welling and rotation-equivariant attention ideas from SE(3)-Transformers to the spectral setting. This yields equiEPNN, an SGNN that is equivariant to O(m) basis rotations in eigenspaces, thereby respecting the intrinsic symmetries of spectral features and overcoming documented completeness gaps. Together, these prior works shape the paper’s critique, theoretical framework, and architectural remedy.

---
*Generated: 2026-01-07T00:21:33.155628*
