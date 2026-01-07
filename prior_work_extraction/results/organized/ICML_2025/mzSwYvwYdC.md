# Prior Work Analysis Report

## Target Paper
**Title:** mzSwYvwYdC
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—an independence test that, given two sets of weights, determines whether models were trained from independent initializations—rests on three pillars: robust similarity statistics, symmetry-aware model alignment, and exact randomization-based inference. First, representation-similarity metrics from SVCCA and CKA provide stable, architecture-agnostic statistics to quantify how close two networks’ layers or features are, even when naively comparing weights is meaningless. Second, the literature on permutation symmetries and weight matching (e.g., Entezari et al. on permutation invariance and Ainsworth et al.’s Git Re-Basin) shows that independently trained networks can be made strikingly closer after neuron/channel alignment. This directly informs the paper’s constrained-setting construction of exchangeable copies: by exploiting architectural symmetries (e.g., layer-wise permutations) they can simulate null surrogates that are distributionally indistinguishable from independently initialized/trained counterparts, enabling fair comparison of similarity statistics. Third, the testing framework builds on classical randomization tests (Dwass) and the exchangeability logic popularized by Model-X knockoffs: sampling exchangeable surrogates under the null yields exact p-values without asymptotics. Finally, the paper’s unconstrained, adversarial setting is motivated by real IP risks exemplified by model stealing (Knockoff Nets), clarifying both the dependence structures that arise in practice (e.g., distillation-induced similarity) and the evasion strategies a robust test must withstand. Together, these strands enable a principled, symmetry-aware Monte Carlo test that reports exact p-values and is empirically validated across open-weight language models.

---
*Generated: 2026-01-07T00:21:32.400268*
