# Prior Work Analysis Report

## Target Paper

**Title:** LiFT: Learning to Fine-Tune via Bayesian Parameter Efficient Meta Fine-Tuning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Minyoung Kim, Timothy Hospedales

**Keywords:** Bayesian methods, Parameter efficient fine-tuning, meta learning

**Abstract:** 
> We tackle the problem of parameter-efficient fine-tuning (PEFT) of a pre-trained large deep model on many different but related tasks. Instead of the simple but strong baseline strategy of task-wise independent fine-tuning, we aim to meta-learn the core shared information that can be used for unseen test tasks to improve the prediction performance further. That is, we propose a method for {\em learning-to-fine-tune} (LiFT). LiFT introduces a novel hierarchical Bayesian model that can be superior...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**LoRA: Low-Rank Adaptation of Large Language Models** (2022)
- *Authors:* Edward J. Hu et al.
- *Direct Connection:* LiFT treats task-specific LoRA parameters as random variables governed by a learned prior, directly building on LoRA’s low-rank adapter parameterization as the PEFT unit to be meta-learned.

### 💡 Inspiration

**Recasting Gradient-Based Meta-Learning as Hierarchical Bayes** (2018)
- *Authors:* Erin Grant et al.
- *Direct Connection:* LiFT operationalizes this paper’s insight that meta-learning is hierarchical Bayes by explicitly modeling a shared prior that regularizes task-specific LoRA modules.

### 🔍 Gap Identification

**Model Soup: Averaging weights of multiple fine-tuned models without retraining** (2022)
- *Authors:* Mitchell Wortsman et al.
- *Direct Connection:* LiFT targets the shortcoming of Model Soup’s weight averaging—which lacks task-aware uncertainty and a shared generative structure—by meta-learning a Bayesian prior that regularizes and predicts task adapters.

### 📊 Baseline

**Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks** (2017)
- *Authors:* Chelsea Finn et al.
- *Direct Connection:* LiFT is positioned to improve over MAML’s single shared initialization by instead learning a hierarchical Bayesian prior over adapter parameters that better captures task variability.

### 🔧 Extension

**Probabilistic Model-Agnostic Meta-Learning (PLATIPUS)** (2018)
- *Authors:* Chelsea Finn et al.
- *Direct Connection:* LiFT extends the probabilistic meta-learning paradigm of PLATIPUS by performing variational inference over task-level latent variables specifically for parameter-efficient LoRA adapters.

### 🔗 Related Problem

**AdapterFusion: Non-Destructive Task Composition for Transfer Learning** (2021)
- *Authors:* Jonas Pfeiffer et al.
- *Direct Connection:* LiFT addresses the limitation of AdapterFusion’s post-hoc composition by learning a generative prior that produces task-specific LoRA parameters for unseen tasks rather than fusing existing ones.

---

## Synthesis: How Prior Work Led to This Paper

Low-rank adaptation (LoRA) introduced a parameter-efficient mechanism to adapt large models by learning small low-rank updates, establishing a compact space of adapter parameters that can be attached or swapped per task. Model-Agnostic Meta-Learning (MAML) proposed learning a shared initialization to enable rapid task adaptation, providing a strong gradient-based meta-learning baseline for few-shot generalization. Recasting gradient-based meta-learning as hierarchical Bayes formalized that successful meta-learning methods implicitly learn a shared prior over task-specific parameters, highlighting that modeling task distributions and uncertainty is central. Probabilistic MAML (PLATIPUS) advanced this view by explicitly introducing task-level latent variables and variational inference, capturing multi-modality and uncertainty across tasks within a Bayesian meta-learning framework. AdapterFusion explored composing multiple lightweight adapters trained on different tasks, showing that adapter mixing can transfer knowledge but is typically post-hoc and lacks a learned generative structure. Model Soup demonstrated that simple weight averaging across fine-tuned models can yield robust performance, yet it does not encode task-specific uncertainty or a principled prior over parameter variations. Together, these works suggest a compact adapter parameterization, a meta-learning objective, and a Bayesian interpretation that emphasizes shared priors and uncertainty. The natural next step is to bring an explicit hierarchical Bayesian prior to the adapter space itself: instead of composing or averaging existing adapters, learn a shared latent structure that generates task-specific LoRA parameters and supports principled posterior inference for unseen tasks. This synthesis yields a method that unifies PEFT with Bayesian meta-learning to improve task transfer beyond independent fine-tuning or ad-hoc adapter mixing.

---

*Analysis generated on: 2026-01-06T11:20:25.725845*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
