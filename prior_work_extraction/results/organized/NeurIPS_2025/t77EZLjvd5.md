# Prior Work Analysis Report

## Target Paper
**Title:** t77EZLjvd5
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

COLA targets a concrete failure mode of CLIP—adversarially amplified misalignment between image and text embeddings—by explicitly repairing cross-modality geometry rather than only tuning prompts or adversarially retraining. The foundation is CLIP’s contrastive image–text space and its zero-shot classifier, where class text embeddings function as linear classifier weights; this motivates COLA’s projection of adversarial image features onto the subspace spanned by text embeddings to filter non-semantic perturbations while preserving discriminative semantics. Prior prompt-learning work such as CoOp exemplifies adaptation strategies that operate at the input/prompt level; COLA reframes robustness as a representation alignment problem, directly addressing the gap in the joint embedding space that prompts alone cannot fix. Instead of relying solely on PGD-style adversarial training (Madry et al.), COLA employs optimal transport to restore global alignment between adversarial image features and class texts. This design is technically grounded in the OT literature: Cuturi’s entropic Sinkhorn algorithm enables efficient, differentiable transport plans, while JDOT formalizes alignment of joint feature–label distributions—paralleling COLA’s matching of adversarial image distributions to label-conditioned text prototypes. Finally, to prevent collapsing or distorted neighborhoods, COLA incorporates a local structural consistency objective inspired by supervised contrastive learning, preserving intra-class neighborhoods and inter-class margins under attack. Together, these strands—CLIP’s text-defined classifier geometry, OT-based global distribution matching, and contrastive local structure preservation—cohere into COLA’s robust cross-modality alignment framework.

---
*Generated: 2026-01-07T00:21:32.290354*
