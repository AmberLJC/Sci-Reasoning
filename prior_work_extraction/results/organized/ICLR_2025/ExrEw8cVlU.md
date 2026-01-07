# Prior Work Analysis Report

## Target Paper
**Title:** ExrEw8cVlU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Poison-splat’s key contribution—turning 3D Gaussian Splatting’s training loop into a computational liability via input poisoning—rests on two intertwined lines of prior work. First, the representation and optimization mechanics of 3DGS define the attack surface: Kerbl et al. detail the gradient-driven densification, splitting, and pruning that determine the number of Gaussians and, consequently, the memory and time footprint. Poison-splat exploits these levers, crafting inputs that provoke pathological densification and push 3DGS toward its worst-case complexity and even OOM. Second, the paper’s attack design and optimization toolkit draw from the data-poisoning literature. The bilevel formulation traces to Biggio et al.’s poisoning framework, while influence functions (Koh and Liang) and bilevel differentiation methods (Franceschi et al.) provide scalable approximations for computing hypergradients through training. Practical poisoning objectives from clean-label attacks (Shafahi et al.) and gradient matching (Geiping et al.) shape Poison-splat’s surrogate losses, enabling poisons that remain visually plausible yet manipulate training dynamics to maximize resource usage. Finally, the strategic focus on computation cost and denial-of-service echoes systems-oriented adversarial work like DeepSloth, reframing the attacker’s goal from accuracy degradation to compute inflation. Together, these works directly inform Poison-splat’s choice of target (3DGS), objective (compute/memory blow-up), and optimization machinery (bilevel/influence/gradient-matching), culminating in a practical, scalable compute-cost attack that exposes a new security vulnerability in modern 3D reconstruction pipelines.

---
*Generated: 2026-01-07T00:02:04.909925*
