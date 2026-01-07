# Prior Work Analysis Report

## Target Paper
**Title:** gKdjHLrHDS
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Classification and Geometry of General Perceptual Manifolds** (2018)
- *Authors:* SueYeon Chung et al.
- *Connection:* Introduced manifold capacity theory and concrete geometric metrics (e.g., manifold radius, dimension, capacity) that this paper directly employs to quantify how task-relevant representational manifolds change during feature learning.

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Connection:* Formalized the lazy (linearized) training regime that underpins the ‘lazy’ side of the lazy–rich dichotomy, providing the theoretical baseline this paper critiques and moves beyond using representational geometry.

**Mean-field theory of two-layer neural networks: dimension-free bounds on population risk** (2018)
- *Authors:* Song Mei et al.
- *Connection:* Provided the contrasting mean-field (feature-learning/rich) regime and training dynamics, forming the other pole of the dichotomy that this paper refines by uncovering diverse sub-regimes via manifold geometry.

### 💡 Inspiration

**How Does the Brain Solve Visual Object Recognition?** (2012)
- *Authors:* James J. DiCarlo et al.
- *Connection:* Articulated the ‘untangling’ principle for object manifolds in the ventral stream; this conceptual lens directly inspires the paper’s core idea that learning manifests as the untangling of task-relevant manifolds.

### 🔍 Gap Identification

**On Lazy Training in Differentiable Programming** (2019)
- *Authors:* Lénaïc Chizat et al.
- *Connection:* Characterized conditions leading to lazy training and the absence of feature learning, highlighting a limitation that directly motivates this paper’s need to dissect multiple feature-learning behaviors beyond a simple dichotomy.

### 📊 Baseline

**Kernel and Rich Regimes in Overparameterized Models** (2020)
- *Authors:* Blake E. Woodworth et al.
- *Connection:* Codified the prevailing kernel (lazy) versus rich taxonomy; the current work directly improves upon this baseline categorization by proposing a geometry-based framework that reveals a richer taxonomy of feature learning.

### 🔧 Extension

**Separability and geometry of object manifolds in deep neural networks** (2020)
- *Authors:* Uri Cohen et al.
- *Connection:* Demonstrated that deep networks progressively untangle object manifolds across layers; the present work extends this framework from static layer-wise comparisons to temporal learning dynamics, revealing distinct feature-learning regimes via manifold geometry.

---

## Synthesis

The paper’s core contribution—probing feature learning through the geometry of task-relevant manifolds to move beyond the lazy–rich dichotomy—rests on two converging intellectual lines. First, manifold-based representational theory from neuroscience and deep learning supplied the measurement language. Chung et al. (2018) established manifold capacity theory and quantitative geometric metrics for classification on object manifolds, while Cohen et al. (2020) showed that deep networks progressively untangle manifolds across layers. DiCarlo et al. (2012) provided the conceptual anchor of ‘untangling’ as the hallmark of effective representations. Together, these works directly enable the present paper’s shift from inspecting individual features to tracking geometry of task-relevant manifolds as learning unfolds.
Second, modern training-theory formalized the lazy–rich dichotomy that this work refines. Jacot et al. (2018) introduced the NTK framework capturing lazy, random-feature-like training, while Mei et al. (2018) developed mean-field analyses capturing feature-learning (rich) dynamics. Chizat and Bach (2019) clarified the conditions and limitations of lazy training, and Woodworth et al. (2020) codified the kernel-versus-rich taxonomy that became the field’s de facto baseline. The present paper directly addresses the gap these works leave—an overly coarse dichotomy—by using manifold geometry to reveal distinct learning behaviors shaped by algorithm, architecture, and data. In synthesis, prior manifold-geometry methods furnish the tools, and lazy–rich theory poses the motivating limitation; their intersection yields a principled, geometry-first framework that uncovers a richer taxonomy of feature learning.

---
*Generated: 2026-01-06T23:07:19.568568*
