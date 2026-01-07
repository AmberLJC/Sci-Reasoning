# Prior Work Analysis Report

## Target Paper

**Title:** STAR: Synthesis of Tailored Architectures

**Conference:** ICLR 2025 (oral)

**Authors:** Armin W Thomas, Rom Parnichkun, Alexander Amini, Stefano Massaroli, Michael Poli

**Keywords:** alternative architectures, deep signal processing, language models

**Abstract:** 
> Iterative improvement of model architectures is fundamental to deep learning: Transformers first enabled scaling, and recent advances in model hybridization have pushed the quality-efficiency frontier. However, optimizing architectures remains challenging and expensive, with a variety of automated or manual approaches that fall short, due to limited progress in the design of search spaces and due to the simplicity of resulting patterns and heuristics. In this work, we propose a new approach for ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Mamba: Linear-Time Sequence Modeling with Selective State Spaces** (2023)
- *Authors:* Gu and Dao et al.
- *Direct Connection:* Mamba formalized input-dependent (selective) state-space operators, providing the concrete linear input-varying systems paradigm that STAR generalizes into a broader architectural search space.

**Regularized Evolution for Image Classifier Architecture Search** (2019)
- *Authors:* Real et al.
- *Direct Connection:* Regularized (aging) evolution established a robust gradient-free algorithm for neural architecture search that STAR adopts and adapts to explore its LIV-based genome space at population scale.

**A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II** (2002)
- *Authors:* Deb et al.
- *Direct Connection:* NSGA-II provides the Pareto-based multi-objective selection mechanism that STAR leverages to simultaneously optimize model quality and efficiency across large architecture populations.

### 🔍 Gap Identification

**DARTS: Differentiable Architecture Search** (2019)
- *Authors:* Liu et al.
- *Direct Connection:* DARTS’s cell-based search spaces tend to yield simple, repetitive motifs, a limitation explicitly targeted by STAR’s richer LIV-theoretic search space and hierarchical genome design.

### 📊 Baseline

**StripedHyena: Efficient Long-Context Language Models with Hybrid Alternating Convolution and Attention** (2024)
- *Authors:* Poli et al.
- *Direct Connection:* StripedHyena demonstrated that manually designed hybrids of attention and long-convolution can push the quality–efficiency frontier, forming the primary hybrid baseline whose hand-crafted patterns STAR aims to automatically synthesize and surpass.

### 🔧 Extension

**Evolving Deep Neural Networks (CoDeepNEAT)** (2017)
- *Authors:* Miikkulainen et al.
- *Direct Connection:* CoDeepNEAT introduced hierarchical genotype–phenotype encodings and recombination for neural architectures, which STAR extends with a numeric, hierarchical genome tailored to linear input-varying operators and their interconnections.

### 🔗 Related Problem

**Hyena Hierarchy: Towards Larger Convolutional Language Models** (2023)
- *Authors:* Poli et al.
- *Direct Connection:* Hyena introduced long-range, FFT-based convolutional operators as efficient alternatives to attention, supplying a key class of deep signal-processing units that STAR includes as primitives in its search space.

---

## Synthesis: How Prior Work Led to This Paper

Selective state-space models showed that sequence processing can be cast as input-dependent linear dynamical operators with hardware-efficient scans, grounding a rigorous class of linear input-varying systems. In parallel, long-range convolutional operators demonstrated that learned filters and FFT-based mechanisms can rival attention for dependency modeling while improving efficiency. Building on these insights, manually engineered hybrids that interleave long convolutions with local attention revealed that mixing complementary units improves the quality–efficiency trade-off, albeit via bespoke design rules. Independently, neuroevolution established hierarchical genotype–phenotype encodings and recombination as practical tools for exploring large architectural spaces, while regularized evolution provided a simple, stable algorithm for population-based search at scale. Multi-objective evolutionary methods further introduced Pareto selection to balance accuracy with deployment costs. Yet differentiable NAS with cell-level search spaces often converged to shallow, repetitive motifs, indicating that the expressiveness of the search space—not just the optimizer—was a key bottleneck.
Together, these strands suggested an opportunity: unify input-varying linear operators and deep signal-processing units as first-class primitives, then automatically discover hybrid interconnections under multi-objective constraints using evolutionary search. By adopting a hierarchical numerical genome tailored to linear input-varying compositions, and by coupling aging evolution with Pareto selection, the current work operationalizes this synthesis, automating the discovery of diverse, efficient hybrids that generalize beyond hand-crafted patterns and overcome the simplicity limits of prior NAS spaces.

---

*Analysis generated on: 2026-01-06T13:40:55.763675*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
