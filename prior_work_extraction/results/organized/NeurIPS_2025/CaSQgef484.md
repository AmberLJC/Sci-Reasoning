# Prior Work Analysis Report

## Target Paper
**Title:** CaSQgef484
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution—grafting—rests on reusing pretrained diffusion transformers to cheaply instantiate and evaluate architectural variants. This idea draws directly from function-preserving and weight-sharing paradigms. Net2Net pioneered transforming pretrained networks to new architectures without losing initialization quality, while Once-for-All demonstrated that one set of shared weights can support many subarchitectures with minimal additional training. Grafting adopts this philosophy in the diffusion-transformer regime, enabling operator-level edits (attention and FFN swaps) without expensive pretraining from scratch.

The experimental scaffold is DiT-XL/2, making Scalable Diffusion Models with Transformers the indispensable base upon which all surgeries occur. The specific operators explored via grafting come from established alternatives in vision transformers. Swin Transformer’s windowed attention supplies a locality-biased attention mechanism, aligning with the paper’s analysis of attention locality and motivating the local-attention graft. Performer contributes a concrete linear-attention formulation to test as a scalable alternative to softmax attention. For modifying MLPs, Restormer’s gated depthwise-convolutional feed-forward design offers a well-validated convolutional FFN variant tailored for images, informing the convolutional and gated FFN replacements examined here. Finally, gated convolution from Yu et al. provides a content-aware gating operator with strong generative vision credentials, justifying the paper’s attention-to-gated-convolution substitutions.

Together, these works enable the paper’s central insight: by transplanting well-motivated operators into a pretrained DiT and doing light tuning, one can systematically probe architectural choices—locality, linearization, and convolutional inductive biases—under small compute budgets.

---
*Generated: 2026-01-07T00:05:12.551078*
