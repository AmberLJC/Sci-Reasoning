# Prior Work Analysis Report

## Target Paper

**Title:** Provable Compositional Generalization for Object-Centric Learning

**Conference:** ICLR 2024 (oral)

**Authors:** Thaddäus Wiedemer, Jack Brady, Alexander Panfilov, Attila Juhos, Matthias Bethge, Wieland Brendel

**Keywords:** compositional generalization, identifiability, object-centric learning, generalization, OOD generalization, unsupervised learning, slot attention, disentanglement, autoencoders, representation learning

**Abstract:** 
> Learning representations that generalize to novel compositions of known concepts is crucial for bridging the gap between human and machine perception. One prominent effort is learning object-centric representations, which are widely conjectured to enable compositional generalization. Yet, it remains unclear when this conjecture will be true, as a principled theoretical or empirical understanding of compositional generalization is lacking. In this work, we investigate when compositional generaliz...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**MONet: Unsupervised Scene Decomposition and Representation** (2019)
- *Authors:* Christopher P. Burgess et al.
- *Direct Connection:* Establishes the spatial mixture-of-objects decoder (per-object reconstructions combined via masks) that matches the structural decoder form assumed in the identifiability and compositionality guarantees.

**Multi-Object Representation Learning with Iterative Variational Inference (IODINE)** (2019)
- *Authors:* Klaus Greff et al.
- *Direct Connection:* Provides a latent-variable generative model with multiple object slots and a per-slot decoder-masking composition, supplying the precise object-centric encoder–decoder decomposition that the theory requires.

### 💡 Inspiration

**Variational Autoencoders and Nonlinear ICA: A Unifying Framework** (2020)
- *Authors:* Ilyes Khemakhem et al.
- *Direct Connection:* Shows that identifiability can be achieved in VAEs under explicit auxiliary conditions, motivating an identifiability-based lens and the need for explicit structural and consistency assumptions that are adapted here to the object-centric, compositional setting.

### 🔍 Gap Identification

**Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations** (2019)
- *Authors:* Francesco Locatello et al.
- *Direct Connection:* Proves impossibility of unsupervised disentanglement without inductive biases, directly motivating the structural decoder and encoder–decoder consistency biases used to obtain identifiability and compositional generalization.

**On the Transfer of Disentangled Representations in Realistic Settings** (2021)
- *Authors:* Andrea Dittadi et al.
- *Direct Connection:* Demonstrates that learned disentangled/object-centric representations often fail under OOD shifts, highlighting the lack of compositional generalization that the present theory addresses with provable guarantees.

### 📊 Baseline

**Object-Centric Learning with Slot Attention** (2020)
- *Authors:* Francesco Locatello et al.
- *Direct Connection:* Introduces the slot-based object-centric autoencoder with per-slot decoding and masking that serves as the canonical architecture whose structural decoder assumptions are formalized and theoretically analyzed for compositional generalization.

### 🔗 Related Problem

**Recurrent Independent Mechanisms** (2021)
- *Authors:* Anirudh Goyal et al.
- *Direct Connection:* Argues that modular, independent components facilitate combinatorial generalization, providing the key intuition that per-object modular decoders can yield compositional generalization when appropriately constrained.

---

## Synthesis: How Prior Work Led to This Paper

Slot-based object-centric models established an architectural bias in which scenes are decomposed into per-object latents, each decoded separately and combined via masks. MONet introduced the spatial mixture-of-objects decoder, where object-wise reconstructions are alpha-composited by masks, and IODINE cast this as an explicit multi-slot generative model with amortized iterative inference, making the encoder–decoder decomposition operational. Slot Attention then became the canonical autoencoding instantiation, using competitive attention to allocate slots and a per-slot decoder, effectively enforcing the mask-based additive structure during reconstruction. In parallel, identifiability theory for latent-variable models showed that guarantees require explicit assumptions: Identifiable VAEs demonstrated that structural or auxiliary conditions can render latent factors recoverable. Complementing this, impossibility results for unsupervised disentanglement proved that without inductive biases such recovery is not achievable, and empirical analyses of transfer exposed that even seemingly disentangled representations often fail under OOD shifts. Finally, the modularity perspective of Recurrent Independent Mechanisms argued that independent components facilitate systematic recombination, suggesting that object-wise modular decoders could support combinatorial generalization.
Together, these works reveal both the right inductive bias—object-wise, mask-composed decoders—and the missing ingredient: conditions that make the learned factors identifiable and robustly recomposable. The present work synthesizes these insights by formalizing the slot-style decoder as a structural assumption and adding an encoder–decoder consistency constraint, then proving that under these conditions the learned object-centric codes are identifiable and provably generalize to novel compositions.

---

*Analysis generated on: 2026-01-06T07:02:42.246593*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
