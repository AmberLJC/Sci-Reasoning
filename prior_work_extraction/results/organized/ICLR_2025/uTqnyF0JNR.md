# Prior Work Analysis Report

## Target Paper

**Title:** IGL-Bench: Establishing the Comprehensive Benchmark for Imbalanced Graph Learning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Jiawen Qin, Haonan Yuan, Qingyun Sun, Lyujin Xu, Jiaqi Yuan, Pengfeng Huang, Zhaonan Wang, Xingcheng Fu, Hao Peng, Jianxin Li, Philip S. Yu

**Keywords:** imbalanced graph learning, graph class-imbalance, graph topology-imbalance, comprehensive benchmark

**Abstract:** 
> Deep graph learning has gained grand popularity over the past years due to its versatility and success in representing graph data across a wide range of domains. However, the pervasive issue of imbalanced graph data distributions, where certain parts exhibit disproportionally abundant data while others remain sparse, undermines the efficacy of conventional graph learning algorithms, leading to biased outcomes. To address this challenge, Imbalanced Graph Learning (IGL) has garnered substantial at...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Open Graph Benchmark: Datasets for Machine Learning on Graphs** (2020)
- *Authors:* Weihua Hu et al.
- *Direct Connection:* OGB established standardized datasets, splits, and evaluation protocols for graph learning, providing the benchmarking philosophy and many base datasets that IGL-Bench extends specifically to the imbalanced-graph setting.

**Topology Imbalance in Graph Neural Networks** (2023)
- *Authors:* Yifan Wang et al.
- *Direct Connection:* By defining and evidencing topology-imbalance as distinct from label imbalance, this work motivated IGL-Bench’s inclusion of topology-aware settings and metrics beyond mere class-frequency imbalance.

### 💡 Inspiration

**Benchmarking Graph Neural Networks** (2020)
- *Authors:* Vijay Prakash Dwivedi et al.
- *Direct Connection:* This work codified rigorous, uniform training and evaluation pipelines for GNNs, directly inspiring IGL-Bench’s emphasis on fair, controlled protocols across heterogeneous models and tasks.

### 🔍 Gap Identification

**Imbalanced Graph Learning: A Survey** (2023)
- *Authors:* Xin Liu et al.
- *Direct Connection:* The survey formalized IGL taxonomies (e.g., class- vs topology-imbalance) and explicitly highlighted inconsistent datasets, splits, and metrics across papers—gaps that IGL-Bench directly addresses with a comprehensive, standardized benchmark.

**Long-Tailed Node Classification on Graphs** (2021)
- *Authors:* Han Liu et al.
- *Direct Connection:* This line of work showed that many IGL methods are evaluated on customized splits and ad-hoc metrics, directly motivating IGL-Bench to unify protocols to make results comparable and reproducible.

### 📊 Baseline

**GraphSMOTE: Imbalanced Node Classification on Graphs with Graph Neural Networks** (2021)
- *Authors:* Chao Huang et al.
- *Direct Connection:* GraphSMOTE is a seminal IGL method using synthetic minority node generation and connectivity augmentation, serving as a canonical algorithm that IGL-Bench implements under unified settings to anchor comparisons.

**TAIL-GCL: Tail-class Oriented Graph Contrastive Learning for Long-Tailed Node Classification** (2022)
- *Authors:* Jing Zhang et al.
- *Direct Connection:* TAIL-GCL introduced a contrastive learning paradigm tailored to long-tailed node distributions, representing the self-supervised IGL family that IGL-Bench systematically evaluates and contrasts under consistent splits and metrics.

---

## Synthesis: How Prior Work Led to This Paper

Standardized graph benchmarks first emerged with the Open Graph Benchmark, which popularized consistent datasets, splits, and metrics for fair GNN evaluation. Complementing this, Benchmarking Graph Neural Networks distilled principled, reproducible pipelines for model training and assessment, shaping best practices for rigorous comparisons. In imbalanced graph learning specifically, GraphSMOTE pioneered synthetic minority oversampling and topology-aware edge construction, becoming a representative technique for countering label skew in node classification. The self-supervised direction was pushed by TAIL-GCL, which designed contrastive objectives to preferentially improve tail classes, exemplifying a distinct family of IGL approaches. Surveys on imbalanced graph learning then systematized the field, delineating class- and topology-imbalance and stressing the community’s fragmented datasets, custom splits, and inconsistent metrics. Closely, works on topology imbalance formalized structural skew as a core challenge separate from label frequencies, underscoring the need for evaluation setups that capture topology-induced bias. Research on long-tailed node classification further documented that reported gains often hinge on idiosyncratic experimental choices, impeding meaningful progress tracking. Against this backdrop, a natural next step was to synthesize these threads into a unified, comprehensive benchmark that spans both class- and topology-imbalance, curates diverse datasets, and re-implements a broad set of IGL algorithms under consistent preprocessing, splits, and metrics. Building on OGB-style rigor and prior IGL methodological diversity, the benchmark resolves comparability gaps and reveals robust insights about when and why different IGL families succeed.

---

*Analysis generated on: 2026-01-06T16:19:01.550756*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
