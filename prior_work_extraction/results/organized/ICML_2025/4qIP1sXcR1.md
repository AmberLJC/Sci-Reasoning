# Prior Work Analysis Report

## Target Paper
**Title:** 4qIP1sXcR1
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ResQ’s core idea—identify a low-rank subspace of high-variance activations and retain it in higher precision while quantizing the remaining dimensions—sits at the intersection of modern LLM quantization practice and classic transform-coding theory. LLM.int8 first exposed activation outliers as the fundamental obstacle to low-bit inference and introduced a mixed-precision remedy by isolating and computing outlier channels in higher precision, a conceptual lineage ResQ embraces and generalizes. SmoothQuant further cemented activation outliers as the bottleneck, proposing to smooth them via per-channel scaling that shifts difficulty into weights; ResQ instead attacks the problem directly in activation space by using PCA to extract principal directions that concentrate variance. AWQ and SpQR demonstrated that preserving salient directions or explicitly separating outliers while quantizing the rest can sustain accuracy at 4 bits—ResQ reinterprets this selectivity geometrically by protecting principal components and quantizing the orthogonal complement. Rotation-based methods such as RPTQ/QuaRot showed that orthogonal transforms (e.g., Hadamard) suppress heavy tails and equalize distributions; ResQ incorporates invariant random rotations within each subspace to further reduce outlier effects pre-quantization. The mixed-precision assignment itself is guided by sensitivity principles popularized by HAWQ, while its provable optimality aligns with transform-coding results from Gersho and Gray: PCA/KLT achieves optimal energy compaction, and allocating more bits to high-variance components minimizes quantization error. Together, these strands converge in ResQ’s principled, subspace-structured mixed-precision PTQ for weights, activations, and KV caches.

---
*Generated: 2026-01-07T00:21:32.383673*
