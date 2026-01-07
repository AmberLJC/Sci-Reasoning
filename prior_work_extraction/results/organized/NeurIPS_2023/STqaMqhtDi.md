# Prior Work Analysis Report

## Target Paper
**Title:** STqaMqhtDi
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The CORP framework’s core innovation—plug-and-play stability via self-recalibration using language-model–generated pseudo-labels—emerges at the intersection of three lines of prior work. First, intracortical communication systems established the feasibility and mechanics of brain-to-text decoding with LM support. Willett et al. (2021) created the high-performance handwriting-based iBCI and integrated language-model autocorrection, while Pandarinath et al. (2017) showed that predictive text can substantially boost communication rates. These works supply CORP’s operational substrate and the insight that linguistic priors can systematically clean decoder outputs.
Second, long-term stability in iBCIs has been pursued through decoder adaptation and alignment. Orsborn et al. (2014) introduced closed-loop decoder adaptation to maintain performance as neural signals drift, and Degenhart et al. (2020) framed day-to-day nonstationarity as a manifold alignment problem. CORP aligns with the continual-update philosophy but eliminates explicit calibration or alignment steps by converting online, LM-corrected text into training supervision.
Third, the methodological backbone is semi-supervised learning via pseudo-labeling (Lee, 2013). CORP operationalizes pseudo-labels in a neuroprosthetic context: LM-corrected outputs become self-generated labels that enable continual online retraining. Complementing this, Moses et al. (2021) reinforced that strong language models can robustly constrain neural-to-text decoding, validating LM-based correction as a reliable supervisory signal. Together, these works directly informed CORP’s design: an LM-in-the-loop, self-training decoder that sustains year-long, interruption-free brain-to-text communication.

---
*Generated: 2026-01-07T00:02:04.791087*
