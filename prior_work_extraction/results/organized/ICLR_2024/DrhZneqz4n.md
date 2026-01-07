# Prior Work Analysis Report

## Target Paper

**Title:** Single Motion Diffusion

**Conference:** ICLR 2024 (spotlight)

**Authors:** Sigal Raab, Inbal Leibovitch, Guy Tevet, Moab Arar, Amit Haim Bermano, Daniel Cohen-Or

**Keywords:** Deep Learning, Motion synthesis, Animation, Single Instance Learning, Generative models

**Abstract:** 
> Synthesizing realistic animations of humans, animals, and even imaginary creatures, has long been a goal for artists and computer graphics professionals. Compared to the imaging domain, which is rich with large available datasets, the number of data instances for the motion domain is limited, particularly for the animation of animals and exotic creatures (e.g., dragons), which have unique skeletons and motion patterns. In this work, we introduce SinMDM, a Single Motion Diffusion Model. It is des...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Human Motion Diffusion Model** (2023)
- *Authors:* Guy Tevet et al.
- *Direct Connection:* SinMDM adopts the diffusion-based formulation for motion (noise schedule, denoising objective, and motion parameterization) introduced by MDM, then redesigns the denoiser and training regime to work from a single motion instance.

### 💡 Inspiration

**SinGAN: Learning a Generative Model from a Single Natural Image** (2019)
- *Authors:* Tamar Rott Shaham et al.
- *Direct Connection:* SinGAN’s core idea of learning the internal patch statistics of a single example directly motivates SinMDM’s single-instance generative paradigm and its use of limited receptive fields to avoid overfitting.

**Deep Image Prior** (2018)
- *Authors:* Dmitry Ulyanov et al.
- *Direct Connection:* The finding that network inductive bias and local receptive fields can capture a single signal’s internal structure informs SinMDM’s shallow, locality-biased architecture for single-motion learning.

### 🔧 Extension

**SinFusion: Training Diffusion Models on a Single Image** (2023)
- *Authors:* I. Gur et al.
- *Direct Connection:* SinFusion demonstrates that diffusion models can be trained effectively on a single instance by carefully constraining capacity and conditioning, a principle SinMDM extends from images to temporal motion with a lightweight denoiser.

**Longformer: The Long-Document Transformer** (2020)
- *Authors:* Iz Beltagy et al.
- *Direct Connection:* Longformer’s sliding-window local attention directly inspires SinMDM’s use of local attention to restrict temporal receptive fields, mitigating overfitting and enabling arbitrary-length motion synthesis.

### 🔗 Related Problem

**Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition** (2018)
- *Authors:* Sijie Yan et al.
- *Direct Connection:* ST-GCN’s formulation of operations constrained by the skeleton’s kinematic graph underlies SinMDM’s topology-aware locality, allowing the denoiser to generalize across arbitrary skeletal rigs.

---

## Synthesis: How Prior Work Led to This Paper

Diffusion-based motion generation was crystallized by the Human Motion Diffusion Model, which established the denoising objective, noise schedule, and practical parameterization for sequences of skeletal poses. Independently, SinGAN revealed that a single example contains rich internal statistics; by learning local patch distributions with constrained receptive fields, a generator can synthesize diverse yet faithful variations from just one input. Deep Image Prior further showed that the inductive bias of shallow, locality-focused networks suffices to capture a single signal’s internal structure without external data. SinFusion then demonstrated that diffusion models themselves can be trained on a single instance, provided capacity and conditioning are carefully controlled—validating that diffusion’s noise-conditioning and iterative denoising can learn an instance’s internal distribution. For handling long sequences, Longformer introduced sliding-window attention that restricts receptive fields while preserving scalability. Finally, ST-GCN formalized modeling along a kinematic graph, reinforcing that locality with respect to skeletal topology is a robust inductive bias for pose sequences.
Synthesizing these insights, a natural gap emerges: motion diffusion had not been adapted to learn from a single motion while remaining topology-agnostic and avoiding overfitting. By merging diffusion for motion with single-instance internal learning, and by instantiating locality through shallow networks and windowed attention aligned with skeletal structure, the current work enables generation of long, diverse motions faithful to a single clip and applicable to arbitrary rigs—precisely the opportunity suggested by these prior advances.

---

*Analysis generated on: 2026-01-06T19:14:13.472814*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
