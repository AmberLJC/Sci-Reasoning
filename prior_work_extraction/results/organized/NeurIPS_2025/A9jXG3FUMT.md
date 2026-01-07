# Prior Work Analysis Report

## Target Paper
**Title:** A9jXG3FUMT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

FAPEX’s key contribution—a learnable fractional neural frame operator (FrNFO) that yields instantaneous amplitude and phase for robust, cross-subject seizure prediction—emerges at the intersection of fractional time–frequency analysis, neural frame theory, and phase-based neuro-biomarkers. The discrete fractional Fourier transform (Candan et al., 2000) furnishes the mathematical backbone for fractional-order representations, enabling rotations in the time–frequency plane that FAPEX renders learnable via fractional-order convolutions. Deep Convolutional Framelets (Jin, Lee, Ye, 2017) casts CNNs as frame operators, a perspective FAPEX extends to a neural frame with fractional adaptivity, producing stable, interpretable amplitude–phase features.
Crucially, Rahaman et al. (2019) document neural networks’ spectral bias toward low frequencies; FAPEX directly counters this by designing a fractional front-end that captures high-frequency preictal dynamics often missed by conventional models. Prior successes with structured, learnable front-ends from raw waveforms (Ravanelli & Bengio, 2018) further support FAPEX’s decision to learn the front-end rather than rely on fixed transforms. To model long-range preictal temporal structure, FAPEX integrates structured state-space modules inspired by S4 (Gu et al., 2022), complementing spectral adaptivity with efficient sequence modeling.
On the neuroscience side, evidence that preictal phase synchronization and cross-frequency phase–amplitude coupling are informative (Le Van Quyen et al., 2001; Tort et al., 2010) motivates FAPEX’s explicit instantaneous phase and amplitude outputs, facilitating biomarker discovery and enhancing out-of-distribution generalization across subjects and modalities. Together, these works directly scaffold FAPEX’s FrNFO design and its integration with temporal SSMs, yielding a principled, phase-aware, spectrally balanced architecture for SASP.

---
*Generated: 2026-01-06T23:42:48.129557*
