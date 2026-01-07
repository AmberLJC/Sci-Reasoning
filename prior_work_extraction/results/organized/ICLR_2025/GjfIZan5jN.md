# Prior Work Analysis Report

## Target Paper
**Title:** GjfIZan5jN
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—Inherent Interpretability Score (IIS) and the finding that boosting classifiability can improve interpretability—sits at the intersection of concept-based interpretability, information-theoretic faithfulness, and linear separability evaluation. Network Dissection and Net2Vec first grounded the idea that internal representations can be decomposed into interpretable concept-aligned components and provided concrete procedures to project features onto concept subspaces. TCAV further crystallized the concept-based view, quantifying model sensitivity along human-defined concept directions. Building on this lineage, IIS shifts from per-unit or per-concept assessments to a holistic metric that estimates the ratio of interpretable semantics within a representation.

To make that shift rigorous, the work draws on formal faithfulness criteria: Yeh et al.’s infidelity and ROAR’s remove-and-retrain both operationalize explanation quality via information preserved or lost. IIS echoes this information-centric framing by quantifying the information gap between the full representation and what interpretations can capture, thereby defining interpretability as an information ratio rather than a count of interpretable units. In parallel, disentanglement metrics (Eastwood & Williams) motivate treating “semantic factor content” as a measurable quantity in representations, which IIS adapts to the supervised visual setting.

Finally, the link to classifiability is anchored by linear probes (Alain & Bengio), providing a standardized measure of linear separability. Using this probe-based lens, the paper demonstrates that representation refinements that improve classifiability also increase IIS, unifying prior strands into a coherent, measurable classifiability–interpretability connection.

---
*Generated: 2026-01-06T23:42:48.094395*
