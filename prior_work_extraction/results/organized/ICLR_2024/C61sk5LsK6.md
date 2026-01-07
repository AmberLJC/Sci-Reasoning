# Prior Work Analysis Report

## Target Paper

**Title:** InfoBatch: Lossless Training Speed Up by Unbiased Dynamic Data Pruning

**Conference:** ICLR 2024 (oral)

**Authors:** Ziheng Qin, Kai Wang, Zangwei Zheng, Jianyang Gu, Xiangyu Peng, xu Zhao Pan, Daquan Zhou, Lei Shang, Baigui Sun, Xuansong Xie, Yang You

**Keywords:** Dynamic Data Pruning; Training acceleration

**Abstract:** 
> Data pruning aims to obtain lossless performances with less overall cost. A common approach is to filter out samples that make less contribution to the training. This could lead to gradient expectation bias compared to the original data. To solve this problem, we propose InfoBatch, a novel framework aiming to achieve lossless training acceleration by unbiased dynamic data pruning. Specifically, InfoBatch
randomly prunes a portion of less informative samples based on the loss distribution and res...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Not All Samples Are Equal: Deep Learning with Importance Sampling** (2018)
- *Authors:* Angelos Katharopoulos et al.
- *Direct Connection:* InfoBatch adopts the inverse-probability weighting principle from importance sampling to rescale gradients after non-uniform pruning so that the expected gradient remains unbiased.

### 💡 Inspiration

**An Empirical Study of Example Forgetting During Deep Neural Network Learning** (2019)
- *Authors:* Elena Toneva et al.
- *Direct Connection:* The finding that many ‘unforgettable’ examples contribute little later in training directly motivates InfoBatch’s focus on pruning low-informative (typically low-loss) samples.

**Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics** (2020)
- *Authors:* Swabha Swayamdipta et al.
- *Direct Connection:* Cartography’s use of loss/consistency dynamics to distinguish easy versus informative samples informs InfoBatch’s loss-distribution-driven policy for identifying prune-worthy examples.

### 🔍 Gap Identification

**Training Region-based Object Detectors with Online Hard Example Mining** (2016)
- *Authors:* Abhinav Shrivastava et al.
- *Direct Connection:* By showing that deterministic top-loss selection accelerates training but biases learning, OHEM motivates InfoBatch’s randomized pruning and reweighting to avoid gradient expectation bias.

### 📊 Baseline

**GradMatch: Gradient Matching based Data Subset Selection for Efficient Deep Learning** (2021)
- *Authors:* Saurabh Killamsetty et al.
- *Direct Connection:* GradMatch’s goal of selecting subsets whose gradients approximate the full-data gradient is the primary baseline that InfoBatch improves upon by guaranteeing unbiasedness via stochastic pruning and scaling.

### 🔗 Related Problem

**GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning** (2021)
- *Authors:* Saurabh Killamsetty et al.
- *Direct Connection:* GLISTER’s bilevel subset selection highlights the accuracy–efficiency trade-off of static pruning, which InfoBatch overcomes by dynamic, per-iteration pruning with unbiased gradient estimates.

---

## Synthesis: How Prior Work Led to This Paper

Importance sampling for deep networks established that non-uniformly chosen training examples can be made statistically sound by inverse-probability weighting, ensuring that the stochastic gradient remains an unbiased estimate of the full gradient. Online Hard Example Mining then popularized loss-driven selection, but its deterministic top-k filtering introduced training bias by over-focusing on hard samples. Work on example dynamics deepened this picture: example forgetting revealed that many samples become ‘unforgettable’ and add little learning signal later, while dataset cartography used loss and confidence trajectories to map easy, ambiguous, and hard regions—showing that low-loss, stable points are typically less informative for continued updates. In parallel, subset selection approaches such as GradMatch sought to match full-dataset gradients with small subsets, and GLISTER formalized generalization-driven selection via bilevel optimization, but both incurred optimization overheads and, being static or episodic, risked selection bias or loss of fidelity to full-data training.
Together, these lines suggested a natural opportunity: prune predominantly low-information examples during training, but retain the statistical guarantees of full-data SGD. By combining loss-dynamics signals to identify low-informative samples with the inverse-probability weighting principle from importance sampling, and by making pruning randomized rather than deterministic, the current work arrives at a plug-and-play, architecture-agnostic scheme that preserves unbiased gradient expectations while delivering consistent, lossless speedups across tasks.

---

*Analysis generated on: 2026-01-06T20:10:35.981422*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
