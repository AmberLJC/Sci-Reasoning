# Prior Work Analysis Report

## Target Paper
**Title:** uvTea5Rfek
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CANDY’s core contribution—learning a shared, low-dimensional dynamical space that aligns heterogeneous neural recordings across sessions and subjects using a rank-based contrastive objective tied to continuous behavior—sits at the intersection of three lines of prior work. First, population neuroscience established that neural activity lies on low-dimensional manifolds whose dynamics remain stable across days (Gallego et al., 2020). Practical alignment methods then demonstrated that decoders can be stabilized by mapping different sessions into a common manifold (Degenhart et al., 2020), and cross-subject models in fMRI formalized per-subject linear mappings into a shared representational space (SRM; Chen et al., 2015). CANDY inherits and unifies these alignment ideas by learning session-specific encoders into a single latent space.
Second, aligning neural and behavioral signals with continuous targets draws on multi-view learning: DCCA (Andrew et al., 2013) provided a correlation-based objective for continuous cross-modal alignment, while modern contrastive learning (van den Oord et al., 2018) offered scalable, negative-sampling formulations. CANDY directly adapts these advances by introducing a rank-based contrastive loss that preserves behavioral ordering and continuity, avoiding discretization.
Third, latent dynamical systems models—ranging from GPFA (Yu et al., 2009) to LFADS (Pandarinath et al., 2018)—showed the value of end-to-end inference of neural trajectories with temporal priors. CANDY incorporates a shared linear dynamical prior within the common embedding, tying alignment to dynamics. Together, these strands yield an end-to-end framework that simultaneously aligns across sessions, respects continuous behavior, and extracts preserved neural dynamics.

---
*Generated: 2026-01-07T00:05:12.524716*
