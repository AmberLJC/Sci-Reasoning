# Prior Work Analysis Report

## Target Paper
**Title:** 761hggw1Wx
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CoLT sits at the intersection of simulation-based inference and modern goodness-of-fit testing. Neural posterior estimation methods such as SNPE (Papamakarios & Murray) made amortized posteriors q(θ|x) practical, but also raised the need for robust validation. The SBI community subsequently embraced diagnostics like simulation-based calibration (Talts et al.) and classifier-based metrics surveyed in Benchmarking SBI (Lueckmann et al.), revealing key shortcomings: many tests aggregate across x, struggle to identify where errors occur, or require many samples per x that are unavailable in typical simulator workflows.

Classifier two-sample tests (Lopez-Paz & Oquab) and classifier-based ratio estimation (Cranmer et al.) demonstrated the power of discriminative objectives to expose distributional discrepancies, influencing many NPE diagnostics. However, these approaches are largely global and not explicitly conditional, limiting their ability to detect localized deviations in q(θ|x). CoLT’s core innovation—learning a localization function θℓ(x) that targets worst-case discrepancies for each x—draws methodological inspiration from kernel testing with learned test locations and witness functions. In particular, Jitkrittum et al. showed that optimizing test locations can dramatically improve power and provide interpretability, while kernelized Stein discrepancy (Liu et al.) introduced witness functions that highlight where a model fails.

By adapting these localization principles to the conditional posterior setting and designing the procedure to work with only a single θ ∼ p(θ|x) per x, CoLT overcomes the data-efficiency and conditional-specificity gaps in prior diagnostics, providing a principled, high-power test tailored to NPE validation.

---
*Generated: 2026-01-07T00:21:32.273336*
