# Prior Work Analysis Report

## Target Paper
**Title:** zNLlglSOwD
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

AdaSPEC targets the core bottleneck of speculative decoding: maximizing the acceptance rate of draft-model tokens during verification by the target model. The speculative decoding framework itself is grounded in the draft-and-verify mechanism and acceptance-rate analysis introduced by Leviathan et al., which makes clear that speedup hinges on aligning the draft with the target specifically on the tokens likely to be accepted. Traditional knowledge distillation, inaugurated by Hinton et al. and adapted to sequence generation by Kim and Rush, offers a teacher–student training pathway but typically minimizes KL divergence across all tokens—an objective that can overemphasize hard or idiosyncratic cases the student cannot fit, especially under capacity constraints, and thus is misaligned with acceptance-centric goals.

AdaSPEC’s key insight—selectively filtering tokens during KD—draws from established ideas in data selection and robust training. Moore–Lewis demonstrated that a reference language model can guide effective filtering, a strategy AdaSPEC repurposes at token granularity to identify difficult-to-fit instances. In parallel, Co-teaching showed that discarding high-loss samples can improve learning by avoiding noisy or overly hard examples; AdaSPEC applies a similar principle to KD for speculative decoding, focusing training on easier, alignment-critical tokens. Finally, practical NLP distillation efforts like DistilBERT exemplify the default token-level KL setup that AdaSPEC deliberately departs from. By combining speculative decoding’s acceptance objective with reference-model-guided, selective KD, AdaSPEC achieves a student better aligned with the target where it matters most for verification, improving acceptance and thus inference efficiency.

---
*Generated: 2026-01-07T00:21:32.308332*
