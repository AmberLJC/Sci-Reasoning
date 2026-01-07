# Prior Work Analysis Report

## Target Paper

**Title:** Unprocessing Seven Years of Algorithmic Fairness

**Conference:** ICLR 2024 (oral)

**Authors:** André Cruz, Moritz Hardt

**Keywords:** fairness, algorithmic fairness, social computing, tabular data, meta study

**Abstract:** 
> Seven years ago, researchers proposed a postprocessing method to equalize the error rates of a model across different demographic groups. The work launched hundreds of papers purporting to improve over the postprocessing baseline. We empirically evaluate these claims through thousands of model evaluations on several tabular datasets. We find that the fairness-accuracy Pareto frontier achieved by postprocessing contains all other methods we were feasibly able to evaluate. In doing so, we address ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Equality of Opportunity in Supervised Learning** (2016)
- *Authors:* Moritz Hardt et al.
- *Direct Connection:* The unprocessing idea explicitly inverts Hardt et al.’s equalized-odds postprocessing (and its ROC-hull characterization), using it as the canonical frontier onto which disparate methods can be mapped for fair comparison.

### 💡 Inspiration

**The Cost of Fairness in Binary Classification** (2018)
- *Authors:* Aditya Krishna Menon et al.
- *Direct Connection:* By characterizing Bayes-optimal fairness–accuracy trade-offs via group-wise threshold frontiers, this work underpins the use of a postprocessing Pareto frontier as the reference set that unprocessing maps methods onto.

### 🔍 Gap Identification

**A Comparative Study of Fairness-Enhancing Interventions in Machine Learning** (2019)
- *Authors:* Sorelle A. Friedler et al.
- *Direct Connection:* This broad empirical study revealed inconsistent evaluation protocols across pre-, in-, and post-processing methods, motivating the need for a principled comparison mechanism that unprocessing provides.

**Fairness Beyond Disparate Treatment & Disparate Impact: Learning Classifiers without Disparate Mistreatment** (2017)
- *Authors:* Muhammad Bilal Zafar et al.
- *Direct Connection:* By enforcing fairness via convex proxy constraints that relax exact error-rate equalities, this line of work exemplifies the differing relaxation levels that unprocessing standardizes for direct comparison.

### 📊 Baseline

**A Reductions Approach to Fair Classification** (2018)
- *Authors:* Alekh Agarwal et al.
- *Direct Connection:* As the dominant in-processing baseline that wraps arbitrary base learners under fairness constraints, this method’s dependence on different base models is a key confound that unprocessing neutralizes to enable apples-to-apples comparisons.

### 🔗 Related Problem

**On Fairness and Calibration** (2017)
- *Authors:* Geoff Pleiss et al.
- *Direct Connection:* Their analysis of group-specific thresholding and randomization to trade off calibration and equalized odds clarified the geometry of postprocessing that unprocessing conceptually reverses.

---

## Synthesis: How Prior Work Led to This Paper

Equalized-odds postprocessing formalized by Hardt, Price, and Srebro establishes that fairness can be achieved by group-specific thresholding and randomization along each group’s ROC, yielding a convex, interpretable frontier of achievable error-rate trade-offs. Menon and Williamson show that Bayes-optimal fairness–accuracy trade-offs for error-rate constraints lie on such threshold frontiers, sharpening the view that postprocessing delineates the relevant Pareto set. Pleiss and colleagues study calibration versus equalized odds, making explicit how group-wise thresholding and randomization navigate trade-offs, thereby clarifying the geometry of postprocessing in practice. On the algorithmic side, Agarwal et al.’s reductions framework became the central in-processing competitor, but its performance depends critically on the choice and capacity of the base learner. Zafar et al. enforce fairness through convex proxies, illustrating how approximate or relaxed constraints can diverge from exact error-rate equalization. Friedler et al.’s large-scale comparison surfaced how heterogeneous pipelines, base models, and constraint relaxations confound empirical claims across fairness interventions. Together these works revealed a need for a principled way to compare methods that use different base models and attain different levels of constraint satisfaction. The present study synthesizes these insights by introducing unprocessing—the conceptual inverse of postprocessing—to map any method’s outcome back onto the canonical ROC-based equalized-odds frontier, aligning base-model capacity and relaxation levels. This enables a clean, large-scale, apples-to-apples evaluation, revealing that the postprocessing Pareto frontier subsumes the performance of competing approaches.

---

*Analysis generated on: 2026-01-07T00:26:39.846975*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
