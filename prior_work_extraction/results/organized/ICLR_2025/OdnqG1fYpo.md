# Prior Work Analysis Report

## Target Paper
**Title:** OdnqG1fYpo
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Moner’s key contribution—training-free joint motion correction and image reconstruction for undersampled radial MRI using an implicit neural representation—emerges at the intersection of untrained priors, continuous neural fields, physics-based reconstruction, and radial motion modeling. Deep Image Prior established that a randomly initialized network can serve as a strong image prior when optimized directly on a single measurement, providing Moner the blueprint to avoid large pretraining datasets. SIREN and the broader INR literature supplied the continuous coordinate-based representation that captures high-frequency image content and gradients, giving Moner a powerful, smoothness-aware prior well-suited to ill-posed MRI inversion.

From the MRI side, SSDU demonstrated that k-space data consistency alone can supervise reconstruction without ground-truth, guiding Moner’s unsupervised objective defined purely from undersampled measurements. Classic motion-corrected reconstruction work by Batchelor formalized incorporating motion within the forward model; Moner instantiates this principle by embedding rigid transforms directly into the INR-based MRI operator and co-optimizing motion and image. Radial MRI motion strategies, notably PROPELLER and XD-GRASP, showed that radial trajectories both tolerate motion and enable quasi-static motion modeling via self-navigation and motion-state binning; Moner leverages these ideas but unifies them into a single-shot, joint optimization. Finally, dynamic neural fields like D-NeRF illustrated how to fuse an implicit representation with a motion field; Moner translates this to MRI by integrating a quasi-static rigid motion model into its INR, achieving accurate motion estimation and artifact-free reconstruction without external training data.

---
*Generated: 2026-01-07T00:02:04.913739*
