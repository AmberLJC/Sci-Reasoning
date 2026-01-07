# Prior Work Analysis Report

## Target Paper
**Title:** nN8TnHB5nw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s key contribution—stable 4-bit storage of optimizer moments via fine-grained, 2D-aware quantization and a zero-point–free linear quantizer for the second moment—sits at the intersection of three prior lines of work. First, block-wise compression of optimizer states (Dettmers et al., 8-bit Optimizers) proved that Adam’s moments can be quantized without destabilizing training, but it plateaued at 8 bits and struggled with heterogeneity inside blocks. Second, memory-reduction strategies that exploit matrix structure (Adafactor) showed that row- and column-wise statistics capture much of the variation in second moments; this structural insight directly inspires using both row- and column-wise information in the quantization scheme to tame complex, anisotropic outlier patterns observed in moment tensors. Third, advances in low-bit quantization for LLMs (LLM.int8, QLoRA) revealed that outliers and distribution shape are decisive at ultra-low precision, and that carefully tailored quantizers can make 4-bit viable. Building on the general quantization framework and zero-point conventions of Jacob et al., the authors identify a specific pathology: asymmetric zero-points bias second-moment quantization near zero. They resolve it with a linear quantizer that excludes the zero point, aligning the codebook with the second moment’s distribution. Framed by the mixed-precision training observation that optimizer states dominate memory, these ingredients combine into a principled path from 8-bit to 4-bit optimizer states: smaller blocks, 2D-aware scaling, and zero-point–free quantization for the second moment.

---
*Generated: 2026-01-06T23:33:35.590798*
