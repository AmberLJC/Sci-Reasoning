# Prior Work Analysis Report

## Target Paper

**Title:** Let SSMs be ConvNets: State-space Modeling with Optimal Tensor Contractions

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yan Ru Pei

**Keywords:** state-space models; convolution; tensor networks; audio processing; speech recognition

**Abstract:** 
> We introduce Centaurus, a class of networks composed of generalized state-space model (SSM) blocks, where the SSM operations can be treated as tensor contractions during training. The optimal order of tensor contractions can then be systematically determined for every SSM block to maximize training efficiency. This allows more flexibility in designing SSM blocks beyond the depthwise-separable configuration commonly implemented. The new design choices will take inspiration from classical convolut...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Efficiently Modeling Long Sequences with Structured State Spaces** (2022)
- *Authors:* Albert Gu et al.
- *Direct Connection:* This work introduced the SSM-as-convolution formulation and the prevalent depthwise-SSM + pointwise-mixing block pattern that Centaurus generalizes by reframing SSM computations as tensor contractions to enable richer (group/full) channel coupling.

### 💡 Inspiration

**Xception: Deep Learning with Depthwise Separable Convolutions** (2017)
- *Authors:* François Chollet
- *Direct Connection:* The depthwise-separable convolution paradigm formalized here is the direct analogue of the homogeneous, separable SSM blocks that Centaurus departs from when importing a broader convolutional design taxonomy into SSMs.

**Aggregated Residual Transformations for Deep Neural Networks (ResNeXt)** (2017)
- *Authors:* Saining Xie et al.
- *Direct Connection:* ResNeXt’s group convolution idea directly inspires Centaurus’s grouped SSM blocks, translating partial channel coupling into the SSM parameterization while maintaining efficiency through optimized contraction ordering.

**Deep Residual Learning for Image Recognition** (2016)
- *Authors:* Kaiming He et al.
- *Direct Connection:* The ResNet bottleneck (compress–transform–expand) pattern motivates Centaurus’s bottleneck SSM blocks, balancing compute/memory and capacity once SSMs are expressed as tensor contractions.

### 📊 Baseline

**Mamba: Linear-Time Sequence Modeling with Selective State Spaces** (2024)
- *Authors:* Albert Gu et al.
- *Direct Connection:* Mamba established highly efficient per-channel (depthwise) selective SSM blocks that serve as Centaurus’s primary baseline and whose limited intra-block channel mixing motivated Centaurus’s contraction-order-optimized group/full/bottleneck SSM designs.

### 🔧 Extension

**Optimized Einsum: Speeding up Einstein Summation in NumPy** (2018)
- *Authors:* Daniel G. A. Smith et al.
- *Direct Connection:* Centaurus extends contraction-path optimization from einsum/tensor-network literature to SSM computation graphs, systematically selecting near-optimal contraction orders that make non-separable SSM blocks trainable and memory-efficient.

---

## Synthesis: How Prior Work Led to This Paper

Structured State Spaces (S4) established that linear state-space dynamics can be recast as long 1D convolutions, yielding an SSM layer typically implemented as depthwise per-channel filtering followed by pointwise channel mixing—a design that became the default SSM block. Mamba advanced this line by introducing selective (input-dependent) SSMs with linear-time scanning, but it retained the depthwise block structure that limits intra-block channel coupling. In convolutional networks, Xception codified depthwise separable convolutions, clarifying the accuracy–efficiency tradeoffs of fully separable operators and cementing a taxonomy that many SSM blocks implicitly mirror. ResNeXt introduced group convolutions to recover partial cross-channel interactions at controlled compute, while ResNet’s bottleneck pattern (1×1 reduce–3×3 compute–1×1 expand) showed how to trade width for efficiency without sacrificing representational power. Independently, the optimized einsum/tensor-network literature demonstrated that reordering tensor contractions can dramatically reduce memory and FLOPs by finding near-optimal contraction paths for a given computation graph.
Taken together, these works reveal both a design space and a bottleneck: SSMs inherited the separable-conv template for efficiency, but lacked a principled way to realize group/full/bottleneck variants without prohibitive training cost. By recasting SSM computations as explicit tensor contractions and importing contraction-path optimization, the current work unlocks efficient non-separable SSM blocks, directly instantiating group and bottleneck analogues from CNNs. This makes a heterogeneous mixture of SSM block types feasible, naturally extending S4/Mamba’s formulation to richer architectures that better balance capacity and efficiency for raw audio tasks.

---

*Analysis generated on: 2026-01-06T18:19:55.279572*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
