# Prior Work Analysis Report

## Target Paper

**Title:** Energy-based Backdoor Defense Against Federated Graph Learning

**Conference:** ICLR 2025 (oral)

**Authors:** Guancheng Wan, Zitong Shi, Wenke Huang, Guibin Zhang, Dacheng Tao, Mang Ye

**Keywords:** Federated Learning, Graph Learning

**Abstract:** 
> Federated Graph Learning is rapidly evolving as a privacy-preserving collaborative approach. However, backdoor attacks are increasingly undermining federated systems by injecting carefully designed triggers that lead to the model making incorrect predictions. Trigger structures and injection locations in Federated Graph Learning are more diverse, making traditional federated defense methods less effective. In our work, we propose an effective Federated Graph Backdoor Defense using Topological Gr...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**How to Backdoor Federated Learning** (2020)
- *Authors:* Eugene Bagdasaryan et al.
- *Direct Connection:* Establishes model-replacement backdoor attacks in FL and shows that standard aggregation can be subverted, directly motivating a defense that can detect and downweight malicious clients during aggregation.

### 💡 Inspiration

**Energy-based Out-of-Distribution Detection** (2020)
- *Authors:* Weitang Liu et al.
- *Direct Connection:* Introduces the energy score from model logits to separate in- vs. out-of-distribution samples, which is directly adapted to encode low energy for benign graphs and high energy for constructed malicious substitutes at each client.

**Learning from Labeled and Unlabeled Data with Label Propagation** (2002)
- *Authors:* Xiaojin Zhu et al.
- *Direct Connection:* Provides the principle of propagating and smoothing signals over a constructed graph, which directly informs the server-side step of building a global energy graph and propagating energy to harmonize selected clients and adjust aggregation weights.

### 🔍 Gap Identification

**FLTrust: Byzantine-robust Federated Learning via Trust Bootstrapping** (2020)
- *Authors:* Xiang Li et al.
- *Direct Connection:* Relies on a small trusted server dataset to derive client trust scores, a requirement this work explicitly removes by using unsupervised energy elements and graph-based propagation to weight aggregation without clean server data.

**GraphBackdoor: Backdoor Attack on Graph Neural Networks** (2021)
- *Authors:* Xiang Zhang et al.
- *Direct Connection:* Demonstrates diverse trigger structures and injection locations on graphs, highlighting why parameter-space defenses are brittle and motivating an energy/topology-aware defense tailored to graph data.

### 📊 Baseline

**Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent** (2017)
- *Authors:* El Mahdi El Mhamdi et al.
- *Direct Connection:* Krum’s distance-based benign-client selection is a primary robust aggregation baseline that this work replaces with energy-graph similarity to cope with graph-specific heterogeneity and backdoor diversity.

### 🔧 Extension

**FLAME: Taming Backdoors in Federated Learning** (2022)
- *Authors:* Tuan Anh Nguyen et al.
- *Direct Connection:* Proposes clustering-based client filtering for backdoor defense, which this work extends by clustering clients in the energy space and then refining selection via energy propagation rather than raw parameter-update similarity.

---

## Synthesis: How Prior Work Led to This Paper

Energy-based Out-of-Distribution Detection introduced a simple, calibrated energy score derived from network logits to distinguish in- from out-of-distribution inputs, showing that learned energy can capture distributional membership. FLAME advanced federated backdoor defenses by clustering client updates to isolate malicious behavior without relying on prior attack knowledge, highlighting the power of similarity-based client selection. Krum formalized robust aggregation through distance-based selection of benign updates, establishing a canonical baseline for filtering outliers in adversarial FL. FLTrust achieved robustness by estimating client trust via similarity to server-held clean gradients, but its dependence on trusted server data revealed a practicality gap in privacy-preserving FL. How to Backdoor Federated Learning demonstrated that model replacement can reliably implant backdoors under standard aggregation, solidifying the need for principled client selection and reweighting. GraphBackdoor showed that backdoors in graph neural networks can exploit both structural and feature triggers at varied injection sites, exposing the brittleness of parameter-space defenses to graph-specific attack diversity. Label Propagation established graph-based smoothing as a way to disseminate information across nodes, a general mechanism for homogenizing signals on a graph.
Together, these works suggest that defenses should (i) encode distributional membership explicitly (energy), (ii) select benign clients via similarity but in a representation aligned with data semantics, and (iii) refine selection through graph-based propagation rather than raw parameter distances or trusted data. The present work synthesizes these insights by constructing energy elements that separate benign and malicious behaviors locally, clustering them to select clients, and then forming a global energy graph to propagate and smooth trust before reweighting aggregation—naturally addressing graph backdoor diversity without server-side clean data.

---

*Analysis generated on: 2026-01-06T11:03:03.999868*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
