# Prior Work Analysis Report

## Target Paper

**Title:** Image2Sentence based Asymmetrical Zero-shot Composed Image Retrieval

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yongchao Du, Min Wang, Wengang Zhou, Shuping Hui, Houqiang Li

**Keywords:** zero-shot, composed image retrieval, asymmetrical

**Abstract:** 
> The task of composed image retrieval (CIR) aims to retrieve images based on the query image and the text describing the users' intent. 
Existing methods have made great progress with the advanced large vision-language (VL) model in CIR task, however, they generally suffer from two main issues: lack of labeled triplets for model training and difficulty of deployment on resource-restricted environments when deploying the large vision-language model. To tackle the above problems, we propose Image2S...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Learning Transferable Visual Models From Natural Language Supervision** (2021)
- *Authors:* Alec Radford et al.
- *Direct Connection:* ISA explicitly leverages CLIP’s text encoder and word embedding space, mapping images to sentence tokens within this space to perform composition and retrieval without labeled triplets.

**CIRR: Composed Image Retrieval on Real-life Images** (2021)
- *Authors:* Xin Eric Wang et al.
- *Direct Connection:* CIRR formalizes real-world relative-caption CIR evaluation and highlights the scarcity of labeled triplets, a key limitation that ISA tackles through zero-shot composition learning from unlabeled images.

**FashionIQ: A New Dataset Toward Retrieving Images by Natural Language Feedback** (2021)
- *Authors:* Yuming Gu et al.
- *Direct Connection:* FashionIQ’s natural-language feedback setup defined practical CIR benchmarks and exposed annotation bottlenecks, motivating ISA’s unlabeled, CLIP-text-space composition and asymmetric deployment design.

### 💡 Inspiration

**Conditional Prompt Learning for Vision-Language Models** (2022)
- *Authors:* Kaiyang Zhou et al.
- *Direct Connection:* ISA generalizes CoCoOp’s image-conditioned textual prompts by producing an image-derived sentence (a sequence of tokens) that is fused with the user’s text modifier in the VL text space.

**An Image Is Worth One Word: Textual Inversion for Personalization of Text-to-Image Models** (2022)
- *Authors:* Rinon Gal et al.
- *Direct Connection:* ISA borrows the core idea of representing visual concepts as learnable tokens in a text embedding space and extends it from single pseudo-words to adaptive multi-token sentences for retrieval composition.

**TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?** (2021)
- *Authors:* Sanghyun Woo et al.
- *Direct Connection:* ISA’s adaptive token learner echoes TokenLearner’s principle of selecting a compact, informative set of tokens from an image, but projects them into a VL text embedding space to act as a sentence.

### 📊 Baseline

**Composing Text and Image for Image Retrieval** (2019)
- *Authors:* Nam Vo et al.
- *Direct Connection:* ISA adopts the CIR formulation introduced by TIRG—modifying an image representation with a text modifier—and directly addresses TIRG’s reliance on labeled triplets by learning the composition in a zero-shot manner via an image-to-sentence mapping in a VL text space.

---

## Synthesis: How Prior Work Led to This Paper

Composed image retrieval was crystallized by prior work that modified an image’s representation using a text modifier to form a query, with TIRG establishing the now-standard composition mechanism. CLIP provided a powerful shared image–text space and, crucially, a text encoder with a word embedding space that can be directly operated on without paired supervision. CoCoOp introduced image-conditioned prompt learning inside CLIP’s text encoder, showing that image features can produce effective textual tokens for downstream transfer. Textual Inversion demonstrated that visual concepts can be represented as learnable tokens within a text embedding space, suggesting a path to encode visual content as text-like units. TokenLearner revealed that a small set of adaptively selected tokens can capture discriminative visual information, motivating compact tokenized representations. Datasets such as CIRR and FashionIQ framed CIR evaluation with relative captions and highlighted the scarcity and cost of labeled triplets, a practical limitation that persisted across methods.
Together, these works revealed an opportunity: use CLIP’s text embedding space as the locus of composition, generate image-conditioned textual tokens to avoid dependency on labeled triplets, and keep gallery encoders lightweight via asymmetric design. The current paper synthesizes these insights by mapping an image into an adaptive, multi-token “sentence” within CLIP’s word embedding space and integrating it with the user’s text modifier, achieving zero-shot composition while retaining an index-friendly, asymmetric retrieval pipeline.

---

*Analysis generated on: 2026-01-06T17:46:46.735273*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
