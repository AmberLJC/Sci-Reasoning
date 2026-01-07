# Prior Work Analysis Report

## Target Paper

**Title:** Coordinate-Aware Modulation for Neural Fields

**Conference:** ICLR 2024 (spotlight)

**Authors:** Joo Chan Lee, Daniel Rho, Seungtae Nam, Jong Hwan Ko, Eunbyung Park

**Keywords:** Neural Fields, Neural Representation

**Abstract:** 
> Neural fields, mapping low-dimensional input coordinates to corresponding signals, have shown promising results in representing various signals. Numerous methodologies have been proposed, and techniques employing MLPs and grid representations have achieved substantial success. MLPs allow compact and high expressibility, yet often suffer from spectral bias and slow convergence speed. On the other hand, methods using grids are free from spectral bias and achieve fast training speed, however, at th...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**On the Spectral Bias of Neural Networks** (2019)
- *Authors:* Nazim Rahaman et al.
- *Direct Connection:* By formalizing that MLPs learn low frequencies first, this work motivates CAM’s design to inject spectral-bias-free information from grids into hidden layers to accelerate high-frequency learning.

### 💡 Inspiration

**FiLM: Visual Reasoning with a General Conditioning Layer** (2018)
- *Authors:* Ethan Perez et al.
- *Direct Connection:* CAM directly adopts the FiLM-style feature-wise scale-and-shift conditioning, extending it so that the modulation parameters are generated from coordinate-dependent grid features.

**Semantic Image Synthesis with Spatially-Adaptive Normalization (SPADE)** (2019)
- *Authors:* Taesung Park et al.
- *Direct Connection:* SPADE’s spatially varying gamma/beta parameters motivate CAM’s coordinate-aware modulation by showing that conditioning via per-location scale/shift can inject spatial information throughout a network.

### 🔍 Gap Identification

**Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains** (2020)
- *Authors:* Matthew Tancik et al.
- *Direct Connection:* Positional encodings mitigate spectral bias for MLP-based neural fields but still require slow training and larger networks, a limitation CAM addresses by replacing fixed encodings with learned grid-driven modulation across layers.

**Plenoxels: Radiance Fields without Neural Networks** (2022)
- *Authors:* Alex Yu et al.
- *Direct Connection:* Plenoxels show grid-only fields train fast and avoid spectral bias but incur high memory, motivating CAM to use grids only to produce modulation signals while keeping a compact MLP backbone.

### 📊 Baseline

**Instant Neural Graphics Primitives with a Multiresolution Hash Encoding** (2022)
- *Authors:* Thomas Müller et al.
- *Direct Connection:* This work is the primary grid+MLP sequential baseline whose grid features are fed into a small MLP, and CAM departs from this design by using grid lookups to modulate intermediate MLP activations instead of supplying them only at the input/head.

### 🔗 Related Problem

**TensoRF: Tensorial Radiance Fields** (2022)
- *Authors:* Anpei Chen et al.
- *Direct Connection:* TensoRF exemplifies the prevalent sequential combination of learned grids with a small MLP, which CAM rethinks by using grid-derived parameters to modulate internal MLP features rather than serve solely as input.

---

## Synthesis: How Prior Work Led to This Paper

Spectral bias in MLPs was established by Rahaman et al., who showed that networks fit low frequencies first, impeding rapid learning of high-frequency signals. Tancik et al. proposed Fourier features to inject high-frequency content into coordinate-based MLPs, alleviating but not eliminating slow convergence and capacity demands. In contrast, explicit/grid methods like Plenoxels demonstrated that optimizing voxel grids yields spectral-bias-free behavior and very fast training, albeit at a substantial memory cost. Hybrid designs, typified by Instant-NGP’s multiresolution hash grids and TensoRF’s tensor decompositions, sequentially feed grid-derived features into a small MLP, capturing detail efficiently but still treating grids as inputs rather than pervasive conditioning. Separately, FiLM introduced feature-wise linear modulation—scale and shift applied to intermediate activations—as a powerful conditioning primitive, and SPADE extended this to spatially adaptive normalization, where per-location modulation injects spatial information throughout a network.
Taken together, these insights suggest a route to combine the frequency richness and speed of grids with the compactness of MLPs by making spatial/coordinate information a first-class conditioning signal across layers. The natural next step is to replace sequential grid-to-MLP pipelines and fixed positional encodings with coordinate-aware modulation: grid lookups generate per-layer scale/shift parameters that modulate hidden features, reducing spectral bias and accelerating convergence while avoiding the memory footprint of fully explicit grids.

---

*Analysis generated on: 2026-01-06T16:18:36.533243*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
