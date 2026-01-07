# Prior Work Analysis Report

## Target Paper
**Title:** efOq8wHH9o
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

MaxSup’s core contribution—analytically decomposing label smoothing (LS) to reveal a misclassification-driven error-amplification term and proposing a targeted top-1 logit penalty—builds on a lineage of work that established, scrutinized, and sought to fix overconfidence and representation collapse. Szegedy et al. introduced LS as a practical regularizer, implicitly blending cross-entropy with a uniform target; MaxSup formalizes this blend and exposes its asymmetric behavior: it regularizes only when predictions are correct but can amplify errors when predictions are wrong. Pereyra et al.’s confidence penalty framed regularization as discouraging excessively peaked posteriors, a conceptual foundation that MaxSup sharpens by suppressing only the maximum logit, thereby applying uniform pressure regardless of correctness and avoiding LS’s error amplification. The calibration perspective of Guo et al. underscores the centrality of overconfidence; MaxSup aims to retain calibration gains without entrenching incorrect beliefs. Müller et al. analyzed when and how LS helps, noting shifts in representation and optimization behavior; their insights motivate MaxSup’s analytical decomposition and redesign of the regularizer. Papyan et al.’s neural collapse theory provides a principled lens on representation compactification; MaxSup explicitly targets LS-induced collapse by preventing excessive dominance of a single logit. Finally, supervised contrastive learning demonstrates that preserving intra-class diversity can enhance generalization; MaxSup positions itself as a lightweight, CE-compatible alternative that preserves diversity by constraining the top-1 logit rather than flattening the entire distribution.

---
*Generated: 2026-01-06T23:42:48.146718*
