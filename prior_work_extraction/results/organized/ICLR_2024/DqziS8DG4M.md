# Prior Work Analysis Report

## Target Paper

**Title:** Point2SSM: Learning Morphological Variations of Anatomies from Point Clouds

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jadie Adams, Shireen Elhabian

**Keywords:** Unsupervised learning, global correspondence, point cloud, statsitical shape modeling

**Abstract:** 
> We present Point2SSM, a novel unsupervised learning approach for constructing correspondence-based statistical shape models (SSMs) directly from raw point clouds. SSM is crucial in clinical research, enabling population-level analysis of morphological variation in bones and organs. Traditional methods of SSM construction have limitations, including the requirement of noise-free surface meshes or binary volumes, reliance on assumptions or templates, and prolonged inference times due to simultaneo...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**A Minimum Description Length Approach to Statistical Shape Modeling** (2002)
- *Authors:* R. H. Davies et al.
- *Direct Connection:* Point2SSM encodes the MDL/compactness principle from Davies et al. as a differentiable cohort-level loss to drive globally consistent correspondences without relying on explicit pairwise registrations.

### 🔍 Gap Identification

**Framework for the Statistical Shape Analysis of Brain Structures using SPHARM-PDM** (2006)
- *Authors:* M. Styner et al.
- *Direct Connection:* Point2SSM explicitly overcomes SPHARM-PDM’s reliance on clean, genus-0 meshes and spherical parameterization by learning correspondences directly from raw point clouds without templates.

**DeepSSM: A Deep Learning Framework for Statistical Shape Modeling of Anatomical Structures** (2020)
- *Authors:* S. Datar et al.
- *Direct Connection:* Unlike DeepSSM, which requires precomputed correspondences and curated surface/volume inputs, Point2SSM removes this dependence by learning correspondences unsupervised from raw point sets.

### 📊 Baseline

**ShapeWorks: Particle-based Shape Modeling** (2017)
- *Authors:* J. Cates et al.
- *Direct Connection:* The paper directly replaces ShapeWorks’ cohort-wide particle optimization with a learned predictor, while mimicking its entropy/compactness objectives to obtain correspondence-based SSMs.

### 🔗 Related Problem

**3D-CODED: 3D Correspondences by Deep Deformation of a Template** (2018)
- *Authors:* T. Groueix et al.
- *Direct Connection:* Point2SSM adopts the idea of learning dense correspondences from point sets but avoids 3D-CODED’s fixed template deformation by enforcing cohort-level SSM compactness to yield template-free, population-consistent landmarks.

**Deep Functional Maps: Structured Prediction for Dense Shape Correspondence** (2017)
- *Authors:* O. Litany et al.
- *Direct Connection:* Point2SSM draws on the learning-based paradigm for global shape correspondence introduced in functional-map methods while addressing their mesh/Laplacian dependency by operating directly on raw point clouds and targeting SSM consistency.

---

## Synthesis: How Prior Work Led to This Paper

The Minimum Description Length (MDL) formulation of Davies et al. established that high-quality shape correspondences should minimize model complexity (i.e., produce compact, low-variance population models), thereby defining a principled, cohort-level objective for statistical shape modeling. Particle-based ShapeWorks operationalized this by optimizing an entropy/compactness–driven energy to place correspondences across a cohort, showing that uniform coverage and global compactness can yield reliable SSMs without template parameterization. In contrast, SPHARM-PDM enforced correspondences through spherical harmonic parameterization of clean, genus-0 meshes, revealing both the utility of global correspondences and the fragility of template/assumption-heavy pipelines. Learning-based correspondence methods such as 3D-CODED demonstrated that dense correspondences can be predicted directly from point sets by deforming a template, while functional-map methods (e.g., Deep Functional Maps) showed how global consistency can be learned but typically require meshes and spectral bases. DeepSSM then brought deep learning to anatomical SSMs, but depended on precomputed correspondences and curated inputs, highlighting the need for end-to-end correspondence learning from raw data. Together, these works exposed a gap: classical SSM objectives efficiently define global correspondence quality, and deep methods can predict correspondences from point sets, yet no approach fused them to yield template-free, fast SSM inference from raw point clouds. Point2SSM takes the natural next step by embedding the MDL/particle compactness principle as a differentiable, cohort-level loss into a point-cloud predictor, producing globally consistent correspondence landmarks per shape without cohort optimization, templates, or mesh prerequisites.

---

*Analysis generated on: 2026-01-06T18:37:22.490100*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
