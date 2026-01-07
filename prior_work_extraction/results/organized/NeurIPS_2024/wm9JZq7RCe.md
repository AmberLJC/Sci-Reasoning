# Prior Work Analysis Report

## Target Paper
**Title:** wm9JZq7RCe
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—explaining when and why tokenization enables transformers to learn higher-order dependencies in k-th order Markov sources—rests on two converging lines of prior work. First, foundational tokenization research (Sennrich et al., 2016; Kudo, 2018; Radford et al., 2019; Bostrom & Durrett, 2020) established that segmenting text into subwords is not merely an engineering detail but a statistical tool: subword schemes like BPE and Unigram LM compress frequent n-grams into single tokens, reducing sequence length and aligning model inputs with recurring motifs. Empirical evidence that tokenizer choice affects cross-entropy (Bostrom & Durrett) and the widespread adoption of byte-level BPE (Radford et al.) underscore tokenization’s impact on learnability.
Second, tokenization-free modeling efforts (Clark et al., 2022; Xue et al., 2022) challenged the necessity of subwords by demonstrating byte- and character-level LMs that can work at scale. However, Makkuva et al. (2024) documented a crucial failure mode: without tokenization, transformers trained on higher-order Markov data can default to unigram predictions, learning extremely slowly or not at all. The present paper synthesizes these threads by showing that appropriate tokenization breaks this barrier, enabling near-optimal modeling of Markov sources. It thereby provides a principled explanation for when tokenization is indispensable: when the data-generating process relies on higher-order local dependencies that subword segmentation can expose as atomic units for efficient transformer learning.

---
*Generated: 2026-01-06T23:33:35.523482*
