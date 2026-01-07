# Prior Work Analysis Report

## Target Paper

**Title:** CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Song Wang, Peng Wang, Tong Zhou, Yushun Dong, Zhen Tan, Jundong Li

**Keywords:** Fairness, Bias, Benchmark, Large Language Models

**Abstract:** 
> As Large Language Models (LLMs) are increasingly deployed to handle various natural language processing (NLP) tasks, concerns regarding the potential negative societal impacts of LLM-generated content have also arisen. To evaluate the biases exhibited by LLMs, researchers have recently proposed a variety of datasets. However, existing bias evaluation efforts often focus on only a particular type of bias and employ inconsistent evaluation metrics, leading to difficulties in comparison across diff...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**BBQ: A Hand-Built Bias Benchmark for Question Answering** (2022)
- *Authors:* Alicia Parrish et al.
- *Direct Connection:* BBQ’s ambiguous vs. disambiguated QA templates and bias-scoring scheme provide a core task and metric that CEB incorporates and normalizes within its broader compositional taxonomy.

**CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models** (2020)
- *Authors:* Nikita Nangia et al.
- *Direct Connection:* CrowS-Pairs’ minimal-pair formulation for stereotypical preference directly informs one of the task types and bias-type dimensions that CEB aggregates and evaluates with consistent metrics.

**StereoSet: Measuring stereotypical bias in pretrained language models** (2021)
- *Authors:* Moin Nadeem et al.
- *Direct Connection:* StereoSet’s stereotype-preference metrics (e.g., SS/ICAT) exemplify the metric fragmentation that CEB resolves by mapping and harmonizing such scores under a unified evaluation framework.

**BOLD: Dataset and Metrics for Measuring Biases in Open-Ended Language Generation** (2021)
- *Authors:* Sunipa Dhamala et al.
- *Direct Connection:* BOLD establishes open-ended generation bias evaluation across topical and demographic categories, a genre that CEB integrates and aligns with its broader social-group taxonomy and standardized metrics.

### 💡 Inspiration

**Holistic Evaluation of Language Models** (2022)
- *Authors:* Percy Liang et al.
- *Direct Connection:* HELM’s multi-dimensional, standardized evaluation and reporting framework inspires CEB’s fairness-specific standardization across tasks, groups, and metrics.

### 🔍 Gap Identification

**Language (Technology) is Power: A Critical Survey of "Bias" in NLP** (2020)
- *Authors:* Su Lin Blodgett et al.
- *Direct Connection:* Their critique that bias work uses inconsistent definitions, tasks, and metrics directly motivates CEB’s move to formalize a compositional taxonomy and unified evaluation criteria across datasets.

### 🔗 Related Problem

**CheckList: A Behavioral Testing Framework for NLP** (2020)
- *Authors:* Marco Tulio Ribeiro et al.
- *Direct Connection:* CheckList’s capability-matrix and compositional behavioral testing concept informs CEB’s design of a structured, compositional coverage across bias types, social groups, and tasks.

---

## Synthesis: How Prior Work Led to This Paper

Work on social bias in NLP revealed fundamental fragmentation: Blodgett et al. showed that definitions, tasks, and metrics are inconsistent, complicating comparison and progress. HELM demonstrated that holistic, multi-dimensional evaluation with standardized reporting can bring coherence across heterogeneous tasks and metrics. In bias-specific datasets, BBQ introduced a careful QA setup contrasting ambiguous and disambiguated contexts with a dedicated bias score, while CrowS-Pairs used minimal pairs to quantify stereotypical preferences in masked LMs. StereoSet advanced stereotype measurement with SS/ICAT, highlighting how different metrics target related but distinct notions of bias. For open-ended generation, BOLD broadened topical and demographic coverage and proposed metrics tailored to generative outputs, exemplifying another task family with its own scoring conventions. Complementing these, CheckList introduced a compositional behavioral testing mindset via capability matrices, encouraging systematic coverage rather than ad hoc probes. Taken together, these works established multiple task formulations (QA, minimal-pair discrimination, open-ended generation) and rich but incompatible metrics, while also hinting at the value of structured, comprehensive coverage. The natural next step was to synthesize these strands: adopt a holistic evaluation paradigm for fairness, define a compositional taxonomy spanning bias types, social groups, and tasks, and reconcile divergent scoring schemes into standardized metrics. By aggregating key datasets across these axes and aligning their measurements, a unified benchmark could enable fair, apples-to-apples comparisons of LLM bias and illuminate gaps in coverage.

---

*Analysis generated on: 2026-01-06T09:08:35.184295*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
