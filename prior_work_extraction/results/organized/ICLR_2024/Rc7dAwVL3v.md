# Prior Work Analysis Report

## Target Paper

**Title:** NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers

**Conference:** ICLR 2024 (spotlight)

**Authors:** Kai Shen, Zeqian Ju, Xu Tan, Eric Liu, Yichong Leng, Lei He, Tao Qin, sheng zhao, Jiang Bian

**Keywords:** text-to-speech, large-scale corpus, non-autoregressive, diffusion

**Abstract:** 
> Scaling text-to-speech (TTS) to large-scale, multi-speaker, and in-the-wild datasets is important to capture the diversity in human speech such as speaker identities, prosodies, and styles (e.g., singing). Current large TTS systems usually quantize speech into discrete tokens and use language models to generate these tokens one by one, which suffer from unstable prosody, word skipping/repeating issue, and poor voice quality. In this paper, we develop NaturalSpeech 2, a TTS system that leverages ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**SoundStream: An End-to-End Neural Audio Codec** (2021)
- *Authors:* Neil Zeghidour et al.
- *Direct Connection:* NaturalSpeech 2 builds on SoundStream’s residual vector quantization audio codec formulation by using RVQ-quantized latent codes as the target space for its diffusion generator.

### 💡 Inspiration

**High-Resolution Image Synthesis with Latent Diffusion Models** (2022)
- *Authors:* Robin Rombach et al.
- *Direct Connection:* NaturalSpeech 2 adopts the key insight of performing diffusion in a learned latent space (rather than raw signals) to enable efficient, high-quality generation—here applied to neural audio codec latents for TTS.

**Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale** (2023)
- *Authors:* Louis Martin (Le) et al.
- *Direct Connection:* NaturalSpeech 2 draws from Voicebox’s non-autoregressive generation of neural codec latents and speech-prompt conditioning, but uses diffusion (rather than flow matching) and explicit prompt-aware predictors to stabilize content and prosody.

### 📊 Baseline

**Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers** (2023)
- *Authors:* Chengyi Wang et al.
- *Direct Connection:* NaturalSpeech 2 directly targets the instability and prosody/word-skipping issues of VALL-E’s autoregressive neural codec LM by replacing token-by-token generation with latent diffusion over codec representations while retaining the zero-shot speech prompting setup.

### 🔧 Extension

**Grad-TTS: A Diffusion Probabilistic Model for Text-to-Speech** (2021)
- *Authors:* Vladislav Popov et al.
- *Direct Connection:* NaturalSpeech 2 extends diffusion-based TTS from mel-spectrogram domains in Grad-TTS to neural codec latent space and augments conditioning with speech prompts for zero-shot style transfer.

**FastSpeech 2: Fast and High-Quality End-to-End Text to Speech** (2021)
- *Authors:* Yi Ren et al.
- *Direct Connection:* NaturalSpeech 2 modifies FastSpeech 2’s duration and pitch predictors by conditioning them on speech prompts to enable in-context learning of speaking rate and F0 patterns for zero-shot synthesis.

### 🔗 Related Problem

**AudioLM: a Language Modeling Approach to Audio Generation** (2022)
- *Authors:* Tomasz Borsos et al.
- *Direct Connection:* NaturalSpeech 2 leverages AudioLM’s insight that a short acoustic prompt can capture speaker identity and style for in-context continuation, adapting this idea to conditioned TTS via codec-latent diffusion.

---

## Synthesis: How Prior Work Led to This Paper

Neural codec work established that high-quality speech could be compressed into residual vector-quantized latents suitable for generative modeling; SoundStream in particular introduced RVQ audio codes that preserve speaker identity and prosody at low bitrates. Latent diffusion further showed that running diffusion in a learned latent space drastically improves efficiency and fidelity compared with operating in raw signal domains, while Grad-TTS demonstrated the viability of diffusion-based text-conditioned speech generation, albeit over mel-spectrograms. Language-modeling approaches to audio revealed the power of in-context acoustic prompting: AudioLM used a short reference segment to preserve voice and style during continuation, and VALL-E brought this prompting paradigm to TTS by autoregressively generating codec tokens, exposing practical issues such as instability, word skipping, and prosody drift. Voicebox advanced non-autoregressive generation over codec latents with speech prompts, indicating that continuous-time generative training can improve robustness at scale. FastSpeech 2 contributed the practical framework of explicit duration and pitch predictors, enabling controllable, non-autoregressive alignment and F0 modeling. Together, these works suggested a path: use RVQ codec latents as a compact target, preserve zero-shot style via speech prompts, replace unstable autoregression with latent diffusion, and marry this with explicit duration/pitch control. NaturalSpeech 2 synthesizes these insights by performing diffusion in codec latent space with prompt-aware conditioning and prompt-conditioned duration/F0 predictors, achieving stable, high-quality zero-shot speech and singing at scale.

---

*Analysis generated on: 2026-01-06T12:47:11.536052*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
