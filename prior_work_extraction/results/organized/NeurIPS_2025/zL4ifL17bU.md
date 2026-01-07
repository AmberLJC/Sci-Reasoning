# Prior Work Analysis Report

## Target Paper
**Title:** zL4ifL17bU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

BE-ToF’s key contribution—encoding illumination as a learnable burst and estimating phase over the entire burst to avoid iToF phase wrapping while boosting SNR—stands on two converging lines of prior work. On the iToF side, multi-frequency and frequency-domain analyses (Godbaz–Cree–Dorrington; Bhandari–Kadambi–Raskar; Gupta–Agrawal–Veeraraghavan) formalized how phase ambiguity arises and how modulation diversity or Fourier representations can extend unambiguous range and improve robustness. These works seeded the central idea that range can be disambiguated by observing signals over longer or richer effective periods rather than a single sinusoidal cycle. In parallel, coding strategies from AMCW/ToF that use long-period pseudo-random sequences (Dorrington and colleagues) demonstrated the practical SNR and ambiguity benefits of code design plus matched filtering—foreshadowing BE-ToF’s correlation over a burst window.
A second thread is end-to-end co-design of capture and inference. Chakrabarti’s differentiable sensor multiplexing showed that jointly optimizing codes with reconstruction yields task-specific gains, which BE-ToF adopts to learn burst patterns and a reconstruction network tailored to long-range, low-photon conditions. Finally, burst photography (Hasinoff et al.) established that aggregating short exposures markedly improves SNR and fidelity in low light; BE-ToF translates this to depth by using a burst-encodable illumination and joint estimation that integrates weak returns over time. Together, these works directly inform BE-ToF’s distinctive combination of burst coding, phase-over-burst estimation, and end-to-end learnable design for high-fidelity, long-distance depth sensing.

---
*Generated: 2026-01-07T00:21:33.151116*
