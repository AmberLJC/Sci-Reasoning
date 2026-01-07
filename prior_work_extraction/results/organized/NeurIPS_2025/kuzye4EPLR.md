# Prior Work Analysis Report

## Target Paper
**Title:** kuzye4EPLR
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

FP4 All the Way synthesizes three strands of prior art to achieve fully quantized training of LLMs. First, foundational work on low-precision training established how to separate precisions across forward and backward passes and to manage dynamic range (Mixed Precision Training), while the FP8 literature codified concrete floating-point formats (E4M3/E5M2), per-tensor/group scaling, and pass-dependent rounding strategies that succeed in transformer training. These insights underpin the paper’s choice of NVFP4 (E2M1) for tensors combined with E4M3 block scales and the decision to employ stochastic rounding asymmetrically across passes.
Second, the 4-bit quantization line—ranging from post-training 4-bit methods with analytical scaling/clipping to QLoRA’s NF4 and group-wise scaling—demonstrated that 4-bit representations can be practical for large models when paired with carefully designed scale granularity and codebooks. FP4 All the Way extends this to the harder setting of full training, systematically testing block sizes (settling on 16) and scale formats, and finding that NVFP4 with E4M3 scaling is superior to alternatives.
Third, theory around gradient quantization (QSGD) and practice quantizing optimizer states (8-bit Optimizers) directly influenced the paper’s treatment of gradients and updates. The new gradient-norm threshold relative to quantization noise concretizes when FP4 training remains effective, while stochastic rounding in backward/updates controls bias and variance accumulation. Together, these threads enable the first end-to-end FP4 training pipeline for LLMs at scale.

---
*Generated: 2026-01-07T00:21:33.153131*
