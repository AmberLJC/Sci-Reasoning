# Prior Work Analysis Report

## Target Paper

**Title:** Ferret: Refer and Ground Anything Anywhere at Any Granularity

**Conference:** ICLR 2024 (spotlight)

**Authors:** Haoxuan You, Haotian Zhang, Zhe Gan, Xianzhi Du, Bowen Zhang, Zirui Wang, Liangliang Cao, Shih-Fu Chang, Yinfei Yang

**Keywords:** Ferret, Multimodal Large Language Model, Referring, Grounding

**Abstract:** 
> We introduce Ferret, a new Multimodal Large Language Model (MLLM) capable of understanding spatial referring of any shape or granularity within an image and accurately grounding open-vocabulary descriptions. To unify referring and grounding in the LLM paradigm, Ferret employs a novel and powerful hybrid region representation that integrates discrete coordinates and continuous features jointly to represent a region in the image. To extract the continuous features of versatile regions,  we propose...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection** (2023)
- *Authors:* Shilong Liu et al.
- *Direct Connection:* Ferret builds on Grounding DINO’s open-vocabulary grounding formulation and uses it to mine region–text pairs and hard negatives for GRIT, integrating grounding into the MLLM setting.

**Generation and Comprehension of Unambiguous Object Descriptions** (2016)
- *Authors:* Junhua Mao et al.
- *Direct Connection:* Ferret inherits the referring-expression task setup from RefCOCOg and extends it beyond box-based comprehension to arbitrary-granularity regions via its hybrid region representation.

### 💡 Inspiration

**Segment Anything** (2023)
- *Authors:* Alexander Kirillov et al.
- *Direct Connection:* Ferret adopts SAM’s promptable region notion (points, boxes, masks) to accept free-form shapes and leverages this paradigm in its spatial-aware sampler and GRIT data construction.

### 🔍 Gap Identification

**Shikra: Unleashing Multimodal LLMs’ Referential Dialogue Skills** (2023)
- *Authors:* B. Chen et al.
- *Direct Connection:* Ferret explicitly augments Shikra’s coordinate-token interface for region referring by adding continuous region features, overcoming Shikra’s box/point-only and purely discrete representation limits.

### 📊 Baseline

**KOSMOS-2: Grounding Multimodal Large Language Models to the World** (2023)
- *Authors:* X. Wang et al.
- *Direct Connection:* Ferret targets Kosmos-2’s coordinate-only phrase grounding with boxes by unifying referring and grounding through a hybrid region token that supports arbitrary shapes and finer granularity.

**Visual Instruction Tuning (LLaVA): Large Language-and-Vision Assistant** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* Ferret follows LLaVA’s multimodal instruction-tuning framework but replaces image-only inputs with a hybrid region representation to enable precise refer-and-ground capabilities.

### 🔧 Extension

**GPT4RoI: Instruction Tuning Large Language Models on Region-of-Interest** (2023)
- *Authors:* H. Li et al.
- *Direct Connection:* Ferret generalizes GPT4RoI’s idea of extracting continuous visual features from specified boxes by introducing a spatial-aware sampler that pools features for regions of any shape and sparsity and pairing them with discrete coordinates.

---

## Synthesis: How Prior Work Led to This Paper

Shikra introduced a simple but influential interface for multimodal LLMs to refer to regions using discrete coordinate tokens, enabling box/point-level referencing while revealing the brittleness of purely discrete spatial tokens for fine-grained shapes. KOSMOS-2 similarly grounded phrases to bounding boxes via coordinate serialization, establishing a coordinate-only grounding paradigm and strong baseline performance on box-level grounding tasks. GPT4RoI moved beyond coordinates by pooling continuous visual features from specified boxes (via RoI operations), demonstrating that coupling language with localized features improves region-aware instruction following while still being limited to rectangular RoIs. Segment Anything popularized promptable region interaction—points, boxes, and free-form masks—showing that diverse region prompts can capture arbitrary shapes and granularity. Grounding DINO provided an open-vocabulary grounding framework that aligns text with spatial regions and offered a practical route to mine large-scale region–text pairs and hard negatives. RefCOCOg formalized the referring-expression problem with natural language descriptions and region targets, seeding benchmarks and data conventions widely used for refer/ground tasks. LLaVA established the multimodal instruction-tuning pipeline that many subsequent MLLMs adopt for aligning vision encoders with LLMs. Together, these works exposed a clear opportunity: coordinate-only MLLMs lacked fine-grained spatial fidelity, and RoI-only methods were constrained to boxes, while instruction-tuned MLLMs lacked a unified region interface and data at scale. Ferret synthesizes these insights by combining discrete coordinates with continuous region features in a single hybrid region token and introducing a spatial-aware sampler to handle arbitrary shapes; leveraging SAM and Grounding DINO, it curates GRIT with hierarchical spatial knowledge and hard negatives, integrating precise refer-and-ground skills into the LLM paradigm.

---

*Analysis generated on: 2026-01-06T19:37:51.178415*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
