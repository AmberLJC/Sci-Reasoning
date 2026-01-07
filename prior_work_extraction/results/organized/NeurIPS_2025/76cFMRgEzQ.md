# Prior Work Analysis Report

## Target Paper
**Title:** 76cFMRgEzQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—modeling mixed-source knowledge propagation as entity flow and introducing an entity-aware probe—sits at the intersection of RAG, probing, and mechanistic interpretability. Lewis et al. (2020) defined the RAG setting that necessitates understanding how parametric and retrieved knowledge interact in LLMs. Abnar and Zuidema (2020) provided the conceptual template for tracing internal computation via flow, which this work generalizes from attention to entity-conditioned information flow across the full forward pass. The entity-aware probe builds directly on linear probing (Alain and Bengio, 2017), but addresses its static-target limitation by conditioning on dynamically specified entities. To ensure the probe’s measurements reflect model internals rather than probe capacity, design principles from Hewitt and Liang (2019) guide the use of minimal additional parameters and controls. The mechanism for specifying targets—special entity markers—draws from successful practice in relation extraction (Soares et al., 2019), enabling precise localization of entity-relevant activations. Implementationally, LoRA (Hu et al., 2022) supplies a lightweight adaptation pathway: a rank-8 update that processes markers without altering the base model broadly. Finally, attribution and localization ideas from ROME (Meng et al., 2022) inspire the validation experiments that check whether detected entity flows correspond to the loci of parametric versus retrieved knowledge. Together, these strands yield a principled, practical framework to trace, attribute, and reconcile knowledge sources within LLMs.

---
*Generated: 2026-01-07T00:02:04.968735*
