# Prior Work Analysis Report

## Target Paper

**Title:** On the Joint Interaction of Models, Data, and Features

**Conference:** ICLR 2024 (oral)

**Authors:** Yiding Jiang, Christina Baek, J Zico Kolter

**Keywords:** Generalization, feature learning, empirical phenomena

**Abstract:** 
> Learning features from data is one of the defining characteristics of deep learning,
but the theoretical understanding of the role features play in deep learning is still in
early development. To address this gap, we introduce a new tool, the interaction
tensor, for empirically analyzing the interaction between data and model through
features. With the interaction tensor, we make several key observations about
how features are distributed in data and how models with different random seeds
learn ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Risk Bounds for the Majority Vote: From a PAC-Bayesian Analysis to a Learning Algorithm** (2015)
- *Authors:* Pascal Germain et al.
- *Direct Connection:* This work formalized disagreement between classifiers as a core statistic for generalization analysis (C-bound), which the present paper reinterprets at the feature level to obtain exact closed-form expressions for expected accuracy and agreement.

**Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles** (2017)
- *Authors:* Balaji Lakshminarayanan et al.
- *Direct Connection:* The paper’s empirical use of cross-seed agreement/disagreement relies on the deep-ensembles paradigm of training multiple independently initialized models, providing the unlabeled observable the interaction tensor links to generalization.

### 💡 Inspiration

**Generalization Disagreement Equality** (2023)
- *Authors:* Christina Baek et al.
- *Direct Connection:* The interaction-tensor framework is explicitly constructed to recover and mechanistically explain the GDE by deriving closed-form links between accuracy and pairwise hypothesis agreement that make unlabeled disagreement a predictor of generalization.

**Adversarial Examples Are Not Bugs, They Are Features** (2019)
- *Authors:* Andrew Ilyas et al.
- *Direct Connection:* The feature-centric view—distinguishing robust and non-robust features—directly motivates modeling data as a distribution over features with varying predictiveness, which the interaction tensor quantifies and the framework formalizes.

**Toy Models of Superposition in Neural Networks** (2022)
- *Authors:* Nelson Elhage et al.
- *Direct Connection:* Insights that features are superposed and compete for limited representational resources inspire modeling how different random seeds learn different subsets/combinations of features, a behavior the interaction tensor measures.

### 🔍 Gap Identification

**On Lazy Training in Differentiable Programming** (2019)
- *Authors:* Lénaïc Chizat et al.
- *Direct Connection:* By showing that lazy/NTK regimes do not capture feature learning, this work highlights a key limitation the paper addresses by explicitly modeling data–model interactions through learned features rather than fixed kernels.

---

## Synthesis: How Prior Work Led to This Paper

The Generalization Disagreement Equality (GDE) demonstrated that, under mild conditions, the generalization error can be inferred from pairwise model disagreement measured on unlabeled data, elevating disagreement to a central, label-free statistic for generalization. PAC‑Bayesian analyses of majority votes had already identified disagreement as a key quantity, deriving C‑bounds that relate ensemble risk to the expected pairwise disagreement, thus providing a formal grounding for using agreement statistics. Deep ensembles operationalized this idea empirically by training multiple independently initialized networks, making cross-seed agreement a practical, robust observable. Complementing these agreement-centric threads, the feature-centric perspective—crystallized by the robust vs. non‑robust feature distinction—argued that neural networks succeed by exploiting a heterogeneous mix of data features with varying predictiveness and transfer properties. Toy models of superposition further suggested that features are represented in overlapping subspaces and compete for capacity, implying that different random seeds may emphasize different feature subsets. Finally, work on lazy training clarified that fixed-feature (kernel) views fail to capture genuine feature learning dynamics, pointing to the need for models and tools that explicitly quantify how features emerge from data–model interaction.
Together these insights reveal a gap: we have strong unlabeled observables (disagreement) and rich qualitative accounts of features, but lack a unifying, feature-level mechanism linking them. The paper synthesizes these strands by introducing an interaction tensor to empirically expose which features are present in data and which are learned by different seeds, and by proposing a feature-learning framework that yields closed-form predictions for accuracy and agreement—thereby mechanistically explaining GDE and related phenomena.

---

*Analysis generated on: 2026-01-06T10:22:26.348357*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
