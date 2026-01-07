# Prior Work Analysis Report

## Target Paper

**Title:** Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI

**Conference:** ICLR 2024 (spotlight)

**Authors:** Weibang Jiang, Liming Zhao, Bao-liang Lu

**Keywords:** EEG, brain-computer interface, representation learning

**Abstract:** 
> The current electroencephalogram (EEG) based deep learning models are typically designed for specific datasets and applications in brain-computer interaction (BCI), limiting the scale of the models and thus diminishing their perceptual capabilities and generalizability. Recently, Large Language Models (LLMs) have achieved unprecedented success in text processing, prompting us to explore the capabilities of Large EEG Models (LEMs). We hope that LEMs can break through the limitations of different ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**BEETL: A Benchmark for EEG Transfer Learning** (2021)
- *Authors:* Dimitrios K. I. Kostas et al.
- *Direct Connection:* BEETL formalized cross-subject and cross-dataset EEG transfer and highlighted heterogeneity in channels, lengths, and sampling rates, directly motivating the need for a unified foundation model that this work proposes.

### 💡 Inspiration

**A Transformer-based Framework for Multivariate Time Series Representation Learning** (2021)
- *Authors:* Anastasia Zerveas et al.
- *Direct Connection:* This work’s transformer encoder design for multivariate time series informs the architecture adapted here, which augments it with EEG-specific spatial/positional encoding to accommodate diverse montages.

**Self-supervised representation learning from electroencephalography signals** (2021)
- *Authors:* Alexandre Banville et al.
- *Direct Connection:* By showing that contrastive/self-supervised objectives and EEG-specific augmentations boost downstream performance, this paper catalyzes the shift toward large-scale unsupervised EEG pretraining adopted here.

### 🔍 Gap Identification

**EEGNet: A Compact Convolutional Neural Network for EEG-based Brain–Computer Interfaces** (2018)
- *Authors:* Vernon J. Lawhern et al.
- *Direct Connection:* EEGNet exemplifies highly task-specific architectures that struggle to generalize across datasets and montages, a limitation this work addresses by learning dataset-agnostic EEG representations.

### 📊 Baseline

**BENDR: BErt-inspired Neural Data Representations for EEG** (2021)
- *Authors:* Dimitrios K. I. Kostas et al.
- *Direct Connection:* BENDR established transformer-based self-supervised pretraining for EEG but assumed fixed channel layouts and task settings, which this paper explicitly generalizes by introducing a unified, montage-agnostic pretraining framework over heterogeneous datasets.

### 🔧 Extension

**Masked Autoencoders Are Scalable Vision Learners** (2022)
- *Authors:* Kaiming He et al.
- *Direct Connection:* The core pretraining strategy extends MAE-style masked reconstruction to multichannel EEG with electrode-aware tokenization and variable-length handling to learn generic representations at scale.

### 🔗 Related Problem

**TS2Vec: Towards Universal Representation Learning for Time Series** (2022)
- *Authors:* Zhiyuan Yang Yue et al.
- *Direct Connection:* TS2Vec’s demonstration that universal time-series embeddings transfer across tasks directly motivates scaling unsupervised pretraining to EEG for broad downstream BCI tasks.

---

## Synthesis: How Prior Work Led to This Paper

Early attempts to generalize EEG representations at scale emerged with BENDR, which introduced transformer-based self-supervised pretraining on large EEG corpora, demonstrating cross-task transfer but presuming fixed channel layouts and relatively homogeneous data. BEETL codified the transfer-learning problem in EEG, surfacing persistent heterogeneity—mismatched electrodes, sampling rates, and trial lengths—that undermines broad generalization. Parallel advances in self-supervision provided the methodological backbone: Masked Autoencoders showed that reconstructive masked modeling yields scalable, data-efficient pretraining; the Transformer-based framework for multivariate time series established viable encoder designs and patching schemes for sensor data; and TS2Vec revealed that universal time-series embeddings can transfer across diverse tasks with minimal supervision. Within EEG specifically, Banville et al. demonstrated that contrastive/self-supervised objectives with domain-tailored augmentations improve downstream BCI performance, underscoring the promise of unsupervised pretraining. Meanwhile, EEGNet remained a compact, task-specific baseline, exemplifying strong within-dataset accuracy yet limited cross-dataset robustness. Together, these works expose an opportunity: combine the scalability and masked-modeling efficiency of MAE with time-series Transformers, while directly addressing EEG’s dataset heterogeneity identified by BEETL and the fixed-montage constraints evident in BENDR. The natural next step is a unified, montage-agnostic pretraining pipeline over massive, diverse EEG corpora that learns generic representations transferable to many BCI tasks, surpassing task-specific CNNs like EEGNet and building on the self-supervised insights from Banville, MAE, TST, and TS2Vec.

---

*Analysis generated on: 2026-01-06T11:51:27.593076*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
