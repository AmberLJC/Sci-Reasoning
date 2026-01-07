# Prior Work Analysis Report

## Target Paper

**Title:** DEEM: Diffusion models serve as the eyes of large language models for image perception

**Conference:** ICLR 2025 (spotlight)

**Authors:** Run Luo, Yunshui Li, Longze Chen, Wanwei He, Ting-En Lin, Ziqiang Liu, Lei Zhang, Zikai Song, Hamid Alinejad-Rokny, Xiaobo Xia, Tongliang Liu, Binyuan Hui, Min Yang

**Keywords:** MLLM; Diffusion Model;

**Abstract:** 
> The development of large language models (LLMs) has significantly advanced the emergence of large multimodal models (LMMs). While LMMs have achieved tremendous success by promoting the synergy between multimodal comprehension and creation, they often face challenges when confronted with out-of-distribution data, such as which can hardly distinguish orientation, quantity, color, structure, etc. This is primarily due to their reliance on image encoders trained to encode images into task-relevant f...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**High-Resolution Image Synthesis with Latent Diffusion Models** (2022)
- *Authors:* Robin Rombach et al.
- *Direct Connection:* DEEM relies on the semantic cross-attention and denoising score properties of latent diffusion (e.g., Stable Diffusion) to extract token-level generative signals that supervise the vision encoder.

**BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models** (2023)
- *Authors:* Junnan Li et al.
- *Direct Connection:* BLIP-2 established the frozen-encoder + lightweight bridge paradigm that DEEM targets, replacing purely discriminative alignment of the encoder with generative feedback-based semantic distribution alignment.

### 💡 Inspiration

**Prompt-to-Prompt Image Editing with Cross-Attention Control** (2022)
- *Authors:* Amir Hertz et al.
- *Direct Connection:* By showing that diffusion cross-attention maps are token-aligned and controllable, Prompt-to-Prompt provides the concrete mechanism that DEEM leverages to harvest semantically grounded generative signals for supervising the image encoder.

### 🔍 Gap Identification

**MME: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models** (2023)
- *Authors:* Yiyang Fu et al.
- *Direct Connection:* MME documents systematic deficiencies of LMMs in fine-grained perception (e.g., color, quantity, orientation), directly motivating DEEM’s use of diffusion-based feedback to fix these OOD perception failures.

### 📊 Baseline

**LLaVA: Visual Instruction Tuning** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* As a representative LMM built on a frozen image encoder plus instruction-tuned adaptor, LLaVA serves as a main baseline that DEEM augments by adding diffusion-driven perceptual alignment to remedy failures in color, counting, and spatial orientation.

**InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning** (2023)
- *Authors:* Wenliang Dai et al.
- *Direct Connection:* InstructBLIP demonstrates instruction-tuned improvements while inheriting the same vision-encoder bottleneck, making it a key baseline that DEEM improves by injecting diffusion-based perceptual supervision rather than relying solely on text-instruction data.

### 🔧 Extension

**DreamFusion: Text-to-3D using 2D Diffusion** (2022)
- *Authors:* Ben Poole et al.
- *Direct Connection:* DEEM extends DreamFusion’s score distillation idea by using gradients from a frozen text-to-image diffusion model as generative feedback to directly align an image encoder’s semantic distribution, rather than optimizing a 3D scene or latent.

---

## Synthesis: How Prior Work Led to This Paper

Frozen-encoder multimodal pipelines established by BLIP-2 showed that lightweight bridges can connect powerful vision encoders to LLMs, but their discriminative training favors task-targeted features and often overlooks fine-grained attributes. LLaVA scaled this recipe with visual instruction tuning, demonstrating strong conversational abilities but continuing to inherit perceptual brittleness from the underlying encoder. InstructBLIP reinforced that instruction data alone cannot fully correct misperceptions such as incorrect counting, color, or orientation. In parallel, latent diffusion models revealed rich token-level semantics via cross-attention and denoising scores, providing a generative prior that is both expressive and broadly trained. Prompt-to-Prompt exposed that these cross-attention maps are controllable and aligned to textual tokens, giving a practical handle to extract and manipulate semantic signals. DreamFusion then crystallized a general recipe—score distillation—for using a frozen text-to-image diffusion model to supervise an external representation by backpropagating generative signals. Benchmarks like MME documented where LMMs actually fail: detailed perception of color, quantity, orientation, and structure under distribution shifts. Taken together, these works reveal both the limitation of discriminative-only encoder alignment and the availability of a strong, token-aligned generative teacher. The natural next step is to treat diffusion models as perceptual oracles and distill their semantic distributions into the image encoder of an LMM. By importing score/cross-attention feedback from latent diffusion into the encoder’s training objective, one can directly correct the precise perceptual errors flagged by benchmarks while remaining compatible with standard LMM architectures and instruction tuning.

---

*Analysis generated on: 2026-01-06T19:00:07.664737*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
