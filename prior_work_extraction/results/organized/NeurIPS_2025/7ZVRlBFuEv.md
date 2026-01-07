# Prior Work Analysis Report

## Target Paper
**Title:** 7ZVRlBFuEv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Structured Denoising Diffusion Models in Discrete State-Spaces** (2021)
- *Authors:* Jacob Austin et al.
- *Connection:* This work introduced the discrete diffusion formulation that enables token-level denoising over vocabularies, providing the core probabilistic framework that d1’s masked diffusion language model builds on.

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Connection:* This paper established the SFT→RLHF post-training pipeline that improves LLM capabilities; d1 ports the same SFT+RL paradigm to diffusion LMs, addressing that prior RL-based reasoning gains were AR-only.

### 💡 Inspiration

**Planning with Diffusion for Decision Making (Diffuser)** (2022)
- *Authors:* Michael Janner et al.
- *Connection:* Diffuser showed how a learned critic/Q-function can guide diffusion trajectories toward high reward; d1 extends this reward/critic-guided diffusion idea to text by using an RL critic to steer masked denoising toward higher-reasoning outputs.

**STaR: Bootstrapping Reasoning with Reasoning** (2022)
- *Authors:* Eric Zelikman et al.
- *Connection:* STaR’s self-improvement via distilling correct rationales directly motivates d1’s masked SFT procedure, which distills reasoning signals into a diffusion LM to seed and stabilize subsequent RL.

### 📊 Baseline

**Diffusion-LM Improves Controllable Text Generation** (2022)
- *Authors:* Xiang Lisa Li et al.
- *Connection:* Diffusion-LM established diffusion-based language modeling for text and demonstrated competitive generation quality, serving as the primary diffusion-LM paradigm that d1 adapts and upgrades for reasoning via SFT+RL.

### 🔧 Extension

**Classifier-Free Diffusion Guidance** (2022)
- *Authors:* Jonathan Ho et al.
- *Connection:* d1 adapts the guidance principle from classifier-free guidance by replacing class-conditioning with an RL-derived critic signal to bias the diffusion sampling process toward reward-aligned (reasoning-correct) completions.

**Process supervision improves mathematical reasoning of language models** (2023)
- *Authors:* Matthew L. Lightman et al.
- *Connection:* This work’s process reward models for step-level evaluation inform d1’s critic design, enabling step/partial-solution-aware signals that guide iterative diffusion refinement during RL.

---

## Synthesis

d1 sits at the intersection of diffusion-based text generation and reinforcement learning for reasoning. Its diffusion backbone traces directly to the discrete diffusion formulation of Austin et al., which made token-space denoising feasible, and to Diffusion-LM, which established masked diffusion as a viable language modeling alternative to autoregression. However, reasoning advances had largely been confined to the AR regime under the SFT→RLHF pipeline popularized by Ouyang et al., leaving a clear gap: could diffusion LMs also benefit from post-training with RL?

Two lines of work directly shape d1’s answer. First, STaR demonstrated that models can self-improve by harvesting correct rationales and distilling them via SFT. d1 adapts this idea to the masked diffusion setting, using masked SFT to inject reasoning behaviors and create a stable starting point for RL. Second, reward-guided diffusion from decision-making (Diffuser) and the broader notion of diffusion guidance (classifier-free guidance) reveal how learned signals can steer the denoising trajectory. d1 extends these principles by introducing an RL-derived critic that provides guidance signals tailored to reasoning quality—akin to process supervision, where step-level reward models (Lightman et al.) evaluate intermediate reasoning. Together, these works supply the core ingredients—discrete diffusion modeling, self-improvement SFT, and critic/guidance-based steering—that d1 integrates to scale reasoning in diffusion language models via reinforcement learning.

---
*Generated: 2026-01-06T23:08:23.959640*
