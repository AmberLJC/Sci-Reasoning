# Prior Work Analysis Report

## Target Paper
**Title:** oBikm5Rshc
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s central claim—that language models learn spurious syntax–domain shortcuts that can override instruction semantics—sits at the intersection of three influential threads. First, work on model shortcuts and dataset artifacts (Gururangan et al., 2018; McCoy et al., 2019; Geirhos et al., 2020) established that neural models often exploit superficial cues. HANS, in particular, provided controlled tests for syntactic heuristics, and the broader shortcut-learning framing clarifies why a syntax→domain mapping can dominate semantic reasoning. Second, methodological advances in controlled evaluation (Lake & Baroni, 2018) and causal data interventions (Kaushik et al., 2020) demonstrated how synthetic or counterfactual setups can diagnose – and manipulate – specific correlations. The present paper builds on this by constructing a synthetic training corpus that intentionally correlates part-of-speech templates with domains, then quantifies the performance degradation on entity-knowledge tasks across OLMo-2 sizes, thereby causally attributing the failure mode to syntax–domain coupling. Third, recent instruction-tuning pipelines (Chung et al., 2022; Wang et al., 2023) popularized large, templated instruction corpora (e.g., FLAN/FLANv2, Self-Instruct). These sources plausibly embed stable surface-form templates tied to task types or domains. Auditing such datasets, the paper introduces an evaluation framework that detects and measures syntax–domain spurious correlations in trained models, showing the phenomenon on a subset of FLANv2. Together, these prior works directly shape the paper’s conceptual framing (shortcuts), experimental methodology (synthetic/controlled probes), and empirical target (templated instruction datasets), enabling a precise diagnosis of syntax-driven domain misgeneralization in LMs.

---
*Generated: 2026-01-07T00:05:12.515367*
