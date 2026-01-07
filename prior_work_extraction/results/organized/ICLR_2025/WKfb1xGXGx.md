# Prior Work Analysis Report

## Target Paper
**Title:** WKfb1xGXGx
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**HairNet: Single-View Hair Reconstruction using Convolutional Neural Networks** (2018)
- *Authors:* Menglei Chai et al.
- *Connection:* Perm adopts HairNet’s strand-parameterization via scalp-aligned geometry textures but departs by explicitly disentangling global structure and local curl patterns and learning separate priors for each.

**Hair Meshes** (2009)
- *Authors:* Cem Yuksel et al.
- *Connection:* Hair Meshes popularized guide-based grooming and interpolation, which Perm echoes by learning guide textures (global structure) and residual textures (local variation) that emulate the practical grooming pipeline.

**A Morphable Model for the Synthesis of 3D Faces** (1999)
- *Authors:* Volker Blanz et al.
- *Connection:* Perm’s core idea of building a compact, controllable PCA parameter space for a complex geometry class directly follows the 3DMM paradigm, adapted to hair strands in the frequency domain.

### 💡 Inspiration

**Two-Layer Deep Hair Model from a Single Image** (2019)
- *Authors:* Yang Zhou et al.
- *Connection:* This work motivated Perm’s explicit separation of coarse hair shape and fine strand details; Perm formalizes that separation with a PCA-based strand representation in the frequency domain and distinct generative parameterizations for each layer.

**The Laplacian Pyramid as a Compact Image Code** (1983)
- *Authors:* Peter J. Burt et al.
- *Connection:* Perm’s decomposition of hair geometry textures into low- and high-frequency components draws on multiscale frequency separation principles exemplified by the Laplacian pyramid.

### 📊 Baseline

**Neural Haircut: Prior-Guided Strand-Based Hair Reconstruction** (2022)
- *Authors:* Saito et al.
- *Connection:* Neural Haircut established the idea of using a learned generative prior for strand-level 3D hair; Perm generalizes this into a parametric prior that separates guide (low-frequency) and residual (high-frequency) components to improve controllability and editing.

---

## Synthesis

Perm’s core contribution—a learned, controllable parametric model that disentangles global hair structure from local curl detail—emerges at the intersection of three intellectual threads. First, the 3D Morphable Model (Blanz and Vetter) established PCA-based parametric shape spaces for human geometry; Perm adapts this principle to hair by representing strands in the frequency domain and learning a compact PCA basis. Second, multiscale frequency decomposition (Burt and Adelson) informs Perm’s explicit split into low- (guide) and high-frequency (residual) components, enabling targeted generative modeling and precise control. Third, production grooming practice, formalized in Yuksel’s Hair Meshes, showed the efficacy of guide-driven global control with interpolated fine structure; Perm emulates this by learning guide textures and residual textures.
On the hair reconstruction side, HairNet introduced a scalp-aligned geometry texture parameterization and defined the modern problem setting for single-view hair prediction. Perm leverages that parameterization but addresses a key limitation in many successors—joint modeling of global and local features—by disentangling them in a principled way. Neural Haircut demonstrated the power of a learned prior for task-agnostic reconstruction, yet its coupled modeling limited precise editing. Perm extends that idea, providing a generative prior split across guide and residual spaces. Finally, two-layer deep hair modeling highlighted the benefits of decoupling base shape and details; Perm turns this intuition into a frequency-PCA formulation with separate generative models, yielding stronger control, editability, and performance across tasks.

---
*Generated: 2026-01-06T23:09:26.639313*
