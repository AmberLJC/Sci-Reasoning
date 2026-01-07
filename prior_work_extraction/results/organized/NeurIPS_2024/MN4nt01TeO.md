# Prior Work Analysis Report

## Target Paper
**Title:** MN4nt01TeO
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Adaptive Randomized Smoothing (ARS) fuses two lines of work: certified defenses via randomized smoothing and compositional guarantees from differential privacy (DP), to certify test-time adaptive models. The seminal randomized smoothing analysis of Cohen et al. (2019) established practical, scalable certification but for a single, fixed classifier. PixelDP (Lécuyer et al., 2019) first formalized a DP-to-robustness bridge, showing that DP guarantees can imply robustness certificates, suggesting that privacy accounting tools might handle more complex pipelines. ARS advances this direction by adopting the f-Differential Privacy framework of Dong, Roth, and Su (2019), whose trade-off function view gives tight, sound composition—crucially under adaptivity. In spirit, this aligns with Mironov’s Rényi DP (2017), which pioneered tighter adaptive composition accounting, but f-DP lets ARS treat general, high-dimensional functions of noisy inputs. Denoised Smoothing (Salman et al., 2020) demonstrated that preprocessing functions (e.g., denoisers) can be composed within smoothing and still be certifiable; ARS significantly generalizes this to multi-step, input-dependent (adaptive) transformations such as high-dimensional masking, including for the L∞ threat model. Finally, modern test-time adaptation methods—Tent (Wang, Shelhamer, et al., 2021) and Test-Time Training (Sun et al., 2020)—motivate ARS’s core goal: certifying predictions of models that adapt at inference. ARS unifies RS with f-DP accounting to provide the first theory handling sound adaptive composition of general functions in multi-step defenses, improving accuracy while maintaining certification.

---
*Generated: 2026-01-07T00:02:04.743117*
