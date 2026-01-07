# Prior Work Analysis Report

## Target Paper
**Title:** Qvvy0X63Fv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core insight—that a simple affine mapping between residual streams lets us transfer linear features across language models—emerges from two converging lines of work. First, representation alignment and model stitching demonstrated that independently trained networks can be rendered functionally compatible via learned linear adapters. Lenc and Vedaldi introduced equivalence via linear transforms between intermediate features, while Kornblith et al.’s CKA provided strong evidence that such representations are similar up to linear mappings across architectures. Git Re-Basin further showed that symmetry-aware linear/permutation alignments can reconcile independently trained models, reinforcing the feasibility of inexpensive cross-model compatibility mappings. A parallel thread in NLP demonstrated the practical power of linear alignment in embedding spaces: Mikolov et al. used orthogonal Procrustes to map word vectors across languages, a methodological template this paper adapts to transformer residual spaces. The second key strand is mechanistic interpretability with linear features. Toy Models of Superposition argues features are linearly superposed, motivating sparse decoders; Anthropic’s SAEs operationalized this by learning monosemantic dictionaries in residual streams. Building on these, the present work shows SAE dictionaries, linear probes, and steering vectors (as in Representation Engineering) can be transferred across model scales using an affine adapter, preserving performance while enabling substantial FLOPs savings. Together, these prior works directly inform both the assumption of linear alignability and the practical choice of feature objects (SAEs, probes, steering vectors) that benefit from cross-model transfer.

---
*Generated: 2026-01-07T00:02:04.933287*
