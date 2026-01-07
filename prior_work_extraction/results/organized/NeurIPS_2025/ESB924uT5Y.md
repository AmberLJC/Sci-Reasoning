# Prior Work Analysis Report

## Target Paper
**Title:** ESB924uT5Y
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

AirRep sits at the intersection of theoretically grounded influence estimation and scalable representation learning. Influence functions established the core objective of training data attribution—quantifying how perturbing a training point affects a test prediction—but their second-order computations are prohibitive at modern scales. TracIn showed that scalable approximations are possible via gradient trajectory dot products, yet they still couple attribution to gradients and checkpoints, limiting practicality and alignment with end-task attribution. Representation-based attribution, exemplified by Representer Point Selection, highlighted that embeddings can proxy influence, but fidelity suffers when representations are not optimized for the attribution task. Datamodels introduced a crucial supervision signal: empirical effects measured by retraining on sampled subsets, enabling learning surrogates that predict model outputs from data subsets. AirRep leverages this idea but uses a ranking objective tailored to attribution quality, directly training a task- and model-aligned encoder that amortizes influence estimation. For group-wise influence—central to many TDA applications—game-theoretic data valuation (Data Shapley) provides a principled target but is computationally expensive; AirRep approximates these effects by learning permutation-invariant set functions. Building on Deep Sets and Set Transformer, AirRep employs attention-based pooling to capture interactions among training examples, enabling accurate group influence estimation. Collectively, these works motivate AirRep’s design: optimizing representations specifically for attribution fidelity, supervised by empirical subset effects, and using attention-based set pooling to scale group-wise influence estimation.

---
*Generated: 2026-01-07T00:02:04.982026*
