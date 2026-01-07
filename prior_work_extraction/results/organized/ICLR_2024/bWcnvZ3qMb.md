# Prior Work Analysis Report

## Target Paper

**Title:** FITS: Modeling Time Series with $10k$ Parameters

**Conference:** ICLR 2024 (spotlight)

**Authors:** Zhijian Xu, Ailing Zeng, Qiang Xu

**Keywords:** Time series analysis, Time series forecasting, Complex-valued neural network

**Abstract:** 
> In this paper, we introduce FITS, a lightweight yet powerful model for time series analysis. Unlike existing models that directly process raw time-domain data, FITS operates on the principle that time series can be manipulated through interpolation in the complex frequency domain, achieving performance comparable to state-of-the-art models for time series forecasting and anomaly detection tasks. Notably, FITS accomplishes this with a svelte profile of just about $10k$ parameters, making it ideal...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**N-BEATS: Neural basis expansion analysis for interpretable time series forecasting** (2020)
- *Authors:* Boris Oreshkin et al.
- *Direct Connection:* N-BEATS framed forecasting as reconstruction from learned bases (trend/seasonality), a perspective FITS concretizes with an explicit Fourier (complex) basis and spectral reconstruction to minimize parameters.

**Deep Complex Networks** (2018)
- *Authors:* Chiheb Trabelsi et al.
- *Direct Connection:* This paper provided the core complex-valued operations and normalization needed for stable learning in the complex domain, which FITS leverages to manipulate spectra directly.

### 💡 Inspiration

**FEDformer: Frequency Enhanced Decomposed Transformer for Long-Term Series Forecasting** (2022)
- *Authors:* Haixu Zhou et al.
- *Direct Connection:* FEDformer showed that modeling and filtering in Fourier space improves long-horizon forecasting, directly motivating FITS to abandon attention and operate purely via complex frequency-domain manipulation.

**Fourier Neural Operator for Parametric Partial Differential Equations** (2021)
- *Authors:* Zongyi Li et al.
- *Direct Connection:* The idea of learning global mappings with a tiny set of complex spectral weights in FNO inspired FITS’s design of compact, learnable operations in the Fourier domain for time-series modeling.

### 📊 Baseline

**Are Transformers Effective for Time Series Forecasting?** (2023)
- *Authors:* Ailing Zeng et al.
- *Direct Connection:* This work established strong lightweight linear baselines (LTSF-Linear/DLinear) and highlighted that heavy attention is unnecessary, which FITS directly targets and surpasses while addressing DLinear’s inability to exploit frequency-domain structure.

### 🔧 Extension

**NHITS: Neural Hierarchical Interpolation for Time Series Forecasting** (2023)
- *Authors:* Cristian Challu et al.
- *Direct Connection:* Building on NHITS’s success with interpolation-based reconstruction, FITS generalizes the interpolation idea by performing it directly in the complex frequency domain for greater compactness and fidelity.

---

## Synthesis: How Prior Work Led to This Paper

Recent studies revealed that effective time-series forecasting does not require heavy attention mechanisms. DLinear (Are Transformers Effective for Time Series Forecasting?) demonstrated that simple linear models with seasonal–trend decomposition can rival or beat complex transformers on long-horizon benchmarks, establishing a minimalist baseline and exposing the limits of purely time-domain linearity. FEDformer showed that selecting and operating on dominant Fourier modes substantially improves long-range modeling, grounding the value of frequency-domain processing. The Fourier Neural Operator introduced learning with complex spectral multipliers to capture global structure using very few parameters, highlighting a path to high capacity per parameter. NHITS proved that interpolation-based reconstruction, especially across multiple resolutions, is a powerful forecasting principle. N-BEATS framed forecasting as reconstructing signals from learned bases (trend/seasonality), suggesting that explicit basis choices can yield interpretable and strong models. Deep Complex Networks supplied the practical machinery for stable learning with complex-valued parameters and activations, essential when operating directly on spectra.
Together, these works pointed to an opportunity: combine interpolation-based reconstruction with explicit Fourier-domain modeling and complex-valued learning to achieve global receptive fields and strong long-horizon performance using a tiny parameter budget. The current paper synthesizes these insights by eschewing attention and time-domain convolutions, reconstructing sequences through complex frequency-domain interpolation with learned spectral parameters, thereby unifying the efficiency of DLinear, the spectral advantages of FEDformer/FNO, and the reconstruction philosophy of NHITS/N-BEATS into a compact, edge-friendly model.

---

*Analysis generated on: 2026-01-06T13:26:26.693689*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
