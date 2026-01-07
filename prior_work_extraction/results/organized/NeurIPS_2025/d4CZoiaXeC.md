# Prior Work Analysis Report

## Target Paper
**Title:** d4CZoiaXeC
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (8 papers)

---

## Synthesis

FactoST’s central idea—factorizing spatio-temporal foundation modeling by decoupling universal temporal pretraining from spatial adaptation—sits at the intersection of three influential lines of work. First, Autoformer introduced decomposition/autocorrelation mechanisms that make temporal regularities (trend/seasonality) explicit, directly motivating FactoST’s multi-frequency reconstruction objective to capture cross-domain time patterns in a space-agnostic backbone. Complementarily, Informer’s ProbSparse attention and Graph WaveNet’s adaptive adjacency both argue for parsimony: retain only the most salient interactions. FactoST operationalizes this in its spatial adapter, which fuses metadata while learning sparse cross-node links, achieving both efficiency and robustness.
Second, parameter-efficient transfer catalyzed by adapter tuning (Houlsby et al.) and its video counterpart ST-Adapter demonstrated that large, frozen backbones can be specialized to new modalities or tasks via small plug-in modules. FactoST adopts this recipe verbatim: freeze or lightly finetune a universal temporal core and attach a lightweight spatial adapter that injects domain and topology awareness without bloating parameters.
Third, adaptation signals are injected through prompts and stabilized over shifts with rehearsal. Prefix-tuning provides the tooling for domain-aware prompting during temporal pretraining, while iCaRL’s memory replay informs FactoST’s continual replay to maintain alignment across evolving domains. Finally, PatchTST’s strong results with a purely temporal Transformer reinforce the paper’s thesis that temporal structure can be learned independently of spatial correlations, enabling the proposed factorization. Together, these works directly scaffold FactoST’s design choices in objective, architecture, efficiency, and adaptation.

---
*Generated: 2026-01-07T00:21:32.329013*
