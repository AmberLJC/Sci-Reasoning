# Prior Work Analysis Report

## Target Paper
**Title:** cx9a4Xvb3l
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—auditing whether commonly used image-quality metrics faithfully reflect human-perceived privacy leakage in reconstruction attacks—emerges at the intersection of two lines of work. First, model and gradient inversion research (Fredrikson et al.; Zhu et al. ‘DLG’; Zhao et al. ‘iDLG’; Geiping et al.) established reconstruction as a central privacy threat and normalized reporting PSNR/SSIM to quantify attack success. These works directly supply the attack mechanisms the authors evaluate and the metric conventions they question. Second, perceptual and inversion literature (Mahendran & Vedaldi; Zhang et al. ‘LPIPS’) emphasized that human visual perception—and not pixelwise error—is the right arbiter of image similarity, providing both conceptual and methodological grounding for human-centered evaluation and learned perceptual metrics.

By combining state-of-the-art reconstruction attacks with broad, human-annotated recognizability assessments across diverse datasets, the paper tests the implicit assumption—stemming from DLG/iDLG/IG practice and SSIM’s historical prominence—that higher PSNR/SSIM implies greater privacy leakage. Drawing on LPIPS’s demonstration that deep features align better with human judgments, the authors probe alternatives and reveal systematic mismatches between hand-crafted metrics and human recognizability, especially when reconstructions preserve semantics but not pixels. The result is a calibrated view of privacy evaluation: reconstruction risk should be measured by human-recognizable content (potentially via human-aligned metrics) rather than by low-level fidelity scores. This shift directly builds on, and corrects, the evaluation paradigm inherited from prior inversion and image-quality assessment works.

---
*Generated: 2026-01-07T00:02:04.866381*
