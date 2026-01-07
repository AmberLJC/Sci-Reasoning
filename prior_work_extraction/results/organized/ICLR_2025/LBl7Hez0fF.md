# Prior Work Analysis Report

## Target Paper

**Title:** Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering

**Conference:** ICLR 2025 (spotlight)

**Authors:** Sheng Liu, Haotian Ye, James Zou

**Keywords:** Large Vision-Language Models, Multimodal large language model, Hallucination

**Abstract:** 
> Hallucination poses a challenge to the deployment of large vision-language models (LVLMs) in applications. Unlike in large language models (LLMs), hallucination in LVLMs often arises from misalignments between visual inputs and textual outputs. This paper investigates the underlying mechanisms of hallucination, focusing on the unique structure of LVLMs that distinguishes them from LLMs. We identify that hallucinations often arise from the sensitivity of text decoders to vision inputs, a natural ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models** (2023)
- *Authors:* J. Li et al.
- *Direct Connection:* BLIP-2’s modular LVLM design with separately pre-trained image encoders and text decoders highlights the fragile cross-modal interface that VTI explicitly stabilizes via latent-space interventions.

**Visual Instruction Tuning** (2023)
- *Authors:* H. Liu et al.
- *Direct Connection:* LLaVA popularized LVLMs built from frozen vision encoders and LLM decoders, a configuration prone to image–text misalignment and sensitivity that VTI targets with inference-time steering.

**Object Hallucination in Image Captioning** (2018)
- *Authors:* A. Rohrbach et al.
- *Direct Connection:* This work introduced the CHAIR metric and showed that language priors drive visual hallucinations, directly motivating VTI’s emphasis on strengthening image-grounded signals during generation.

### 💡 Inspiration

**Plug and Play Language Models: A Simple Approach to Controlled Text Generation** (2020)
- *Authors:* S. Dathathri et al.
- *Direct Connection:* VTI adopts PPLM’s core idea of inference-time activation steering without additional training, but repurposes it to stabilize cross-modal representations in LVLMs to suppress hallucinations.

### 📊 Baseline

**Visual Contrastive Decoding for Reducing Hallucinations in LVLMs** (2024)
- *Authors:* X. Yue et al.
- *Direct Connection:* VCD serves as a primary training-free baseline that combats hallucinations by contrasting image-conditioned and language-only outputs, whereas VTI instead steers hidden representations to reinforce visual evidence.

### 🔗 Related Problem

**Decoding by Contrasting Layers Improves Factuality** (2023)
- *Authors:* Y. Chuang et al.
- *Direct Connection:* By showing that decoding-time manipulation using internal layer signals can improve factuality, DoLa motivates VTI’s use of model-internal representations (rather than external supervision) to reduce hallucinations at test time.

---

## Synthesis: How Prior Work Led to This Paper

Plug and Play Language Models demonstrated that one can steer generation by directly modifying hidden activations at inference, achieving controllable text without any fine-tuning. Decoding by Contrasting Layers then showed that internal layer signals can be exploited at decoding time to improve factuality, leveraging model-internal representations rather than external supervision. In multimodal modeling, BLIP-2 established the now-standard LVLM architecture that couples frozen vision encoders with large language model decoders through a learned bridge, foregrounding a fragile cross-modal interface. Visual Instruction Tuning (LLaVA) further popularized this modular recipe at scale, revealing both the practical utility and the misalignment-induced sensitivity of text decoders to visual inputs. Earlier, Object Hallucination in Image Captioning introduced the CHAIR metric and pinpointed language priors as a key driver of visual hallucinations, crystallizing the importance of amplifying image-grounded signals. Most recently, Visual Contrastive Decoding provided a strong, training-free baseline that mitigates hallucinations by subtracting language-only priors at the logit level to emphasize visual evidence. Together, these works revealed a consistent opportunity: training-free, decoding-time interventions can improve factuality, and LVLM hallucinations stem from a brittle cross-modal interface where language priors dominate visual signals. The natural next step is to move from output-level contrasts to representation-level control within the multimodal hidden states. By steering the latent space at test time, one can stabilize vision features precisely where the encoder–decoder interface is fragile, retaining the simplicity of no-training interventions while directly addressing the root cause of LVLM hallucinations.

---

*Analysis generated on: 2026-01-06T07:37:19.201126*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
