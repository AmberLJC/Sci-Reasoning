# Prior Work Analysis Report

## Target Paper

**Title:** Role of Locality and Weight Sharing in Image-Based Tasks: A Sample Complexity Separation between CNNs, LCNs, and FCNs

**Conference:** ICLR 2024 (spotlight)

**Authors:** Aakash Lahoti, Stefani Karp, Ezra Winston, Aarti Singh, Yuanzhi Li

**Keywords:** Deep Learning Theory, Sample Complexity, Convolutional Neural Networks

**Abstract:** 
> Vision tasks are characterized by the properties of locality and translation invariance. 
    The superior performance of convolutional neural networks (CNNs) on these tasks is widely attributed to the inductive bias of locality and weight sharing baked into their architecture.
    Existing attempts to quantify the statistical benefits of these biases in CNNs over locally connected convolutional neural networks (LCNs) and fully connected neural networks (FCNs) fall into one of the following cate...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Group Equivariant Convolutional Networks** (2016)
- *Authors:* Taco Cohen et al.
- *Direct Connection:* This paper formalized translation equivariance/invariance via weight sharing, providing the conceptual basis for modeling data as shifted local patches—a structural assumption the DSD task explicitly encodes.

**On the Expressive Power of Deep Convolutional Networks via Hierarchical Tensor Decompositions** (2016)
- *Authors:* Nadav Cohen et al.
- *Direct Connection:* This paper connected locality and weight sharing to concrete representational advantages, grounding the idea that shared filters capture recurring local patterns across positions, as operationalized in the DSD construction.

### 💡 Inspiration

**SGD Learns Over-Parametrized Convolutional Networks (One-Filter Case) with Global Pooling** (2017)
- *Authors:* Alon Brutzkus et al.
- *Direct Connection:* Proving that SGD can provably learn a single shared convolutional filter under a teacher–student model inspired this paper’s optimization-aware analysis showing how weight sharing reduces sample complexity on the DSD task.

### 🔍 Gap Identification

**On the Inductive Bias of Neural Tangent Kernels** (2019)
- *Authors:* Stéphane Bietti et al.
- *Direct Connection:* This work quantified the benefits of convolutional inductive biases through kernel-based uniform-convergence bounds but lacked separating lower bounds and optimization-aware analysis, a gap this paper explicitly addresses.

**On the Power and Limitations of Convolutional Neural Networks** (2019)
- *Authors:* Gal Yehudai et al.
- *Direct Connection:* By using simplified synthetic setups to probe CNN advantages, this paper highlighted that common tasks do not faithfully encode both locality and translation invariance, directly motivating the more realistic DSD task introduced here.

**Convolutional Neural Tangent Kernels** (2019)
- *Authors:* Sanjeev Arora et al.
- *Direct Connection:* By characterizing CNN inductive bias through the CNNTK and providing generalization upper bounds without matching lower bounds, this work underscored the need for the separation results established here.

---

## Synthesis: How Prior Work Led to This Paper

Kernel-based analyses established that convolutional inductive biases confer statistical advantages: Bietti and Mairal showed how locality and translation invariance manifest in neural tangent kernels, while Arora and collaborators’ CNNTK characterized the function spaces induced by CNNs. These works offered uniform-convergence style upper bounds but stopped short of matching lower bounds or optimizer-aware learning guarantees. From a representational perspective, Cohen and colleagues formalized how weight sharing and local connectivity encode translation equivariance and compositional structure, theoretically grounding the role of shared filters in capturing repeated local patterns. Complementing these, Brutzkus and collaborators provided optimization results indicating SGD can learn a single shared filter with global pooling in a teacher–student setting, evidencing an algorithmic pathway for exploiting convolutional structure. Meanwhile, Yehudai and Shamir used simplified synthetic tasks to probe CNN strengths and weaknesses, illuminating that commonly used benchmarks do not simultaneously capture realistic locality and translation invariance. Collectively, these works revealed a gap: we had either representational or kernel-based arguments without separating lower bounds and with oversimplified tasks, or optimization results on too narrow setups. The current paper synthesizes these strands by introducing the Dynamic Signal Distribution task, which encodes both locality and translation invariance, and by giving optimization-aware analyses with separating sample-complexity bounds for CNNs versus LCNs and FCNs, showing precisely how weight sharing and locality reduce data requirements.

---

*Analysis generated on: 2026-01-06T07:47:37.341374*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
