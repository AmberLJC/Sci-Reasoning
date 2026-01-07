# Prior Work Analysis Report

## Target Paper

**Title:** Mixed-Type Tabular Data Synthesis with Score-based Diffusion in Latent Space

**Conference:** ICLR 2024 (oral)

**Authors:** Hengrui Zhang, Jiani Zhang, Zhengyuan Shen, Balasubramaniam Srinivasan, Xiao Qin, Christos Faloutsos, Huzefa Rangwala, George Karypis

**Keywords:** Tabular data, tabular generation, diffusion models

**Abstract:** 
> Recent advances in tabular data generation have greatly enhanced synthetic data quality. However, extending diffusion models to tabular data is challenging due to the intricately varied distributions and a blend of data types of tabular data. This paper introduces TabSyn, a methodology that synthesizes tabular data by leveraging a diffusion model within a variational autoencoder (VAE) crafted latent space. The key advantages of the proposed Tabsyn include (1) Generality: the ability to handle a ...

---

## Key Prior Works (7 papers with direct influence)

### 💡 Inspiration

**High-Resolution Image Synthesis with Latent Diffusion Models** (2022)
- *Authors:* Robin Rombach et al.
- *Direct Connection:* Latent Diffusion’s core idea—train diffusion in an autoencoder’s latent to ease optimization and accelerate sampling—directly inspires TabSyn’s decision to perform diffusion in a VAE latent for tabular data.

### 🔍 Gap Identification

**STaSy: Score-based Tabular Data Synthesis** (2021)
- *Authors:* Kim et al.
- *Direct Connection:* STaSy showed the promise of score-based diffusion for tables but struggled with discrete/continuous mixtures and slow reverse processes, which TabSyn overcomes by unifying all types in a continuous latent and using far fewer diffusion steps.

**CTAB-GAN+: Enhancing Tabular Data Synthesis by Type-Aware Transformations** (2022)
- *Authors:* Zhao et al.
- *Direct Connection:* CTAB-GAN+’s engineered, type-specific preprocessing (e.g., mode-specific normalization) highlights the challenge of reconciling skewed continuous and categorical distributions, which TabSyn replaces with a learned latent unification.

### 📊 Baseline

**TabDDPM: Modelling Tabular Data with Diffusion Models** (2023)
- *Authors:* Sergey Kotelnikov et al.
- *Direct Connection:* TabSyn directly replaces TabDDPM’s data-space diffusion (with ad‑hoc categorical handling and long sampling chains) by running score-based diffusion in a learned VAE latent, addressing both mixed-type difficulty and sampling speed.

**Modeling Tabular Data using Conditional GAN** (2019)
- *Authors:* Lei Xu et al.
- *Direct Connection:* CTGAN defined a widely used conditional formulation for mixed-type tabular synthesis that TabSyn targets as a primary baseline, replacing adversarial training with latent-score diffusion to improve fidelity and mode coverage.

### 🔧 Extension

**Handling Incomplete Heterogeneous Data using VAEs** (2020)
- *Authors:* M. Nazabal et al.
- *Direct Connection:* By introducing per-variable likelihoods in a VAE to encode mixed categorical and continuous variables into a unified continuous space, HIVAE provides the template that TabSyn extends to craft a latent space suitable for downstream diffusion.

### 🔗 Related Problem

**Structured Denoising Diffusion Models in Discrete State-Spaces** (2021)
- *Authors:* Jacob Austin et al.
- *Direct Connection:* D3PM formalized discrete-state diffusion for categorical variables, but its computational and integration burdens with continuous features motivate TabSyn’s choice to avoid discrete diffusion by operating in a continuous latent space.

---

## Synthesis: How Prior Work Led to This Paper

CTGAN introduced a conditional framework tailored to mixed-type tables, addressing imbalanced categorical modes but suffering from adversarial instability and limited coverage. CTAB-GAN+ pushed this line further with type-aware transformations like mode-specific normalization to better handle skewed continuous and categorical variables, yet relied on hand-engineered preprocessing and still inherited GAN training fragility. HIVAE offered a principled way to encode heterogeneous variables by assigning type-specific likelihoods within a VAE, yielding a unified continuous latent that preserves mixed-type semantics. In parallel, STaSy demonstrated that score-based diffusion can preserve inter-column dependencies in tabular synthesis, though it struggled with discrete features and required many reverse steps. TabDDPM generalized denoising diffusion to tables by operating in data space with special handling for categories, but incurred long sampling chains and ad hoc treatments for mixed types. D3PM formalized discrete diffusion for categorical variables, revealing that categorical noise schedules are possible but often computationally heavy and awkward to integrate with continuous fields. Latent Diffusion showed that moving diffusion into an autoencoder latent can dramatically ease training and speed sampling while preserving quality.
Together, these works exposed a gap: diffusion models produce high-fidelity tables but are slow and brittle with mixed types, while VAEs can unify heterogeneous variables yet underperform in generation quality. The natural synthesis is to learn a mixed-type-aware VAE that maps all columns into a well-behaved continuous latent and to run score-based diffusion there, as in latent diffusion, thus explicitly capturing inter-column relations, improving the latent distribution for diffusion training, and yielding far fewer reverse steps than prior tabular diffusion models.

---

*Analysis generated on: 2026-01-06T09:08:57.288180*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
