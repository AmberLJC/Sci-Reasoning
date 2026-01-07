# Prior Work Analysis Report

## Target Paper
**Title:** x9vcgXmRD0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Utility Engineering’s central move—testing whether large language models exhibit internally coherent ‘values’ and then shaping those values—draws directly from utility theory, preference inference, and recent alignment practice. Von Neumann–Morgenstern provides the foundational representation result that coherent preferences can be captured by a utility function; Afriat’s revealed-preference program turns that idea into testable consistency criteria and constructive utility recovery, which the authors adapt from economics to the LLM setting. On the machine learning side, Ng and Russell’s inverse reinforcement learning reframes behavior as evidence about latent rewards/utilities, while Christiano et al. operationalize preference-based learning to build and optimize such utilities from pairwise comparisons—machinery that underpins the paper’s ‘control’ side of engineering utilities.

The empirical claim that coherence strengthens with model size is situated within the emergence literature, most notably Wei et al., who document qualitative capability shifts with scale; here, value coherence is treated as a new emergent property. For steering those emergent utilities, Constitutional AI demonstrates how explicit normative principles can systematically shape assistant behavior, and Utility Engineering generalizes this toward engineering the underlying utility landscape rather than only surface outputs. Finally, prior work by Hendrycks and colleagues on aligning AI with shared human values supplies both motivation and benchmarks for value-sensitive evaluation; the present paper advances from measuring moral judgments to probing whether models possess structured, utility-like value systems and how those systems can be analyzed and controlled.

---
*Generated: 2026-01-06T23:42:48.142151*
