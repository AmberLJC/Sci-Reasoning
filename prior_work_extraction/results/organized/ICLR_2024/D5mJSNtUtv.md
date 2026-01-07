# Prior Work Analysis Report

## Target Paper

**Title:** Finite-State Autoregressive Entropy Coding for Efficient Learned Lossless Compression

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yufeng Zhang, Hang Yu, Jianguo Li, Weiyao Lin

**Keywords:** Lossless Compression, Autoregressive Model, Acceleration, Entropy Coding, Autoencoder

**Abstract:** 
> Learned lossless data compression has garnered significant attention recently due to its superior compression ratios compared to traditional compressors. However, the computational efficiency of these models jeopardizes their practicality. This paper proposes a novel system for improving the compression ratio while maintaining computational efficiency for learned lossless data compression. Our approach incorporates two essential innovations. First, we propose the Finite-State AutoRegressive (FSA...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Asymmetric Numeral Systems: entropy coding combining speed of Huffman coding with compression of arithmetic coding** (2013)
- *Authors:* Jarek Duda
- *Direct Connection:* We adopt ANS’s table-driven finite-state formulation as the basis for our FSAR coder, extending the lookup-table transition mechanism to index distributions by Markov state for autoregressive coding.

**Estimating or Propagating Gradients Through Stochastic Neurons** (2013)
- *Authors:* Yoshua Bengio et al.
- *Direct Connection:* Our Straight-Through Hardmax Quantization directly relies on the straight-through estimator introduced here to backpropagate through discrete argmax decisions in the latent space.

### 💡 Inspiration

**Context-based adaptive binary arithmetic coding in the H.264/AVC video compression standard** (2003)
- *Authors:* Detlev Marpe et al.
- *Direct Connection:* CABAC’s finite-state context adaptation for fast entropy coding inspired our design of a compact Markov state machine that captures local dependencies while keeping coding operations table-driven.

### 🔍 Gap Identification

**Joint Autoregressive and Hierarchical Priors for Learned Image Compression** (2018)
- *Authors:* David Minnen et al.
- *Direct Connection:* This work showed that autoregressive context models markedly boost compression but introduce costly serial decoding, directly motivating our finite-state, lookup-table autoregressive coder to retain dependencies without per-symbol neural inference.

**Categorical Reparameterization with Gumbel-Softmax** (2017)
- *Authors:* Eric Jang et al.
- *Direct Connection:* The temperature-tuned soft relaxation for categorical variables in Gumbel-Softmax motivates our hardmax+STE alternative, explicitly avoiding its bias/temperature tradeoffs during discrete latent optimization.

### 📊 Baseline

**Lossless Image Compression with Learned Probabilities (L3C)** (2019)
- *Authors:* Fabian Mentzer et al.
- *Direct Connection:* L3C provides the hierarchical learned lossless framework and practical baseline our system plugs into and surpasses, with our FSAR coder replacing its probability-estimation bottleneck while preserving speed.

### 🔧 Extension

**Neural Discrete Representation Learning (VQ-VAE)** (2017)
- *Authors:* Aaron van den Oord et al.
- *Direct Connection:* Building on VQ-VAE’s straight-through updates for hard assignments, we modify the mechanism by discarding codebooks and applying a hardmax over categorical logits to realize STHQ for discrete latents.

---

## Synthesis: How Prior Work Led to This Paper

Autoregressive context modeling was shown to significantly improve entropy models when combined with hierarchical priors, but the serial nature of masked-convolution context inference made decoding slow and computationally heavy, as highlighted by Minnen and colleagues. Practical learned lossless systems like L3C established a hierarchical framework and fast causal probability estimation as a strong baseline for real-world compressors. Independently, Asymmetric Numeral Systems introduced a table-driven finite-state entropy coder that achieves arithmetic-coding efficiency with near-Huffman speed by using lookup-table state transitions. In engineered codecs, CABAC demonstrated that finite-state context adaptation can capture local dependencies efficiently within an entropy-coding loop. For discrete optimization, Bengio’s straight-through estimator provided a principled way to propagate gradients through non-differentiable decisions. The Gumbel-Softmax relaxation offered a differentiable proxy for categorical variables but introduced temperature tuning and mismatch between training and discrete inference. VQ-VAE showed that straight-through updates for hard assignments could stabilize training with discrete representations without relying on continuous relaxations. Together, these works revealed a path: replace expensive neural autoregressive context evaluation with a finite-state, table-driven mechanism that preserves dependency modeling, and train truly discrete latents using hard decisions with straight-through gradients. By fusing ANS-style lookup transitions with a compact Markov state to realize fast autoregressive entropy coding, and by adopting hardmax straight-through quantization instead of soft relaxations, the current work naturally extends this lineage to deliver higher compression ratios without sacrificing computational efficiency.

---

*Analysis generated on: 2026-01-06T22:46:24.332671*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
