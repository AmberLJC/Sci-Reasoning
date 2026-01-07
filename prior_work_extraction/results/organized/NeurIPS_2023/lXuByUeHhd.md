# Prior Work Analysis Report

## Target Paper
**Title:** lXuByUeHhd
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

DoReMi’s core innovation—automatically optimizing domain mixture proportions for language model pretraining via a small proxy model—sits at the intersection of distributionally robust optimization and domain-aware pretraining. The methodological spine comes from Group DRO (Sagawa et al., 2020), which formulates worst-case risk over predefined groups; DoReMi maps pretraining domains to these groups and directly adopts Group DRO’s minimax weighting to emphasize underperforming domains. This builds on earlier subpopulation-robust learning ideas from Hashimoto et al. (2018) and the broader theoretical framework of f-divergence–based DRO and reweighting developed by Namkoong and Duchi (2017), which justify the stability and efficacy of minimax-derived weights.

On the data side, Gururangan et al. (2020) established that domain-aware pretraining materially affects downstream performance, motivating systematic control of domain composition rather than heuristic mixing. The Pile (Gao et al., 2020) concretized the multi-domain pretraining setting with explicit mixture weights, providing both the practical need (heuristic weights can be suboptimal) and the evaluation substrate for DoReMi.

Finally, Ren et al. (2018) showed that learned data weights obtained from a small proxy learner can transfer to improve full-scale training. While DoReMi does not rely on labeled validation like meta-reweighting, it borrows the key operational insight: use a smaller model to efficiently learn informative sampling weights that generalize. Together, these strands yield DoReMi’s proxy-driven, Group-DRO-based domain reweighting that accelerates and improves large-scale LM pretraining.

---
*Generated: 2026-01-06T23:42:48.031533*
