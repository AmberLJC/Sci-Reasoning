# Prior Work Analysis Report

## Target Paper
**Title:** T62TYoF8R3
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

FPSAttention targets the principal performance bottleneck in modern video diffusion—3D spatiotemporal attention—by co-designing FP8 quantization and sparsity with training awareness and a hardware-native kernel. The architectural context for this focus stems from Video Diffusion Models and latent video diffusion variants, which cemented 3D/temporal attention as core to high-quality video synthesis. On the quantization side, the FP8 formats and scaling recipes introduced by Micikevicius et al. provide the numerical foundation and hardware alignment that FPSAttention exploits; FlashAttention-3 further shows how tile-wise scheduling and FP8 tensor-core paths can be engineered for both speed and accuracy, guiding FPSAttention’s native kernel and tiling choices. For sparsity, SparseGPT highlights both the promise and pitfalls of training-free, unstructured pruning in transformer blocks, underscoring the need for training-aware calibration to avoid catastrophic quality loss—especially acute in diffusion. SpQR goes a step further by evidencing that sparsity and low-bit quantization should be coordinated rather than stacked independently, motivating FPSAttention’s unified 3D tile granularity that simultaneously governs both mechanisms. Finally, Karras et al.’s analysis of diffusion noise schedules clarifies that error tolerance is timestep-dependent, directly informing FPSAttention’s denoising-step–aware policy that adapts quantization and sparsity across the trajectory. Together, these works crystallize the need for a training-aware, tile-coherent, FP8-and-sparsity co-design specialized for 3D video attention.

---
*Generated: 2026-01-07T00:21:32.312647*
