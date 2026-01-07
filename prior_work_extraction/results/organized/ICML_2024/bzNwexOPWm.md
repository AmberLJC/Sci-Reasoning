# Prior Work Analysis Report

## Target Paper
**Title:** bzNwexOPWm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**An Empirical Study of Example Forgetting during Deep Neural Network Learning** (2019)
- *Authors:* Ilia Toneva et al.
- *Connection:* Introduced the notion of example-level forgetting events and operationalized how to detect 'forgotten' training examples, which this paper directly builds on by forecasting which upstream examples will be forgotten after an update.

### 💡 Inspiration

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Connection:* Provided the core idea of predicting how parameter updates induced by one example affect the loss on other examples; the present work adopts this causal viewpoint to forecast harm (forgetting) on upstream examples caused by online corrections.

**Online Continual Learning with Maximal Interfered Retrieval** (2019)
- *Authors:* Rahaf Aljundi et al.
- *Connection:* Proposed selecting replay items whose loss would increase most under a new update by approximating interference; this paper generalizes the idea from heuristic selection to explicit forecasting of which upstream examples will be forgotten to drive targeted replay.

### 🔍 Gap Identification

**Gradient-based Sample Selection for Online Continual Learning** (2019)
- *Authors:* Rahaf Aljundi et al.
- *Connection:* Demonstrated gradient-similarity heuristics for replay selection but with limited controllability and reliance on local estimates; the current work addresses this gap by learning predictors that forecast forgotten upstream examples, reducing variance and improving controllability.

### 📊 Baseline

**Tiny Episodic Memories in Continual Learning** (2019)
- *Authors:* Arslan Chaudhry et al.
- *Connection:* Popularized reservoir-style/random replay as a strong, simple baseline in continual learning; this paper explicitly shows such random replay is high-variance and improves upon it by forecasting and replaying specifically the examples predicted to be forgotten.

### 🔧 Extension

**Estimating Training Data Influence by Tracing Gradient Descent (TracIn)** (2020)
- *Authors:* Garima Pruthi et al.
- *Connection:* Showed that inner products of gradients across checkpoints can approximate influence; the paper’s black-box classifier that uses inner-product signals to predict which pretraining instances will be forgotten is a direct adaptation of this influence-as-inner-product principle.

### 🔗 Related Problem

**Gradient Episodic Memory for Continual Learning** (2017)
- *Authors:* David Lopez-Paz et al.
- *Connection:* Established gradient-conflict (inner-product) signals as indicators of interference and forgetting in continual learning, which underpins this paper’s use of inner-product-based criteria to forecast forgetting and guide replay.

---

## Synthesis

The paper’s core contribution—forecasting which upstream examples a language model will forget after an update—emerges from a clear lineage in example-level forgetting and influence estimation. Toneva et al. established the very construct of example forgetting events, giving this work its target variable: identifying forgotten examples. Koh and Liang provided the causal lens for anticipating how an update driven by one example impacts the loss on others, which this paper repurposes to forecast harm from online corrections to pretraining data points. Building on practical influence estimation, TracIn showed that inner products of gradients across checkpoints approximate influence, directly inspiring the paper’s black-box inner-product classifier for predicting forgetting. In continual learning, Lopez-Paz and Ranzato’s GEM framed gradient conflicts (via inner products) as signals of interference, a conceptual backbone for using inner-product signals to anticipate forgetting. Aljundi’s MIR and gradient-based sample selection further demonstrated that predicting which samples will suffer maximal interference can guide replay; the present work extends these heuristics into a learned forecasting framework that explicitly predicts forgotten upstream examples, thereby improving controllability and reducing variance. Finally, Chaudhry et al. popularized random/ reservoir replay as a baseline; this paper’s results and motivation directly respond to its limitations by replacing unguided replay with forecasts that prioritize at-risk upstream examples.

---
*Generated: 2026-01-06T23:09:26.434092*
