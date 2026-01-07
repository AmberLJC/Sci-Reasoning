# Prior Work Analysis Report

## Target Paper

**Title:** How Well Do Supervised 3D Models Transfer to Medical Imaging Tasks?

**Conference:** ICLR 2024 (oral)

**Authors:** Wenxuan Li, Alan Yuille, Zongwei Zhou

**Keywords:** Transfer Learning, Medical Image Analysis, Organ Segmentation

**Abstract:** 
> The pre-training and fine-tuning paradigm has become prominent in transfer learning. For example, if the model is pre-trained on ImageNet and then fine-tuned to PASCAL, it can significantly outperform that trained on PASCAL from scratch. While ImageNet pre-training has shown enormous success, it is formed in 2D, and the learned features are for classification tasks; when transferring to more diverse tasks, like 3D image segmentation, its performance is inevitably compromised due to the deviation...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**AMOS: A Large-Scale Abdominal Multi-Organ Benchmark for Versatile Medical Image Segmentation** (2022)
- *Authors:* Ji et al.
- *Direct Connection:* AMOS defined standardized abdominal organ segmentation tasks and label conventions that this paper adopts as key downstream benchmarks to quantify transfer from its supervised 3D pre-training.

### 🔍 Gap Identification

**AbdomenCT-1K: Is Abdominal Multi-Organ Segmentation A Solved Problem?** (2021)
- *Authors:* Ma et al.
- *Direct Connection:* AbdomenCT-1K showed the value of curated abdominal multi-organ supervision but was constrained to ~1K scans and fewer organs, motivating this paper’s AbdomenAtlas 1.1 with an order-of-magnitude more volumes and a richer, standardized label space.

**TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT** (2023)
- *Authors:* Wasserthal et al.
- *Direct Connection:* TotalSegmentator provided comprehensive voxel-wise labels but at ~1K scans and mixed whole-body coverage, highlighting the need for a much larger, abdomen-focused, high-quality supervised corpus that this paper delivers for 3D pre-training.

### 📊 Baseline

**Models Genesis: Generic Autodidactic Models for 3D Medical Image Analysis** (2019)
- *Authors:* Zongwei Zhou et al.
- *Direct Connection:* Models Genesis is the canonical self-supervised 3D pre-training approach that this work explicitly contrasts against, addressing its lack of semantic supervision by demonstrating the advantages of large-scale supervised 3D pre-training for downstream segmentation.

**nnU-Net: A Self-Configuring Method for Deep Learning-Based Biomedical Image Segmentation** (2021)
- *Authors:* Isensee et al.
- *Direct Connection:* nnU-Net serves as the dominant from-scratch segmentation baseline against which this work demonstrates the consistent benefits of supervised 3D pre-training on AbdomenAtlas across diverse targets.

### 🔧 Extension

**Med3D: Transfer Learning for 3D Medical Image Analysis** (2019)
- *Authors:* Chen et al.
- *Direct Connection:* Med3D established the supervised 3D pre-training paradigm on aggregated labeled medical datasets, which this paper directly scales up in scope and rigor by pre-training on AbdomenAtlas and systematically measuring transfer to diverse medical tasks.

---

## Synthesis: How Prior Work Led to This Paper

Supervised pre-training for 3D medical images was crystallized by Med3D, which aggregated labeled datasets to train generic 3D backbones and showed that such supervision transfers across medical tasks. In parallel, Models Genesis demonstrated that self-supervised pre-training on 3D volumes can yield transferable features, albeit without explicit anatomical semantics. Abdominal multi-organ datasets then sharpened the supervision available for organ-centric transfer: AbdomenCT-1K curated around a thousand abdominal CTs with consistent labels to study multi-organ segmentation, while AMOS standardized abdominal organ definitions and benchmarks across CT/MRI for broad evaluation. Complementing these, TotalSegmentator scaled label granularity to 104 anatomical structures but remained limited in sample size and was not abdomen-focused, underscoring that both scale and targeted anatomy matter for robust transfer. Throughout this period, nnU-Net set a strong from-scratch segmentation baseline, sometimes narrowing perceived gains from pre-training and raising the bar for demonstrating clear transfer benefits. Together, these works revealed a gap: existing 3D supervised resources were either too small, too heterogeneous in anatomy, or lacked the scale needed to decisively outperform strong from-scratch baselines. The natural next step was to scale the Med3D-style supervised paradigm within a coherent abdominal label space, pre-train modern 3D models at unprecedented data scale, and rigorously compare against self-supervised (Models Genesis) and from-scratch (nnU-Net) baselines on standardized downstream benchmarks (e.g., AMOS), thereby isolating when and how supervised 3D pre-training most effectively transfers.

---

*Analysis generated on: 2026-01-07T00:16:56.503523*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
