# Prior Work Analysis Report

## Target Paper
**Title:** 3gamyee9Yh
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

QuantSR advances low-bit image super-resolution by introducing the Redistribution-driven Learnable Quantizer (RLQ), whose design is rooted in two complementary lines of prior work: learnable quantizers and scale-redistribution techniques. From LSQ, QuantSR inherits the core principle of learning quantizer parameters with STE-based gradients, but identifies that merely optimizing step sizes is insufficient at 2–4 bits due to representation homogeneity. PACT further shaped the activation-side perspective by demonstrating that learnable clipping stabilizes low-bit QAT; RLQ broadens this idea by injecting learnable redistribution signals that enhance representational diversity without incurring inference-time cost. In parallel, Cross-Layer Equalization established that rebalancing scales (redistribution) across network components alleviates outliers for quantization. QuantSR internalizes this redistribution concept into the quantizer itself, applying it during both forward and backward passes to systematically improve signal expressivity and gradient flow at ultra-low precision. The STE formalism provides the backbone for passing gradients through non-differentiable quantizers; RLQ augments this pathway to deliver richer, more informative gradients. Finally, the practical impetus and validation grounds come from high-capacity SR backbones like RCAN and SwinIR, whose intricate channel attention and transformer dynamics are notoriously fragile under aggressive quantization. By unifying learnable quantization with principled redistribution tailored to SR feature statistics, QuantSR achieves flexible, accurate inference at low bits across both CNN and transformer SR models.

---
*Generated: 2026-01-07T00:02:04.866929*
