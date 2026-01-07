# Prior Work Analysis Report

## Target Paper
**Title:** 8aDG51pxFc
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—an efficient, closed-form Expected Model Change Maximization (EMCM) criterion tailored to GNNs—builds on three threads: active learning by model change/error, semi-supervised graph learning, and tractable approximations of parameter updates. Settles and Craven’s expected gradient length formalizes EMCM, directly inspiring the paper’s objective to quantify how much labeling a node would alter the model. Roy and McCallum’s expected error reduction supplies the theoretical anchor; the authors explicitly connect their EMCM score to minimizing expected prediction error, yielding guarantees. On the graph learning side, Kipf and Welling’s GCN defines the semi-supervised node-classification setting and produces the embeddings whose uncertainty the method must quantify. Manifold regularization provides the Laplacian-based prior that justifies a Bayesian perspective on graph-based representations, enabling the authors to derive a probabilistic characterization of GNN embeddings under semi-supervision. Wu et al.’s SGC perspective (graph propagation followed by a linear classifier) makes the GNN amenable to closed-form analysis—crucial for computing EMCM without retraining. Finally, Koh and Liang’s influence functions motivate efficient estimation of parameter change, conceptually supporting the paper’s training-free expected-update computation. Together, these works enable a principled, theoretically grounded acquisition function that marries EMCM with the Bayesian, semi-supervised structure of GNNs, achieving both accuracy and efficiency.

---
*Generated: 2026-01-07T00:02:04.789718*
