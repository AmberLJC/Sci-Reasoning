# Prior Work Analysis Report

## Target Paper

**Title:** ModernTCN: A Modern Pure Convolution Structure for General Time Series Analysis

**Conference:** ICLR 2024 (spotlight)

**Authors:** Luo donghao, wang xue

**Keywords:** Time Series Analysis, Deep Learning

**Abstract:** 
> Recently, Transformer-based and MLP-based models have emerged rapidly and
won dominance in time series analysis. In contrast, convolution is losing steam
in time series tasks nowadays for inferior performance. This paper studies the
open question of how to better use convolution in time series analysis and makes
efforts to bring convolution back to the arena of time series analysis. To this end,
we modernize the traditional TCN and conduct time series related modifications
to make it more suitab...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**WaveNet: A Generative Model for Raw Audio** (2016)
- *Authors:* Aaron van den Oord et al.
- *Direct Connection:* The core idea of stacking causal dilated convolutions and gated temporal blocks to capture long dependencies originates from WaveNet, which is adapted and generalized in ModernTCN’s convolutional sequence modeling backbone.

### 💡 Inspiration

**A ConvNet for the 2020s** (2022)
- *Authors:* Zhuang Liu et al.
- *Direct Connection:* ConvNeXt’s design rules—depthwise separable large‑kernel convolutions, inverted bottlenecks, and simplified activation/normalization—are transplanted to 1D to modernize TCN blocks in ModernTCN.

**Scaling Up Your Kernels to 31x31: Revisiting Large Kernel Design in CNNs** (2022)
- *Authors:* Xiangyu Ding et al.
- *Direct Connection:* Evidence that very large kernels can approximate global receptive fields efficiently motivates ModernTCN’s use of large 1D temporal kernels to capture long‑range dependencies without attention.

### 🔍 Gap Identification

**Are Transformers Effective for Time Series Forecasting?** (2023)
- *Authors:* Ailing Zeng et al.
- *Direct Connection:* By showing simple per‑channel linear temporal filters (DLinear) can outperform heavy Transformers, this work exposes the over‑complexity gap that ModernTCN addresses with lightweight, pure convolutional temporal operators.

### 📊 Baseline

**A Time Series is Worth 64 Words: Long-term Forecasting with Transformers** (2023)
- *Authors:* Yue Nie et al.
- *Direct Connection:* PatchTST’s channel‑independent patching and decoupling of temporal vs. channel mixing form a primary SOTA baseline and inspire ModernTCN’s depthwise temporal filtering plus pointwise channel mixing strategy.

**TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis** (2023)
- *Authors:* Haixu Wu et al.
- *Direct Connection:* TimesNet established a strong general‑purpose time‑series benchmark across tasks, providing the key CNN/MLP baseline that ModernTCN aims to surpass while retaining convolutional efficiency.

### 🔧 Extension

**An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling** (2018)
- *Authors:* Shaojie Bai et al.
- *Direct Connection:* ModernTCN directly upgrades the TCN’s causal, dilated residual temporal convolutions by replacing its plain conv blocks with modern large‑kernel depthwise separable designs and refined normalization to improve long‑range modeling and efficiency.

---

## Synthesis: How Prior Work Led to This Paper

Causal, dilated temporal convolution for sequence modeling was crystallized by TCN, which demonstrated that deep residual stacks of dilated 1D convolutions can rival recurrent models on long sequences, albeit with plain small‑kernel blocks and standard activations. This builds on WaveNet’s insight that stacked causal dilations and gating efficiently capture long‑range dependencies without recurrence. In parallel, ConvNeXt codified a set of modern CNN design principles—depthwise separable large‑kernel convolutions, inverted bottlenecks, and streamlined normalization/activation—that lift convolutional capacity while preserving efficiency. Large‑kernel studies such as RepLKNet showed that very wide kernels can approximate global context competitively with attention, suggesting a path to long‑range modeling via purely convolutional receptive fields. On the time‑series front, PatchTST revealed that channel‑independent temporal processing and patching are crucial for strong forecasting, advocating a separation between temporal filtering and channel mixing. TimesNet established a general‑purpose benchmark across multiple time‑series tasks using convolutional priors, setting the bar for efficiency and versatility. Meanwhile, DLinear exposed that simple per‑channel temporal filters can outperform heavy Transformers, highlighting the potential of lightweight operators. Together these works suggest that a TCN‑style causal, dilated backbone, if refactored with modern depthwise, large‑kernel design and explicit decoupling of temporal and channel mixing, could reclaim state of the art across diverse time‑series tasks. ModernTCN synthesizes these insights by retrofitting TCN with ConvNeXt/RepLKNet‑inspired large‑kernel depthwise temporal convolutions and pointwise channel mixing, aligning with PatchTST’s channel independence and DLinear’s simplicity to achieve strong generalization and efficiency.

---

*Analysis generated on: 2026-01-06T12:10:12.356087*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
