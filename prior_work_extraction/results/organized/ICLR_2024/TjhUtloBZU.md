# Prior Work Analysis Report

## Target Paper

**Title:** Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Hao Chen, Jindong Wang, Ankit Shah, Ran Tao, Hongxin Wei, Xing Xie, Masashi Sugiyama, Bhiksha Raj

**Keywords:** Pre training, Noisy model learning, Label noise, Noise mitigation

**Abstract:** 
> Pre-training on large-scale datasets and then fine-tuning on downstream tasks have become a standard practice in deep learning. However, pre-training data often contain label noise that may adversely affect the generalization of the model. This paper aims to understand the nature of noise in pre-training datasets and to mitigate its impact on downstream tasks. More specifically, through extensive experiments of supervised pre-training models on synthetic noisy ImageNet-1K and YFCC15M datasets, w...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**WebVision Database: Visual Learning and Understanding from Web Data** (2017)
- *Authors:* Wen Li et al.
- *Direct Connection:* WebVision formalized supervised learning from large-scale web data with substantial label noise, providing the pre-training-with-noise setting and motivation that this work systematically studies for transfer.

**WILDS: A Benchmark of in-the-Wild Distribution Shifts** (2021)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* WILDS crystallized the ID vs OOD generalization framework under distribution shift, which this work adopts to disentangle how pre-training noise differentially impacts in-domain versus out-of-domain transfer.

**Do Better ImageNet Models Transfer Better?** (2019)
- *Authors:* Simon Kornblith et al.
- *Direct Connection:* This paper established standardized transfer evaluation from ImageNet pre-training to diverse downstream tasks, providing the evaluation paradigm this work extends to analyze the effect of label noise in pre-training.

### 💡 Inspiration

**Tent: Fully Test-Time Adaptation by Entropy Minimization** (2021)
- *Authors:* Dequan Wang et al.
- *Direct Connection:* The lightweight, black-box adaptation principle of TENT—updating only a small set of affine parameters without accessing source data—directly inspired NMTune’s design for post-hoc feature correction of noisy pre-trained models.

### 🔍 Gap Identification

**Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels** (2018)
- *Authors:* Bo Han et al.
- *Direct Connection:* Co-teaching exemplifies noise-robust training that requires intervention during training on noisy data, a limitation this work addresses by proposing a downstream, black-box mitigation method that operates after pre-training.

### 🔧 Extension

**Deep CORAL: Correlation Alignment for Deep Domain Adaptation** (2016)
- *Authors:* Baochen Sun et al.
- *Direct Connection:* NMTune adopts the same core idea of an affine feature-space transformation as Deep CORAL’s linear alignment, extending it from matching domain statistics to explicitly correcting the feature distortions induced by noisy pre-training.

---

## Synthesis: How Prior Work Led to This Paper

Learning from web-scale labeled data introduced the practical reality of noisy supervision, with WebVision defining a benchmark and setting in which large datasets contain pervasive label errors. Robust training under such noise, as typified by Co-teaching, showed that selectively trusting samples can stabilize learning—yet these methods intervene during training and assume access to the noisy corpus. Separately, transfer evaluation was systematized by work demonstrating how pre-trained representations carry over to many tasks, and WILDS formalized in-domain versus out-of-domain performance under distribution shift, providing a lens to assess when transfer succeeds or fails. On the representation side, Deep CORAL revealed that simple affine transformations of features can effectively align distributions by matching second-order statistics, while TENT demonstrated that small, black-box updates to affine components can adapt models at test time without revisiting source data.
Taken together, these threads expose an opportunity: leverage the power of affine feature-space adjustments and black-box adaptation to mitigate the specific distortions that noisy pre-training imprints on representations, and evaluate the outcome through the ID/OOD lens. Building on CORAL’s linear alignment idea and TENT’s lightweight adaptation mechanism—while addressing the training-time dependency of traditional noisy-label methods—the current work naturally emerges as a post-hoc, black-box approach that reshapes feature geometry to recover OOD transfer without re-training on the pre-training data.

---

*Analysis generated on: 2026-01-06T09:34:40.635337*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
