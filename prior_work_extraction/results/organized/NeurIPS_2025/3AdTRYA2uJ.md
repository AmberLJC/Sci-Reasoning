# Prior Work Analysis Report

## Target Paper
**Title:** 3AdTRYA2uJ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CaMVo’s core innovation—online, cost-aware selection of a subset of LLMs per instance with weighted majority aggregation absent ground truth—sits at the intersection of contextual bandits and crowdsourced label aggregation. LinUCB (Li et al., 2010) is the methodological backbone for CaMVo’s per-instance querying policy: contextual embeddings represent items, and uncertainty-aware upper confidence bounds drive exploration versus exploitation over LLMs. The framework’s explicit budget-conscious querying is informed by Bandits with Knapsacks (Badanidiyuru et al., 2013) and combinatorial bandits (Chen et al., 2013), which formalize selecting sets of arms under resource constraints, closely mirroring CaMVo’s subset-of-LLMs decision under cost. On the aggregation side, CaMVo’s Bayesian estimator that infers (and lower-bounds) per-LLM accuracy without supervision directly descends from classic crowd models. Dawid–Skene (1979) established unsupervised annotator reliability estimation; GLAD (Whitehill et al., 2009) added instance difficulty and expertise-weighted voting; and Raykar et al. (2010) framed probabilistic aggregation for multiple noisy annotators. CaMVo adapts these principles to machine annotators (LLMs), fusing them with online selection to weight votes by inferred reliability. Finally, recent LLM literature shows the efficacy of voting over multiple signals—Self-Consistency (Wang et al., 2023) empirically validates that plurality and aggregation improve accuracy—providing the immediate LLM context and the baseline CaMVo aims to match at lower cost. Together, these works directly enable CaMVo’s design: a contextual-bandit-driven, cost-aware querying strategy coupled with principled, unsupervised reliability-weighted voting for high-quality, economical LLM-based annotation.

---
*Generated: 2026-01-07T00:29:42.054520*
