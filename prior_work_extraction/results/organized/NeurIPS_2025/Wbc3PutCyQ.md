# Prior Work Analysis Report

## Target Paper
**Title:** Wbc3PutCyQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Puppeteer unifies automatic rigging and animation by marrying classic rigging objectives with modern sequence and graph-transformer modeling. The problem formulation and quality targets are rooted in Pinocchio and Bounded Biharmonic Weights: Pinocchio defined the pipeline of inferring a plausible skeletal hierarchy and LBS skinning from a static mesh, while BBW codified what high-quality, topology-aware skinning weights should look like. RigNet catalyzed the shift to learning-based rigging, showing that skeletons and skinning can be predicted by neural networks; Puppeteer advances this paradigm with a more expressive transformer design.

On the modeling side, Puppeteer’s auto-regressive skeleton generator is directly informed by sequence/graph generation research: GraphRNN motivates viewing joint sets and their connections as a generative sequence with principled ordering, and XLNet inspires Puppeteer’s stochastic perturbation of hierarchical orderings to obtain bidirectional context benefits within an autoregressive objective. For skinning prediction, Puppeteer’s topology-aware joint attention borrows from Graphormer’s core idea of injecting shortest-path/graph-distance biases into attention, enabling the network to reason over the skeletal graph explicitly rather than only via learned embeddings.

Finally, to animate the auto-rigged assets, Puppeteer draws on deformation-transfer principles to retarget motions onto predicted skeletons in a rig-consistent manner. Together, these works converge to a coherent system: an autoregressively generated, hierarchically valid skeleton; attention-based, topology-aware skinning; and motion retargeting, yielding a practical end-to-end rig-and-animate pipeline for diverse 3D models.

---
*Generated: 2026-01-07T00:21:32.350553*
