# Prior Work Analysis Report

## Target Paper
**Title:** o8hWyJIgAV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper builds on a two-stage paradigm crystallized by VQ-VAE and VQ-VAE-2: compress images into discrete codes and then model them with an autoregressive generator. These works established the controllable axes of tokenization—codebook size, hierarchy, and compression rate—while already hinting at trade-offs between aggressive compression and reconstruction fidelity. VQGAN deepened this connection by showing that the tokenizer’s objective can be tailored for downstream generation quality, providing a clear precedent for designing tokenizers with the end generator in mind. DALL·E’s large-scale dVAE+Transformer pipeline then made the practical tension salient: choices that ease the transformer’s modeling burden (e.g., stronger compression) can harm pixel-wise reconstruction but improve overall generative utility.
Scaling-law analyses for autoregressive generative modeling supplied the methodological backbone to study these effects rigorously, linking performance to model size, data, and compute. Rate–distortion theory from learned image compression anchored the compression side of the analysis, while the perception–distortion trade-off offered a conceptual rationale for why “worse” reconstructions might be “better” for generation. Together, these threads directly motivate the paper’s core contribution: characterizing how compression interacts with generator capacity under compute constraints and proposing Causally Regularized Tokenization, which explicitly uses knowledge of the stage-2 autoregressive procedure to shape the tokenizer so that its codes are easier to model—even when that means accepting higher reconstruction distortion.

---
*Generated: 2026-01-07T00:21:32.248216*
