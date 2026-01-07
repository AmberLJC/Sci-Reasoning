# Prior Work Analysis Report

## Target Paper

**Title:** Decision ConvFormer: Local Filtering in MetaFormer is Sufficient for Decision Making

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jeonghye Kim, Suyoung Lee, Woojun Kim, Youngchul Sung

**Keywords:** MetaFormer, Convolution, Reinforcement Learning, Representation Learning

**Abstract:** 
> The recent success of Transformer in natural language processing has sparked its use in various domains. In offline reinforcement learning (RL), Decision Transformer (DT) is emerging as a promising model based on Transformer. However, we discovered that the attention module of DT is not appropriate to capture the inherent local dependence pattern in trajectories of RL modeled as a Markov decision process. To overcome the limitations of DT, we propose a novel action sequence predictor, named Deci...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**MetaFormer is Actually What You Need for Vision** (2022)
- *Authors:* Weihao Yu et al.
- *Direct Connection:* DC adopts the MetaFormer paradigm that the generic Transformer ‘skeleton’—independent of attention—is key, instantiating it with a local convolutional token mixer instead of attention exactly as MetaFormer advocates.

### 💡 Inspiration

**An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling** (2018)
- *Authors:* Shaojie Bai et al.
- *Direct Connection:* DC is motivated by TCN’s finding that causal/dilated temporal convolutions effectively capture sequence dependencies, guiding the choice of local convolutional mixing for RL trajectories.

### 📊 Baseline

**Decision Transformer: Reinforcement Learning via Sequence Modeling** (2021)
- *Authors:* Lili Chen et al.
- *Direct Connection:* DC retains DT’s return-conditioned sequence modeling formulation but directly replaces DT’s global self-attention token mixer with a local convolutional mixer to better match the Markovian local dependencies in trajectories.

### 🔧 Extension

**Patches Are All You Need?** (2022)
- *Authors:* Daniel Trockman et al.
- *Direct Connection:* DC extends ConvMixer’s idea of using depthwise convolution as the token mixer by adapting it from spatial image patches to causal temporal trajectory tokens for decision making.

### 🔗 Related Problem

**Trajectory Transformer: Model-Based Offline Reinforcement Learning with Sequence Modeling** (2021)
- *Authors:* Michael Janner et al.
- *Direct Connection:* DC targets the same offline RL trajectory modeling setup established by Trajectory Transformer but replaces attention-based token mixing with local convolution to address overreliance on global context.

**Conformer: Convolution-augmented Transformer for Speech Recognition** (2020)
- *Authors:* Anmol Gulati et al.
- *Direct Connection:* DC draws on Conformer’s insight that explicitly modeling local patterns with convolution benefits sequence tasks, but goes further by making convolution the sole token mixer for decision sequences.

---

## Synthesis: How Prior Work Led to This Paper

Decision Transformer showed that offline reinforcement learning could be cast as conditional sequence modeling, conditioning on desired return and actions in an autoregressive manner with a Transformer backbone; its key mechanism is global self-attention to mix trajectory tokens. MetaFormer then demonstrated that the Transformer’s success often stems from the overall architectural scaffold—normalization, token mixer, and feedforward blocks—rather than attention itself, and that the mixer can be swapped with simpler alternatives. ConvMixer provided a concrete recipe for replacing attention with depthwise convolution as the token mixer, highlighting that local filtering can be both expressive and efficient for token interactions. Temporal Convolutional Networks established that causal (and dilated) temporal convolutions excel at capturing dependencies in sequences, offering a strong local modeling prior. Trajectory Transformer reinforced the viability of sequence modeling for RL trajectories with attention, framing the same offline RL problem setup. Conformer, in a different sequence domain, showed that adding convolutions specifically to capture local patterns can improve modeling quality. Together these works revealed a tension: sequence models in RL used global attention despite RL’s locally Markovian structure, while MetaFormer-style designs and temporal convolutions suggested local token mixing could suffice. The natural next step was to instantiate the MetaFormer skeleton for decision making with a causal, local convolutional token mixer—preserving the DT-style return-conditioned sequence formulation while addressing attention’s mismatch and improving efficiency.

---

*Analysis generated on: 2026-01-06T07:59:59.339304*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
