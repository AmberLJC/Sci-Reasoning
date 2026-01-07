# Prior Work Analysis Report

## Target Paper

**Title:** Quick-Tune: Quickly Learning Which Pretrained Model to Finetune and How

**Conference:** ICLR 2024 (oral)

**Authors:** Sebastian Pineda Arango, Fabio Ferreira, Arlind Kadra, Frank Hutter, Josif Grabocka

**Keywords:** Finetuning, pretrained model hubs, transfer learning, hyperparameter optimization, meta-learning

**Abstract:** 
> With the ever-increasing number of pretrained models, machine learning practitioners are continuously faced with which pretrained model to use, and how to finetune it for a new dataset. In this paper, we propose a methodology that jointly searches for the optimal pretrained model and the hyperparameters for finetuning it. Our method transfers knowledge about the performance of many pretrained models with multiple hyperparameter configurations on a series of datasets. To this aim, we evaluated ov...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Auto-WEKA: Combined Selection and Hyperparameter Optimization of Machine Learning Algorithms** (2013)
- *Authors:* Chris Thornton et al.
- *Direct Connection:* Quick-Tune adopts the CASH formulation introduced by Auto-WEKA—jointly selecting an algorithm/model and its hyperparameters—and instantiates it for choosing among pretrained models while tuning their finetuning hyperparameters.

### 💡 Inspiration

**Efficient and Robust Automated Machine Learning** (2015)
- *Authors:* Matthias Feurer et al.
- *Direct Connection:* Quick-Tune borrows Auto-sklearn’s idea of transferring meta-knowledge across datasets to warm-start search, extending it from classical ML pipelines to deep finetuning over a hub of pretrained models.

**Freeze-Thaw Bayesian Optimization** (2014)
- *Authors:* Kevin Swersky et al.
- *Direct Connection:* Quick-Tune leverages the core insight of using partially observed learning curves to guide resource allocation, replacing Freeze-Thaw’s BO with a meta-learned predictor specialized to finetuning.

### 🔍 Gap Identification

**LogME: Practical Assessment of Pre-trained Models for Transfer Learning** (2021)
- *Authors:* Kaichao You et al.
- *Direct Connection:* Quick-Tune addresses LogME’s limitation of zero-shot model scoring by exploiting short finetuning learning curves and jointly optimizing hyperparameters to select both the model and its finetuning regime.

### 📊 Baseline

**BOHB: Robust and Efficient Hyperparameter Optimization at Scale** (2018)
- *Authors:* Stefan Falkner et al.
- *Direct Connection:* BOHB serves as the multi-fidelity HPO baseline that Quick-Tune surpasses by augmenting early-stopping resource allocation with a meta-learned performance model and the additional model-selection dimension.

### 🔧 Extension

**Speeding up Automatic Hyperparameter Optimization of Deep Neural Networks by Extrapolation of Learning Curves** (2015)
- *Authors:* Dominik Domhan et al.
- *Direct Connection:* Quick-Tune extends learning-curve extrapolation by training a meta-learned gray-box predictor on finetuning curves across many models and datasets to forecast final accuracy from early epochs.

---

## Synthesis: How Prior Work Led to This Paper

The CASH paradigm established by Auto-WEKA defined the joint problem of selecting an algorithm while optimizing its hyperparameters, showing that treating model choice and hyperparameter tuning as one search yields superior solutions. Auto-sklearn added a crucial ingredient: transferring meta-knowledge across datasets to warm-start search, using prior runs to inform new tasks. In parallel, learning-curve–based gray-box methods demonstrated that partial training trajectories are predictive of final performance: Domhan et al. modeled deep nets’ curves to extrapolate outcomes, while Freeze-Thaw Bayesian optimization operationalized the same idea by pausing and resuming runs based on early progress. BOHB unified Bayesian optimization with Hyperband-style early stopping to allocate resources efficiently using early performance signals, establishing a strong multi-fidelity HPO baseline. In transfer learning, LogME provided a practical zero-shot score to rank pretrained models for a target dataset without training, but by design ignored the impact of finetuning hyperparameters and training dynamics. Together, these works indicated that (i) joint model selection and HPO is the right formulation, (ii) meta-knowledge across datasets can accelerate search, and (iii) early learning curves carry powerful predictive signals, yet transferability metrics failed to incorporate finetuning and HPO methods ignored the choice among pretrained models. Quick-Tune naturally synthesizes these strands by meta-learning a gray-box performance predictor from large-scale finetuning learning curves to rapidly co-decide which pretrained model to use and how to tune it on a new dataset.

---

*Analysis generated on: 2026-01-06T19:21:11.999646*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
