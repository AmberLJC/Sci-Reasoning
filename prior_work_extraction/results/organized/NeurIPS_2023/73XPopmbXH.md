# Prior Work Analysis Report

## Target Paper
**Title:** 73XPopmbXH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core advance—showing that smoothing the loss enables online SGD to learn single index models (SIMs) at the statistically optimal n ≳ d^{k*/2}—is tightly anchored to three prior threads. First, Ben Arous et al. (2021) analyzed online SGD on the unsmoothed population loss for SIMs and proved that n ≳ d^{k*−1} samples suffice (and are effectively necessary for vanilla online SGD). This result highlighted a gap with the centered statistical query (CSQ) lower bounds for gradient-based methods, such as those developed by Shamir (2016), which imply that only n ≳ d^{k*/2} samples are information-theoretically necessary. Closing this gap requires amplifying the learnable Hermite-k* signal in gradients without invoking higher-complexity tensor methods.
A second thread comes from tensor PCA. Richard and Montanari (2014) and the broader tensor-decomposition literature (e.g., Anandkumar et al., 2014) show that degree-k signals naturally exhibit optimal sample scaling ≈ d^{k/2}, mirroring the SIM information exponent k*. This paper leverages that insight by designing a smoothed objective whose gradient selectively enhances the k*th Hermite component, allowing first-order SGD to exploit the same low-degree signal that tensor methods target.
Finally, the connection to minibatch SGD’s implicit regularization is grounded in works like Mandt et al. (2017) and Yaida (2018), which model SGD noise as inducing an effective smoothing of the loss landscape. These results conceptually justify why explicit smoothing should boost signal-to-noise in gradients and explain the paper’s observed parallels between smoothed-loss SGD and practical minibatch SGD behavior.

---
*Generated: 2026-01-06T23:42:49.103202*
