# Prior Work Analysis Report

## Target Paper

**Title:** Whole-Song Hierarchical Generation of Symbolic Music Using Cascaded Diffusion Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ziyu Wang, Lejun Min, Gus Xia

**Keywords:** Cascaded generative models, Diffusion models, Symbolic Music Generation

**Abstract:** 
> Recent deep music generation studies have put much emphasis on long-term generation with structures. However, we are yet to see high-quality, well-structured **whole-song** generation. In this paper, we make the first attempt to model a full music piece under the realization of *compositional hierarchy*. With a focus on symbolic representations of pop songs, we define a hierarchical language, in which each level of hierarchy focuses on the semantics and context dependency at a certain music scop...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Structured Denoising Diffusion Models in Discrete State-Spaces** (2021)
- *Authors:* Jacob Austin et al.
- *Direct Connection:* Their formulation of diffusion in discrete state spaces provides the training objective and forward–reverse processes that enable diffusion modeling over symbolic music tokens at each level of the proposed hierarchical language.

### 💡 Inspiration

**Jukebox: A Generative Model for Music** (2020)
- *Authors:* Prafulla Dhariwal et al.
- *Direct Connection:* Jukebox’s hierarchical, top-down priors for song-length audio demonstrated that high-level structure (e.g., sections) should guide lower-level generation, directly motivating the current paper’s multi-level conditioning across form, phrase, and notes in the symbolic domain.

**Hierarchical Variational Autoencoders for Music (MusicVAE)** (2018)
- *Authors:* Adam Roberts et al.
- *Direct Connection:* MusicVAE showed that explicit hierarchical latent organization (e.g., bar/phrase controllers) improves long-term musical coherence, a key insight the paper adopts by defining a hierarchical language (form/phrase/cadence vs. notes/chords) that conditions generation top-down.

### 🔍 Gap Identification

**Music Transformer: Generating Music with Long-Term Structure** (2018)
- *Authors:* Cheng-Zhi Anna Huang et al.
- *Direct Connection:* While relative attention improves longer-range coherence, Music Transformer struggles to produce whole-song form, highlighting the gap in explicit global structure modeling that the hierarchical cascaded approach is designed to fill.

### 📊 Baseline

**Pop Music Transformer: Beat-based Modeling and Generation of Expressive Music (REMI)** (2020)
- *Authors:* Yu-Siang Huang et al.
- *Direct Connection:* This work’s REMI-style event modeling and pop-song focus serve as a primary baseline for symbolic pop generation, whose limitations in capturing full verse–chorus form the paper addresses via higher-level languages and cascaded conditioning.

### 🔧 Extension

**Cascaded Diffusion Models for High Fidelity Image Synthesis** (2022)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* The paper directly generalizes Ho et al.’s cascaded diffusion paradigm—progressively conditioning lower stages on higher-level outputs—by reinterpreting “resolution” as musical scope (form→phrase→notes) to realize a top-down, multi-level symbolic music generator.

---

## Synthesis: How Prior Work Led to This Paper

Cascaded Diffusion Models for High Fidelity Image Synthesis established a powerful multi-stage diffusion recipe where later stages are conditioned on earlier ones; critically, the notion of cascading conditioned refinements enables mapping coarse-to-fine generation. Structured Denoising Diffusion Models in Discrete State-Spaces provided the concrete machinery to run diffusion over categorical sequences, defining the forward corruption and reverse denoising processes for token-based modeling. Jukebox proved that hierarchical, top-down generation is essential for full-song music: high-level priors representing sections guide lower tiers to realize coherent long-range structure in audio. MusicVAE similarly demonstrated that explicit hierarchical organization—bar/phrase-level controllers with lower-level decoders—materially improves long-term coherence in symbolic music. Music Transformer introduced relative attention to extend temporal dependencies, but its purely flat sequence modeling left global form underrepresented. Pop Music Transformer refined event representations (e.g., beat, chord tokens) for pop and improved local rhythmic/harmonic modeling, yet it still lacked mechanisms to enforce whole-song verse–chorus form and cadential planning.

Together these works reveal a gap: flat sequence models and local event representations struggle with whole-song form, while hierarchical priors and cascaded refinement excel at long-range structure but had not been realized for symbolic tokens. The current paper synthesizes these insights by defining an explicit multi-level symbolic language (form, phrase, cadence → notes/chords) and instantiating it with a cascaded diffusion pipeline, where each lower level is conditioned on the higher-level plan, enabling coherent, whole-song symbolic generation.

---

*Analysis generated on: 2026-01-06T14:35:23.621913*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
