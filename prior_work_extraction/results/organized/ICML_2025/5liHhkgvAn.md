# Prior Work Analysis Report

## Target Paper
**Title:** 5liHhkgvAn
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

SDP-CROWN sits at the intersection of two verification paradigms: scalable linear bound propagation and tight (but costly) semidefinite relaxations. Linear relaxation pipelines such as Wong and Kolter’s convex outer adversarial polytope, Dvijotham et al.’s dual approach, and the CROWN-IBP framework established how per-neuron linear bounds can be propagated efficiently and optimized, enabling certification and even certified training at scale. However, the per-neuron nature of these relaxations—highlighted by the convex relaxation barrier—often misses crucial inter-neuron coupling, leading to loose bounds on challenging networks.

On the other hand, SDP-based methods, notably Raghunathan et al.’s semidefinite relaxations and the IQC/SDP formulations by Fazlyab et al., naturally encode cross-neuron, L2-type coupling through second-moment or quadratic constraints, yielding significantly tighter certificates but with cubic complexity that limits applicability to small models. SDP-CROWN bridges this gap by extracting an L2-norm-based, inter-neuron coupling inequality from the SDP/IQC perspective and translating it into a single additional linear parameter per layer. This preserves the composability and speed of IBP/LiRPA propagation while injecting the key coupling information that SDPs exploit. Theoretically, this yields up to a sqrt(n) tightening over traditional per-neuron bounds; practically, it integrates seamlessly into existing dual/LiRPA frameworks like CROWN-IBP, improving certificates without invoking full SDPs. In short, SDP-CROWN operationalizes SDP tightness within a linear propagation toolkit, overcoming known LP barriers while retaining large-scale efficiency.

---
*Generated: 2026-01-07T00:21:33.191693*
