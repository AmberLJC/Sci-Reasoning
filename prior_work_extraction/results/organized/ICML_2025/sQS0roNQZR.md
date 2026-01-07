# Prior Work Analysis Report

## Target Paper
**Title:** sQS0roNQZR
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—turning token-level language models into character-level distributions via exact and approximate algorithms—synthesizes two mature lines of research: subword tokenization and weighted finite-state methods for marginalization. BPE (Sennrich et al., 2016) and SentencePiece (Kudo & Richardson, 2018) establish deterministic mappings from characters to tokens that are many-to-one, creating segmentation ambiguity at the character level. Subword Regularization (Kudo, 2018) crystallizes the idea that correct string likelihoods require summing over all tokenizations consistent with a given character sequence, directly motivating the paper’s summation over latent segmentations.

On the algorithmic side, Mohri–Pereira–Riley (2002) provide the formal WFST framework for composing a language model with a lexicon/transducer and performing forward-style marginalization over all paths. This perspective naturally treats the tokenizer/detokenizer as a transducer from token sequences to characters, allowing a pushforward of the token-level distribution onto character strings. Practical advances from OpenFst (Allauzen et al., 2007) and Pynini (Gorman, 2021) inform efficient, on-the-fly composition and pruning strategies crucial for scaling exact computation and for devising fast approximations.

Finally, the dynamic-programming template of CTC (Graves et al., 2006)—summing probabilities over exponentially many latent alignments—offers a closely related computational pattern for aggregating token-level paths into character-level probabilities. Together, these works yield both the theoretical underpinning (composition and marginalization over segmentations) and the practical blueprint (deterministic transducers, on-the-fly composition, and pruning) for the paper’s exact and approximate algorithms.

---
*Generated: 2026-01-07T00:04:09.138581*
