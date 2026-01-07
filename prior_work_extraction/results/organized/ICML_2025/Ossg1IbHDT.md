# Prior Work Analysis Report

## Target Paper
**Title:** Ossg1IbHDT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

STFlow’s core contribution—joint, whole-slide generation of spatial transcriptomes conditioned on histology with scalable slide-level encoding—emerges from three converging lines of prior work. First, the histology-to-transcriptomics literature (HE2RNA) demonstrated that gene expression can be inferred from WSIs, later adapted to the spatial setting by HisToGene and Hist2ST. However, these works typically predict each spot independently, only weakly incorporating neighborhood context and leaving slide-level dependencies under-modeled. Second, spatial transcriptomics methods like SpaGCN established that spatial adjacency and cell–cell interactions are crucial signals, motivating models that capture correlations across spots rather than factorizing the task. Third, recent advances in generative modeling—Flow Matching and its conditional variant—provide a practical, scalable way to train continuous-time flows for conditional generation, offering a principled path to model the joint distribution of gene expression across an entire slide given histology. Finally, scalable WSI representation learning, exemplified by HIPT’s local/hierarchical attention, provides architectural guidance for handling the extreme token counts of whole slides. STFlow synthesizes these threads: it conditions a flow-matched generative model on slide-level features, uses local spatial attention to remain memory-efficient, and models the joint distribution over all spots to explicitly encode cell–cell interactions, overcoming the independence and scalability limitations of prior spot-wise predictors.

---
*Generated: 2026-01-07T00:21:32.400799*
