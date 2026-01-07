# Prior Work Analysis Report

## Target Paper

**Title:** Sentence-level Prompts Benefit Composed Image Retrieval

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yang bai, Xinxing Xu, Yong Liu, Salman Khan, Fahad Khan, Wangmeng Zuo, Rick Siow Mong Goh, Chun-Mei Feng

**Keywords:** Composed Image Retrieval, Vision-Language Pre-trained Models

**Abstract:** 
> Composed image retrieval (CIR) is the task of retrieving specific images by using a query that involves both a reference image and a relative caption. Most existing CIR models adopt the late-fusion strategy to combine visual and language features. Besides, several approaches have also been suggested to generate a pseudo-word token from the reference image, which is further integrated into the relative caption for CIR. However, these pseudo-word-based prompting methods have limitations when targe...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**CIRR: A Dataset for Composed Image Retrieval in the Wild** (2021)
- *Authors:* Yong Liu et al.
- *Direct Connection:* CIRR formalized real-world CIR evaluation emphasizing complex semantic changes, providing the benchmark setting and motivating focus on cases where pseudo-word prompts underperform.

### 💡 Inspiration

**Learning to Prompt for Vision-Language Models** (2022)
- *Authors:* Kaiyang Zhou et al.
- *Direct Connection:* CoOp’s learnable textual context for CLIP inspires treating the prompt as the primary trainable component, which the current work adapts by learning a sentence-level prompt concatenated to the relative caption for CIR.

**P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks** (2022)
- *Authors:* Xiao Liu et al.
- *Direct Connection:* P-Tuning v2 demonstrates that soft prompt optimization can substitute full model fine-tuning, motivating the design where the sentence-level prompt is the main trainable component while keeping the V-L backbone largely frozen.

### 🔍 Gap Identification

**Textual Inversion: Generating Images with Pseudo Words** (2022)
- *Authors:* Rinon Gal et al.
- *Direct Connection:* The idea of learning a pseudo-word token to represent visual concepts inspired pseudo-word-based CIR prompting, whose limitations on complex edits (e.g., object removal/attribute changes) are explicitly addressed by replacing the token with a sentence-level prompt.

### 📊 Baseline

**Composing Text and Image for Image Retrieval (TIRG)** (2019)
- *Authors:* Nam Vo et al.
- *Direct Connection:* TIRG established late-fusion composition of image and text features for CIR, serving as the primary late-fusion paradigm that the new method departs from by moving composition into the language side via sentence-level prompting.

### 🔧 Extension

**BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models** (2023)
- *Authors:* Junnan Li et al.
- *Direct Connection:* The paper leverages BLIP-2’s frozen VLM architecture to condition and generate sentence-level prompts from the reference image, directly enabling the proposed sentence-level prompt for composed image retrieval.

---

## Synthesis: How Prior Work Led to This Paper

BLIP-2 introduces a frozen vision-language pipeline that conditions powerful language heads on visual inputs, enabling sentence-level conditioning and generation tied to images without end-to-end fine-tuning. CoOp shows that learnable textual prompts for CLIP can be the main locus of adaptation, with prompts learned as continuous vectors prepended to class names, effectively steering vision-language models through the text channel. P-Tuning v2 generalizes soft prompt optimization, demonstrating that task performance can be recovered by training only prompts while keeping the backbone frozen, establishing a practical recipe for parameter-efficient adaptation. Textual Inversion presents pseudo-word tokens that encapsulate visual concepts, catalyzing follow-on uses of learned tokens injected into text, but also revealing brittleness when representing complex, compositional edits. TIRG crystallizes the late-fusion paradigm for CIR, combining image features with language via residual gating, shaping baselines that fuse modalities post-encoding. CIRR provides a challenging, real-world benchmark where fine-grained object and attribute changes are central, exposing failure modes of simplistic token-based prompting and late fusion.
Collectively, these works indicate that composition can be shifted from late-fusion feature mixing to prompt-driven language conditioning, with soft prompts serving as efficient task adapters and BLIP-2 providing image-conditioned sentence scaffolds. The limitations of pseudo-word tokens on complex edits, highlighted by Textual Inversion’s conceptual scope and CIRR’s evaluation, foreground the need for richer, sentence-level prompts. Synthesizing these insights, the current work learns image-conditioned sentence prompts concatenated to relative captions, retaining frozen V-L backbones while overcoming late-fusion and pseudo-token shortcomings on compositional changes.

---

*Analysis generated on: 2026-01-06T19:27:19.159376*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
