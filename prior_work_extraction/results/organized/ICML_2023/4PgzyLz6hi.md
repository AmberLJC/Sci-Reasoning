# Prior Work Analysis Report

## Target Paper
**Title:** 4PgzyLz6hi
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**On Calibration of Modern Neural Networks** (2017)
- *Authors:* Chuan Guo et al.
- *Connection:* Established the modern miscalibration problem and standard metrics (e.g., ECE, temperature scaling) that CML explicitly targets and extends to the multimodal setting where confidence can perversely increase under modality corruption.

**Multimodal Learning with Deep Boltzmann Machines** (2012)
- *Authors:* Nitish Srivastava et al.
- *Connection:* Introduced a principled multimodal framework with missing-modality inference, grounding CML’s core principle that more modalities should not increase uncertainty and, conversely, removing a modality should not boost confidence.

### 💡 Inspiration

**Regularizing Neural Networks by Penalizing Confident Output Distributions** (2017)
- *Authors:* Gabriel Pereyra et al.
- *Connection:* Inspired CML’s regularization view on overconfidence; CML departs by imposing a pairwise monotonicity constraint between full-input and modality-ablated predictions instead of a global entropy penalty.

**Mean Teachers Are Better Role Models: Weight-Averaged Consistency Targets Improve Semi-Supervised Learning** (2017)
- *Authors:* Antti Tarvainen et al.
- *Connection:* Motivated CML’s consistency-style training across perturbations; CML adapts this idea by enforcing inequality-based consistency (confidence should not increase) specifically for perturbations that remove modalities.

**Training Products of Experts by Minimizing Contrastive Divergence** (2002)
- *Authors:* Geoffrey Hinton
- *Connection:* Product-of-Experts theory implies that adding independent evidence should increase certainty; CML operationalizes the complementary discriminative constraint that removing an expert (modality) must not raise predictive confidence.

### 🔍 Gap Identification

**Can You Trust Your Model’s Uncertainty Under Dataset Shift?** (2019)
- *Authors:* Yarin Ovadia et al.
- *Connection:* Showed that predictive uncertainty often deteriorates under distribution shift; CML directly addresses the analogous, multimodal-specific shift—modality removal/corruption—by enforcing that confidence must not increase when evidence is reduced.

### 📊 Baseline

**Beyond Temperature Scaling: Obtaining Well-Calibrated Multiclass Probabilities with Dirichlet Calibration** (2019)
- *Authors:* Meelis Kull et al.
- *Connection:* Provides a principal post-hoc calibration baseline that CML consistently outperforms by integrating calibration into training via a modality-aware regularizer rather than post-hoc adjustment.

---

## Synthesis

Calibrating Multimodal Learning (CML) is grounded in the modern understanding that deep networks are miscalibrated, as formalized by Guo et al., whose metrics and post-hoc baseline (temperature scaling) define the calibration yardstick. Ovadia et al. demonstrated that uncertainty often fails under distribution shift; CML pinpoints a multimodal analog—modality corruption/removal—and designs a training-time remedy tailored to that shift. Rather than rely on post-hoc fixes like Dirichlet calibration (Kull et al.), which serve as key baselines, CML embeds calibration into learning via a targeted regularizer. Two strands directly inspire this design: confidence-targeted regularization (Pereyra et al.) and consistency regularization under perturbations (Tarvainen & Valpola). CML synthesizes these by enforcing a pairwise, inequality-based consistency—confidence with all modalities must not be higher than with a subset—thereby specifically penalizing overconfidence when evidence is reduced. This principle is theoretically consonant with classic multimodal foundations: Srivastava & Salakhutdinov’s multimodal DBMs underscore that more modalities should reduce uncertainty and enable missing-modality reasoning, while Hinton’s Product-of-Experts formalizes that adding independent experts concentrates belief. CML translates these generative intuitions into a discriminative calibration constraint, producing a plug-in regularizer that improves both calibration and accuracy across multimodal classifiers and directly addresses the core gap of unreliable confidence under modality corruption.

---
*Generated: 2026-01-06T23:09:26.567014*
