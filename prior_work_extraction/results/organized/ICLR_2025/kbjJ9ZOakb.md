# Prior Work Analysis Report

## Target Paper

**Title:** Learning and aligning single-neuron invariance manifolds in visual cortex

**Conference:** ICLR 2025 (oral)

**Authors:** Mohammad Bashiri, Luca Baroni, Ján Antolík, Fabian H. Sinz

**Keywords:** neural invariances, invariance manifold, MEI, implicit neural representations, contrastive learning, invariance alignment, clustering, visual cortex, macaque V1, primary visual cortex

**Abstract:** 
> Understanding how sensory neurons exhibit selectivity to certain features and invariance to others is central to uncovering the computational principles underlying robustness and generalization in visual perception. Most existing methods for characterizing selectivity and invariance identify single or finite discrete sets of stimuli. Since these are only isolated measurements from an underlying continuous manifold, characterizing invariance properties accurately and comparing them across neurons...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Evolving Images for Visual Neurons Using Deep Generative Networks** (2019)
- *Authors:* Carlos R. Ponce et al.
- *Direct Connection:* By establishing generator-based closed-loop optimization to obtain most-exciting inputs (MEIs) and diverse high-response exemplars for single neurons, this paper provided the starting point that the current work generalizes from discrete exemplars to a continuous invariance manifold.

**Metamers of the ventral stream** (2011)
- *Authors:* Jeremy Freeman and Eero P. Simoncelli
- *Direct Connection:* This work formalized the idea of equivalence classes (metamers) along representational manifolds, providing the conceptual basis for treating all stimuli that leave a unit’s representation unchanged as a continuous invariance manifold learned in the current paper.

### 💡 Inspiration

**Implicit Neural Representations with Periodic Activation Functions (SIREN)** (2020)
- *Authors:* Vincent Sitzmann et al.
- *Direct Connection:* SIREN’s continuous, differentiable image parameterization directly enables the current method’s INR-based learning of smooth, high-fidelity invariance manifolds around a neuron’s MEI.

### 🔍 Gap Identification

**Neural population control via deep image synthesis** (2019)
- *Authors:* Pouya Bashivan et al.
- *Direct Connection:* While demonstrating powerful closed-loop control of cortical activity with synthesized stimuli, this study yielded finite sets of excitatory images and lacked a principled way to characterize continuous invariances or compare them across neurons—limitations the present paper directly addresses.

### 🔧 Extension

**Learning continuous invariance manifolds of single neurons with implicit neural representations** (2024)
- *Authors:* Luca Baroni et al.
- *Direct Connection:* This work introduced the INR-based formulation for learning a continuous family of maximally exciting stimuli for an individual neuron, which the current paper extends by making the learned manifolds accurate and, crucially, aligning them across neurons to enable population-level comparisons.

### 🔗 Related Problem

**Generalization in data-driven models of primary visual cortex** (2020)
- *Authors:* Gregor Lurz et al.
- *Direct Connection:* By introducing retinotopy-aware shared-core modeling that disentangles shared computations from neuron-specific readouts, this paper motivated aligning neural properties (here, learned invariance manifolds) across neurons with different receptive field locations and sizes.

---

## Synthesis: How Prior Work Led to This Paper

Generator-driven closed-loop studies established how to elicit strong responses and explore tuning with synthesized images: Ponce et al. showed that deep generative models can produce most-exciting inputs and diverse high-response stimuli for individual neurons, and Bashivan et al. demonstrated population-level control using similar synthesis, but both approaches yielded finite, discrete exemplars. Freeman and Simoncelli introduced the metamers concept, framing sets of stimuli that a representation deems equivalent as continuous manifolds—an idea that naturally extends from perception to single-neuron response invariances. SIREN provided a practical mechanism to represent images as continuous implicit functions, making it possible to optimize over smooth, differentiable families of stimuli rather than isolated points. Building on these ingredients, Baroni et al. recently formulated an INR-based method to learn a continuous manifold of maximally exciting stimuli for a single neuron, providing the first concrete recipe to estimate neuron-specific invariance manifolds. In parallel, Lurz et al. showed that retinotopy-aware shared-core models can align computations across neurons with different receptive field positions and sizes, highlighting the importance of cross-neuron alignment. Together, these works reveal a gap: despite the ability to learn continuous manifolds per neuron, there is no principled way to accurately characterize them and align them across neurons for population-level analysis. The present paper synthesizes the metameric manifold perspective with INR-based continuous stimulus parameterization and retinotopy-aware alignment ideas, introducing a method that both learns high-fidelity single-neuron invariance manifolds and aligns them across neurons—enabling systematic clustering and comparison of invariance types in V1.

---

*Analysis generated on: 2026-01-06T14:02:16.734550*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
