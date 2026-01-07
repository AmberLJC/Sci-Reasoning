# Prior Work Analysis Report

## Target Paper

**Title:** TabReD: Analyzing Pitfalls and Filling the Gaps in Tabular Deep Learning Benchmarks

**Conference:** ICLR 2025 (spotlight)

**Authors:** Ivan Rubachev, Nikolay Kartashev, Yury Gorishniy, Artem Babenko

**Keywords:** Tabular Data, Benchmarks, Reality Check, Tabular Deep Learning, Applications

**Abstract:** 
> Advances in machine learning research drive progress in real-world applications. 
To ensure this progress, it is important to understand the potential pitfalls on the way from a novel method's success on academic benchmarks to its practical deployment. In this work, we analyze existing tabular deep learning benchmarks and find two common characteristics of tabular data in typical industrial applications that are underrepresented in the datasets usually used for evaluation in the literature.
Firs...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**OpenML Benchmarking Suites** (2017)
- *Authors:* Bernd Bischl et al.
- *Direct Connection:* This suite standardized the tabular benchmarks used by many studies but typically lacks timestamp metadata and features stemming from industrial pipelines, forming the foundational setup that TabReD revises.

**Leakage in Data Mining: Formulation, Detection, and Avoidance** (2011)
- *Authors:* S. Kaufman et al.
- *Direct Connection:* By formalizing how random splits induce leakage under temporal dependencies and engineered features, this work provides the methodological basis for TabReD's insistence on time-aware, leakage-resistant evaluation protocols.

### 💡 Inspiration

**WILDS: A benchmark of in-the-wild distribution shifts** (2021)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* WILDS introduced the principle of deployment-realistic, shift-aware evaluation via semantically meaningful splits, which TabReD adapts to tabular domains by enforcing time-based splits to reflect distribution drift.

### 🔍 Gap Identification

**Revisiting Deep Learning Models for Tabular Data** (2021)
- *Authors:* Yury Gorishniy et al.
- *Direct Connection:* This widely adopted benchmark relied on random splits and largely non-temporal, raw-feature datasets, directly motivating TabReD to fix these evaluation blind spots with time-based splits and more industrially realistic data curation.

**Why do tree-based models still outperform deep learning on tabular data?** (2022)
- *Authors:* Léonard Grinsztajn et al.
- *Direct Connection:* By concluding that tree models outperform deep nets on standard random-split academic datasets, this work exposed the very benchmark biases (absence of temporal drift and engineered-feature pipelines) that TabReD explicitly interrogates and rectifies.

**Tabular Data: Deep Learning is Not All You Need** (2022)
- *Authors:* Roy Shwartz-Ziv et al.
- *Direct Connection:* Its evidence against tabular deep learning rests on random cross-validation over common academic suites, highlighting the evaluation setting whose mismatch to deployment (temporal drift, engineered features) TabReD systematically addresses.

---

## Synthesis: How Prior Work Led to This Paper

A line of influential tabular learning studies consolidated evaluation on standardized academic datasets with random splits. Revisiting Deep Learning Models for Tabular Data established a comprehensive benchmark and popular baselines under random splitting, focusing on non-temporal tasks with largely raw features. Two follow-ups, Why do tree-based models still outperform deep learning on tabular data? and Tabular Data: Deep Learning is Not All You Need, used these same suites and protocols to argue the dominance of tree-based methods, implicitly assuming stationarity and overlooking pipeline-engineered features common in production. The OpenML Benchmarking Suites underpinned this ecosystem by providing widely reused tasks, which, while convenient, often lack timestamp metadata and preclude time-aware evaluation. In parallel, WILDS pioneered benchmark design that encodes real-world distribution shifts through semantically meaningful splits, demonstrating how evaluation must mirror deployment. Even earlier, Leakage in Data Mining formalized how random splits can leak future information—especially acute with engineered features and temporal dependence—and advocated leakage-resistant validation. Together these works reveal a gap: tabular deep learning evaluations have not systematically reflected temporal drift or the prevalence of engineered feature pipelines that shape signal and leakage in practice. Building on WILDS’s shift-aware split philosophy and the leakage principles from classic work, while directly revisiting the dominant OpenML-based protocols and conclusions, the current paper introduces a benchmark with time-based splits and datasets curated to reflect industrial feature pipelines, enabling a more faithful reality check of tabular methods.

---

*Analysis generated on: 2026-01-06T05:59:39.806241*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
