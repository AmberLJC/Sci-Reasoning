# Prior Work Analysis Report

## Target Paper
**Title:** WaLI8slhLw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DeWave’s key contribution—translating EEG into open-vocabulary text without eye-fixation/event markers—emerges from uniting discrete latent modeling with language-model-based decoding paradigms. The discrete side is grounded in VQ-VAE, which introduced learning codebooks to convert continuous signals into symbolic units, and vq-wav2vec, which showed how to obtain such units from audio. Textless NLP extended this by demonstrating that strong language models can operate directly over learned discrete units, enabling natural language generation without supervised transcripts. wav2vec-U further crystallized the recipe for segmentation-free mapping from discrete units to text by pairing unit discovery with a language model, offering a template DeWave adapts from speech to EEG. Conceptually, CTC provided the foundational principle for learning from unsegmented sequences, reinforcing DeWave’s removal of word-level alignment requirements. In parallel, recent brain-to-text advances from fMRI decoding used pretrained language models as powerful priors to reconstruct continuous language, validating the strategy of leveraging PLMs for brain signal interpretation. Finally, EEG-and-eye-tracking reading work such as ZuCo established a prevailing reliance on fixation/event markers for word-level alignment; DeWave’s discrete “codex” and LM alignment specifically target eliminating that constraint. Together, these lines of work directly shape DeWave’s design: learn discrete EEG units, align them with a pretrained LM, and perform open-vocabulary EEG-to-text translation without external segmentation.

---
*Generated: 2026-01-07T00:02:04.869385*
