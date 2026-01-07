# Prior Work Analysis Report

## Target Paper
**Title:** iSfCWhvEGA
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LTE’s central idea—training large language models to "learn to be efficient" by activating only a structured subset of neurons—sits at the intersection of conditional computation, differentiable sparsity, and modern LLM activation design. The conditional-computation lineage begins with sparsely gated Mixture-of-Experts (Shazeer et al., 2017), then matures with GShard (Lepikhin et al., 2020) and Switch Transformers (Fedus et al., 2021), which show that routing a token to a few experts yields strong efficiency–quality trade-offs. LTE seeks comparable gains but inside dense FFNs, avoiding full MoE conversion and its routing/serving complexity.
Differentiable sparsity mechanisms provide LTE with the tooling to make activation selection learnable. L0 regularization (Louizos et al., 2018) offers discrete, trainable gates that switch units off while preserving differentiability, and k-sparse autoencoders (Makhzani & Frey, 2013) demonstrate that enforcing top-k activations can yield structured representations—both directly echoing LTE’s structured activation sparsity objective.
A key practical challenge is that state-of-the-art LLMs (e.g., LLaMA) use non-ReLU activations such as SwiGLU (Shazeer, 2020), which do not naturally zero out activations. LTE pushes beyond ReLU-dependent sparsity by learning structure atop such smooth activations. Finally, LTE’s efficiency-aware training objective aligns with the broader paradigm of optimizing compute–accuracy trade-offs during training, as epitomized by Adaptive Computation Time (Graves, 2016). Together, these works furnish the conceptual and algorithmic foundations for LTE to amplify inherent activation sparsity into structured, learnable sparsity that accelerates inference without sacrificing performance.

---
*Generated: 2026-01-06T23:33:35.573696*
