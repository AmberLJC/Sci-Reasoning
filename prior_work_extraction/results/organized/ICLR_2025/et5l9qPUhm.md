# Prior Work Analysis Report

## Target Paper
**Title:** et5l9qPUhm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**The Curse of Recursion: Training on Generated Data Makes Models Forget** (2023)
- *Authors:* Vitaly Shumailov et al.
- *Connection:* Introduced and empirically characterized 'model collapse' when models are trained on their own synthetic data; Strong Model Collapse formalizes and strengthens this phenomenon in a supervised regression and scaling-laws setting.

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Jared Kaplan et al.
- *Connection:* Provides the scaling-laws framework (loss vs. data/model size) that Strong Model Collapse explicitly adopts to study how even tiny synthetic-data contamination disrupts expected data-scaling improvements.

**Random Features for Large-Scale Kernel Machines** (2007)
- *Authors:* Ali Rahimi and Benjamin Recht
- *Connection:* Introduces random-feature (random projections) approximations that Strong Model Collapse uses as a tunable-width proxy for neural networks to analyze collapse vs. model size.

### 💡 Inspiration

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Jordan Hoffmann et al.
- *Connection:* Posits the model–data trade-off central to modern scaling; Strong Model Collapse directly probes this question under contamination, showing theoretically and empirically that larger models can amplify collapse.

### 🔧 Extension

**Surprises in High-Dimensional Ridgeless Least Squares Interpolation** (2019)
- *Authors:* Trevor Hastie et al.
- *Connection:* Characterizes interpolation thresholds and risk behavior in ridgeless regression; Strong Model Collapse extends this lens to contaminated data, linking interpolation thresholds to amplification/mitigation of collapse by model size.

**Generalization Error of Random Features Regression: Double Descent Curve and Universality** (2022)
- *Authors:* Song Mei et al.
- *Connection:* Provides precise high-dimensional asymptotics for random-features regression; Strong Model Collapse adapts this machinery to mixtures with synthetic data to prove strong collapse even at vanishing contamination.

---

## Synthesis

Strong Model Collapse sits at the intersection of two lines of work: the empirical discovery of model collapse from synthetic data and the theory of scaling and high-dimensional regression. Shumailov et al. established the core phenomenon—training on generated data degrades models—which this paper rigorously strengthens in a supervised regression setting, proving that even minute contamination prevents standard scaling-law gains. The study is framed within the scaling-laws paradigm inaugurated by Kaplan et al., asking how loss should scale with data and model size when contamination is present. Hoffmann et al.’s compute-optimal perspective directly motivates the central question of whether enlarging models alleviates or worsens collapse; the paper shows larger models can in fact amplify collapse under realistic regimes. Methodologically, the work relies on modeling neural networks via random projections, a strategy rooted in Rahimi and Recht’s random features, to create a tunable-width surrogate amenable to analysis. The behavior around the interpolation threshold and double-descent is drawn from Hastie et al., whose ridgeless asymptotics and interpolation lens are extended here to contaminated training distributions. Finally, the paper leverages and modifies the precise asymptotic tools of Mei et al. for random-features regression, deriving risk formulas under synthetic-data mixtures. Together, these works directly underpin the paper’s main result: a strong, theoretically grounded collapse law that ties small synthetic contamination and model-size scaling to a breakdown of expected data-driven performance improvements.

---
*Generated: 2026-01-06T23:09:26.596111*
