# Prior Work Analysis Report

## Target Paper
**Title:** HTLJptF7qM
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution is an identifiability theory for confusion-matrix–based noisy-label learning when confusion matrices vary across instances, yielding occasional outliers. This advances beyond the standard class-conditional (instance-invariant) transition-matrix assumption popularized in noisy-label learning and loss-correction methods. Natarajan et al. and Patrini et al. formalized and operationalized the transition-matrix view, but their guarantees hinge on a fixed matrix, leaving identifiability open when noise is instance dependent. Xia et al. articulated the practical and theoretical difficulties of instance-dependent label noise—particularly acute when each example has only a single noisy label—foreshadowing the impossibility the present work makes explicit.

The resolution draws on the crowdsourcing lineage. Dawid and Skene introduced the annotator confusion-matrix model and EM estimation, establishing the core statistical structure for multi-annotator data. Raykar et al. coupled this with a predictive model, showing the feasibility of jointly inferring ground truth and annotator reliabilities. Modern provable approaches, exemplified by Zhang et al., reveal that cross-annotator moment structure ("crowd wisdom") can identify per-worker confusion matrices in multiclass settings. This multi-view identifiability perspective is broadly grounded in tensor/moment methods (Anandkumar et al.), which justify recovering latent parameters from higher-order correlations. The present paper leverages these insights to show that, while single-annotator labels are fundamentally insufficient to detect instance-dependent outliers, multiple annotators provide the redundancy needed to identify the ground-truth classifier and the underlying confusion mechanisms, thereby extending confusion-matrix methods to a more realistic, instance-dependent regime.

---
*Generated: 2026-01-06T23:33:35.532336*
