# Prior Work Analysis Report

## Target Paper

**Title:** Neural Fine-Tuning Search for Few-Shot Learning

**Conference:** ICLR 2024 (oral)

**Authors:** Panagiotis Eustratiadis, Łukasz Dudziak, Da Li, Timothy Hospedales

**Keywords:** stochastic, neural, architecture, search, few, shot, learning, adapters

**Abstract:** 
> In few-shot recognition, a classifier that has been trained on one set of classes is required to rapidly adapt and generalize to a disjoint, novel set of classes. To that end, recent studies have shown the efficacy of fine-tuning with carefully-crafted adaptation architectures. However this raises the question of: How can one design the optimal adaptation strategy? In this paper, we study this question through the lens of neural architecture search (NAS). Given a pre-trained neural network, our ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**SNAS: Stochastic Neural Architecture Search** (2019)
- *Authors:* Sirui Xie et al.
- *Direct Connection:* Provided the stochastic, differentiable NAS framework for optimizing discrete architectural choices, which this work adapts to select layer-wise adapter placement and freeze/fine-tune decisions under few-shot constraints.

**Rethinking Few-Shot Image Classification: a Good Embedding Is All You Need** (2020)
- *Authors:* Yonglong Tian et al.
- *Direct Connection:* Demonstrated that strong pretraining with minimal adaptation is highly competitive, crystallizing the problem of designing effective fine-tuning strategies that this paper automates via search.

**Meta-Dataset: A Dataset of Datasets for Learning to Learn from Few Examples** (2020)
- *Authors:* Eleni Triantafillou et al.
- *Direct Connection:* Defined a realistic, multi-domain few-shot evaluation protocol that this work explicitly targets and reports state-of-the-art results on, grounding the problem formulation and metrics.

### 💡 Inspiration

**Learning Multiple Visual Domains with Residual Adapters** (2017)
- *Authors:* Sylvestre-Alvise Rebuffi et al.
- *Direct Connection:* Introduced residual adapter modules and explored their placement in ResNets, providing the core idea of layer-inserted adapters that this work generalizes by automatically searching their arrangement for few-shot adaptation.

### 🔍 Gap Identification

**AdapterDrop: On the Efficiency of Adapters in Transformers** (2021)
- *Authors:* Philipp Rücklé et al.
- *Direct Connection:* Showed that not all layers require adapters and proposed heuristic dropping, directly motivating this paper’s principled NAS to learn which layers need adapters versus being frozen or fine-tuned.

### 📊 Baseline

**AdaptFormer: Adapting Vision Transformers for Efficient Transfer Learning** (2022)
- *Authors:* Shoufa Chen et al.
- *Direct Connection:* Established adapter-based transfer for ViTs with fixed, hand-designed placement, serving as the primary manual baseline whose adapter insertion strategy this work replaces with a learned, task-driven search.

---

## Synthesis: How Prior Work Led to This Paper

Residual adapters were introduced to enable lightweight, layer-inserted adaptation in deep networks, with early studies examining where in ResNets such modules should be placed to best handle domain shifts. Building on this, AdaptFormer established adapters as a practical, parameter-efficient mechanism for Vision Transformers, using fixed, hand-crafted choices for where to insert the modules along depth. Complementing these, AdapterDrop showed that inserting adapters everywhere is unnecessary and that dropping some layers can retain performance—albeit via heuristics rather than learning the best configuration. Independently, stochastic neural architecture search provided a way to optimize discrete architectural decisions through differentiable, sampling-based relaxations, enabling efficient exploration of large combinatorial design spaces. Meanwhile, transfer-based few-shot works revealed that strong pretraining plus minimal adaptation is highly competitive, focusing attention on which parts of a pretrained model to update versus freeze for rapid generalization. Meta-Dataset then codified a challenging, multi-domain few-shot evaluation regime that stresses the robustness of adaptation strategies.
These strands collectively exposed a clear opportunity: adapters are effective, placement matters, not all layers need updating, and discrete design choices can be optimized via stochastic NAS. The present work synthesizes these insights by treating the few-shot adaptation recipe itself as an architecture to search—jointly deciding where to place adapters and which layers to freeze or fine-tune—yielding task-driven configurations that outperform hand-engineered strategies under Meta-Dataset-style evaluation.

---

*Analysis generated on: 2026-01-06T18:15:56.146937*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
