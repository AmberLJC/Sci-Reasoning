# Prior Work Analysis Report

## Target Paper

**Title:** LRM: Large Reconstruction Model for Single Image to 3D

**Conference:** ICLR 2024 (oral)

**Authors:** Yicong Hong, Kai Zhang, Jiuxiang Gu, Sai Bi, Yang Zhou, Difan Liu, Feng Liu, Kalyan Sunkavalli, Trung Bui, Hao Tan

**Keywords:** 3D Reconstruction, Large-Scale Training, Transformers

**Abstract:** 
> We propose the first Large Reconstruction Model (LRM) that predicts the 3D model of an object from a single input image within just 5 seconds. In contrast to many previous methods that are trained on small-scale datasets such as ShapeNet in a category-specific fashion, LRM adopts a highly scalable transformer-based architecture with 500 million learnable parameters to directly predict a neural radiance field (NeRF) from the input image. We train our model in an end-to-end manner on massive multi...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis** (2020)
- *Authors:* Ben Mildenhall et al.
- *Direct Connection:* LRM adopts the NeRF volumetric radiance field representation and its differentiable photometric rendering objective, directly predicting a scene-specific NeRF from a single image.

**Objaverse: A Universe of Annotated 3D Objects** (2023)
- *Authors:* Alexander Deitke et al.
- *Direct Connection:* LRM’s large-scale training is enabled by Objaverse’s massive, diverse 3D asset corpus and multi-view renderings, which provide the supervisory signal to learn a highly generalizable single-image-to-NeRF mapping.

### 🔍 Gap Identification

**ShapeNet: An Information-Rich 3D Model Repository** (2015)
- *Authors:* Angel X. Chang et al.
- *Direct Connection:* The community’s reliance on small, category-specific datasets like ShapeNet exposed limited generalization, a key limitation LRM overcomes by training on orders-of-magnitude larger and more diverse multi-view data.

### 📊 Baseline

**Zero-1-to-3: Zero-shot One Image to 3D Object** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* As a primary single-image-to-3D competitor that relies on diffusion-based view synthesis plus NeRF optimization, Zero-1-to-3 highlights the slowness and inconsistency LRM addresses with a direct, end-to-end NeRF prediction in seconds.

### 🔧 Extension

**pixelNeRF: Neural Radiance Fields from One or Few Images** (2021)
- *Authors:* Alex Yu et al.
- *Direct Connection:* LRM scales and generalizes the pixelNeRF idea of feed-forward, image-conditioned NeRF prediction by replacing small CNN-based conditioning with a 500M-parameter transformer and massive multi-view training data to enable single-image reconstruction without per-scene optimization.

### 🔗 Related Problem

**IBRNet: Learning Multi-View Image-Based Rendering** (2021)
- *Authors:* Qianqian Wang et al.
- *Direct Connection:* LRM builds on the generalizable-NeRF paradigm exemplified by IBRNet but eliminates the need for multiple input views at inference by learning to infer a full radiance field from a single image.

---

## Synthesis: How Prior Work Led to This Paper

Neural radiance fields established a differentiable volumetric rendering framework that represents scenes as view-dependent color and density along rays, providing a principled photometric training signal for learning 3D from images. Building on this representation, pixelNeRF introduced a feed-forward formulation that conditions a scene-specific radiance field on image features to reconstruct from one or few views, demonstrating that generalization across scenes is possible without per-scene optimization. IBRNet further advanced generalizable NeRFs by learning to aggregate multi-view features for robust novel view synthesis, but it still presumes multiple input views at inference. In parallel, Zero-1-to-3 showed a practical single-image-to-3D pipeline via diffusion-based novel view synthesis followed by NeRF optimization, yet its two-stage design is slow and can yield inconsistent geometry. Dataset scale is pivotal: ShapeNet popularized category-specific training but limited diversity encouraged overfitting, whereas Objaverse provided a massive, diverse corpus of 3D assets and multi-view renderings suitable for training high-capacity models. Together, these works suggested that feed-forward, image-conditioned radiance fields could scale with data to eliminate per-scene optimization. The evident gap was a single-image model that unifies generalizable NeRF conditioning with large-scale training and high-capacity architectures to directly output a full radiance field. LRM synthesizes these insights by leveraging Objaverse-scale supervision and a transformer-based, high-parameter model to map a single image to a NeRF in one pass, addressing the speed and generalization limits of diffusion-plus-optimization and few-view generalizable NeRF approaches.

---

*Analysis generated on: 2026-01-07T00:15:31.935751*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
