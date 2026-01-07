# Prior Work Analysis Report

## Target Paper

**Title:** InternVid: A Large-scale Video-Text Dataset for Multimodal Understanding and Generation

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yi Wang, Yinan He, Yizhuo Li, Kunchang Li, Jiashuo Yu, Xin Ma, Xinhao Li, Guo Chen, Xinyuan Chen, Yaohui Wang, Ping Luo, Ziwei Liu, Yali Wang, Limin Wang, Yu Qiao

**Keywords:** video-language dataset, video understanding, video generation, multimodal understanding, action recognition, video retrieval

**Abstract:** 
> This paper introduces InternVid, a large-scale video-centric multimodal dataset that enables learning powerful and transferable video-text representations for multimodal understanding and generation. InternVid contains over 7 million videos lasting nearly 760K hours, yielding 234M video clips accompanied by detailed descriptions of total 4.1B words. Our core contribution is to develop a scalable approach to autonomously build a high-quality video-text dataset with large language models (LLM), th...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**HowTo100M: Learning a Text-Video Embedding by Watching Hundred Million Narrated Video Clips** (2019)
- *Authors:* Antoine Miech et al.
- *Direct Connection:* HowTo100M established the web-scale video–text pretraining paradigm using weak ASR transcripts, whose noisy and weakly grounded supervision InternVid directly addresses by replacing metadata/transcripts with LLM-generated, temporally granular descriptions.

**Learning Transferable Visual Models From Natural Language Supervision (CLIP)** (2021)
- *Authors:* Alec Radford et al.
- *Direct Connection:* CLIP introduced the contrastive image–text objective and zero-shot evaluation protocol that InternVid’s ViCLIP directly adopts and extends to video, aligning the dataset design with contrastive video–text representation learning.

### 💡 Inspiration

**LAION-5B: An open large-scale dataset for training next generation image-text models** (2022)
- *Authors:* Christoph Schuhmann et al.
- *Direct Connection:* LAION-5B demonstrated autonomous web-scale curation with automatic filtering, deduplication, and quality control, which InternVid extends to the video domain and augments by synthesizing richer text using LLMs rather than relying solely on raw web metadata.

**LLaVA: Large Language and Vision Assistant** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* LLaVA showed that prompting LLMs with visual inputs can transform sparse captions into rich, instruction-like descriptions, directly motivating InternVid’s use of LLM prompting to generate detailed video descriptions at multiple temporal scales.

### 📊 Baseline

**Frozen in Time: A Joint Video and Image Encoder for End-to-End Retrieval** (2021)
- *Authors:* Max Bain et al.
- *Direct Connection:* Frozen in Time introduced the WebVid scraping recipe showing that short web video titles/descriptions suffice for contrastive pretraining, and InternVid explicitly builds on this scalable harvesting pipeline while overcoming its sparse captions via LLM-written multi-scale descriptions and much larger coverage.

### 🔗 Related Problem

**Video-ChatGPT: Towards Detailed Video Understanding via Large Vision and Language Models** (2023)
- *Authors:* Hassan Maaz et al.
- *Direct Connection:* Video-ChatGPT pioneered leveraging LLMs to synthesize dense supervision for videos (QA/instructions) from frames/transcripts, which InternVid adapts by producing descriptive, multi-granularity captions instead of QA to enable large-scale video–text training.

---

## Synthesis: How Prior Work Led to This Paper

Large-scale video–text learning emerged with HowTo100M, which paired web instructional videos with ASR transcripts to train video–language embeddings despite noisy, weak alignments. Frozen in Time operationalized a scalable web scraping recipe (WebVid) showing that short titles/descriptions paired with videos suffice for strong retrieval when used with contrastive pretraining. Meanwhile, LAION-5B proved that autonomous web-scale curation—crawling, deduplication, and automatic quality filters—can yield high-quality multimodal data without manual labeling. On the modeling side, CLIP established the contrastive language–vision objective and zero-shot evaluation paradigm that many video–text methods inherit. More recently, LLaVA demonstrated that prompting LLMs with visual cues can synthesize rich, instruction-like descriptions from sparse web captions, and Video-ChatGPT extended this LLM-in-the-loop annotation idea to videos by generating detailed QA-style supervision from frames/transcripts.
Together, these works suggested both the opportunity and the bottlenecks: web scraping achieves massive scale but produces sparse or noisy text, while LLM prompting can densify and structure supervision. Building on the web-scale harvesting and filtering practices of WebVid/LAION and the CLIP contrastive training recipe, the logical next step was to replace weak metadata with LLM-authored, temporally aware text. InternVid synthesizes these insights by prompting LLMs at multiple temporal granularities to generate high-quality video descriptions, aligning the data with CLIP-style objectives and enabling ViCLIP to achieve strong zero-shot understanding and retrieval at unprecedented scale.

---

*Analysis generated on: 2026-01-06T12:31:58.537910*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
