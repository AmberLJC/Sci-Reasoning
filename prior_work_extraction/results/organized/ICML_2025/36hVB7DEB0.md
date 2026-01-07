# Prior Work Analysis Report

## Target Paper
**Title:** 36hVB7DEB0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—demonstrating grokking in a non-neural setting by coupling kernel machines with Recursive Feature Machines (RFM) driven by the Average Gradient Outer Product (AGOP)—builds on two converging threads: empirical characterizations of grokking on modular arithmetic and algorithms that induce feature learning beyond neural architectures. Power et al. (2022) established grokking on modular tasks, defining the late-emergence template the present work seeks to replicate without neural networks. Follow-up mechanistic studies, typified by Nanda et al. (2023), argued that grokking stems from representation formation rather than a quirk of SGD alone, directly motivating a test of whether non-neural feature-learning procedures can produce the same phase transition.

That feature-learning mechanism arrives via RFM/AGOP. The RFM framework (Radhakrishnan, Pandit, Belkin, 2024) provides a general, iterative method to extract task-aligned features using AGOP, conceptually grounded in Amari’s natural gradient view of the gradient outer product as encoding learning geometry. By marrying RFM with kernel machines, the authors explicitly step outside the NTK fixed-feature regime characterized by Jacot et al. (2018), showing that once kernels are equipped with adaptive features, they too can grok. Finally, the interpretive lens of double descent from Belkin et al. (2019) frames why sharp generalization transitions can occur even when training loss is identically zero, aligning the paper’s observed phase transition with broader modern generalization phenomena. Together, these works directly inform the algorithmic choice (RFM/AGOP), the task and phenomenon (modular arithmetic grokking), and the theoretical framing (emergent phase transitions under interpolation) that constitute the paper’s key innovation.

---
*Generated: 2026-01-07T00:21:32.366653*
