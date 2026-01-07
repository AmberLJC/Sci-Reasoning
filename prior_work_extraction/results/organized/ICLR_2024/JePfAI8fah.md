# Prior Work Analysis Report

## Target Paper

**Title:** iTransformer: Inverted Transformers Are Effective for Time Series Forecasting

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yong Liu, Tengge Hu, Haoran Zhang, Haixu Wu, Shiyu Wang, Lintao Ma, Mingsheng Long

**Keywords:** Time Series Forecasting, Transformer

**Abstract:** 
> The recent boom of linear forecasting models questions the ongoing passion for architectural modifications of Transformer-based forecasters. These forecasters leverage Transformers to model the global dependencies over temporal tokens of time series, with each token formed by multiple variates of the same timestamp. However, Transformers are challenged in forecasting series with larger lookback windows due to performance degradation and computation explosion. Besides, the embedding for each temp...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting** (2021)
- *Authors:* Zhou et al.
- *Direct Connection:* Informer established the long-sequence time-series forecasting setting and datasets and tackled temporal attention scalability via sparsification, a setup that the inverted design revisits by eliminating long temporal attention altogether.

### 💡 Inspiration

**A Time Series is Worth 64 Words: Long-term Forecasting with Transformers (PatchTST)** (2023)
- *Authors:* Nie et al.
- *Direct Connection:* PatchTST’s demonstration that channel-independent processing and avoiding early variate mixing improves forecasting informs the iTransformer’s variate-centric design that treats variates as tokens and applies attention across them.

**TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis** (2023)
- *Authors:* Wu et al.
- *Direct Connection:* TimesNet’s evidence that channel-independent, variate-centric processing captures core temporal patterns motivates iTransformer’s choice to keep Transformer components unchanged while reorganizing them around variate-centric representations.

### 🔍 Gap Identification

**Are Transformers Effective for Time Series Forecasting?** (2023)
- *Authors:* Zeng et al.
- *Direct Connection:* This work’s finding that Transformer temporal attention degrades with longer lookbacks and that simple channel-wise linear models (e.g., DLinear) often outperform Transformers directly motivates inverting the modeling axis to avoid long temporal attention and recover scalability.

### 📊 Baseline

**FEDformer: Frequency Enhanced Decomposed Transformer for Long-term Series Forecasting** (2022)
- *Authors:* Zhou et al.
- *Direct Connection:* FEDformer reduces temporal attention cost with frequency-domain decomposition but still operates on temporal tokens mixing variates, a limitation the inverted approach addresses by operating directly over variate tokens.

### 🔗 Related Problem

**Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting** (2023)
- *Authors:* Zhang et al.
- *Direct Connection:* By explicitly modeling dependencies across the time and variable dimensions, Crossformer highlights the value of attention along the variable axis, which iTransformer streamlines by applying standard Transformer blocks on the inverted (variable) dimension.

---

## Synthesis: How Prior Work Led to This Paper

Evidence accumulated that temporal self-attention is fragile and costly for long lookbacks: Are Transformers Effective for Time Series Forecasting? showed that, as context grows, standard Transformer forecasters often degrade and are outperformed by simple per-channel linear models, implying that heavy temporal attention is not the key driver of accuracy. PatchTST pinpointed early variate mixing as harmful and showed that channel-independent processing with patching yields stronger representations, arguing for keeping variates separate during modeling. Crossformer further emphasized the importance of cross-dimension structure by explicitly attending across variable and temporal dimensions, showing clear gains when variable-wise dependencies are modeled. Informer defined the long-sequence forecasting setting and benchmarks, and pursued sparsity to alleviate temporal attention’s quadratic cost. FEDformer sought efficiency through frequency-domain decomposition yet still inherited the temporal-token paradigm that fuses multiple variates into each token. TimesNet, from a non-Transformer angle, validated variate-centric, channel-independent design as a strong inductive bias for multivariate time series. Together these works reveal two convergent signals: (1) long-horizon temporal attention is expensive and often unnecessary, and (2) early mixing of variates into temporal tokens undermines representation quality. The natural next step is to reassign the Transformer’s core operations to the variable dimension. By inverting tokenization so that variates become tokens and applying unmodified attention and feed-forward layers over them, the current work leverages channel-independence, preserves meaningful attention, and sidesteps long-temporal scaling—synthesizing the empirical gaps and inductive insights surfaced by these studies.

---

*Analysis generated on: 2026-01-07T00:18:04.588505*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
