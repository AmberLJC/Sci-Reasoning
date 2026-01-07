# Prior Work Analysis Report

## Target Paper

**Title:** SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition

**Conference:** ICLR 2024 (spotlight)

**Authors:** Hongwei Ren, Yue Zhou, Xiaopeng LIN, Yulong Huang, Haotian FU, Jie Song, Bojun Cheng

**Keywords:** Spiking Neural Betwork, Point Cloud, Event Camera, Action Recognition

**Abstract:** 
> Event cameras are bio-inspired sensors that respond to local changes in light intensity and feature low latency, high energy efficiency, and high dynamic range. Meanwhile, Spiking Neural Networks (SNNs) have gained significant attention due to their remarkable efficiency and fault tolerance. By synergistically harnessing the energy efficiency inherent in event cameras and the spike-based processing capabilities of SNNs, their integration could enable ultra-low-power application scenarios, such a...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation** (2017)
- *Authors:* Charles R. Qi et al.
- *Direct Connection:* SpikePoint adopts PointNet’s permutation-invariant point-wise MLP plus symmetric aggregation paradigm as the foundational way to operate directly on unordered event point clouds without rasterization.

### 💡 Inspiration

**PointMLP: A MLP Architecture for Point Cloud Classification** (2022)
- *Authors:* Xinlong Ma et al.
- *Direct Connection:* SpikePoint is inspired by PointMLP’s efficient single-stage per-point processing that attains both local and global discrimination without heavy hierarchical modules, adapting this simplicity to a spiking setting.

### 🔍 Gap Identification

**PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space** (2017)
- *Authors:* Charles R. Qi et al.
- *Direct Connection:* SpikePoint explicitly avoids PointNet++’s multi-stage sampling/grouping hierarchy, addressing its latency and memory overhead by designing a single-stage spiking module that captures both local and global features.

**Event Spike Tensor: An Unbiased Representation for Event-based Cameras** (2019)
- *Authors:* Matthias Gehrig et al.
- *Direct Connection:* SpikePoint targets the core limitation of EST’s voxelized/temporal binning—loss of sparsity and extra data mapping—by operating directly on raw event points in an end-to-end spiking architecture.

**HATS: Histograms of Averaged Time Surfaces for Robust Event-based Object Classification** (2018)
- *Authors:* Alessio Sironi et al.
- *Direct Connection:* SpikePoint responds to HATS-style grid/histogram conversions that impose dense frames on asynchronous events by eliminating rasterization and keeping computations sparse in the point domain with spikes.

### 🔧 Extension

**Dynamic Graph CNN for Learning on Point Clouds (DGCNN)** (2019)
- *Authors:* Yue Wang et al.
- *Direct Connection:* SpikePoint extends DGCNN’s EdgeConv-style local neighborhood aggregation to a spike-driven formulation so that local geometric relations in event point clouds are extracted within an SNN while preserving sparsity.

---

## Synthesis: How Prior Work Led to This Paper

PointNet established that unordered sets can be processed directly with per-point MLPs and symmetric pooling, yielding global descriptors without resorting to grids. PointNet++ extended this by progressively grouping neighborhoods to model local structures, but its multi-stage hierarchy adds repeated sampling, neighborhood searches, and latency. DGCNN introduced EdgeConv, dynamically building k-NN graphs to encode local geometric relations while preserving permutation invariance, showing that local neighborhoods can be captured effectively alongside global aggregation. PointMLP later showed that a streamlined, single-stage per-point MLP augmented with lightweight geometric priors can recover both local discrimination and global semantics without complex hierarchical stacks. In the event-vision community, EST demonstrated voxelized temporal binning to make events CNN-friendly, while HATS built histogram-based time-surface representations; both convert sparse asynchronous events into dense grids, sacrificing sparsity and inducing extra data mapping before learning.

Together, these works suggested that event streams should be treated as point clouds to preserve sparsity, and that effective local-global feature extraction need not rely on heavy multi-stage hierarchies. SpikePoint synthesizes PointNet’s permutation-invariant point processing, DGCNN’s local neighborhood reasoning, and PointMLP’s single-stage efficiency, while directly addressing the EST/HATS rasterization gap by keeping the raw event cloud representation. The natural next step was to implement these point operators with spiking neurons and surrogate training, enabling an end-to-end, ultra-efficient, single-stage SNN that extracts local and global features on event clouds without dense conversions.

---

*Analysis generated on: 2026-01-06T13:38:49.336361*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
