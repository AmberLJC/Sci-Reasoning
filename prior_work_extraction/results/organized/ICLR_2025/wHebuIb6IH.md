# Prior Work Analysis Report

## Target Paper

**Title:** VLMaterial: Procedural Material Generation with Large Vision-Language Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Beichen Li, Rundi Wu, Armando Solar-Lezama, Changxi Zheng, Liang Shi, Bernd Bickel, Wojciech Matusik

**Keywords:** generative model, procedural material, appearance modeling

**Abstract:** 
> Procedural materials, represented as functional node graphs, are ubiquitous in computer graphics for photorealistic material appearance design. They allow users to perform intuitive and precise editing to achieve desired visual appearances. However, creating a procedural material given an input image requires professional knowledge and significant effort. In this work, we leverage the ability to convert procedural materials into standard Python programs and fine-tune a large pre-trained vision-l...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Learning to Infer Graphics Programs from Hand-Drawn Images** (2018)
- *Authors:* Kevin Ellis et al.
- *Direct Connection:* Provided the core paradigm of inferring executable graphics programs from images within a domain-specific language, which VLMaterial extends to procedural material graphs using a VLM rather than symbolic search.

**LLaVA: Visual Instruction Tuning** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* Supplied the pre-trained vision-language modeling and instruction-tuning recipe that VLMaterial fine-tunes to map material images to Python programs implementing procedural graphs.

### 💡 Inspiration

**pix2code: Generating Code from a Graphical User Interface Screenshot** (2017)
- *Authors:* Tony Beltramelli
- *Direct Connection:* Established the image-to-program formulation that VLMaterial adopts, replacing GUI DSL code with executable procedural material programs predicted directly from input images.

### 🔍 Gap Identification

**Single-Image SVBRDF Capture with a Rendering-Aware CNN** (2018)
- *Authors:* Victor Deschaintre et al.
- *Direct Connection:* Highlighted that single-image material reconstruction typically yields non-programmatic SVBRDFs with limited editability, motivating VLMaterial’s shift to procedural programs that are inherently editable.

### 🔧 Extension

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* Directly informs VLMaterial’s program-level augmentation strategy by prompting another LLM to synthesize diverse training programs and prompts to enable effective fine-tuning.

### 🔗 Related Problem

**ShapeAssembly: Learning to Generate Programs for 3D Shape Structure** (2020)
- *Authors:* Daniel Ritchie et al.
- *Direct Connection:* Demonstrated that representing structured visual content as interpretable, editable programs is practical and desirable, directly motivating VLMaterial’s choice of programmatic procedural materials for editability.

**DiffVG: Differentiable Vector Graphics Rasterization** (2020)
- *Authors:* Wenzheng Li et al.
- *Direct Connection:* Showed how programmatic graphics representations can be rendered and compared to images, underpinning VLMaterial’s render-and-validate paradigm for program outputs even without explicit differentiability.

---

## Synthesis: How Prior Work Led to This Paper

Early image-to-program research established that visual inputs can be translated into executable code: pix2code framed the task by mapping GUI screenshots to DSL code, and Learning to Infer Graphics Programs showed that images could specify graphics programs within a domain-specific language. In parallel, ShapeAssembly demonstrated the advantages of representing complex visual structure as interpretable, editable programs, cementing editability as a core benefit of programmatic representations. On the modeling side, LLaVA introduced visual instruction tuning, revealing that pre-trained VLMs can be adapted to follow image-conditioned instructions and output structured text like code. Self-Instruct then showed that instruction-following models can be effectively improved via synthetic, LLM-generated training data, a recipe well-suited to expanding program datasets. Complementing these, DiffVG connected programmatic graphics to raster supervision by rendering and comparing program outputs to images, while single-image SVBRDF methods like Deschaintre et al. illustrated that non-programmatic reconstructions limit downstream editing.

Together these works exposed an opportunity: leverage a pre-trained VLM’s image-conditioned code generation, boost it with LLM-synthesized program data, and target a representation that preserves editability. VLMaterial naturally synthesizes these ideas by converting procedural material graphs into executable Python programs, fine-tuning a VLM to generate them from images, and validating via rendering—addressing the editability gap in prior material reconstruction methods.

---

*Analysis generated on: 2026-01-06T12:48:06.305884*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
