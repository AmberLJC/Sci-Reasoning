# Prior Work Analysis Report

## Target Paper
**Title:** ltzTHGFF5i
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Jetfire’s key contribution—an end-to-end INT8 data flow for transformer pretraining coupled with per-block quantization—emerges from two converging lines of prior work: integer-only computation paths for transformers and accuracy-preserving quantization schemes. I-BERT established that transformers can be executed with integer-only arithmetic by carefully redesigning operations, while Jacob et al. formalized integer quantization dataflows with int8/int32 accumulations and rescaling. Jetfire extends these ideas beyond inference to pretraining, emphasizing that staying in INT8 throughout the block avoids the frequent dequantization that inflates memory traffic in standard QAT pipelines.

On the accuracy side, LSQ demonstrated that learning quantization scales is crucial, and DoReFa-Net popularized fully quantized training with STE—yet both typically rely on layer-wise quantize–compute–dequantize patterns that are suboptimal for transformers. For transformers specifically, LLM.int8() introduced blockwise/outlier-aware quantization for efficient 8-bit matmuls, and SmoothQuant tackled activation outliers via weight–activation smoothing to stabilize 8-bit inference. Jetfire draws on these insights to adopt per-block quantization that directly addresses transformer outliers during training, stabilizing INT8 forward and backward passes.

Finally, FP8 training results validated that 8-bit precision can maintain accuracy in large-scale transformer training with proper scaling and recipes. Jetfire leverages similar scaling discipline but in the INT8 integer domain, achieving superior memory-access efficiency and practical speedups by fusing an INT8-first dataflow with per-block quantization tailored to transformer pretraining.

---
*Generated: 2026-01-07T00:02:04.879010*
