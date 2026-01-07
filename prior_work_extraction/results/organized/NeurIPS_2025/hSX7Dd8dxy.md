# Prior Work Analysis Report

## Target Paper
**Title:** hSX7Dd8dxy
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—formalizing reward hacking in inference-time alignment and introducing Best-of-Poisson (BoP) as a near-exact approximation to the optimal reward–KL policy—rests on three converging lines of prior work. First, Christiano et al. and Ouyang et al. established the modern alignment stack: learning reward models from preferences and optimizing a KL-regularized objective against a reference policy. This framework both enables inference-time reranking and creates the conditions for Goodhart-style failures, as flagged by Amodei et al. Second, practical inference-time alignment methods like Constitutional AI and self-consistency popularized Best-of-n style selection—either via reward-model rejection sampling or multi-sample reranking—demonstrating large empirical gains while implicitly exposing sensitivity to mis-specified proxies. This paper systematizes those procedures, analyzing Best-of-n and a soft variant (SBoN) to reveal characteristic reward-hacking patterns and motivate principled hedging on the proxy reward. Third, theory on the optimal policy under reward–KL (as in DPO) shows that the ideal solution is an exponential tilt of the reference policy. Bridging this theory to practical decoding, the paper draws on extreme-value/perturb-and-select insights typified by the Gumbel-Top-k literature to craft Best-of-Poisson—a Poisson point-process-based sampler that closely matches the exponential-tilted target at inference time. Together, these works directly inform the paper’s diagnosis of reward hacking under inference-time selection and its BoP-based, theoretically grounded mitigation strategy.

---
*Generated: 2026-01-06T23:42:48.122630*
