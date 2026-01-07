# Prior Work Analysis Report

## Target Paper
**Title:** 8oCrlOaYcc
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Connection:* Introduced the modern Mixture-of-Experts framework and routing formulation that SoftMoE builds upon; this paper directly revisits the necessity of multiple experts in that lineage within the RL setting.

**An Image is Worth 16×16 Words: Transformers for Image Recognition at Scale** (2020)
- *Authors:* Alexey Dosovitskiy et al.
- *Connection:* Established patch tokenization as a core design for processing spatial features; the present paper directly adopts this tokenization principle for RL encoder outputs and shows it explains SoftMoE’s gains even with a single expert.

**Human-level control through deep reinforcement learning** (2015)
- *Authors:* Volodymyr Mnih et al.
- *Connection:* Standardized the practice of flattening convolutional features before fully connected heads in deep RL; the current work directly targets this legacy design choice by replacing flattening with tokenization and attributing SoftMoE’s efficacy to that change.

### 💡 Inspiration

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Connection:* Popularized efficient expert routing and scaling practices that influenced SoftMoE-style designs; the current work challenges the assumption that expert multiplicity is the key driver of performance by isolating tokenization effects.

### 📊 Baseline

**SoftMoE: Scaling Online Reinforcement Learning with Soft Mixture-of-Experts** (2024)
- *Authors:* Ghada Sokar et al.
- *Connection:* Provides the SoftMoE architecture that this paper dissects; the present work shows the reported gains primarily stem from tokenizing the encoder output rather than from using multiple experts, and that a single appropriately scaled expert with tokenization preserves the benefits.

### 🔗 Related Problem

**Scaling Vision with Sparse Mixture of Experts** (2021)
- *Authors:* Carlos Riquelme et al.
- *Connection:* Demonstrated that MoE combined with patch tokenization benefits vision transformers; this connection motivated examining whether, in RL, the tokenization of spatial features (rather than expert multiplicity) is the critical ingredient.

---

## Synthesis

The core innovation of this paper is to reveal that the key to SoftMoE’s success in online RL is not expert multiplicity but the tokenization of encoder outputs. This insight sits squarely on the SoftMoE baseline itself (Sokar et al., 2024), which first demonstrated strong gains from soft mixture-of-experts in online RL but left the underlying cause unclear. The lineage of expert-based scaling originates with Shazeer et al. (2017), who introduced the modern MoE framework, and was further catalyzed by Switch Transformers (Fedus et al., 2021), which showed how routing and sparse capacity could scale models dramatically. In computer vision, V-MoE (Riquelme et al., 2021) combined MoE with patch-token processing and hinted that tokenized spatial representations interact synergistically with experts. That token-centric perspective is grounded in ViT (Dosovitskiy et al., 2020), which established patch tokenization as a superior alternative to flattening spatial features. In RL, the dominant architectural convention dating back to DQN (Mnih et al., 2015) is to flatten convolutional features into a single vector before the head, a choice this work directly challenges. By deconstructing the SoftMoE stack and demonstrating that a single expert with ViT-style tokenization preserves the performance gains, the paper reframes the narrative: the decisive factor in scaling deep RL is how spatial information is represented and processed (tokenized), not the number of experts per se.

---
*Generated: 2026-01-06T23:09:26.597895*
