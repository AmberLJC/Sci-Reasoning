# Prior Work Analysis Report

## Target Paper
**Title:** haHIji0yFt
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—SE(3)-equivariant convolution and attention defined in ray space—sits at the intersection of group-equivariant deep learning and ray-based representations in vision. Cohen and Welling’s Group Equivariant CNNs established the principle of building convolutions equivariant to group actions, which this work concretizes for SE(3). Extending beyond Euclidean domains, Gauge Equivariant CNNs supplied the machinery to construct convolutions on homogeneous spaces/manifolds using local gauges; this is essential for handling the space of oriented rays as a homogeneous space of SE(3). Spherical CNNs demonstrated how to realize SO(3)-equivariant convolutions on S^2, directly informing how ray directions (living on the sphere) can be treated within an equivariant framework.
3D Steerable CNNs and Tensor Field Networks contributed the representation-theoretic toolkit (irreducible features, spherical harmonics, and Clebsch–Gordan-based constraints) needed to parameterize equivariant kernels and to design valid SE(3)-equivariant maps, including the crucial ray-space-to-R^3 mappings introduced in this paper. On the attention side, SE(3)-Transformers provided the template for equivariant attention; here, the authors lift that idea to tokens in ray space, yielding the proposed SE(3)-equivariant transformer in a non-Euclidean signal domain. Finally, NeRF’s ray-based formulation of novel view synthesis motivated ray space as a natural domain for learning geometric priors, clarifying why enforcing SE(3) equivariance over rays is impactful for reconstruction and view synthesis under limited viewpoints.

---
*Generated: 2026-01-07T00:02:04.816991*
