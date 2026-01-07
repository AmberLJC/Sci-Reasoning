# Prior Work Analysis Report

## Target Paper

**Title:** What should a neuron aim for? Designing local objective functions based on information theory

**Conference:** ICLR 2025 (oral)

**Authors:** Andreas Christian Schneider, Valentin Neuhaus, David Alexander Ehrlich, Abdullah Makkeh, Alexander S Ecker, Viola Priesemann, Michael Wibral

**Keywords:** local learning, interpretability, neuro-inspired, information theory, partial information decomposition

**Abstract:** 
> In modern deep neural networks, the learning dynamics of individual neurons are often obscure, as the networks are trained via global optimization. Conversely, biological systems build on self-organized, local learning, achieving robustness and efficiency with limited global information. Here, we show how self-organization between individual artificial neurons can be achieved by designing abstract bio-inspired local learning goals. These goals are parameterized using a recent extension of inform...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Nonnegative Decomposition of Multivariate Information** (2010)
- *Authors:* Paul L. Williams et al.
- *Direct Connection:* This paper introduced Partial Information Decomposition (PID) and the unique/redundant/synergistic partition that directly parameterizes the neuron-local objectives designed here.

### 💡 Inspiration

**Towards deep learning with segregated dendrites** (2017)
- *Authors:* H. Guerguiev et al.
- *Direct Connection:* It formalizes neurons receiving distinct feedforward, feedback, and lateral inputs for local learning, motivating the explicit treatment of these input classes whose contributions are shaped via PID.

### 🔧 Extension

**Quantifying Unique Information** (2014)
- *Authors:* Nils Bertschinger et al.
- *Direct Connection:* It provides an operational, optimization-based definition of unique information under fixed marginals, supplying the concrete semantics for the ‘unique’ term that the proposed local objective explicitly targets.

**Measuring multivariate redundant information with pointwise common change in surprisal** (2017)
- *Authors:* Robin A. A. Ince
- *Direct Connection:* By introducing a pointwise (sample-wise) redundancy/synergy measure, this work enables local decompositions that inform the construction of differentiable, neuron-local PID-weighted losses.

**BROJA-2PID: A Configurable Framework for Unique Information Decomposition of Two Sources** (2018)
- *Authors:* Abdullah Makkeh et al.
- *Direct Connection:* This toolbox operationalizes PID via practical estimators of unique, redundant, and synergistic information, making it feasible to optimize such quantities as targets for neuron-level learning.

### 🔗 Related Problem

**An approximation of the error backpropagation algorithm in a predictive coding network** (2017)
- *Authors:* James C. R. Whittington et al.
- *Direct Connection:* Demonstrating local objectives with feedback and lateral signals, this work highlights the need for principled, interpretable neuron-level goals—here provided by explicit control over unique/redundant/synergistic integration.

**Dendritic cortical microcircuits approximate the backpropagation algorithm** (2018)
- *Authors:* João Sacramento et al.
- *Direct Connection:* By showing compartmentalized neurons can use feedforward and feedback streams for credit assignment, it motivates designing local objectives that dictate how those streams should uniquely, redundantly, or synergistically contribute.

---

## Synthesis: How Prior Work Led to This Paper

Partial Information Decomposition (PID) introduced a principled way to parse how multiple sources relate to a target into unique, redundant, and synergistic components, establishing the vocabulary for controlling multi-source integration at a fine-grained level (Williams and Beer, 2010). An optimization-based semantics for unique information under fixed marginals anchored the meaning of ‘unique’ and provided a basis for deriving computable objectives (Bertschinger et al., 2014). Pointwise common change in surprisal supplied local (sample-wise) redundancy/synergy terms, making it possible to attribute information contributions at a resolution compatible with neuron-level learning signals (Ince, 2017). Practical PID toolkits and estimators, such as BROJA-2PID, translated these definitions into tractable computations, enabling optimization of unique, redundant, and synergistic quantities in practice (Makkeh et al., 2018). In parallel, neuroscience-inspired models posited neurons with distinct feedforward, feedback, and lateral compartments and showed that local learning can exploit these segregated streams (Guerguiev et al., 2017; Sacramento et al., 2018). Predictive-coding formulations further demonstrated that feedback and lateral signals can implement local objectives capable of training deep networks (Whittington and Bogacz, 2017). Together, these strands exposed a gap: while compartmentalized local learning was feasible, there was no principled, interpretable way to specify what each neuron should integrate from each input class. By marrying PID’s unique–redundant–synergistic calculus with compartmentalized input streams, the current work formulates explicit neuron-local objectives that weight and optimize these information components, yielding self-organized, interpretable control over how feedforward, feedback, and lateral inputs are integrated.

---

*Analysis generated on: 2026-01-06T10:17:01.885532*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
