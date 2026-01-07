# Prior Work Analysis Report

## Target Paper
**Title:** FXJDcriMYH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core idea—codifying model growth into atomic operators and showing that depthwise stacking (G_stack) yields superior compute–performance during LLM pre-training—stands on a lineage that merges function-preserving transformation with deep-Transformer stabilization and modern scaling evaluation. Net2Net introduced the central mechanism for growth via function-preserving depth/width expansions; G_stack is effectively a Transformer-tailored Net2Deeper, transplanting and duplicating blocks so the larger model inherits and accelerates from a smaller model’s representation. Network Morphism generalized such weight mappings, providing the conceptual template this work adopts when formalizing growth operators for Transformers.
At the architecture/training level, making growth practical demands stable optimization of much deeper stacks. DeepNet (DeepNorm) supplied the residual-scaling principles that allow deep Transformers to train reliably after stacking, ensuring that the copied layers do not destabilize optimization. Empirically, LayerDrop established that Transformer depth can be manipulated during training, encouraging a systematic comparison of depthwise strategies and positioning G_stack against a natural depth-variation baseline.
Finally, the paper’s comprehensive, compute-aware evaluation is anchored in the LLM scaling canon: Kaplan et al.’s scaling laws and Hoffmann et al.’s compute-optimality (Chinchilla) shape the experimental design and metrics for fair comparisons across growth paths. Together, these prior works enable the authors to (1) formalize growth operators, (2) make depthwise stacking stable and effective at LLM scale, and (3) derive actionable, compute-grounded guidelines for efficient pre-training.

---
*Generated: 2026-01-06T23:39:42.969615*
