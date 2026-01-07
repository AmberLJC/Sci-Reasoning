# Prior Work Analysis Report

## Target Paper
**Title:** ugBmWX3H1R
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CUPID’s core insight—training physics-driven deep MRI reconstructions without any access to raw k-space—sits at the intersection of compressibility priors, parallel-imaging physics, and unrolled deep reconstruction. Lustig–Donoho–Pauly’s compressed sensing MRI established compressibility as a powerful prior and a workable objective, a principle CUPID repurposes as an unsupervised image-domain regularization when only routine reconstructions are available. The fidelity side is grounded in parallel imaging: SENSE formalized the multi-coil forward model, while GRAPPA became the ubiquitous clinical PI recon on scanners. CUPID leverages this reality by defining a “parallel-imaging fidelity” that can be instantiated from readily available vendor recon outputs, eliminating the need for raw k-space during training.
Model-wise, CUPID inherits the unrolled PD-DL paradigm from MoDL and variational networks—alternating learned priors with physics consistency—yet replaces the conventional k-space data-consistency with its PI-based fidelity. From the learning perspective, SSDU demonstrated that PD-DL can be trained without fully sampled ground truth by exploiting measurement splits; CUPID advances this line by removing the raw-data dependency altogether, expanding applicability to under-resourced sites where only final images can be exported. Finally, Plug-and-Play priors provide the algorithmic justification for decoupling learned image priors from the measurement model, supporting CUPID’s strategy of training priors on image-only corpora and enforcing physics via a separate fidelity mechanism. Together, these works directly scaffold CUPID’s compressibility-inspired objective and its practical, raw-free fidelity formulation.

---
*Generated: 2026-01-06T23:42:48.118429*
