# Prior Work Analysis Report

## Target Paper
**Title:** 9hd5WA6QCn
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MODA’s core innovation—modular duplex attention with a correct-after-align strategy—builds on a decade of converging ideas in multimodal transformers. Early two-stream VL models such as ViLBERT and LXMERT showed the value of separating intra-modal processing from cross-modal exchange via co-attention or dedicated cross-modality encoders, but incurred sequential, sometimes unstable, fusion across deep stacks. ALBEF reframed the pipeline with an align-before-fuse paradigm, demonstrating that explicit pre-alignment improves downstream fusion. Subsequent MLLM connectors, notably BLIP-2’s Q-Former and Flamingo’s gated cross-attention with a Perceiver-style resampler, further decoupled alignment and fusion to protect language modeling while injecting visual context, mitigating attention dilution in deep models.

MODA integrates and advances these strands by making the separation structural and simultaneous: an attention block that performs inner-modal refinement and inter-modal interaction in parallel, preceded by an explicit alignment that maps tokens into duplex modality subspaces defined by learned bases. This design tackles two practical failure modes—cross-modal attention inconsistency and layer-wise attention decay—by confining and coordinating token mixing across layers and applying correction after alignment. Insights from sentiment/emotion-focused architectures like MulT and MISA, which emphasize directional cross-modal flows and the factorization of modality-specific versus invariant components, inform MODA’s emphasis on fine-grained cognition and affective understanding. Together, these prior works directly motivate MODA’s unified, modular attention that decouples alignment from mixing and stabilizes cross-modal reasoning across depth.

---
*Generated: 2026-01-07T00:21:33.194632*
