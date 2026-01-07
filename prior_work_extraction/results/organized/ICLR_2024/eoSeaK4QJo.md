# Prior Work Analysis Report

## Target Paper

**Title:** Towards Energy Efficient Spiking Neural Networks: An Unstructured Pruning Framework

**Conference:** ICLR 2024 (spotlight)

**Authors:** Xinyu Shi, Jianhao Ding, Zecheng Hao, Zhaofei Yu

**Keywords:** Spiking Neural Networks, Network Pruning

**Abstract:** 
> Spiking Neural Networks (SNNs)  have emerged as energy-efficient alternatives to  Artificial Neural Networks (ANNs) when deployed on neuromorphic chips.  While recent studies have demonstrated the impressive performance of deep SNNs on challenging tasks, their energy efficiency advantage has been diminished. Existing methods targeting energy consumption reduction do not fully exploit sparsity, whereas powerful pruning methods can achieve high sparsity but are not directly targeted at energy effi...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Loihi: A Neuromorphic Manycore Processor with On-Chip Learning** (2018)
- *Authors:* Mike Davies et al.
- *Direct Connection:* Loihi’s energy model and demonstrations that energy scales with spike and synapse activity established that unstructured connectivity sparsity yields real hardware energy savings, grounding the paper’s objective to maximize sparsity utilization.

### 💡 Inspiration

**Learning Efficient Convolutional Networks through Network Slimming** (2017)
- *Authors:* Zhuang Liu et al.
- *Direct Connection:* The idea of removing neurons/channels based on learned importance provided the key conceptual spark for introducing neuron-level importance and pruning—here adapted to unstructured neuron pruning for SNNs rather than structured channel pruning in ANNs.

### 🔍 Gap Identification

**Deep Residual Learning in Spiking Neural Networks** (2021)
- *Authors:* Wei Fang et al.
- *Direct Connection:* By pushing deep SNN accuracy with residual architectures while incurring higher spike activity and energy, this work highlighted the unmet need for sparsity-centric approaches to recover energy efficiency, which the new framework directly targets.

**Going Deeper with Directly-Trained Larger Spiking Neural Networks (with Temporal-Dependent Batch Normalization)** (2021)
- *Authors:* Zheng et al.
- *Direct Connection:* This paper demonstrated that deep, directly trained SNNs can match ANN accuracy but did not introduce energy-targeted sparsification, motivating the proposed pruning approach to explicitly exploit sparsity for energy savings.

**Temporal Efficient Training of Spiking Neural Networks** (2022)
- *Authors:* Deng et al.
- *Direct Connection:* By reducing timesteps to cut compute/energy without exploiting synaptic or neuron sparsity, this method exposed a complementary gap that the new framework fills via unstructured weight and neuron pruning.

### 📊 Baseline

**Learning both Weights and Connections for Efficient Neural Networks** (2015)
- *Authors:* Song Han et al.
- *Direct Connection:* This work’s magnitude-based unstructured weight pruning is adopted as the core weight-sparsification mechanism that the paper integrates into a spike- and energy-aware pruning framework.

---

## Synthesis: How Prior Work Led to This Paper

Magnitude-based unstructured weight pruning showed that many connections can be removed with minimal accuracy loss, establishing a practical route to fine-grained sparsity that maps well to computational savings. Network Slimming then demonstrated that neuron/channel importance can be learned and used to remove units, indicating that pruning at the neuron level—beyond weights—can further reduce compute. In spiking models, residual spiking architectures achieved strong accuracy, but their depth and activity increased spike events and compute, signaling that accuracy gains were eroding the energy advantage. Deeper, directly trained SNNs with temporal-dependent normalization similarly proved high performance was attainable without introducing mechanisms to curb spiking energy via structural sparsity. Temporal Efficient Training reduced timesteps, lowering temporal cost, yet left spatial sparsity largely untapped. Meanwhile, neuromorphic hardware results on Loihi made explicit that energy is tightly coupled to spike and synapse activity and that unstructured sparse connectivity directly translates to energy savings.
Bringing these threads together revealed a clear opportunity: combine fine-grained weight sparsity with neuron-level sparsity tailored to SNN dynamics to exploit neuromorphic sparsity end-to-end. The present framework synthesizes magnitude-based unstructured weight pruning with unstructured neuron pruning informed by spiking activity, directly targeting the energy model of neuromorphic processors. This is a natural next step after performance-centric deep SNNs and timestep reduction methods, aligning pruning granularity with hardware-relevant sparsity to restore and amplify SNN energy efficiency.

---

*Analysis generated on: 2026-01-07T00:24:57.428187*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
