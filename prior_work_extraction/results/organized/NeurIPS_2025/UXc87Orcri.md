# Prior Work Analysis Report

## Target Paper
**Title:** UXc87Orcri
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

MetaGS’s key contribution—robust out-of-distribution 3D relighting by meta-learning a physics-guided Gaussian representation—rests on two converging lines of prior work. First, the representation and rendering backbone derives from 3D Gaussian Splatting, which established a fast, differentiable point-based alternative to NeRFs. MetaGS retools this backbone by replacing per-Gaussian appearance (e.g., SH colors) with a physically motivated Blinn–Phong decomposition, directly inspired by classic illumination models that cleanly separate diffuse and specular shading. The decision to embed physical priors is reinforced by inverse-rendering advances like NeRV, which showed that disentangling reflectance, lighting, and visibility is essential for controllable relighting.
Second, MetaGS targets generalization under lighting shifts. NeRF-W highlighted the importance of modeling appearance/illumination variability, while pixelNeRF demonstrated that learned priors can generalize across scenes from limited inputs. MetaGS synthesizes these insights with meta-learning: leveraging a MAML-style objective to train Gaussian geometry and appearance so they are explicitly optimized to adapt quickly and reliably to unseen lighting. This unifies generalizable priors with fast adaptation, but at the level of a real-time Gaussian renderer and under a physics-based shading parameterization. Together, these works directly inform MetaGS’s design: a Gaussian representation capable of efficient relighting, stabilized by physical shading structure, and trained with meta-learning to maintain reconstruction fidelity and view synthesis quality under severe OOD illumination.

---
*Generated: 2026-01-07T00:05:12.520589*
