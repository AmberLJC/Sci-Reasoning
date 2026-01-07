# Prior Work Analysis Report

## Target Paper
**Title:** 7sdkLVuYCU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

QTIP’s central advance is to replace conventional vector quantization in post-training quantization with trellis-coded quantization (TCQ), achieving high-dimensional shaping without the exponential codebook growth that constrains prior VQ-based PTQ. This builds squarely on the TCQ lineage: Marcellin and Fischer established TCQ’s stateful quantizer using Viterbi decoding and set-partitioned labeling, while Gersho and Gray’s classic text formalized both the shaping benefits of high-dimensional quantization and the codebook-scaling barrier in VQ that TCQ circumvents. The trellis and labeling principles trace to Ungerboeck’s trellis-coded modulation, whose set-partitioning directly informs how QTIP designs practical, hardware-efficient trellises.
Crucially, QTIP operationalizes TCQ in the LLM PTQ regime by leveraging the Viterbi algorithm as a lightweight dynamic program across weight sequences, turning the stateful decoder into a throughput benefit rather than a bottleneck. Against the prevailing VQ toolkit, product quantization exemplifies the need to limit subvector dimension to keep codebooks manageable; QTIP avoids this compromise by separating bitrate from effective dimensionality. Moreover, ideas from compositional coding (Additive Quantization) motivate QTIP’s spectrum between lookup-based and computed codes, trading memory for arithmetic while retaining expressivity. Finally, hardware-aware quantization with power-of-two levels (APoT) directly inspires QTIP’s computed, lookup-free “bitshift” trellis codes, aligning the TCQ design with efficient bitshift/add execution. Together, these works converge to enable QTIP’s ultra–high-dimensional, stateful, and hardware-friendly quantization for LLMs.

---
*Generated: 2026-01-06T23:42:49.039692*
