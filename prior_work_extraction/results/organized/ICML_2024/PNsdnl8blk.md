# Prior Work Analysis Report

## Target Paper
**Title:** PNsdnl8blk
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**A Survey on Metamorphic Testing** (2016)
- *Authors:* Sergio Segura et al.
- *Connection:* Segura et al. formalized metamorphic testing and metamorphic relations as a principled way to encode expected relations between inputs and outputs without requiring exact labels; MAgg adopts this framework to define and utilize metamorphic relations among transformed combinatorial instances at inference time.

**Learning to Solve NP-Complete Problems: A Graph Neural Network for Decision TSP** (2019)
- *Authors:* Marcelo O. R. Prates et al.
- *Connection:* Prates et al. established the decision-TSP satisfiability prediction task with GNNs, which MAgg targets; MAgg leverages natural metamorphic relations in this setting (e.g., cost scaling with threshold adjustment) to construct relation graphs for improved test-time aggregation.

### 💡 Inspiration

**DeepTest: Automated testing of deep-neural-network-driven autonomous cars** (2018)
- *Authors:* Yuchi Tian et al.
- *Connection:* DeepTest demonstrated how domain-specific metamorphic relations can relate outputs across transformed inputs for DNNs; MAgg is inspired by this idea but repurposes it from testing to inference by exploiting such relations to aggregate predictions across metamorphically related instances.

### 🔍 Gap Identification

**Deep Sets** (2017)
- *Authors:* Manzil Zaheer et al.
- *Connection:* Deep Sets established permutation-invariant set aggregation (e.g., mean/sum) that underlies common TTA ensembling; MAgg addresses the limitation that such set pooling ignores known relational constraints between augmented instances by introducing a relation-graph and GNN-based aggregation.

### 📊 Baseline

**Test-time data augmentation for estimation of heteroscedastic aleatoric uncertainty in deep neural networks** (2018)
- *Authors:* S. Ayhan et al.
- *Connection:* MAgg directly generalizes the standard TTA practice formalized by Ayhan & Berens—averaging predictions over label-preserving augmentations—by replacing naive averaging with relation-aware aggregation and allowing non–label-preserving transformations via metamorphic relations.

**Learning a SAT Solver from Single-Bit Supervision** (2019)
- *Authors:* Daniel Selsam et al.
- *Connection:* NeuroSAT introduced GNN-based SAT satisfiability prediction, a primary task setting evaluated by MAgg; MAgg builds on this formulation and improves inference by aggregating predictions over metamorphically related SAT instances rather than relying on a single prediction or naive TTA.

### 🔧 Extension

**Neural Message Passing for Quantum Chemistry** (2017)
- *Authors:* Justin Gilmer et al.
- *Connection:* MAgg extends the message-passing paradigm to a new setting where nodes are transformed problem instances and directed edges encode metamorphic label mappings, using a GNN over this relation graph to aggregate predictions.

---

## Synthesis

MAgg’s core idea arises from unifying two lines of thought: test-time augmentation (TTA) and metamorphic testing (MT). TTA methods, typified by Ayhan & Berens, improve robustness by averaging predictions over label‑preserving transforms, but their permutation‑invariant set aggregation (as formalized by Deep Sets) ignores known dependencies between augmented views and cannot exploit non–label‑preserving transformations. Metamorphic testing, synthesized in Segura et al.’s survey and operationalized for DNNs in DeepTest, provides exactly such dependencies: metamorphic relations that specify how outputs should change under structured input transformations even when exact labels are unavailable. MAgg leverages this insight at inference time, modeling metamorphic relations among transformed instances as a directed relation graph and aggregating predictions with message passing, extending Gilmer et al.’s MPNN framework to propagate information according to MR‑induced label mappings. This design directly addresses the central gap in standard TTA—its reliance on label preservation and naive averaging—by learning relation‑aware aggregation over richer, MR‑defined transformation families. The approach is instantiated on canonical ML-for-combinatorial tasks that provided the problem formulations and baselines: SAT satisfiability prediction via NeuroSAT and decision‑TSP via Prates et al. MAgg improves inference on these tasks by constructing MR graphs (e.g., literal/constraint transformations for SAT; cost scaling with threshold adjustment for decision‑TSP) and learning to aggregate across them, yielding an inference‑time augmentation mechanism grounded in metamorphic relations rather than constrained to invariances alone.

---
*Generated: 2026-01-06T23:09:26.436638*
