# Prior Work Analysis Report

## Target Paper

**Title:** Analyzing Feed-Forward Blocks in Transformers through the Lens of Attention Maps

**Conference:** ICLR 2024 (spotlight)

**Authors:** Goro Kobayashi, Tatsuki Kuribayashi, Sho Yokoi, Kentaro Inui

**Keywords:** Transformer, Attention map, Feed-forward, Contextualization, Interpretation, Analysis, Pre-trained models, Masked language models, Causal language models

**Abstract:** 
> Transformers are ubiquitous in wide tasks.
Interpreting their internals is a pivotal goal. 
Nevertheless, their particular components, feed-forward (FF) blocks, have typically been less analyzed despite their substantial parameter amounts.
We analyze the input contextualization effects of FF blocks by rendering them in the attention maps as a human-friendly visualization scheme.
Our experiments with both masked- and causal-language models reveal that FF networks modify the input contextualizatio...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**What Does BERT Look at? An Analysis of BERT’s Attention** (2019)
- *Authors:* Clark et al.
- *Direct Connection:* By establishing attention maps as a human-interpretable lens that captures linguistic relations, this work provides the visualization paradigm that the paper targets when translating FFN effects into attention maps.

### 💡 Inspiration

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Geva et al.
- *Direct Connection:* By reframing FFN sublayers as key–value memories that write targeted features into the residual stream, this work directly motivated analyzing how FFNs change token contextualization and thus inspired rendering their effects in an attention-map-like space.

### 🔧 Extension

**Quantifying Attention Flow in Transformers** (2020)
- *Authors:* Abnar and Zuidema
- *Direct Connection:* The attention flow/rollout mechanism for composing layer-wise attention into end-to-end token-to-token maps is extended here to incorporate the FFN-induced transformations, enabling FF effects to be visualized as effective attention maps.

**Transformer Interpretability Beyond Attention Visualization** (2021)
- *Authors:* Chefer et al.
- *Direct Connection:* Their LRP-style relevance propagation through both attention and MLP blocks informed the methodological choice to propagate FFN contributions along computational paths, which this paper adapts by re-expressing FFN effects as attention-map entries rather than generic relevance scores.

### 🔗 Related Problem

**Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned** (2019)
- *Authors:* Voita et al.
- *Direct Connection:* Evidence that specific attention heads encode syntactic/coreferential patterns set up concrete linguistic compositions against which FFN-induced contextualization changes can be compared once mapped into attention space.

**Locating and Editing Factual Knowledge in GPT** (2022)
- *Authors:* Meng et al.
- *Direct Connection:* Showing that factual knowledge is localized primarily in FFN parameters underscored the importance of isolating and visualizing FFN contributions to token representations, directly motivating an FF-focused analysis.

---

## Synthesis: How Prior Work Led to This Paper

Feed-forward networks in Transformers were reframed as key–value memories by Geva et al., who showed these sublayers write targeted features into the residual stream; this positioned FFNs as active sources of content that can steer representations. Abnar and Zuidema introduced attention flow, composing layer-wise attention to produce end-to-end token-to-token maps, thereby defining a concrete mechanism for visualizing contextualization as effective attention. Chefer et al. progressed interpretability by propagating relevance through both attention and MLP sublayers, demonstrating that non-attention paths can be traced and attributed alongside attention, not merely ignored. Clark et al. established attention maps as a human-interpretable lens that aligns with linguistic relations, while Voita et al. revealed that specific heads specialize in syntactic and coreferential patterns, giving a catalog of linguistic compositions observable in attention space. Complementing these, Meng et al. localized factual knowledge primarily to FFNs, emphasizing that understanding model knowledge requires isolating FFN contributions.
Together, these works suggested a gap: although attention maps are a trusted visualization medium, FFN-induced contextualization—known to encode knowledge and influence representations—was not captured in that space. Extending attention flow with propagation through FFN paths, and guided by relevance-propagation principles, the paper synthesizes these ideas to translate FFN effects into attention-map form. This enables direct comparison with known attention-based linguistic patterns and reveals interactions—including amplification and cancellation—between FFNs and attention, a natural next step given the recognized importance of FFNs and the established utility of attention maps.

---

*Analysis generated on: 2026-01-06T08:55:40.385462*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
