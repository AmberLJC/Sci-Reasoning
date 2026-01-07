# Prior Work Analysis Report

## Target Paper
**Title:** bzxlOyjWbU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The Deep Value Benchmark (DVB) sits at the intersection of preference-based alignment and robustness to spurious correlations. Preference learning (Christiano et al., 2017) and its large-scale instantiation in LLMs via RLHF (Ouyang et al., 2022) provide the training paradigm DVB targets: learning from human feedback. Yet, Constitutional AI (Bai et al., 2022) highlights an aspiration to go beyond mere preference imitation toward explicit principles—raising the question DVB seeks to answer: do models truly internalize deep values or just surface proxies? Methodologically, DVB borrows the rigorous diagnostic strategy from HANS (McCoy et al., 2019) and Waterbirds/GroupDRO (Sagawa et al., 2020): engineer training distributions where shallow features correlate with correct choices, then evaluate out-of-correlation to test reliance on shortcuts. This paradigm directly addresses the dataset artifact concerns surfaced by Poliak et al. (2018), ensuring that apparent success is not driven by stylistic or lexical cues. While prior ethical benchmarks like ETHICS (Hendrycks et al., 2021) assess moral competence, they do not disentangle deep moral principles from confounded surface attributes. DVB’s core innovation is to fuse these strands: it evaluates RLHF/values-trained LLMs under controlled confounding, operationalizing the principle-versus-preference distinction. In doing so, it offers a principled test of value generalization that can validate (or falsify) claims that instruction- or constitution-trained models capture human values robustly rather than overfitting to superficial patterns.

---
*Generated: 2026-01-07T00:02:04.931692*
