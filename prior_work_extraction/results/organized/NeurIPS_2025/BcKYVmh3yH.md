# Prior Work Analysis Report

## Target Paper
**Title:** BcKYVmh3yH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—sampling-efficient Best-of-N via self-estimated, early-decoding selection (ST-BoN)—sits at the intersection of test-time scaling, multi-candidate decoding, and adaptive compute. Prior RLHF work established BoN as a powerful inference-time tool: Stiennon et al. (2020) and Ouyang et al. (2022) showed that generating multiple candidates and choosing with a reward model improves quality, but at the cost of extra memory, latency, and the need to train and deploy a separate scorer. In parallel, self-consistency (Wang et al., 2023) and Tree-of-Thoughts (Yao et al., 2023) demonstrated that one can exploit model-internal signals—agreement among samples or evaluations of partial thoughts—without reward models, suggesting a path to eliminating the RM overhead.
Classical decoding advances like Diverse Beam Search (Vijayakumar et al., 2016) and Noisy Parallel Approximate Decoding (Cho, 2016) established the effectiveness of exploring multiple candidates, but typically required fully generating and then rescoring, exacerbating compute and memory use. Finally, Confident Adaptive Language Modeling (Schuster et al., 2022) introduced the broader idea of adapting computation based on early uncertainty signals.
ST-BoN synthesizes these threads: it preserves BoN’s quality gains while borrowing the self-evaluation ethos of self-consistency/ToT and the adaptive-compute principle of CALM. Concretely, it leverages early sampling consistency and likelihood cues on partial prefixes to predict which candidate will ultimately win, truncating the rest to save GPU memory and latency—thereby jointly addressing BoN’s two main bottlenecks (fully decoding N samples and relying on reward models).

---
*Generated: 2026-01-07T00:29:42.060359*
