# Prior Work Analysis Report

## Target Paper

**Title:** Sparse components distinguish visual pathways & their alignment to neural networks

**Conference:** ICLR 2025 (spotlight)

**Authors:** Ammar I Marvi, Nancy Kanwisher, Meenakshi Khosla

**Keywords:** visual representations, alignment, sparse decomposition, neural pathways, brain and machine vision

**Abstract:** 
> The ventral, dorsal, and lateral streams in high-level human visual cortex are implicated in distinct functional processes. Yet, deep neural networks (DNNs) trained on a single task model the entire visual system surprisingly well, hinting at common computational principles across these pathways. To explore this inconsistency, we applied a novel sparse decomposition approach to identify the dominant components of visual representations within each stream. Consistent with traditional neuroscience...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Separate visual pathways for perception and action** (1992)
- *Authors:* A. David Milner and Melvyn A. Goodale
- *Direct Connection:* By establishing distinct dorsal and ventral visual pathways with different functional goals, this work motivates a stream-specific decomposition and alignment analysis that the new method explicitly performs.

**Representational similarity analysis – connecting the branches of systems neuroscience** (2008)
- *Authors:* Nikolaus Kriegeskorte et al.
- *Direct Connection:* RSA provides the foundational framework for brain–model representational comparison that the new Sparse Component Alignment is designed to refine by operating over sparse, interpretable axes rather than undifferentiated representational dissimilarities.

### 💡 Inspiration

**A Reduced-Dimension fMRI Shared Response Model** (2015)
- *Authors:* Po-Hsuan Chen et al.
- *Direct Connection:* SRM’s idea of describing brain activity via a small set of shared latent components directly inspires using component-based representations, which the new work extends with sparsity and applies within cortical streams to align with DNNs.

**Learning the parts of objects by non-negative matrix factorization** (1999)
- *Authors:* Daniel D. Lee and H. Sebastian Seung
- *Direct Connection:* NMF’s demonstration that sparse, parts-based factors yield interpretable visual features motivates seeking sparse component bases in neural data to uncover parts-like selectivity across streams.

### 📊 Baseline

**Similarity of neural network representations revisited** (2019)
- *Authors:* Simon Kornblith et al.
- *Direct Connection:* CKA is a primary baseline metric for comparing representations, and the new method is proposed to address CKA’s lack of component-level interpretability by aligning brains and DNNs along sparse components.

**Brain-Score: Which Artificial Neural Network for Object Recognition is Most Brain-Like?** (2018)
- *Authors:* Martin Schrimpf et al.
- *Direct Connection:* Brain-Score’s global alignment benchmarks motivate the need for a fine-grained alternative, and the new approach targets this gap by quantifying stream- and component-specific alignment that global scores miss.

### 🔧 Extension

**Sparse Principal Component Analysis** (2006)
- *Authors:* Hui Zou et al.
- *Direct Connection:* The sparse decomposition in this paper builds on SPCA-style objectives to extract sparse loading vectors, enabling interpretable components that reveal category-selective axes within each visual stream.

---

## Synthesis: How Prior Work Led to This Paper

Evidence that the visual system comprises distinct pathways for perception and action established that dorsal and ventral streams implement different computations, motivating analyses that respect stream-specific structure. Component-based models of fMRI, particularly the Shared Response Model, showed that brain responses can be captured by low-dimensional latent axes that summarize shared variance across subjects. In parallel, methods such as Sparse PCA and non-negative matrix factorization demonstrated that imposing sparsity yields parts-based, interpretable factors that map cleanly onto meaningful features in visual data. For comparing biological and artificial representations, representational similarity analysis provided a general geometry-based framework, and CKA offered a robust, widely used similarity measure for neural network representations. Large-scale benchmarks like Brain-Score then standardized global model–brain comparisons, emphasizing that single-task DNNs can predict neural responses surprisingly well but leaving open how alignment varies across pathways and along interpretable representational axes. Taken together, these works revealed both the feasibility and the limits of current practice: low-dimensional components can summarize brain activity, sparsity yields interpretability, and alignment metrics enable model–brain comparison, yet standard metrics average over dimensions and ignore pathway structure. The natural next step is to learn sparse, interpretable components within each visual stream and to assess alignment along these axes. By combining SRM-like componentization with sparsity principles from SPCA/NMF and embedding them in an alignment framework that refines RSA/CKA, the new approach isolates pathway-specific components and quantifies how DNNs align with those components, resolving the mismatch between global alignment and functional specialization.

---

*Analysis generated on: 2026-01-06T07:35:09.269617*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
