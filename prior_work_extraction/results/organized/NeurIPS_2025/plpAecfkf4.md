# Prior Work Analysis Report

## Target Paper
**Title:** plpAecfkf4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

SQS fuses two lines of progress: query-centric transformers for autonomous driving and differentiable multi-view rendering. On the rendering side, NeRF inaugurated view-synthesis as a powerful self-supervised signal, while 3D Gaussian Splatting replaced volumetric fields with efficient, stable, and differentiable 3D Gaussians. SQS adopts this representation not as an end in itself, but as a pretraining target: it asks sparse queries to predict Gaussian parameters and uses splatting-based reconstruction of multi-view images and depth to inject fine-grained geometric and photometric priors into the queries. On the transformer side, DETR introduced the notion of learnable queries and interaction mechanisms, refined by Deformable DETR’s reference-point sampling. In multi-camera 3D perception, DETR3D’s 3D-to-2D querying and BEVFormer’s cross-view deformable attention provided the mechanics to connect 3D queries to multi-view features, while Sparse4D demonstrated that efficient sparse perception models can eschew dense BEV/volumetric construction entirely. SQS synthesizes these ideas: it replaces point-like references with richer Gaussian primitives during pretraining, leverages cross-view deformable sampling to couple queries with images, and then uses DETR-style query interaction to bridge pre-trained Gaussian queries with task-specific queries for occupancy and detection. This pretraining-to-finetuning pathway directly targets SPMs, yielding stronger context encoding without sacrificing their hallmark efficiency.

---
*Generated: 2026-01-07T00:21:32.359519*
