# Prior Work Analysis Report

## Target Paper

**Title:** Conformal Risk Control

**Conference:** ICLR 2024 (spotlight)

**Authors:** Anastasios Nikolas Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, Tal Schuster

**Keywords:** conformal prediction, uncertainty quantification

**Abstract:** 
> We extend conformal prediction to control the expected value of any monotone loss function. The algorithm generalizes split conformal prediction together with its coverage guarantee. Like conformal prediction, the conformal risk control procedure is tight up to an $\mathcal{O}(1/n)$ factor. We also introduce extensions of the idea to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics. Worked examples from computer vision and natural...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Algorithmic Learning in a Random World** (2005)
- *Authors:* Vladimir Vovk, Alex Gammerman, Glenn Shafer
- *Direct Connection:* The paper supplies the exchangeability-based conformal prediction framework and finite-sample validity logic that CRC repurposes from coverage control to risk (expected monotone loss) control.

**Distribution-Free Predictive Inference for Regression** (2018)
- *Authors:* Jing Lei et al.
- *Direct Connection:* CRC directly generalizes the split conformal template—fit on training data then calibrate on a holdout via order statistics—lifting its marginal coverage guarantee to control of expected monotone loss while preserving O(1/n) tightness.

### 💡 Inspiration

**Conditional validity of inductive conformal predictors** (2012)
- *Authors:* Vladimir Vovk et al.
- *Direct Connection:* CRC’s simultaneous/multiple risk control echoes Mondrian (group-conditional) conformal calibration by enforcing guarantees across partitions via groupwise calibration.

### 📊 Baseline

**Distribution-Free, Risk-Controlling Prediction Sets** (2021)
- *Authors:* Stephen Bates et al.
- *Direct Connection:* CRC extends RCPS from indicator-style classification set risks to arbitrary monotone losses and provides a unified split-style calibration with finite-sample guarantees, directly addressing RCPS’s scope and methodological limitations.

### 🔧 Extension

**Conformalized Quantile Regression** (2019)
- *Authors:* Yaniv Romano et al.
- *Direct Connection:* CRC’s quantile risk control adapts the CQR idea of conformalizing a quantile functional using order-statistic calibration, but applies it to the distribution of losses rather than the response.

**Conformal Prediction under Covariate Shift** (2019)
- *Authors:* Ryan Tibshirani et al.
- *Direct Connection:* CRC’s distribution-shift variant inherits the importance-weighted calibration scheme from weighted conformal prediction to target guarantees under the test distribution.

### 🔗 Related Problem

**Adaptive Conformal Inference Under Distribution Shift** (2021)
- *Authors:* Chuanrui (Drew) Gibbs and Emmanuel Candès
- *Direct Connection:* CRC’s adversarial/multiple risk control borrows the adaptive recalibration perspective—maintaining guarantees under nonstationarity—which it translates to controlling loss-based risks rather than coverage.

---

## Synthesis: How Prior Work Led to This Paper

Conformal prediction’s core logic—validity from exchangeability—was crystallized by Vovk, Gammerman, and Shafer, establishing finite-sample guarantees derived from order statistics. Split conformal prediction then operationalized this theory for modern learning by fitting on a training split and calibrating on a holdout to obtain marginal coverage with minimal O(1/n) slack. Risk-Controlling Prediction Sets pushed beyond coverage by tuning prediction-set procedures to satisfy average loss constraints in classification, demonstrating that risk-style control could be distribution-free but remaining tied to specific indicator losses and set constructions. Conformalized Quantile Regression showed how to conformalize a quantile functional using order statistics, offering a template to guarantee quantiles rather than expectations. Under distribution shift, weighted conformal prediction introduced importance-weighted calibration to target test-distribution guarantees, and adaptive conformal inference highlighted recalibration strategies for nonstationary settings. Finally, Mondrian (group-conditional) conformal predictors established that partitioned, groupwise calibration can deliver simultaneous guarantees across multiple subpopulations.
Together, these works exposed a natural generalization: use the split conformal calibration mechanism and exchangeability logic to control not just coverage but the expected value (and quantiles) of any monotone loss, while retaining finite-sample tightness. Importance weighting and adaptive/groupwise calibration furnish principled routes to extend this control under distribution shift and across multiple or adversarially chosen constraints. By unifying RCPS-style risk goals with split conformal calibration, quantile conformalization, and groupwise/weighted adaptations, the resulting framework delivers distribution-free guarantees for broad loss-based risks in a single, simple procedure.

---

*Analysis generated on: 2026-01-06T19:06:48.064726*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
