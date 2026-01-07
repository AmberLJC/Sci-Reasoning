# Prior Work Analysis Report

## Target Paper

**Title:** RMP-SAM: Towards Real-Time Multi-Purpose Segment Anything

**Conference:** ICLR 2025 (oral)

**Authors:** Shilin Xu, Haobo Yuan, Qingyu Shi, Lu Qi, Jingbo Wang, Yibo Yang, Yining Li, Kai Chen, Yunhai Tong, Bernard Ghanem, Xiangtai Li, Ming-Hsuan Yang

**Keywords:** segment anything; real-time segmentation; multi-purpose model;

**Abstract:** 
> Recent segmentation methods, which adopt large-scale data training and transformer architecture, aim to create one foundation model that can perform multiple tasks.
    However, most of these methods rely on heavy encoder and decoder frameworks, hindering their performance in real-time scenarios.
    To explore real-time segmentation, recent advancements primarily focus on semantic segmentation within specific environments, such as autonomous driving. However, they often overlook the generalizat...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Masked-attention Mask Transformer for Universal Image Segmentation (Mask2Former)** (2022)
- *Authors:* Bowen Cheng et al.
- *Direct Connection:* RMP-SAM adopts the Mask2Former idea of per-mask queries with masked-attention decoding as the unified representation to support multi-task segmentation within a single model.

**Panoptic Segmentation** (2019)
- *Authors:* Alexander Kirillov et al.
- *Direct Connection:* The panoptic segmentation formulation and metrics define the joint semantic+instance targets that RMP-SAM’s unified head must produce in its panoptic mode.

**YouTube-VIS: A Large-Scale Video Instance Segmentation Benchmark** (2019)
- *Authors:* Linjie Yang et al.
- *Direct Connection:* YouTube-VIS establishes the VIS problem and benchmark that RMP-SAM explicitly targets with real-time mask association and tracking-aware outputs.

### 🔍 Gap Identification

**SEEM: Segment Everything Everywhere All at Once** (2023)
- *Authors:* Xueyan Zou et al.
- *Direct Connection:* SEEM showed a single promptable model can cover diverse segmentation modes but is computationally heavy, motivating RMP-SAM’s push to achieve comparable breadth in real time.

### 📊 Baseline

**MobileSAM: Towards Fast Segment Anything** (2023)
- *Authors:* Chaoning Zhang et al.
- *Direct Connection:* MobileSAM serves as the primary real-time interactive segmentation baseline that RMP-SAM generalizes beyond, extending speed-oriented SAM designs from a single task to a multi-purpose setting.

### 🔧 Extension

**Segment Anything** (2023)
- *Authors:* Alexander Kirillov et al.
- *Direct Connection:* RMP-SAM directly extends SAM’s promptable mask-decoder paradigm by redesigning it to produce task-conditioned masks for interactive, panoptic, and video instance segmentation while making the encoder–decoder real-time.

### 🔗 Related Problem

**Video Mask2Former** (2023)
- *Authors:* Bowen Cheng et al.
- *Direct Connection:* RMP-SAM leverages the Video Mask2Former insight of temporally updating mask queries to maintain instance identities across frames, adapting it under a real-time budget for VIS.

---

## Synthesis: How Prior Work Led to This Paper

Segment Anything introduced a promptable mask decoder that predicts high-quality masks conditioned on points, boxes, or masks, but its ViT-H backbone and heavy decoder hinder real-time use. Mask2Former established a unified segmentation formulation using per-mask queries with masked attention, enabling a single architecture to handle semantic, instance, and panoptic outputs. Video Mask2Former extended this idea temporally, updating mask queries across frames to maintain instance identity and produce coherent video segmentation. SEEM demonstrated that a single promptable framework can cover interactive, open-vocabulary, and video-style segmentation with diverse prompts, but its compute cost limits real-time deployment. MobileSAM showed that SAM’s promptable pipeline can be distilled and re-architected for speed, proving real-time interactive segmentation is feasible even if restricted to a single task. The panoptic segmentation formulation precisely defines the joint semantic+instance target and evaluation criteria for unified image-level outputs. YouTube-VIS formalized video instance segmentation as temporally consistent instance masks and provided the benchmark that drives real-time, multi-instance video evaluation.

Together, these works reveal both the unifying representational leverage of mask-query decoding (Mask2Former/Video Mask2Former) and the practicality of promptable segmentation (SAM) while exposing a gap: no single system handles interactive, panoptic, and VIS in real time. RMP-SAM fuses SAM’s promptable mask decoding with Mask2Former’s per-mask query unification, draws temporal association cues from Video Mask2Former, and applies MobileSAM-style efficiency principles, aligning training and outputs to the panoptic and YouTube-VIS formulations to deliver a single end-to-end, real-time multi-purpose segmenter.

---

*Analysis generated on: 2026-01-06T11:59:04.679200*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
