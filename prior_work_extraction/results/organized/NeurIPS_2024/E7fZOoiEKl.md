# Prior Work Analysis Report

## Target Paper
**Title:** E7fZOoiEKl
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

FuseFL targets the long-standing tension in federated learning between communication efficiency and accuracy under non-IID data, especially acute in one-shot aggregation. FedAvg established model averaging as the workhorse for communication efficiency but suffers from pronounced degradation when client updates are isolated and heterogeneous. Causal robustness work—particularly Invariant Risk Minimization—clarified that models trained across environments (clients) can overfit spurious correlations, motivating learning mechanisms that extract invariant features. FuseFL’s central idea follows this causal lens: using other clients as distinct environments and augmenting intermediate representations helps suppress spurious fits.
Split learning showed that exchanging intermediate activations enables effective cross-party knowledge transfer without raw data sharing, suggesting the power of feature-level interaction; FuseFL captures a similar benefit implicitly via block-wise fusion, avoiding extra communication. The progressive, bottom-up training/fusion design is rooted in greedy layer-wise training, leveraging stable incremental representation building. In parallel, mixup’s success with feature-space augmentation inspired the notion that mixing representations promotes smoother, more invariant decision boundaries—here realized by fusing intermediate features from disparate clients. While control-variate methods like SCAFFOLD tackle client drift in multi-round FL, FuseFL adapts the insight—heterogeneity-induced drift arises from isolation—by addressing it causally via progressive feature fusion in a single round. Finally, rather than relying on distillation’s additional data/logit exchanges (as popularized by Hinton et al.), FuseFL achieves one-shot knowledge transfer through structured model decomposition and fusion, delivering OFL-level communication with markedly improved robustness.

---
*Generated: 2026-01-06T23:33:35.578407*
