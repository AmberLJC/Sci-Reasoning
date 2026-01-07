# Prior Work Analysis Report

## Target Paper
**Title:** mp8u2Pcmqz
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

DuQuant’s core contribution—dual transformations that redistribute activation outliers via targeted rotations and block-balancing permutations—directly grows from the LLM quantization literature on identifying and mitigating outlier channels and from classical quantization preconditioning. LLM.int8() established that activation outliers are concentrated in a few identifiable dimensions and that handling them specially dramatically improves low-bit inference; DuQuant explicitly uses those outlier indices as priors to construct rotations that diffuse their mass. SmoothQuant demonstrated that channel-wise rescaling can migrate and smooth normal outliers, enabling low-bit activations, but struggles with extremely large magnitudes; DuQuant complements this by employing orthogonal rotations to tame massive outliers that resist simple scaling. AWQ emphasized activation-aware, channel-level sensitivity and group-wise decisions; DuQuant operationalizes this sensitivity by actively re-distributing high-magnitude channels both within blocks (rotations) and across blocks (permutation) to equalize variance. GPTQ’s block/group quantization is a standard backbone but is vulnerable when outliers cluster within groups; DuQuant’s zigzag permutation explicitly spreads outlier channels to stabilize group-wise statistics. Finally, the notion that pre-quantization orthogonal transforms can minimize distortion traces to Optimized Product Quantization, while Outlier Channel Splitting provides a conceptual precedent for redistributing a single channel’s extreme magnitude—an effect DuQuant attains implicitly via rotation without modifying network topology. Together, these works motivate and enable DuQuant’s rotation-plus-permutation strategy to robustly handle both normal and massive outliers in low-bit LLMs.

---
*Generated: 2026-01-06T23:42:49.040568*
