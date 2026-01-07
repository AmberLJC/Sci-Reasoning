# Prior Work Analysis Report

## Target Paper
**Title:** kQokjfoGjk
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—self-supervised re-labeling for time series forecasting via SCAM—sits at the intersection of pseudo-labeling, blind denoising, masking-based reconstruction, noisy-label learning, and loss-landscape regularization. Pseudo-Label (Lee, 2013) provides the foundational paradigm of using model-generated labels to boost learning, which SCAM adapts by turning reconstruction intermediates into pseudo labels for unreliable forecast targets. Noise2Self (Batson & Royer, 2019) and Masked Autoencoders (He et al., 2022) demonstrate that masking and reconstruction can yield strong supervision without clean targets; SCAM operationalizes this by reconstructing time-series segments and using those reconstructions as substitutes where ground-truth values appear corrupted or overfit. From the noisy-label literature, Co-teaching (Han et al., 2018) inspires SCAM’s selective mechanism: instead of uniformly trusting all targets, it adaptively identifies overfitted components and replaces them, akin to filtering noisy labels rather than learning them. Complementing this data-centric correction, Confident Learning (Northcutt et al., 2021) motivates the explicit identification and remediation of label errors, aligning with SCAM’s premise that “not all data are good labels.” Finally, to prevent the pseudo-labeling loop from amplifying noise, SCAM borrows from loss-landscape regularization: Spectral Normalization (Miyato et al., 2018) constrains network Lipschitzness, and Sharpness-Aware Minimization (Foret et al., 2021) motivates seeking flatter minima, both curbing overfitting and stabilizing optimization. Together, these threads crystallize into SCAM’s self-correction with adaptive masking and SNR, a model-agnostic way to construct cleaner supervisory signals for time-series forecasting.

---
*Generated: 2026-01-07T00:02:04.947289*
