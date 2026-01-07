# Prior Work Analysis Report

## Target Paper
**Title:** v7I5FtL2pV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Charms sits at the intersection of privileged information learning, cross-modal distillation, and distributional alignment. The LUPI paradigm (Vapnik & Vashist) establishes the central problem setting: expert tabular attributes are available only during training yet should improve an image-only predictor at test time. Lopez-Paz et al. formalize how teacher–student distillation operationalizes LUPI, while Gupta et al. show that supervision can be transferred across heterogeneous modalities when one is absent at inference, directly motivating Charms’s tabular-to-image supervision transfer.
To make this transfer selective and semantically grounded, Charms revives the attribute-to-visual alignment idea from zero-shot learning (Lampert et al.), treating expert tabular descriptors as attributes that should map to specific visual factors. The key algorithmic engine enabling such heterogeneous matching is optimal transport: Cuturi’s Sinkhorn distances provide efficient, differentiable OT, and JDOT (Courty et al.) shows how aligning joint distributions can steer knowledge transfer. Charms adapts these insights to align distributions of tabular attributes with image channel responses, effectively identifying which channels encode attribute-relevant morphology. Finally, by maximizing mutual information in a contrastive manner (van den Oord et al.), Charms strengthens cross-modal correspondences and guards against spurious matches, while accommodating different treatments for numerical versus categorical attributes within the OT/MI framework. Together, these works crystallize into Charms’s core contribution: a channel-wise, OT-driven, MI-regularized transfer of expert tabular knowledge into image classifiers that operate without tabular inputs at inference.

---
*Generated: 2026-01-06T23:42:48.056593*
