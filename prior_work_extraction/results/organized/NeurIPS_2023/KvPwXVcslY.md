# Prior Work Analysis Report

## Target Paper
**Title:** KvPwXVcslY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—introducing critical band masking as a unified behavioral assay to compare humans and neural networks on natural object recognition and linking the resulting spatial-frequency channel signatures to shape bias and adversarial robustness—rests on two converging literatures. First, classic human vision studies established spatial-frequency channelization and the critical-band masking methodology. Graham and Nachmias (1971) provided direct evidence for multiple spatial-frequency channels via frequency-specific masking between gratings, while Pelli and Farell (1999) formalized the use of controlled external noise to reveal perceptual filters. Building on this foundation, Solomon and Pelli (1994) and Majaj et al. (2002) showed that letter recognition is mediated by a bandpass filter roughly one octave wide, supplying the exact human benchmark—one-octave channelization—that the present work tests for natural images.
Second, modern deep learning studies connected feature usage to robustness and perceptual similarity. Geirhos et al. (2019) demonstrated that CNNs exhibit a texture bias and that promoting shape bias improves robustness, providing behavioral metrics the current paper relates to frequency-channel signatures. Ilyas et al. (2019) reframed adversarial vulnerability as reliance on non-robust features, often associated with high-frequency information, motivating an explicit frequency-based probe. Dapello et al. (2020) showed that injecting V1-like bandpass channels into CNNs enhances robustness and shape-biased behavior, aligning with the paper’s finding that human-like one-octave channelization correlates with desirable robustness properties. Together, these works enabled the paper to operationalize a frequency-resolved, noise-based behavioral comparator across humans and 76 networks, revealing a canonical human one-octave channel for natural objects and explaining model variability via shape bias and adversarial robustness.

---
*Generated: 2026-01-06T23:33:35.586653*
