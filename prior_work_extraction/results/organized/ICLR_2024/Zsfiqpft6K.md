# Prior Work Analysis Report

## Target Paper

**Title:** Diffusion Model for Dense Matching

**Conference:** ICLR 2024 (oral)

**Authors:** Jisu Nam, Gyuseong Lee, Sunwoo Kim, Hyeonsu Kim, Hyoungwon Cho, Seyeon Kim, Seungryong Kim

**Keywords:** Diffusion Models, Visual Correspondence

**Abstract:** 
> The objective for establishing dense correspondence between paired images con- sists of two terms: a data term and a prior term. While conventional techniques focused on defining hand-designed prior terms, which are difficult to formulate, re- cent approaches have focused on learning the data term with deep neural networks without explicitly modeling the prior, assuming that the model itself has the capacity to learn an optimal prior from a large-scale dataset. The performance improvement was ob...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**EpicFlow: Edge-Preserving Interpolation of Correspondences for Optical Flow** (2015)
- *Authors:* Revaud et al.
- *Direct Connection:* This work formalized dense matching as a data term plus a hand-crafted prior (edge-aware smoothness/interpolation), providing the explicit likelihood–prior decomposition that DiffMatch re-instantiates with a learned generative prior.

**PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume** (2018)
- *Authors:* Sun et al.
- *Direct Connection:* By popularizing deep cost volumes as the learned data term for dense correspondence, PWC-Net established the conditioning signal (matching cost) that DiffMatch directly consumes in its conditional diffusion process.

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Song et al.
- *Direct Connection:* This paper provides the score-based diffusion framework and denoising objectives that DiffMatch adopts to learn and sample from a prior over dense correspondence fields.

### 💡 Inspiration

**Diffusion Posterior Sampling for General Noisy Inverse Problems** (2022)
- *Authors:* Chung et al.
- *Direct Connection:* DPS’s key idea of combining a measurement-consistency (likelihood) term with a learned diffusion prior during sampling directly inspires DiffMatch’s formulation p(correspondence|cost) ∝ p(cost|correspondence) p_prior(correspondence), where the matching cost plays the data term.

### 📊 Baseline

**RAFT: Recurrent All-Pairs Field Transforms for Optical Flow** (2020)
- *Authors:* Teed et al.
- *Direct Connection:* RAFT’s strong cost-volume + iterative update framework serves as the primary learned-data-term baseline whose failure modes in textureless/repetitive regions motivate DiffMatch’s explicit prior injection via diffusion.

### 🔧 Extension

**CATs: Cost Aggregation Transformers for Visual Correspondence** (2021)
- *Authors:* Kim et al.
- *Direct Connection:* CATs introduced transformer-based cost aggregation for dense matching; DiffMatch directly extends this cost-aggregation view by treating the aggregated matching cost as the likelihood input to a diffusion sampler that imposes a learned prior over correspondence fields.

---

## Synthesis: How Prior Work Led to This Paper

Classical optical flow and correspondence methods explicitly decomposed the task into a data term and a prior, as exemplified by EpicFlow, which enforced edge-aware regularization on sparse matches to resolve ambiguities through a hand-designed prior. Deep learning shifted focus to learning the data term: PWC-Net established modern cost-volume conditioning via pyramids and warping, and RAFT advanced this paradigm by building a dense all-pairs cost volume with iterative refinement, achieving strong accuracy but relying on the network to implicitly learn priors. Transformer-based cost aggregation, such as CATs, further improved how matching evidence is pooled, yielding sharper and more discriminative cost maps yet still leaving inherent ambiguities (textureless regions, repetitive patterns, large motions) unresolved without an explicit prior. In parallel, score-based diffusion models provided a principled generative framework for learning priors (via SDEs and denoising) and, crucially, diffusion posterior sampling demonstrated how to fuse a likelihood term with a learned prior during the generative process to solve inverse problems. Together these works revealed a gap: strong learned data terms exist for dense matching, but explicit, learnable priors had not been integrated into inference. The natural synthesis is to treat the aggregated matching cost as a likelihood and impose a learned correspondence prior via a conditional diffusion sampler, unifying the classical energy view with modern diffusion guidance to robustly disambiguate matches under challenging conditions.

---

*Analysis generated on: 2026-01-06T18:06:38.065061*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
