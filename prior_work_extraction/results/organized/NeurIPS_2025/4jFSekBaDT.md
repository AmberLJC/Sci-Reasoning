# Prior Work Analysis Report

## Target Paper
**Title:** 4jFSekBaDT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

GRAPE’s core contribution—selecting, for each instruction, the response that best matches the target model’s pretrained distribution using normalized log-likelihood—sits at the intersection of classic domain-adaptive data selection and modern alignment methods. The Moore–Lewis method and Axelrod et al. established that selecting pseudo in-domain data via language-model cross-entropy differences substantially improves downstream performance; GRAPE internalizes this principle at the granularity of instruction–response pairs, treating the target model’s own likelihood as the in-domain proxy. GNMT’s length normalization provides the practical scoring machinery to compare candidate sequences fairly, preventing length biases in selection. 

Concurrently, alignment work such as InstructGPT demonstrated the value of staying close to the pretrained distribution (via KL penalties) to preserve capabilities and robustness; DPO further showed that model log-likelihoods can serve as effective alignment signals without explicit reward models. GRAPE translates these alignment insights into a data-centric procedure: instead of constraining the optimization objective during training, it curates training targets that naturally adhere to the base model’s distribution. 

Finally, Gururangan et al.’s evidence that in-domain data boosts performance and Self-Instruct’s practice of sourcing supervision from external teachers highlight the risks of distribution mismatch in SFT. GRAPE addresses this by gathering multi-source responses and using the target model’s likelihood to pick the most in-distribution target, yielding higher-quality, better-matched supervision with standard SFT.

---
*Generated: 2026-01-07T00:02:04.936713*
