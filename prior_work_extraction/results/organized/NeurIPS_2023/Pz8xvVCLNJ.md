# Prior Work Analysis Report

## Target Paper
**Title:** Pz8xvVCLNJ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Zhang et al. frame the first systematic robustness study of deep no-reference VQA under adversarial manipulation as a constrained, black-box optimization problem in the spatiotemporal domain. Two strands of adversarial work directly shape their methodology. First, query-efficient black-box attack design is guided by stochastic search principles from Ilyas et al., while Square Attack contributes the crucial insight that localized, randomly sampled square regions yield strong black-box performance. The authors extend this to videos via patch-based random search across space and time, tailored to the regression nature of VQA scores. Second, boundary-focused optimization (Brendel et al.) and margin-style loss shaping (Carlini & Wagner) motivate their Score-Reversed Boundary Loss, which pushes predictions across a critical quality threshold and reverses the score direction, operationalizing a boundary-seeking objective for continuous outputs rather than class labels.

Their practical threat model is grounded by perceptual constraints: classical JND modeling (Watson) provides the invisibility criterion to which their perturbations must adhere, aligning the attack with human visual sensitivity rather than simple Lp norms. Finally, contemporary NR-VQA systems such as RAPIQUE supply representative, high-performing targets whose success in real applications necessitates a robustness audit. Together, these influences converge into a black-box, patch-based, JND-constrained attack with a boundary-aware loss tailored to VQA regression, enabling a principled assessment of the vulnerabilities of modern CNN/Transformer-based NR-VQA models.

---
*Generated: 2026-01-07T00:02:04.845908*
