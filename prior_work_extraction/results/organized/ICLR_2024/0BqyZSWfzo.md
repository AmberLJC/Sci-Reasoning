# Prior Work Analysis Report

## Target Paper

**Title:** One-shot Empirical Privacy Estimation for Federated Learning

**Conference:** ICLR 2024 (oral)

**Authors:** Galen Andrew, Peter Kairouz, Sewoong Oh, Alina Oprea, Hugh Brendan McMahan, Vinith Menon Suriyakumar

**Keywords:** differential privacy, federated learning, empirical privacy

**Abstract:** 
> Privacy estimation techniques for differentially private (DP) algorithms are useful for comparing against analytical bounds, or to empirically measure privacy loss in settings where known analytical bounds are not tight. However, existing privacy auditing techniques usually make strong assumptions on the adversary (e.g., knowledge of intermediate model iterates or the training data distribution), are tailored to specific tasks, model architectures, or DP algorithm, and/or require retraining the ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Subsampled Rényi Differential Privacy and Analytical Moments Accountant** (2019)
- *Authors:* Yu-Xiang Wang et al.
- *Direct Connection:* Their accountant is the standard analytical upper bound for (sampled) Gaussian mechanisms used in DP-SGD/FL, serving both as the formal composition framework and the primary analytic bound this work benchmarks and complements with empirical estimates.

**Gaussian Differential Privacy** (2019)
- *Authors:* Jinshuo Dong et al.
- *Direct Connection:* The hypothesis-testing view and Gaussian likelihood-ratio characterization from GDP directly enable computing run-specific privacy loss contributions from the actual Gaussian noise realizations observed during training.

**Learning Differentially Private Recurrent Language Models** (2018)
- *Authors:* H. Brendan McMahan et al.
- *Direct Connection:* This work instantiated user-level DP in cross-device federated learning via client subsampling, per-client clipping, and Gaussian noising, precisely the mechanism structure the one-shot estimator targets and exploits.

### 💡 Inspiration

**Privacy Odometers and Filters: Pay-as-you-go Composition for Differential Privacy** (2016)
- *Authors:* Ryan Rogers et al.
- *Direct Connection:* The idea of tracking realized privacy consumption over a specific execution inspired the single-run, online estimation paradigm extended here to empirical (data- and randomness-dependent) privacy loss in federated training.

### 🔍 Gap Identification

**Evaluating Differentially Private Machine Learning in Practice** (2019)
- *Authors:* Bargav Jayaraman et al.
- *Direct Connection:* Their membership-inference-based auditing requires many retrainings and task-specific calibration, a bottleneck this work removes by estimating privacy loss during a single training run without auxiliary retraining.

### 📊 Baseline

**Auditing Differentially Private Machine Learning: How Private is Private SGD?** (2023)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* This state-of-the-art audit framework provides empirical lower bounds for DP-SGD via thousands of retrainings and access to training internals; the present method targets comparable empirical tightness but in a one-shot, single-run setting without such assumptions.

---

## Synthesis: How Prior Work Led to This Paper

Early empirical audits of differentially private learning showed how to turn membership inference into privacy lower bounds, but did so by calibrating attacks through many shadow trainings and task-specific tuning (Jayaraman et al.). More recent audits achieved stronger lower bounds for DP-SGD by running thousands of retrainings and sometimes leveraging training internals, further underscoring the cost and fragility of multi-run procedures (Carlini et al.). In parallel, analytical accounting matured: subsampled Rényi DP and the analytical moments accountant formalized tight composition for the sampled Gaussian mechanism that underlies DP-SGD and DP-FL, yielding standard upper bounds used in practice (Wang, Balle, Kasiviswanathan). The hypothesis-testing formulation of privacy and the Gaussian likelihood-ratio view clarified how Gaussian mechanisms induce additive privacy loss random variables amenable to composition (Dong, Roth, Su). On the systems side, user-level DP in federated learning was instantiated with client subsampling, per-client clipping, and Gaussian noising of aggregated updates, precisely defining the randomized steps and observables in cross-device training (McMahan et al.). Finally, privacy odometers and filters proposed tracking realized privacy consumption over the actual sequence of mechanisms rather than worst-case schedules (Rogers et al.). Taken together, these strands revealed a gap: analytical bounds can be loose for real runs, while empirical audits are impractically multi-run. By marrying GDP’s likelihood-ratio decomposition with the DP-FL mechanism structure and the odometer perspective, the current work naturally advances to a one-shot estimator that computes empirical privacy directly from a single federated training execution.

---

*Analysis generated on: 2026-01-06T10:01:39.207560*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
