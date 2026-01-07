# Prior Work Analysis Report

## Target Paper

**Title:** RegMix: Data Mixture as Regression for Language Model Pre-training

**Conference:** ICLR 2025 (spotlight)

**Authors:** Qian Liu, Xiaosen Zheng, Niklas Muennighoff, Guangtao Zeng, Longxu Dou, Tianyu Pang, Jing Jiang, Min Lin

**Keywords:** language model pre-training, data mixture, regression

**Abstract:** 
> The data mixture for large language model pre-training significantly impacts performance, yet how to determine an effective mixture remains unclear. We propose RegMix to automatically identify a high-performing data mixture by formulating it as a regression task. RegMix trains many small models on diverse data mixtures, uses regression to predict performance of unseen mixtures, and applies the best predicted mixture to train a large-scale model with orders of magnitude more compute. To empirical...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Pile: An 800GB Dataset of Diverse Text for Language Modeling** (2021)
- *Authors:* Leo Gao et al.
- *Direct Connection:* By formalizing LM pretraining as a mixture over many heterogeneous sources, The Pile established the multi-source mixture setting that RegMix treats as a regression over mixture weights.

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Jordan Hoffmann et al.
- *Direct Connection:* Chinchilla’s compute-optimal scaling results justify RegMix’s design of using small, cheap runs to guide choices for longer, larger-scale training, assuming systematic cross-scale regularities that a regression model can exploit.

### 💡 Inspiration

**Tensor Programs V: Tuning Large Neural Networks via μ-Transfer** (2022)
- *Authors:* Greg Yang et al.
- *Direct Connection:* μ-Transfer’s core insight—that hyperparameters tuned on small models can reliably transfer to large models—directly inspires RegMix’s strategy of training many small proxy models to learn a predictor that selects mixtures for much larger-scale training.

### 🔍 Gap Identification

**LLaMA: Open and Efficient Foundation Language Models** (2023)
- *Authors:* Hugo Touvron et al.
- *Direct Connection:* LLaMA highlighted that heuristic, human-chosen data mixture weights critically affect performance, motivating RegMix’s aim to automate mixture selection and outperform manual recipes across scales.

### 📊 Baseline

**DoReMi: Optimizing Data Mixtures Makes Language Models Better** (2023)
- *Authors:* Anonymous et al.
- *Direct Connection:* RegMix directly targets the same problem as DoReMi—automatically finding effective pretraining data mixtures—but replaces DoReMi’s online mixture-weight optimization with a surrogate regression trained on many small-scale mixture runs to predict the best unseen mixture.

### 🔗 Related Problem

**Fast Bayesian Optimization of Machine Learning Hyperparameters on Large Datasets (FABOLAS)** (2017)
- *Authors:* Aaron Klein et al.
- *Direct Connection:* FABOLAS shows that low-fidelity evaluations (e.g., smaller datasets) can train a surrogate to predict high-fidelity performance, a principle RegMix adapts by fitting a regression surrogate from small-scale mixture runs to forecast performance of unseen mixtures at large scale.

---

## Synthesis: How Prior Work Led to This Paper

A body of work established that large language model pretraining typically draws from heterogeneous corpora, with The Pile explicitly framing pretraining as a mixture over diverse sources and thereby defining mixture weights as a key design variable. LLaMA, while relying on heuristic composition across web, code, books, and scholarly text, underscored that the precise mixture critically affects final performance, revealing the fragility and manual nature of existing data recipes. Beyond data, scaling studies such as Chinchilla showed stable cross-scale regularities that permit principled decisions about compute and data, suggesting that choices made at small scale can guide large-scale outcomes. In parallel, μ-Transfer demonstrated that hyperparameters tuned on small proxy models can transfer faithfully to much larger models, providing a concrete mechanism for leveraging small-scale experiments to inform large-scale training. From an optimization standpoint, FABOLAS established that low-fidelity evaluations can train a surrogate predictor for high-fidelity performance, legitimizing surrogate-based search under resource constraints. Finally, DoReMi directly tackled mixture optimization for LM pretraining via online weight updates, empirically validating that automated mixture search can beat human selection.
Together these works expose a clear opportunity: automate mixture selection using many inexpensive, small-scale trials while ensuring decisions transfer to large-scale training. The current paper synthesizes these insights by casting data mixture selection as supervised regression, fitting a surrogate on numerous small-model runs to predict performance for unseen mixtures, and then scaling the best predicted mixture to large compute—achieving automation that addresses LLaMA’s heuristic gap and rivals DoReMi with a simpler, more scalable surrogate approach.

---

*Analysis generated on: 2026-01-06T16:43:37.636278*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
