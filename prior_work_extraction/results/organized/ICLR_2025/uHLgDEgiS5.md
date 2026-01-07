# Prior Work Analysis Report

## Target Paper

**Title:** Capturing the Temporal Dependence of Training Data Influence

**Conference:** ICLR 2025 (oral)

**Authors:** Jiachen T. Wang, Dawn Song, James Zou, Prateek Mittal, Ruoxi Jia

**Keywords:** data attribution

**Abstract:** 
> Traditional data influence estimation methods, like influence function, assume that learning algorithms are permutation-invariant with respect to training data. However, modern training paradigms—especially for foundation models using stochastic algorithms and non-convergent, multi-stage curricula—are sensitive to data ordering, thus violating this assumption. This mismatch renders influence functions inadequate for answering some critical questions in current machine learning: How can we differ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Curriculum Learning** (2009)
- *Authors:* Yoshua Bengio et al.
- *Direct Connection:* By showing that ordering and staging of training data materially affect learned models, curriculum learning provides the foundational rationale for defining influence that is conditional on the precise data sequence and training stage.

### 💡 Inspiration

**Estimating Training Data Influence by Tracing Gradient Descent** (2020)
- *Authors:* Garima Pruthi et al.
- *Direct Connection:* By summing gradient inner-products across checkpoints, TracIn connected data influence to the optimization path, inspiring the formalization here of a principled, leave-one-out influence that is explicitly tied to a specific training iteration along the actual trajectory.

**An Empirical Study of Example Forgetting During Deep Neural Network Learning** (2019)
- *Authors:* Mariya Toneva et al.
- *Direct Connection:* The discovery of per-example forgetting events across epochs evidences that an example’s effect is time-dependent, motivating an influence measure that records when during training a point exerts its impact via trajectory-specific LOO.

### 🔍 Gap Identification

**Data Shapley: Equitable Valuation of Data for Machine Learning** (2019)
- *Authors:* Amirata Ghorbani et al.
- *Direct Connection:* Data Shapley formulates data valuation as marginal contributions over permutations of a set, implicitly ignoring the temporal order in which data are encountered, a limitation the trajectory-specific LOO influence addresses by conditioning value on when a point appears during training.

**Representer Point Selection for Explaining Deep Neural Networks** (2018)
- *Authors:* Chih-Kuan Yeh et al.
- *Direct Connection:* Representer methods attribute predictions using a kernel at the final model snapshot, which fails to capture non-convergent, multi-stage dynamics, prompting a shift to an influence notion that accounts for the full training trajectory and specific iteration removal.

**Influence Functions in Deep Learning Are Fragile** (2021)
- *Authors:* Shubham Basu et al.
- *Direct Connection:* This work demonstrates that classical influence-function estimates are unstable for deep networks and SGD, underscoring the need for a trajectory- and order-aware leave-one-out influence that remains meaningful under modern training regimes.

### 📊 Baseline

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* This classic influence-function framework defines leave-one-out influence at a converged ERM solution under a permutation-invariant data assumption, whose breakdown under stochastic, order-sensitive training directly motivates replacing it with a trajectory-specific LOO definition conditioned on iteration and data order.

---

## Synthesis: How Prior Work Led to This Paper

Influence functions introduced a principled leave-one-out sensitivity for individual training points by differentiating the ERM optimum, but they presuppose a permutation-invariant dataset and a stable converged solution. TracIn reframed attribution through the optimization path, estimating influence by accumulating gradient inner-products across checkpoints, implicitly linking data effects to where the trajectory passes. Data Shapley cast data valuation as marginal contributions over permutations, a set-function view that treats order as irrelevant. Representer point selection attributed predictions via a final-layer kernel at a single trained snapshot, sidestepping the dynamics of how parameters evolved. Empirical studies of forgetting events showed examples can flip between learned and unlearned across epochs, indicating that the contribution of a point depends on when it is seen. Curriculum learning further established that staging and order systematically shape training outcomes. Finally, evidence that influence functions are fragile for deep nets trained with SGD highlighted the brittleness of static, end-of-training approximations.
Together, these works reveal a gap: existing attribution either ignores order, collapses dynamics to a final snapshot, or heuristically traces gradients without a leave-one-out semantics. The natural next step is to endow influence with an explicit dependence on the actual optimization path and the specific iteration at which a point appears. By formalizing trajectory-specific leave-one-out influence, the current work synthesizes path-aware tracing with principled LOO semantics, addressing the instability of classical IF and the order-insensitivity of Shapley/representer approaches while capturing time-resolved effects that forgetting and curricula make salient.

---

*Analysis generated on: 2026-01-06T07:57:57.831924*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
