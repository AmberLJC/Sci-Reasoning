# Prior Work Analysis Report

## Target Paper

**Title:** Generating Images with 3D Annotations Using Diffusion Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Wufei Ma, Qihao Liu, Jiahao Wang, Angtian Wang, Xiaoding Yuan, Yi Zhang, Zihao Xiao, Guofeng Zhang, Beijia Lu, Ruxiao Duan, Yongrui Qi, Adam Kortylewski, Yaoyao Liu, Alan Yuille

**Keywords:** Synthetic Data, Transfer Learning, Diffusion Models, 3D

**Abstract:** 
> Diffusion models have emerged as a powerful generative method, capable of producing stunning photo-realistic images from natural language descriptions. However, these models lack explicit control over the 3D structure in the generated images. Consequently, this hinders our ability to obtain detailed 3D annotations for the generated images or to craft instances with specific poses and distances. In this paper, we propose 3D Diffusion Style Transfer (3D-DST), which incorporates 3D geometry control...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Render for CNN: Viewpoint Estimation in Images Using CNNs Trained with Rendered 3D Model Views** (2015)
- *Authors:* Hao Su et al.
- *Direct Connection:* Render for CNN established the pipeline of rendering 3D models across viewpoints to obtain precise 6-DoF annotations, which 3D-DST uses as the geometry source before diffusion stylization.

**ShapeNet: An Information-Rich 3D Model Repository** (2015)
- *Authors:* Angel X. Chang et al.
- *Direct Connection:* ShapeNet provides the category-aligned CAD assets that are rendered from diverse poses to produce the edge prompts underpinning the method’s 3D-controllable image generation.

**Objaverse: A Universe of Annotated 3D Objects** (2023)
- *Authors:* Nate Deitke et al.
- *Direct Connection:* Objaverse supplies large-scale, diverse 3D meshes whose multi-view renders enable broad coverage of object shapes and poses for edge-conditioned diffusion generation with 3D annotations.

### 🔍 Gap Identification

**Contrastive Learning for Unpaired Image-to-Image Translation (CUT)** (2020)
- *Authors:* Taesung Park et al.
- *Direct Connection:* CUT represents the state-of-the-art GAN-based synthetic-to-real style transfer whose tendency to distort fine object geometry highlights the need for a diffusion-based transfer that preserves 3D structure.

### 📊 Baseline

**Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks (CycleGAN)** (2017)
- *Authors:* Jun-Yan Zhu et al.
- *Direct Connection:* As a primary unpaired translation baseline for sim-to-real, CycleGAN’s label drift and geometry changes motivate replacing GAN translation with a controllable diffusion process to maintain CAD-derived structure.

### 🔧 Extension

**Adding Conditional Control to Text-to-Image Diffusion Models** (2023)
- *Authors:* Lvmin Zhang et al.
- *Direct Connection:* 3D-DST directly adopts ControlNet’s conditional branch to inject Canny edge maps rendered from 3D CAD models, enabling structure-preserving generation while text controls the style.

### 🔗 Related Problem

**Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World** (2017)
- *Authors:* Josh Tobin et al.
- *Direct Connection:* Domain randomization showed synthetic training can transfer but leaves a realism gap and limited pose-specific control, motivating a photorealistic yet geometry-preserving alternative using diffusion.

---

## Synthesis: How Prior Work Led to This Paper

Conditional diffusion offered a way to inject structural constraints into text-to-image generation when ControlNet introduced a parallel conditioning branch that faithfully follows signals like Canny edges while preserving the semantic power of large T2I models. In parallel, unpaired image-to-image translation methods such as CycleGAN and CUT sought to bridge the synthetic-to-real gap for rendered assets, but both were prone to label drift and geometry distortion, especially under large domain shifts from CAD renders to photographs. Earlier, Render for CNN established the practical pipeline of rendering 3D models from multiple viewpoints to obtain precise 6-DoF labels, highlighting the value of 3D repositories as a source of richly annotated training imagery. ShapeNet created the category-aligned CAD corpus that made such rendering pipelines systematic, and Objaverse later expanded the scale and diversity of 3D assets, enabling broader coverage of object shapes, materials, and poses. Meanwhile, domain randomization demonstrated that heavy appearance randomization on renders can yield some transfer to real data, but at the cost of realism and without explicit control over geometry-specific factors like pose and distance.
Together these works reveal a clear opportunity: use large 3D repositories to generate perfectly annotated geometry, then replace GAN-based or randomized stylization with a controllable diffusion mechanism that locks geometry while achieving photorealistic style. By conditioning on edge maps rendered from CAD models, the approach inherits exact 3D annotations and explicit pose control from the rendering pipeline while leveraging ControlNet’s faithful structure following to avoid geometry drift, naturally yielding scalable, realistic images with reliable 3D labels.

---

*Analysis generated on: 2026-01-06T18:47:02.454723*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
