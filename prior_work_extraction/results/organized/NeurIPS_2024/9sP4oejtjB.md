# Prior Work Analysis Report

## Target Paper
**Title:** 9sP4oejtjB
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CTDS emerges at the intersection of latent dynamical systems for neural populations and biologically grounded E/I network principles. Foundational latent models such as GPFA and LDS/PLDS (with scalable variational inference) established that population activity can be captured by low-dimensional latent trajectories, while LFADS further showed how dynamical priors and inferred inputs explain single-trial variability and perturbations. Parallel advances in structured state-space models, exemplified by recurrent switching LDS, highlighted how modular, interpretable latent structures and constrained interactions improve explanatory power.

On the biological side, classic Wilson–Cowan theory and modern E/I RNNs trained under Dale’s law demonstrated that excitatory and inhibitory populations exert sign-consistent influences that shape circuit dynamics and computation. CTDS fuses these threads: it defines separate latent variables tied to identified cell classes and imposes sign constraints on both dynamics and emissions so that excitatory latents have positive and inhibitory latents negative effects. This design directly encodes Dale’s principle into a probabilistic LDS, providing interpretable decompositions of circuit activity and principled predictions of cell-type-specific perturbations. Finally, the demixing ethos of dPCA informs CTDS’s insistence on factorized, interpretable subspaces—here organized by biology rather than task variables—while retaining full latent dynamical coupling. The result is a model that advances beyond generic latent dynamics by binding latent structure to cell identity and biophysical constraints, enabling new insights into the functional roles of distinct cell classes.

---
*Generated: 2026-01-06T23:33:35.530527*
