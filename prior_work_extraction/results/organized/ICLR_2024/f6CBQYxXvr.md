# Prior Work Analysis Report

## Target Paper

**Title:** Project and Probe: Sample-Efficient Adaptation by Interpolating Orthogonal Features

**Conference:** ICLR 2024 (spotlight)

**Authors:** Annie S Chen, Yoonho Lee, Amrith Setlur, Sergey Levine, Chelsea Finn

**Keywords:** distribution-shift robustness, fine-tuning, adaptation, transfer learning

**Abstract:** 
> Transfer learning with a small amount of target data is an effective and common approach to adapting a pre-trained model to distribution shifts. In some situations, target data labels may be expensive to obtain, so we may only have access to a limited number of target data points. To make the most of a very small target dataset, we propose a lightweight, sample-efficient approach that learns a diverse set of features and adapts to a target distribution by interpolating these features. Our approa...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**The Use of Multiple Measurements in Taxonomic Problems** (1936)
- *Authors:* R. A. Fisher
- *Direct Connection:* Pro^2 adopts the core LDA idea of learning a low-dimensional set of discriminative, mutually orthogonal directions and adapts it to pretrained embeddings by training an orthonormal projection with supervised source labels before reweighting on the target.

**Do Better ImageNet Models Transfer Better?** (2019)
- *Authors:* Kornblith et al.
- *Direct Connection:* Building on the finding that linear probes on fixed representations are strong and sample-efficient transfer baselines, Pro^2 keeps linear-probe adaptation but first reshapes the representation via an orthogonal, label-predictive projection to improve probe efficiency under shift.

**WILDS: A Benchmark of in-the-Wild Distribution Shifts** (2021)
- *Authors:* Koh et al.
- *Direct Connection:* WILDS provides the distribution-shift setting and benchmarks that frame the paper’s target problem—adapting with very limited labeled target data—against which Pro^2’s sample-efficient adaptation is evaluated.

### 💡 Inspiration

**Partial Least Squares** (1984)
- *Authors:* Herman Wold
- *Direct Connection:* Pro^2 borrows PLS’s insight of extracting multiple orthogonal latent components that are directly predictive of labels, then linearly combining them, by learning source-supervised, orthogonal feature directions that can be recombined with few labeled target samples.

**Model Soups: Averaging Weights of Multiple Fine-Tuned Models Improves Accuracy Without Extra Inference Cost** (2022)
- *Authors:* Wortsman et al.
- *Direct Connection:* Pro^2 is motivated by the observation that interpolating diverse solutions yields robust generalization, operationalizing this in feature space by constructing diverse (orthogonal) source-predictive directions and interpolating them with a target linear classifier.

### 📊 Baseline

**Parameter-Efficient Transfer Learning for NLP** (2019)
- *Authors:* Houlsby et al.
- *Direct Connection:* Adapters serve as a primary parameter-efficient fine-tuning baseline that relies on target supervision, which Pro^2 explicitly aims to outperform in label-scarce regimes by freezing the encoder and only reweighting orthogonal source-trained features with a small target set.

### 🔗 Related Problem

**Editing Models with Task Arithmetic** (2023)
- *Authors:* Ilharco et al.
- *Direct Connection:* Echoing task arithmetic’s linear composition of task-specific directions in weight space, Pro^2 composes task-relevant orthogonal directions in feature space to represent and adapt to shifted target tasks via simple linear recombination.

---

## Synthesis: How Prior Work Led to This Paper

Classical discriminative projection methods established that compact sets of orthogonal directions could capture task-relevant variation: Fisher’s linear discriminant analysis explicitly seeks orthogonal, low-dimensional discriminative axes, while partial least squares constructs orthogonal latent components that are directly predictive of labels and designed to be linearly recombined. In transfer learning, Kornblith et al. showed that linear probes on frozen representations are strong and sample-efficient, positioning simple linear adaptation as a robust default. Parameter-efficient fine-tuning via adapters demonstrated that small, learnable modules enable transfer with limited compute but still rely on substantial target supervision. Meanwhile, model soups revealed that interpolation across diverse solutions reliably improves out-of-distribution generalization, and task arithmetic showed that task-specific directions can be linearly composed to achieve new capabilities. The WILDS benchmark codified the practical scenario of adapting to real-world distribution shifts with scarce target labels.
Together, these works suggest a pathway: build multiple, diverse, predictive directions that can be linearly recombined in the target domain. The orthogonal, supervised-components perspective from LDA/PLS dovetails with the linear-probe paradigm to promise sample-efficient adaptation, while insights from model interpolation and task composition argue for constructing diversity and then reweighting rather than relearning. This naturally leads to learning an orthonormal, source-supervised projection to produce diverse predictive features, then using a tiny target set to interpolate among them with a linear classifier, addressing adapters’ label-hungry adaptation and improving robustness under shift.

---

*Analysis generated on: 2026-01-06T14:30:01.975592*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
