# Prior Work Analysis Report

## Target Paper

**Title:** Initializing Models with Larger Ones

**Conference:** ICLR 2024 (spotlight)

**Authors:** Zhiqiu Xu, Yanjie Chen, Kirill Vishniakov, Yida Yin, Zhiqiang Shen, Trevor Darrell, Lingjie Liu, Zhuang Liu

**Keywords:** Deep Learning, Neural Networks, Weight Initialization, Small Models, Computer Vision

**Abstract:** 
> Weight initialization plays an important role in neural network training. Widely used initialization methods are proposed and evaluated for networks that are trained from scratch. However, the growing number of pretrained models now offers new opportunities for tackling this classical problem of weight initialization. In this work, we introduce weight selection, a method for initializing smaller models by selecting a subset of weights from a pretrained larger model. This enables the transfer of ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Net2Net: Accelerating Learning via Knowledge Transfer** (2016)
- *Authors:* Tianqi Chen et al.
- *Direct Connection:* Net2Net established function-preserving transformations to map weights across architectures of different width/depth, supplying the core premise that weights can be transferred across sizes that this paper adopts in the reverse (large-to-small) direction via selection.

### 💡 Inspiration

**Network Morphism** (2016)
- *Authors:* Tianxiang Wei et al.
- *Direct Connection:* Network Morphism generalized Net2Net’s weight mappings to add/remove layers and change widths while preserving functions, inspiring the idea that a smaller network can be initialized by a structured subset of a larger network’s parameters.

**The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks** (2019)
- *Authors:* Jonathan Frankle et al.
- *Direct Connection:* LTH demonstrated that subnetworks initialized with inherited weights can train effectively, motivating the paper’s strategy of selecting a subnetwork from a pretrained larger model to initialize a smaller one for faster, better training.

### 🔍 Gap Identification

**Once for All: Train One Network and Specialize it for Efficient Deployment** (2020)
- *Authors:* Han Cai et al.
- *Direct Connection:* OFA showed that many smaller models can inherit weights by slicing a specially trained supernet, and this paper addresses its key limitation by enabling weight subset selection from standard pretrained large models that were not trained as supernets.

### 📊 Baseline

**Distilling the Knowledge in a Neural Network** (2015)
- *Authors:* Geoffrey Hinton et al.
- *Direct Connection:* Knowledge distillation is the dominant baseline for leveraging a large model to improve a small one, against which the paper positions weight selection as a complementary, weight-level initialization alternative.

### 🔧 Extension

**Slimmable Neural Networks** (2019)
- *Authors:* Jiahui Yu et al.
- *Direct Connection:* This work introduced the practical 'first-k' channel/head slicing rule for instantiating thinner sub-networks from a larger set of shared weights, which the current paper generalizes by selecting compatible weight subsets from an off-the-shelf pretrained larger model without slimmable training.

---

## Synthesis: How Prior Work Led to This Paper

Slimmable neural networks established a concrete recipe for deriving thinner models by slicing the first k channels or heads from a shared, larger weight space, showing that submodels can operate effectively with subset weights if trained appropriately. Once-for-All advanced this idea by training a supernet that supports a large family of architectures via progressive shrinking, enabling subnets to directly inherit weights without retraining, but only when the parent model was specially trained for such slicing. Net2Net introduced function-preserving mappings such as Net2WiderNet and Net2DeeperNet, proving that weights can be systematically transferred across networks of different width and depth to accelerate training. Network Morphism broadened these transformations to a more general class of architecture changes, including adding or removing layers while preserving function, further grounding the feasibility of weight-level transfers across sizes. The Lottery Ticket Hypothesis provided the key empirical insight that subnetworks with inherited initializations can train rapidly and reach strong performance, underscoring the value of selecting rather than reinitializing parameters. In parallel, knowledge distillation became the standard pathway to exploit large models for small ones, but it transfers behaviors via outputs or features rather than weights.
Together, these works suggested a gap: weight inheritance is powerful but typically requires supernet training or upward morphisms, while popular transfer methods focus on targets, not parameters. The natural next step is to directly initialize smaller models by selecting compatible subsets of weights from ordinary pretrained large models, blending slimmable-style slicing with morphism-inspired structural mapping to deliver faster, stronger small-model training without specialized pretraining.

---

*Analysis generated on: 2026-01-06T23:33:49.080343*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
