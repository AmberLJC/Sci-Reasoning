# Prior Work Analysis Report

## Target Paper
**Title:** WJujF9An5L
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

FuXi-Ocean’s core advance—stable six-hourly global ocean forecasts at eddy-resolving 1/12° with depth—stands on three converging lines of prior work. First, recent breakthroughs in data-driven weather models established that autoregressive, sub-daily forecasting at global scale is feasible and efficient. Pangu-Weather and GraphCast demonstrated that stacking attention blocks (or learned graph operators), conditioning on recent history, and iterating 6-hour steps can rival numerical models. FuXi-Ocean imports this recipe into the oceanic domain, where multivariate, 3D dynamics and eddy-resolving resolution amplify stability challenges. FourCastNet and the Fourier Neural Operator line further legitimized operator-learning and spectral efficiency for high-resolution geophysical dynamics, shaping FuXi-Ocean’s emphasis on scalable training and inference.
Second, the Mixture-of-Time (MoT) module adapts mixture-of-experts principles to the temporal axis. Inspired by sparsely gated MoE, FuXi-Ocean treats predictors at different temporal horizons as the “experts,” learning gates that adaptively combine their outputs based on context. This is complemented by ideas from Temporal Fusion Transformers, whose gated fusion of multiple temporal signals directly motivates MoT’s aggregation of multi-horizon predictions.
Third, the model tackles autoregressive error accumulation—a key barrier for sub-daily forecasts—by drawing on sequence learning strategies akin to scheduled sampling and stable iterative rollout practices from modern weather models. Collectively, these strands yield a context-aware, attention-based architecture whose MoT module fuses temporal scales to deliver robust, sub-daily, eddy-resolving global ocean forecasts.

---
*Generated: 2026-01-07T00:21:32.283672*
