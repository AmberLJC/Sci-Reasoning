# Prior Work Analysis Report

## Target Paper
**Title:** yb5xV8LFDq
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Active Learning for Convolutional Neural Networks: A Core-Set Approach** (2018)
- *Authors:* O. Sener et al.
- *Connection:* Introduced the modern core-set perspective for deep models under a cardinality constraint; the present work generalizes this framing by inverting the objective to minimize cardinality subject to a performance constraint.

**Learning to Reweight Examples for Robust Deep Learning** (2018)
- *Authors:* M. Ren et al.
- *Connection:* Provides the bilevel, validation-driven reweighting mechanism that underpins our performance-first selection; we adapt this idea to discrete selection and couple it with explicit coreset-size minimization.

### 🔍 Gap Identification

**Beyond Neural Scaling Laws: Beating Power-Law Scaling via Data Pruning** (2022)
- *Authors:* M. Sorscher et al.
- *Connection:* Showed large fractions of data can be pruned without hurting accuracy but lacked a principled way to find the minimal subset for a target performance, a gap the refined coreset formulation explicitly addresses.

### 📊 Baseline

**Coresets for Data-efficient Training of Neural Networks** (2020)
- *Authors:* H. Mirzasoleiman et al.
- *Connection:* Established fixed-budget coreset selection for deep nets via submodular/gradient-based surrogates; the present work directly improves on this paradigm by replacing a pre-set size with a performance-constrained formulation that adaptively finds the smallest subset preserving accuracy.

**Grad-Match: Gradient Matching based Data Subset Selection for Efficient Deep Learning** (2021)
- *Authors:* K. Killamsetty et al.
- *Connection:* Serves as a leading budgeted coreset baseline our method supersedes, shifting from optimizing gradient similarity under a fixed size to prioritizing model performance and searching for the minimal subset that achieves it.

### 🔧 Extension

**GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning** (2021)
- *Authors:* K. Killamsetty et al.
- *Connection:* Builds on GLISTER’s bilevel, validation-loss–driven selection by transforming its fixed-cardinality objective into a lexicographic program that first satisfies a target validation performance and then minimizes coreset size.

### 🔗 Related Problem

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* P. W. Koh et al.
- *Connection:* Influence functions quantify how removing training points affects validation loss, directly motivating our priority to safeguard validation performance when shrinking the dataset.

---

## Synthesis

The core innovation of refined coreset selection—minimizing coreset size under explicit performance constraints with a performance-first (lexicographic) priority—emerges by rethinking established, budgeted subset selection. Early work by Sener and Savarese cast deep learning data selection as a core-set problem under a fixed cardinality, setting the foundational framing. CRAIG operationalized this for end-to-end neural network training via submodular/gradient-based surrogates, while Grad-Match popularized gradient matching as a strong fixed-budget baseline. In parallel, Ren et al. introduced bilevel, validation-driven reweighting, demonstrating that optimizing a validation objective through training-set weights is feasible and effective—an idea later specialized to subset selection by GLISTER, which formalized bilevel selection but still under a fixed budget. Together, these works established both the problem formulation (select a subset) and the principal optimization tools (bilevel/validation-driven criteria and gradient proxies), yet all assumed the subset size is given. Empirical advances in data pruning, particularly Sorscher et al., highlighted that substantial data can be removed with minimal accuracy loss but did not offer a principled mechanism to determine the minimal set meeting a target performance. The present work directly extends bilevel subset selection (GLISTER) by inverting the objective: it enforces a target validation performance and only then reduces the subset size, guided conceptually by influence-based thinking on how point removal affects validation loss. This yields an efficiency-focused, constraint-aware coreset selection procedure with theoretical convergence guarantees.

---
*Generated: 2026-01-06T23:09:26.488661*
