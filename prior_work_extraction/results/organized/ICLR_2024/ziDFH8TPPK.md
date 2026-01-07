# Prior Work Analysis Report

## Target Paper

**Title:** Long-Term Typhoon Trajectory Prediction: A Physics-Conditioned Approach Without Reanalysis Data

**Conference:** ICLR 2024 (spotlight)

**Authors:** Young-Jae Park, Minseok Seo, Doyi Kim, Hyeri Kim, Sanghoon Choi, Beomkyu Choi, Jeongwon Ryu, Sohee Son, Hae-Gon Jeon, Yeji Choi

**Keywords:** Weather Forecasting, Typhoon Trajectory Forecasting, Tropical Cyclone, Climate Change

**Abstract:** 
> In the face of escalating climate changes, typhoon intensities and their ensuing damage have surged. Accurate trajectory prediction is crucial for effective damage control. Traditional physics-based models, while comprehensive, are computationally intensive and rely heavily on the expertise of forecasters. Contemporary data-driven methods often rely on reanalysis data, which can be considered to be the closest to the true representation of weather conditions. However, reanalysis data is not prod...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Operational Beta and Advection Model (BAM) for Tropical Cyclone Track Forecasting** (2006)
- *Authors:* Sampson et al.
- *Direct Connection:* BAM codified the steering-flow principle (deep-layer mean environmental winds and beta effect) that the paper leverages as the core physical prior to condition its data-driven trajectory predictor.

**The Met Office Unified Model: Global Atmosphere/Global Land configuration** (2019)
- *Authors:* Walters et al.
- *Direct Connection:* This description of the operational Unified Model underpins the paper’s key choice of real-time UM fields as inputs, enabling a reanalysis-free, operationally deployable physics-conditioned track predictor.

### 💡 Inspiration

**Physics-guided Neural Networks (PGNN): An application in lake temperature modeling** (2017)
- *Authors:* Karpatne et al.
- *Direct Connection:* PGNN established the idea of embedding physics knowledge into learning systems, directly inspiring the paper’s physics-conditioned design that guides the predictor with physically meaningful UM-derived signals.

### 🔍 Gap Identification

**Pangu-Weather: Accurate medium-range global weather forecasting with 3D neural networks** (2023)
- *Authors:* Bi et al.
- *Direct Connection:* This work showed that state-of-the-art data-driven weather forecasts rely on reanalysis (e.g., ERA5), which is not available in real time, directly motivating the paper’s shift to operational UM inputs for long-horizon typhoon tracking.

**GraphCast: Learning skillful medium-range global weather forecasting** (2023)
- *Authors:* Lam et al.
- *Direct Connection:* By achieving strong medium-range forecasts from ERA5, GraphCast exemplified the power—and operational limitation—of reanalysis-driven models that the current paper overcomes by conditioning on real-time NWP (UM) fields.

**Physics-Informed Neural Networks: A Deep Learning Framework for Solving PDEs** (2019)
- *Authors:* Raissi et al.
- *Direct Connection:* PINNs’ requirement to enforce PDE residuals is impractical at global NWP scale, motivating the paper’s alternative of conditioning on physically relevant NWP fields rather than imposing full dynamical constraints.

### 📊 Baseline

**Prediction of Typhoon Trajectories using Recurrent Neural Networks** (2018)
- *Authors:* Rüttgers et al.
- *Direct Connection:* This early deep-learning track-forecasting setup provided the baseline learning formulation that the paper extends by injecting explicit physical conditioning and switching from reanalysis/satellite proxies to real-time UM predictors for >72 h horizons.

---

## Synthesis: How Prior Work Led to This Paper

Modern data-driven weather models demonstrated that large neural forecasters trained on reanalysis can achieve skillful medium-range predictions: Pangu-Weather showed strong performance by learning from ERA5 fields with 3D architectures, and GraphCast reinforced this by delivering competitive 10-day guidance, again from reanalysis. Early deep-learning work specific to typhoons, such as Rüttgers et al., framed track prediction as a sequence learning problem using data proxies (e.g., satellite or reanalysis), but lacked explicit physical priors. In parallel, physics-guided learning advanced the idea of embedding domain knowledge into neural models; PGNN illustrated how incorporating physical guidance improves generalization, while PINNs proposed enforcing PDE residuals but proved difficult to scale to high-dimensional, global NWP settings. Classical tropical cyclone guidance such as the Beta and Advection Model (BAM) distilled the core physical insight that deep-layer environmental winds and the beta effect steer cyclone motion, effectively identifying the most predictive physical signals for track evolution. Operational NWP systems like the Met Office Unified Model (UM) provide these steering-relevant fields in real time, without the latency of reanalysis. Together, these works revealed a gap: reanalysis-powered learning is powerful but operationally delayed, while pure data-driven track models underuse well-known steering physics. The natural next step is to combine operational NWP fields that encode steering dynamics with a learning system guided by physics, avoiding heavy PDE residual enforcement. By conditioning a track predictor on UM-derived physically meaningful features, the approach preserves the strengths of data-driven forecasting while removing dependence on reanalysis and enabling reliable >72 h guidance.

---

*Analysis generated on: 2026-01-06T18:20:43.930430*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
