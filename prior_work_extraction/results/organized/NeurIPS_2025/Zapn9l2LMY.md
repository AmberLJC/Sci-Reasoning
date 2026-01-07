# Prior Work Analysis Report

## Target Paper
**Title:** Zapn9l2LMY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ST-TTC’s core idea—performing lightweight, real-time bias correction at inference by operating in the spectral domain and updating only a minimal set of parameters—sits at the intersection of test-time adaptation, time-series shift correction, and frequency-aware forecasting. Tent and TTT provide the foundational blueprint for label-free adaptation at test time: limit updates to a small module and drive them with unsupervised or auxiliary objectives to ensure stability, speed, and generality. RevIN translates this paradigm to time-series forecasting, proving that simple, per-instance corrections can substantially reduce the impact of distribution shifts without retraining, thereby validating the value of a plug-in “calibrator” that adjusts predictions online.
On the modeling side, Autoformer and TimesNet foreground the centrality of periodic structure and phase in long-horizon forecasting—insights that directly motivate ST-TTC’s choice to calibrate in the frequency domain, where periodic biases are compact and interpretable. FDA contributes the key mechanism: modulating amplitude (and respecting phase) in Fourier space to bridge domain gaps, which ST-TTC adapts into a phase–amplitude modulation calibrator that mitigates periodic shifts specific to spatio-temporal data. Finally, LoRA informs the engineering of the flash updating mechanism, showing how parameter-efficient, low-rank updates can deliver fast, low-compute adaptation. Together, these works shape ST-TTC into a test-time computing framework that is model-agnostic, computation-conscious, and explicitly targeted at correcting non-stationary, periodic biases that undermine spatio-temporal forecasts.

---
*Generated: 2026-01-07T00:21:32.312176*
