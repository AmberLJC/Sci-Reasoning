# Prior Work Analysis Report

## Target Paper
**Title:** ZZ09oX2Xpo
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DexGarmentLab sits at the intersection of dexterous manipulation, deformable-object simulation, and benchmark design. Foundational dexterous-hand works—OpenAI’s in-hand manipulation and DAPG—demonstrated that realistic hand kinematics, contact modeling, and learning-from-demonstrations are key to mastering complex skills, guiding DexGarmentLab’s focus on multi-finger, bimanual control and efficient data collection. On the deformable side, CLOTH3D offered large-scale, high-quality garment meshes across categories, which motivated DexGarmentLab’s asset pipeline and its central idea of leveraging structural correspondences to generalize across garment types. FabricFlowNet showed that embedding cloth structure (keypoints/flow) into policy or motion generation dramatically improves reliability in bimanual manipulation, directly informing DexGarmentLab’s automatic trajectory generation using garment structural correspondence from a small seed of supervision. To ensure practical deployment, domain randomization illuminated how to narrow the sim-to-real gap, a principle DexGarmentLab adapts with garment-specific physics refinements and randomized parameters for cloth-hand interactions. Finally, RLBench and MuJoCo provided the template and substrate for multi-task, reproducible benchmarks and high-fidelity contact dynamics, respectively. Together, these works directly shaped DexGarmentLab’s core contribution: a realistic, dexterous garment manipulation environment with scalable assets and an automatic, structure-aware dataset generation pipeline enabling generalizable policies across diverse garments and tasks.

---
*Generated: 2026-01-07T00:21:32.336169*
