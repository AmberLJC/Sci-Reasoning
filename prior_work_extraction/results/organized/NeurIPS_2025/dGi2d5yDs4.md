# Prior Work Analysis Report

## Target Paper
**Title:** dGi2d5yDs4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Angular Steering reframes behavior control in language models as a geometric rotation within the 2D subspace spanned by the current activation and a target behavior direction. This view directly builds on the concept-direction paradigm introduced by TCAV, which established that human-meaningful concepts can be represented as linear directions in intermediate representations. Earlier geometric interventions like Bolukbasi et al.’s hard debiasing and the NLP-focused INLP demonstrated that projecting out or nulling such directions can suppress unwanted attributes, but these approaches can be brittle and over-suppressive. In parallel, work on GAN latent spaces (GANSpace) showed that traversing interpretable directions affords smooth, continuous control—an intuition Angular Steering adopts for LMs, but implements via rotation rather than translation.

Theoretical groundwork from Toy Models of Superposition highlighted that features cohabit activation subspaces and interfere, motivating Angular Steering’s design to constrain edits to a fixed plane and control magnitude via angle to mitigate collateral interactions. Practical insights from ROME’s layer-localized activation edits inform the adaptive variant of Angular Steering, guiding where rotations are most effective with minimal side effects. Finally, the task-vector literature demonstrated that linear directions can capture complex behaviors and be composed algebraically; Angular Steering operates in the same spirit but provides a more stable, continuous knob than raw addition. Together, these strands converge on a principled, geometry-first intervention that preserves model competence while enabling fine-grained control over behaviors such as refusal and compliance.

---
*Generated: 2026-01-07T00:21:32.238095*
