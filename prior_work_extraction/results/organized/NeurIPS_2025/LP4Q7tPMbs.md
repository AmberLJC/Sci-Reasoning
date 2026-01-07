# Prior Work Analysis Report

## Target Paper
**Title:** LP4Q7tPMbs
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

NormFit sits at the intersection of federated optimization under non-IID data, parameter-efficient fine-tuning (PEFT), and few-shot adaptation of vision–language models. FedAvg established the decentralized aggregation paradigm and exposed the core bottlenecks of communication and local computation that NormFit explicitly targets. SCAFFOLD formalized client drift in non-IID regimes, motivating NormFit’s strategy to constrain the update space so that client gradients align better and aggregation becomes more stable. FedBN demonstrated that normalization layers are particularly effective handles for coping with feature heterogeneity across clients; NormFit extends this insight from BatchNorm to LayerNorm in ViT/CLIP backbones.
BitFit showed that carefully choosing a tiny subset of parameters (bias terms) can preserve most adaptation capacity, and LoRA generalized this PEFT principle with strong accuracy–efficiency tradeoffs. These works directly inform NormFit’s design choice to fine-tune an even smaller and more principled target: the Pre-LayerNorm affine parameters. Finally, CoOp demonstrated that CLIP can be adapted for few-shot tasks through small learnable modules rather than full fine-tuning, validating NormFit’s premise that minimal updates can yield large gains in downstream performance.
Together, these strands lead to NormFit’s core contribution: selectively tuning only Pre-LN parameters in CLIP’s vision encoder to jointly achieve low communication and computation cost, while improving accuracy and robustness under non-IID client data—an approach theoretically motivated by drift/variance considerations and architecturally grounded in Pre-LN Transformer behavior.

---
*Generated: 2026-01-07T00:21:32.326377*
