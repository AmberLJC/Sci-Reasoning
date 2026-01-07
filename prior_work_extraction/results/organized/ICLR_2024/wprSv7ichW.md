# Prior Work Analysis Report

## Target Paper

**Title:** Benchmarking Algorithms for Federated Domain Generalization

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ruqi Bai, Saurabh Bagchi, David I. Inouye

**Keywords:** federated learning, distributed learning, domain generalization, out-of-distribution generalization, benchmarking, data paritioning.

**Abstract:** 
> While prior federated learning (FL) methods mainly consider client heterogeneity, we focus on the *Federated Domain Generalization (DG)* task, which introduces train-test heterogeneity in the FL context. Existing evaluations in this field are limited in terms of the scale of the clients and dataset diversity. Thus, we propose a Federated DG benchmark that aim to test the limits of current methods with high client heterogeneity, large numbers of clients, and diverse datasets. Towards this objecti...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**In Search of Lost Domain Generalization** (2020)
- *Authors:* Ishaan Gulrajani et al.
- *Direct Connection:* This work established the modern DG benchmarking protocol and suite (DomainBed), whose datasets, evaluation rigor, and adaptation of centralized DG methods directly underpin the federated DG benchmarking methodology adopted and extended here.

**WILDS: A Benchmark of in-the-Wild Distribution Shifts** (2021)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* WILDS formalized realistic train–test distribution shifts and provided diverse domain datasets that are directly repurposed via the paper’s partitioning scheme to create federated DG tasks at scale.

**Agnostic Federated Learning** (2019)
- *Authors:* Mehryar Mohri et al.
- *Direct Connection:* By framing FL objectives to be robust to unknown test-time mixtures over clients, this work motivates the train–test heterogeneity setting and evaluation criteria that the federated DG benchmark explicitly operationalizes.

### 🔍 Gap Identification

**LEAF: A Benchmark for Federated Settings** (2019)
- *Authors:* Sebastian Caldas et al.
- *Direct Connection:* LEAF popularized FL benchmarking and client-scale simulations but lacked domain-shift tasks and controllable domain heterogeneity, gaps the new benchmark fills with domain-aware partitioning and diverse datasets.

### 📊 Baseline

**FedBN: Federated Learning on Non-IID Features via Local Batch Normalization** (2021)
- *Authors:* Xiang Li et al.
- *Direct Connection:* FedBN is a principal heterogeneity-robust FL baseline that the benchmark explicitly includes and stress-tests, revealing its limitations under unseen-domain generalization in federated settings.

### 🔧 Extension

**Measuring the Effects of Non-Identical Data Distribution for Federated Learning** (2019)
- *Authors:* Tzu-Hsiang Hsu et al.
- *Direct Connection:* The widely used Dirichlet-based client partitioning from this paper is generalized into the paper’s new domain-aware partition method, enabling controlled client heterogeneity and variable client counts for any domain dataset.

**Invariant Risk Minimization** (2020)
- *Authors:* Martin Arjovsky et al.
- *Direct Connection:* IRM’s invariance principle is directly adapted as a DG algorithm within the federated training protocol to assess how invariance-based DG scales under multi-client, domain-shifted federated scenarios.

---

## Synthesis: How Prior Work Led to This Paper

Rigorous domain generalization (DG) evaluation was shaped by In Search of Lost Domain Generalization, which codified standardized datasets, strong ERM baselines, and careful model selection protocols that revealed how evaluation choices can overturn claims. WILDS extended this lens to real-world distribution shifts, curating datasets and metrics that emphasize train–test heterogeneity across domains. In federated learning (FL), Hsu et al. introduced Dirichlet-based client partitioning to control non-IID levels by tuning concentration parameters, creating a practical recipe for simulating client heterogeneity. Agnostic Federated Learning formalized robustness to unknown mixtures over client distributions, explicitly connecting FL training to worst-case generalization under distribution shift. FedBN demonstrated a strong, simple way to mitigate feature shift across clients by keeping batch-normalization local, becoming a de facto baseline for domain-shifted FL. In parallel, Invariant Risk Minimization proposed learning predictors whose optimality is invariant across environments, a central DG idea subsequently treated as a core algorithmic family to compare against. LEAF provided early FL benchmarks and client-scale evaluation practices, though without explicit domain-shift tasks. Taken together, these works expose a gap: DG rigor and OOD datasets exist, and FL has heterogeneity simulators and benchmarks, but there is no unified framework to stress-test DG methods under realistic federated client scales and controlled domain heterogeneity. The current work synthesizes DomainBed-style rigor with WILDS-like shifts, extends Dirichlet partitioning to domain-aware allocations, and systematically adapts DG methods (e.g., IRM) alongside FL heterogeneity baselines (e.g., FedBN), yielding a federated DG benchmark that isolates performance under scalable, controllable train–test heterogeneity.

---

*Analysis generated on: 2026-01-06T08:37:47.130287*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
