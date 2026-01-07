# Prior Work Analysis Report

## Target Paper

**Title:** Prototypical Information Bottlenecking and Disentangling for Multimodal Cancer Survival Prediction

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yilan Zhang, Yingxue Xu, Jianqi Chen, Fengying Xie, Hao Chen

**Keywords:** multimodal survival prediction, computational pathology

**Abstract:** 
> Multimodal learning significantly benefits cancer survival prediction, especially the integration of pathological images and genomic data. Despite advantages of multimodal learning for cancer survival prediction, massive redundancy in multimodal data prevents it from extracting discriminative and compact information: (1) An extensive amount of intra-modal task-unrelated information blurs discriminability, especially for gigapixel whole slide images (WSIs) with many patches in pathology and thous...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**DeepSurv: Personalized Treatment Recommender System Using A Cox Proportional Hazards Deep Neural Network** (2018)
- *Authors:* Katzman et al.
- *Direct Connection:* PIBD trains with the Cox partial likelihood from DeepSurv to model time-to-event risk, grounding its learning objective in the established survival analysis formulation.

### 💡 Inspiration

**Prototypical Networks for Few-shot Learning** (2017)
- *Authors:* Snell et al.
- *Direct Connection:* The notion of class prototypes motivates PIBD’s prototype dictionary and assignment mechanism, which aggregates numerous WSI patches or genomic pathways into a small set of discriminative prototypes to mitigate intra-modal redundancy.

### 🔍 Gap Identification

**CLAM: Data Efficient and Weakly Supervised Clustering and Attention Multiple Instance Learning for Whole Slide Image Classification** (2021)
- *Authors:* Lu et al.
- *Direct Connection:* By highlighting that attention-based MIL still over-selects redundant or task-irrelevant patches in gigapixel WSIs, CLAM exposes the intra-modal redundancy problem that PIBD addresses via prototype-based information bottlenecking instead of instance attention alone.

### 📊 Baseline

**Pathomic Fusion: An Integrated Framework for Fusing Histopathology and Genomic Features for Cancer Prognosis** (2020)
- *Authors:* Chen et al.
- *Direct Connection:* As a primary multimodal survival baseline combining WSIs and omics, Pathomic Fusion’s lack of redundancy suppression motivates PIBD’s replacement of late fusion with prototypical bottlenecking plus disentangling to preserve modality-specific prognostic signals.

### 🔧 Extension

**Deep Variational Information Bottleneck** (2017)
- *Authors:* Alemi et al.
- *Direct Connection:* PIBD directly extends the VIB objective by implementing a prototype-driven stochastic bottleneck to compress intra-modal content while preserving survival-relevant information, replacing instance-wise encoders with prototype-level compression.

**Learning Factorized Multimodal Representations** (2019)
- *Authors:* Tsai et al.
- *Direct Connection:* PIBD adopts and adapts the shared–private factorization idea to explicitly disentangle common versus modality-specific components across pathology and genomics, adding prototype-level disentangling and information constraints to curb inter-modal redundancy.

---

## Synthesis: How Prior Work Led to This Paper

The variational information bottleneck formalism establishes a principled way to compress inputs while retaining task-relevant content, but is typically instantiated at the instance level (Alemi et al., 2017). Prototypical networks introduced prototype-based summarization, where embeddings are aggregated into representative prototypes that capture discriminative structure (Snell et al., 2017). In multimodal learning, factorized representations separating shared from private components were shown to reduce cross-modal interference via explicit disentanglement with orthogonality and reconstruction constraints (Tsai et al., 2019). For multimodal cancer prognosis specifically, Pathomic Fusion demonstrated the efficacy of combining histopathology and genomics for survival prediction through late/tensor-based fusion, yet lacked mechanisms to eliminate redundant shared content that can swamp modality-specific signals (Chen et al., 2020). On the pathology side, CLAM revealed that even attention-based MIL still over-selects redundant or task-irrelevant patches in gigapixel WSIs, motivating stronger mechanisms to compact instance sets into discriminative summaries (Lu et al., 2021). Training across these settings is commonly anchored in the Cox proportional hazards objective, as established in DeepSurv for deep survival modeling (Katzman et al., 2018). Together, these insights highlight a gap: multimodal survival systems needed a way to simultaneously remove intra-modal redundancy and disentangle inter-modal shared versus specific signals, without sacrificing prognostic information. PIBD naturally synthesizes these threads by replacing instance-level encoders with prototype-driven information bottlenecks to compact each modality and by extending shared–private factorization with prototype-level disentangling under an IB objective, all optimized end-to-end with a Cox loss—thereby preserving discriminative, modality-specific survival cues while suppressing redundant noise within and across modalities.

---

*Analysis generated on: 2026-01-06T18:10:41.972287*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
