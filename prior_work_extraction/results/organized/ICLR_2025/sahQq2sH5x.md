# Prior Work Analysis Report

## Target Paper

**Title:** Benchmarking Predictive Coding Networks -- Made Simple

**Conference:** ICLR 2025 (spotlight)

**Authors:** Luca Pinchetti, Chang Qi, Oleh Lokshyn, Cornelius Emde, Amine M'Charrak, Mufeng Tang, Simon Frieder, Bayar Menzat, Gaspard Oliviers, Rafal Bogacz, Thomas Lukasiewicz, Tommaso Salvatori

**Keywords:** cognitive science, predictive coding, computational neuroscience

**Abstract:** 
> In this work, we tackle the problems of efficiency and scalability for predictive coding networks (PCNs) in machine learning. To do so, we  propose a library that focuses on performance and simplicity, and use it to implement a large set of standard benchmarks for the community to use for their experiments. As most works in the field propose their own tasks and architectures, do not compare one against each other, and focus on small-scale tasks, a simple and fast open-source library, and a compr...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Predictive coding in the visual cortex: a functional interpretation** (1999)
- *Authors:* Rao and Ballard
- *Direct Connection:* This work established the hierarchical predictive coding framework with prediction and error units that underlies the PCN formulations standardized and evaluated across tasks in the benchmark.

### 📊 Baseline

**An Approximation of the Error Back-Propagation Algorithm in a Predictive Coding Network** (2017)
- *Authors:* Whittington and Bogacz
- *Direct Connection:* Its supervised PCN learning rule that approximates backprop serves as the primary algorithmic baseline the library implements, optimizes, and scales to larger architectures and datasets.

### 🔧 Extension

**Predictive Coding Approximates Backprop Along Arbitrary Computation Graphs** (2020)
- *Authors:* Millidge et al.
- *Direct Connection:* The benchmark adopts this general formulation of PCN updates for arbitrary network graphs, implementing these variants to compare their efficiency and scalability under a unified setup.

### 🔗 Related Problem

**Equilibrium Propagation: Bridging the Gap Between Energy-Based Models and Backpropagation** (2017)
- *Authors:* Scellier and Bengio
- *Direct Connection:* Its two-phase nudging and energy-minimization procedure directly inspired algorithmic variants adapted into the PCN framework and included as standardized baselines in the benchmark.

**Random synaptic feedback weights support error backpropagation for deep learning** (2016)
- *Authors:* Lillicrap et al.
- *Direct Connection:* The idea of fixed random feedback pathways (Direct Feedback Alignment) is integrated as a PCN-compatible training variant to assess bio-plausible alternatives within the shared benchmarking suite.

**Difference Target Propagation** (2015)
- *Authors:* Lee et al.
- *Direct Connection:* Local target-setting from DTP motivates PCN variants with layerwise targets that the library implements to systematically compare against standard PCN learning on common datasets.

---

## Synthesis: How Prior Work Led to This Paper

Rao and Ballard formalized hierarchical predictive coding with distinct prediction and error units, defining the computational scaffold used by modern predictive coding networks. Whittington and Bogacz then provided a concrete supervised learning rule for these networks, showing iterative inference and local updates can approximate backpropagation, which quickly became the de facto PCN training baseline. Millidge and colleagues generalized this equivalence beyond simple chains, deriving update equations for arbitrary computation graphs and clarifying how PCN dynamics map onto standard deep models. In parallel, energy-based approaches like Equilibrium Propagation introduced two-phase nudged inference to compute gradients without explicit backprop, while Direct Feedback Alignment demonstrated that fixed random feedback pathways can guide deep learning without symmetric weight transport. Difference Target Propagation contributed a complementary local-learning perspective by constructing layerwise targets, enabling learning with only local signals rather than global error backpropagation.
Together these works established the PCN computational template, multiple closely related bio-plausible training mechanisms, and a set of algorithmic variants that had largely been evaluated on small-scale tasks with disparate implementations. This created a clear need for a unified, efficient platform to instantiate the canonical PCN rule and its generalizations, and to adapt EP-, DFA-, and DTP-inspired procedures within the same predictive-coding formalism. The present work naturally follows by standardizing these methods into a simple, high-performance library and comprehensive benchmarks, enabling fair, scalable comparisons across algorithms and architectures, and revealing how design choices and inference schemes impact PCN performance at modern scales.

---

*Analysis generated on: 2026-01-06T11:15:37.620598*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
