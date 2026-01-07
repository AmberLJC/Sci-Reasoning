# Prior Work Analysis Report

## Target Paper
**Title:** QQBPWtvtcn
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LVSM’s core contribution—scalable, generalizable novel view synthesis with minimal 3D inductive bias—arises at the intersection of three lines of work. First, NeRF and 3D Gaussian Splatting established that high-fidelity view synthesis often hinges on explicit 3D structure and rendering pipelines. LVSM explicitly rejects those priors, setting a target to match or exceed their quality purely through data-driven learning. Second, generalizable NVS methods such as pixelNeRF and MVSNeRF demonstrated across-scene performance from sparse views but relied on 3D sampling along rays or plane-sweep cost volumes, embedding strong geometry into architecture. LVSM retains the generalization objective while discarding these hand-crafted geometric operators, replacing them with learned attention over image tokens.
Third, geometry-free scene representation work—most notably the Scene Representation Transformer and the earlier Generative Query Network—showed that a model can infer a latent scene from context views and render queries without explicit 3D supervision. LVSM directly builds on this abstraction but scales it: an encoder–decoder variant uses a fixed number of 1D latent tokens as a learned scene memory, while a decoder-only variant removes intermediate latents entirely to maximize capacity and quality. This latent-token design tracks the Perceiver IO family’s latent bottleneck for handling large token sets efficiently, enabling scalability in both views and resolution. Together, these influences shape LVSM’s two architectures and training recipe, yielding a purely learned, transformer-based NVS system that attains state-of-the-art quality and zero-shot generalization without 3D inductive biases.

---
*Generated: 2026-01-06T23:42:48.085699*
