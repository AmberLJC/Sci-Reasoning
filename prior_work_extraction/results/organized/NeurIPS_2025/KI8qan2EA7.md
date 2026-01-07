# Prior Work Analysis Report

## Target Paper
**Title:** KI8qan2EA7
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**The Shapley Taylor Interaction Index** (2020)
- *Authors:* Kedar Dhamdhere et al.
- *Connection:* ProxySPEX’s goal of attributing higher-order feature interactions is grounded in the Shapley–Taylor formalization of interaction attributions that defines the problem objective it seeks to approximate efficiently.

### 💡 Inspiration

**A Lasso for Hierarchical Interactions** (2013)
- *Authors:* Jacob Bien et al.
- *Connection:* The strong heredity (hierarchy) principle formalized by Bien–Taylor–Tibshirani motivates ProxySPEX’s core assumption that higher-order interactions co-occur with their lower-order subsets, enabling a more efficient interaction search.

**Extracting Tree-Structured Representations of Trained Networks** (1996)
- *Authors:* Mark Craven et al.
- *Connection:* ProxySPEX adapts the classic surrogate-model idea of training trees on a neural network’s queries to the modern LLM setting, distilling masked-output behavior into an interpretable tree ensemble for interaction mining.

### 📊 Baseline

**SPEX: Efficiently Discovering Sparse Feature Interactions in LLMs** (2025)
- *Authors:* Justin Singh Kang et al.
- *Connection:* ProxySPEX directly replaces SPEX’s inference-heavy sparse-interaction search with a boosted-tree proxy fit to the same masked LLM outputs, retaining SPEX’s sparsity premise while eliminating tens of thousands of model calls.

### 🔧 Extension

**From local explanations to global understanding with explainable AI for trees** (2020)
- *Authors:* Scott M. Lundberg et al.
- *Connection:* ProxySPEX leverages tree-based exact interaction readouts (e.g., TreeSHAP-style path-based interaction values) from gradient-boosted trees trained on masked LLM outputs, extending these techniques to serve as a proxy for black-box LLM interaction discovery.

### 🔗 Related Problem

**Predictive Learning via Rule Ensembles** (2008)
- *Authors:* Jerome H. Friedman et al.
- *Connection:* Friedman–Popescu introduced interaction quantification in tree ensembles (e.g., the H-statistic), which ProxySPEX operationalizes by ranking interactions extracted from its boosted-tree proxy of the LLM.

**Detecting Statistical Interactions from Neural Network Weights** (2018)
- *Authors:* Michael Tsang et al.
- *Connection:* This work demonstrated scalable discovery of sparse, higher-order interactions in neural nets, reinforcing the sparsity premise ProxySPEX assumes and informing its focus on non-enumerative interaction detection.

---

## Synthesis

ProxySPEX’s core advance—efficiently attributing sparse, hierarchical feature interactions in LLMs—emerges by fusing three strands of prior work. First, the problem formulation comes from interaction attribution via Shapley–Taylor, which defines how higher-order effects should be measured but suffers from combinatorial explosion. SPEX directly tackled this by exploiting interaction sparsity for LLMs, yet required tens of thousands of masked inferences; ProxySPEX takes SPEX’s objective as the primary baseline while addressing its key limitation: inference cost. Second, ProxySPEX draws on decades of tree-based interaction analysis. Friedman and Popescu showed that ensembles can quantify interaction strength; Lundberg et al. later provided exact, efficient interaction attributions for tree models (e.g., TreeSHAP), making trees a practical substrate for extracting multi-order interactions. ProxySPEX extends this paradigm by fitting gradient-boosted trees to masked LLM outputs and then reading out interactions from the proxy, eliminating further LLM calls. Third, the algorithm’s efficiency hinges on the strong heredity (hierarchical) assumption from statistics (Bien–Taylor–Tibshirani), positing that higher-order interactions are accompanied by their subsets. This structural prior focuses the search and aligns naturally with how trees capture interactions through split hierarchies. Complementing these, neural interaction detection work (Tsang et al.) provides evidence and techniques for scalable, non-enumerative discovery of sparse interactions in deep models. Together, these works directly shape ProxySPEX’s design: the objective from Shapley–Taylor, the baseline and gap from SPEX, the proxy-extraction mechanism from tree explainability, and the hierarchy prior from statistical heredity.

---
*Generated: 2026-01-06T23:08:23.940828*
