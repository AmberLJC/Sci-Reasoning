# Prior Work Analysis Report

## Target Paper

**Title:** OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text

**Conference:** ICLR 2025 (spotlight)

**Authors:** Qingyun Li, Zhe Chen, Weiyun Wang, Wenhai Wang, Shenglong Ye, Zhenjiang Jin, Guanzhou Chen, Yinan He, Zhangwei Gao, Erfei Cui, Jiashuo Yu, Hao Tian, Jiasheng Zhou, Chao Xu, Bin Wang, Xingjian Wei, Wei Li, Wenjian Zhang, Bo Zhang, Pinlong Cai, Licheng Wen, Xiangchao Yan, Pei Chu, Yi Wang, Min Dou, Changyao Tian, Xizhou Zhu, Lewei Lu, Yushi Chen, Junjun He, Tong Lu, Yali Wang, Limin Wang, Dahua Lin, Yu Qiao, Botian Shi, Conghui He, Jifeng Dai

**Keywords:** Image-text interleaved dataset

**Abstract:** 
> Image-text interleaved data, consisting of multiple images and texts arranged in a natural document format, aligns with the presentation paradigm of internet data and closely resembles human reading habits. Recent studies have shown that such data aids multimodal in-context learning and maintains the capabilities of large language models during multimodal fine-tuning. However, the limited scale and diversity of current image-text interleaved data restrict the development of multimodal large lang...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Flamingo: a Visual Language Model for Few-Shot Learning** (2022)
- *Authors:* Jean-Baptiste Alayrac et al.
- *Direct Connection:* Flamingo established that pretraining on naturally interleaved image–text sequences enables multimodal in-context learning while preserving LLM abilities, directly motivating the need for very large interleaved corpora.

**WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Learning** (2021)
- *Authors:* Krishna Srinivasan et al.
- *Direct Connection:* WIT demonstrated the value of multilingual, document-style associations of multiple images with surrounding text, a formulation OmniCorpus generalizes to broader, noisier web sources at far larger scale.

### 🔍 Gap Identification

**IDEFICS: An Open-Source Visual Language Model** (2023)
- *Authors:* Hugo Laurençon et al.
- *Direct Connection:* IDEFICS showed strong gains from training on OBELICS-style interleaved data but explicitly noted the bottleneck of limited public interleaved data, highlighting the need for a much larger, higher-quality corpus.

**OpenFlamingo: An Open-Source Framework for Training Large Autoregressive Vision-Language Models** (2023)
- *Authors:* Anas Awadalla et al.
- *Direct Connection:* OpenFlamingo’s gap to proprietary Flamingo was traced largely to the scarcity and scale limits of open interleaved web data (primarily OBELICS/mmC4), directly motivating a dramatically larger interleaved dataset.

### 📊 Baseline

**OBELICS: Open Web-Scale Document-Level Vision–Text Dataset** (2023)
- *Authors:* Hugo Laurençon et al.
- *Direct Connection:* OBELICS introduced an open pipeline for extracting and filtering document-level, layout-preserving interleaved image–text data from the web, which OmniCorpus scales and diversifies far beyond.

**mmC4: Multimodal C4** (2023)
- *Authors:* Zhu et al.
- *Direct Connection:* mmC4 formulated a large-scale interleaved corpus by inserting webpage images into cleaned C4 text documents, serving as a primary public baseline whose limited scale and source diversity OmniCorpus addresses.

---

## Synthesis: How Prior Work Led to This Paper

Flamingo showed that training on sequences where images and text are interleaved in natural web order yields multimodal in-context learning while preserving strong language abilities, identifying interleaved, document-level data as uniquely valuable. OBELICS operationalized this by extracting layout-preserving image–text documents from the open web with a practical filtering pipeline, offering a first broadly accessible corpus for interleaved pretraining. In parallel, mmC4 proposed constructing interleaved data by inserting on-page images into cleaned C4 documents, creating a scalable but still limited public resource. IDEFICS trained open models directly on these interleaved corpora and emphasized that the principal constraint for further gains is the scarcity and limited diversity of public interleaved datasets. OpenFlamingo reinforced this diagnosis by attributing its gap to proprietary Flamingo largely to the small quantity and constrained coverage of available open interleaved data (chiefly OBELICS and mmC4). Earlier, WIT evidenced the benefits of multilingual, document-style image–text associations, foreshadowing the need for broader linguistic and source diversity. Together, these works defined interleaved web documents as the right pretraining substrate, provided initial open pipelines, and exposed a scale and diversity ceiling that capped model performance. The natural next step was to build a unified, much larger corpus that preserves document structure across vastly more sources and languages—including video-centric sites—while maintaining quality through an efficient data engine, thereby removing the data bottleneck that had limited open multimodal pretraining.

---

*Analysis generated on: 2026-01-06T15:57:08.896844*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
