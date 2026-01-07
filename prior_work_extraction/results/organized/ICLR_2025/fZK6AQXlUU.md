# Prior Work Analysis Report

## Target Paper

**Title:** Conformal Prediction Sets Can Cause Disparate Impact

**Conference:** ICLR 2025 (spotlight)

**Authors:** Jesse C. Cresswell, Bhargava Kumar, Yi Sui, Mouloud Belbahri

**Keywords:** Conformal Prediction, Fairness, Uncertainty Quantification, Trustworthy ML, Human Subject Experiments

**Abstract:** 
> Conformal prediction is a statistically rigorous method for quantifying uncertainty in models by having them output sets of predictions, with larger sets indicating more uncertainty. However, prediction sets are not inherently actionable; many applications require a single output to act on, not several. To overcome this limitation, prediction sets can be provided to a human who then makes an informed decision. In any such system it is crucial to ensure the fairness of outcomes across protected g...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Multicalibration: Calibration for the (Computationally-Identifiable) Masses** (2018)
- *Authors:* Ilan Hebert-Johnson et al.
- *Direct Connection:* Establishes subgroup-conditional calibration as a fairness principle, which underlies the equalized-coverage goal (group-conditional validity) that this paper scrutinizes in the context of prediction sets.

**Disparate Interactions: An Algorithm-in-the-Loop Experiment in Criminal Justice Risk Assessment** (2019)
- *Authors:* Ben Green and Yiling Chen
- *Direct Connection:* Demonstrates that human decision-makers’ use of model outputs can induce disparate impact, directly motivating the paper’s human-subject experiments assessing how prediction sets affect downstream group outcomes.

### 💡 Inspiration

**Least Ambiguous Set-Valued Classifiers with Bounded Error** (2019)
- *Authors:* Mauricio Sadinle and Jing Lei
- *Direct Connection:* Introduces the ambiguity notion (expected set size) as the key efficiency measure for set-valued classifiers, directly motivating the paper’s proposal to equalize set sizes across protected groups as a fairness objective.

### 🔍 Gap Identification

**On Fairness and Calibration** (2017)
- *Authors:* Geoff Pleiss et al.
- *Direct Connection:* Shows inherent tensions between calibration-like constraints and error-based fairness, prompting the paper’s central question of whether enforcing equalized coverage (a coverage-calibration analogue) actually improves downstream fairness.

### 📊 Baseline

**Distribution-Free, Risk-Controlling Prediction Sets** (2021)
- *Authors:* Stephen Bates et al.
- *Direct Connection:* Provides the standard multi-class conformal prediction procedures (e.g., APS/RAPS) and calibration protocols that the paper uses to construct marginal and group-calibrated prediction sets when evaluating fairness and disparate impact.

### 🔗 Related Problem

**Preventing Fairness Gerrymandering: Auditing and Learning for Subgroup Fairness** (2018)
- *Authors:* Michael Kearns et al.
- *Direct Connection:* Frames fairness as guaranteeing comparable behavior across protected (and richer) subgroups, a perspective that informs both equalized coverage and the paper’s shift toward parity in set sizes across groups.

---

## Synthesis: How Prior Work Led to This Paper

Distribution-free predictive set methods established concrete procedures for constructing and calibrating multi-class prediction sets, including mechanisms to attain marginal coverage and to adjust calibration to target specific groups. Complementing this, set-valued classification research formalized ambiguity—the expected size of a prediction set—as the primary efficiency notion, revealing that controlling set size is central to the usability of set outputs. Independent work on multicalibration articulated subgroup-conditional guarantees as a fairness objective, cultivating the idea that coverage should hold uniformly across protected groups. Human–algorithm interaction studies then documented that people use model outputs in ways that can amplify disparities, underscoring that fairness must be judged on downstream decisions, not just statistical guarantees. Finally, results on fairness–calibration incompatibilities highlighted that enforcing calibration-like constraints can trade off with other fairness goals, and subgroup-fairness frameworks advocated parity across groups or subgroups as the fairness target. Taken together, these threads created a natural tension: equalized coverage offers a principled fairness guarantee for prediction sets, while ambiguity-driven efficiency and human decision dynamics determine real outcomes. The current work synthesizes these insights by empirically testing how equalized coverage affects human decisions and by leveraging the ambiguity notion to propose equalizing set sizes across groups, showing this parity-of-ambiguity criterion better aligns statistical uncertainty reporting with downstream fairness.

---

*Analysis generated on: 2026-01-06T10:20:43.748696*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
