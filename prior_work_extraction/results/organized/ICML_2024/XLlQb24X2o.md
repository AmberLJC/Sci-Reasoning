# Prior Work Analysis Report

## Target Paper
**Title:** XLlQb24X2o
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution—test-time degradation adaptation for open-set image restoration—unifies two lines of prior art: powerful generative priors and on-the-fly adaptation under distribution shift. Diffusion models (Ho et al., 2020) supply a degradation-agnostic clean-image prior, which DDRM (Kawar et al., 2022) and DPS (Chung & Ye, 2022) showed can be harnessed for restoration by decoupling the forward degradation from the prior and guiding sampling with a degradation operator. However, these methods typically assume a known or parameterized forward model; the present paper addresses the harder open-set setting by learning that operator at test time. This idea is rooted in single-image, zero-shot optimization paradigms from Deep Image Prior (Ulyanov et al., 2018) and ZSSR (Shocher et al., 2018), which demonstrated that image-specific adaptation can recover structure without external supervision. KernelGAN (Bell-Kligler et al., 2019) further operationalized blind test-time degradation estimation by fitting a per-image blur kernel, directly inspiring the proposed degradation adapter that is optimized from the input alone. Finally, the framework’s adapt-at-inference philosophy is grounded in Test-Time Training (Sun et al., 2020), which formalized self-supervised objectives to mitigate distribution shift during deployment. Synthesizing these strands, the paper couples a pretrained diffusion prior with a lightweight, self-supervised degradation adapter learned per test instance, enabling robust restoration under previously unseen degradations.

---
*Generated: 2026-01-07T00:02:04.874541*
