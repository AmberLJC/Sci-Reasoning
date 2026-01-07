# Prior Work Analysis Report

## Target Paper

**Title:** DSPO: Direct Score Preference Optimization for Diffusion Model Alignment

**Conference:** ICLR 2025 (oral)

**Authors:** Huaisheng Zhu, Teng Xiao, Vasant G Honavar

**Keywords:** Text-to-image generation

**Abstract:** 
> Diffusion-based Text-to-Image (T2I) models have achieved impressive success in generating high-quality images from textual prompts. While large language models (LLMs) effectively leverage Direct Preference Optimization (DPO) for fine-tuning on human preference data without the need for reward models, diffusion models have not been extensively explored in this area. Current preference learning methods applied to T2I diffusion models immediately adapt existing techniques from LLMs. However, this d...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Denoising Diffusion Probabilistic Models** (2020)
- *Authors:* Ho et al.
- *Direct Connection:* DSPO explicitly aligns its fine-tuning loss with the DDPM denoising score-matching objective, ensuring the preference-learning objective matches the diffusion model’s pretraining criterion.

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Song et al.
- *Direct Connection:* DSPO leverages the time-dependent data score formulation and its estimators from score-based generative modeling to derive preference gradients directly in score space rather than via likelihood surrogates.

**A Connection Between Score Matching and Denoising Autoencoders** (2011)
- *Authors:* Vincent
- *Direct Connection:* DSPO builds its preference objective on the denoising score-matching identity that links denoising residuals to data scores, enabling preference optimization without estimating log-likelihoods.

**Pick-a-Pic: A Large-Scale Dataset of Human Preferences for Text-to-Image Generation** (2023)
- *Authors:* Kirstain et al.
- *Direct Connection:* DSPO adopts the pairwise human preference formulation exemplified by Pick-a-Pic (two images per prompt with a winner), using such comparisons to construct its score-based preference loss.

### 💡 Inspiration

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023)
- *Authors:* Rafailov et al.
- *Direct Connection:* DSPO adopts DPO’s pairwise Bradley–Terry likelihood framing and reference-policy ratio idea but replaces token log-likelihoods with diffusion scores to avoid the intractable image likelihood estimation that arises when naively porting DPO to T2I.

### 🔍 Gap Identification

**ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation** (2023)
- *Authors:* Xu et al.
- *Direct Connection:* By demonstrating that reward-model-based T2I alignment requires training separate evaluators and can suffer from reward hacking, ImageReward motivates DSPO’s reward-free, direct preference optimization in diffusion score space.

---

## Synthesis: How Prior Work Led to This Paper

Direct Preference Optimization introduced a reward-free way to align generation with human choices by maximizing a pairwise Bradley–Terry likelihood under a reference-policy ratio, providing a simple, stable alternative to RLHF. Denoising Diffusion Probabilistic Models established diffusion training as denoising score matching, wherein the model learns the data score via a noise-prediction objective. Score-based generative modeling through SDEs formalized time-dependent data scores and their estimators, clarifying how gradients with respect to noisy samples correspond to likelihood gradients. Vincent’s connection between denoising and score matching tied denoising residuals to the data score, making it possible to optimize objectives without computing intractable likelihoods. ImageReward showed the promise of T2I alignment with human preferences but relied on separate reward models and RL fine-tuning, exposing instability and reward hacking risks. Pick-a-Pic standardized pairwise preference data for T2I, popularizing the two-candidate per prompt setup that underpins most preference-learning objectives.
Bringing these strands together reveals a gap: directly porting DPO-style likelihood-ratio objectives to diffusion models forces estimated image log-likelihoods, breaking alignment with the diffusion training objective and degrading performance. The natural next step is to marry the pairwise preference framing with the diffusion pretraining criterion itself: express preference learning in the diffusion score space. By using denoising score matching identities and time-dependent scores, one can define a reward-free, pairwise preference loss that is consistent with pretraining, avoids likelihood estimation, and preserves the stability that made DPO appealing.

---

*Analysis generated on: 2026-01-06T15:32:59.180776*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
