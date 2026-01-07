# Prior Work Analysis Report

## Target Paper
**Title:** glfYOAzh2f
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core innovation—selective generation with theoretical guarantees on the false discovery rate of incorrect outputs defined via textual entailment—emerges at the intersection of selective prediction, conformal risk control, and NLI-based correctness assessment. Benjamini and Hochberg (1995) supply the foundational notion of false discovery rate and the BH procedure, which the authors adapt to the generative setting to define and control FDR with respect to entailment (FDR-E). Building on abstention-based supervised methods, SelectiveNet (Geifman & El-Yaniv, 2019) provides the selective prediction blueprint that SGenSup directly modifies: the acceptance rule is retained, but correctness is redefined by an entailment relation rather than task-specific labels. Conformal Risk Control (Angelopoulos et al., 2022) contributes the calibration philosophy for distribution-free risk guarantees using verifiers, informing both the design of SGen’s acceptance thresholds and the semi-supervised extension that leverages unlabeled data with verifier feedback. To make principled guarantees tractable in open-ended language generation, the work reuses textual entailment as a universal correctness predicate, grounded in the RTE formulation (Dagan et al., 2005). MNLI (Williams et al., 2018) supplies broad-coverage, human-annotated entailment data for training/selecting robust NLI verifiers, which SGenSup depends on. Finally, FactCC (Kryściński et al., 2020) establishes the practical effectiveness of NLI-style verifiers for detecting hallucinations in generated text, justifying SGen’s choice of entailment as the operative correctness signal for risk control. Together, these works directly underwrite SGen’s theoretical and algorithmic path to FDR-controlled, verifier-driven selective language generation.

---
*Generated: 2026-01-06T23:33:35.527044*
