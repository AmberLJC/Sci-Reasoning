# Prior Work Analysis Report

## Target Paper
**Title:** JxnOZwFNcU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Conformal Risk Control** (2022)
- *Authors:* Anastasios N. Angelopoulos et al.
- *Connection:* aLTT inherits the core problem formulation of post-hoc population-risk control via hypothesis testing across candidate configurations introduced by CRC, but implements it sequentially with e-processes instead of fixed-sample p-values.

**Time-uniform, nonparametric, nonasymptotic confidence sequences** (2021)
- *Authors:* Steven L. Howard et al.
- *Connection:* The anytime-valid inference framework based on nonnegative supermartingales underpins aLTT’s use of e-processes to justify early stopping without inflating error rates.

### 💡 Inspiration

**Safe Testing** (2020)
- *Authors:* Peter D. Grünwald et al.
- *Connection:* This work introduced e-values/e-processes and their optional-stopping validity, directly enabling aLTT’s anytime-valid, data-dependent sequential tests with early termination.

### 🔍 Gap Identification

**SAFFRON: an adaptive algorithm for online control of the false discovery rate** (2018)
- *Authors:* J. Ramdas et al.
- *Connection:* As a state-of-the-art p-value–based online FDR method, SAFFRON highlights the limitations of p-values under adaptivity and optional stopping that aLTT overcomes by switching to e-processes for more efficient sequential screening.

### 📊 Baseline

**Learn-then-Test (LTT): Risk-Controlling Post-hoc Model Selection** (2024)
- *Authors:* Sangwoo Park et al.
- *Connection:* aLTT directly replaces LTT’s batch, p-value-based multiple testing with an e-process-driven, sequential MHT that enables early stopping while preserving the same finite-sample population-risk guarantees.

### 🔧 Extension

**False Discovery Rate Control with E-values** (2022)
- *Authors:* Jingshu Wang et al.
- *Connection:* aLTT adapts tools for combining and thresholding e-values (e.g., e-BH) to perform statistically valid multiple testing over hyperparameters under sequential, data-dependent screening.

---

## Synthesis

Adaptive Learn-then-Test (aLTT) builds squarely on the learn-then-test (LTT) paradigm for post-hoc model and hyperparameter selection under finite-sample population-risk guarantees. The core LTT idea—pose selection as multiple hypothesis tests that ensure the chosen configuration meets a target risk—traces back to conformal risk control (CRC), which formalized risk control via fixed-sample, p-value–based testing. aLTT’s key advance is to make this testing sequential, data-dependent, and early-stoppable without sacrificing validity. That advance is directly enabled by the e-process framework from Safe Testing and the broader anytime-valid inference literature on confidence sequences and nonnegative supermartingales, which provide the mathematical machinery to maintain error control under optional stopping and adaptivity. To scale risk control to families of hyperparameters, aLTT relies on multiple testing with e-values, drawing on results like e-BH from “False Discovery Rate Control with E-values,” which furnish combination and thresholding rules that preserve error guarantees in the e-value regime. Finally, prior p-value–based online FDR methods such as SAFFRON underscore the limitations of p-values for adaptive, sequential procedures—limitations aLTT explicitly addresses by adopting e-processes. Together, these works form a direct intellectual lineage: CRC and LTT define the objective and baseline procedure; Safe Testing and anytime-valid e-process theory make sequential, early-stopping tests possible; and e-value–based MHT supplies the multiple-testing toolkit aLTT adapts to hyperparameter selection.

---
*Generated: 2026-01-06T23:07:19.579200*
