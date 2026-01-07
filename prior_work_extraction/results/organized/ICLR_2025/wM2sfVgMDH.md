# Prior Work Analysis Report

## Target Paper

**Title:** Diffusion-Based Planning for Autonomous Driving with Flexible Guidance

**Conference:** ICLR 2025 (oral)

**Authors:** Yinan Zheng, Ruiming Liang, Kexin ZHENG, Jinliang Zheng, Liyuan Mao, Jianxiong Li, Weihao Gu, Rui Ai, Shengbo Eben Li, Xianyuan Zhan, Jingjing Liu

**Keywords:** diffusion planning, autonomous driving

**Abstract:** 
> Achieving human-like driving behaviors in complex open-world environments is a critical challenge in autonomous driving. Contemporary learning-based planning approaches such as imitation learning methods often struggle to balance competing objectives and lack of safety assurance,due to limited adaptability and inadequacy in learning complex multi-modal behaviors commonly exhibited in human planning, not to mention their strong reliance on the fallback strategy with predefined rules. We propose a...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Diffusion Models Beat GANs** (2021)
- *Authors:* Prafulla Dhariwal et al.
- *Direct Connection:* The flexible classifier guidance in this paper is built on Dhariwal and Nichol’s classifier-guided diffusion framework, using gradient-based conditioning to steer sampling toward desired attributes.

**UniAD: A Unified Framework for Autonomous Driving** (2023)
- *Authors:* Jianren Weng et al.
- *Direct Connection:* UniAD’s unified architecture for joint prediction and planning motivated the paper’s single-architecture formulation that models both prediction and planning for cooperative behaviors.

### 💡 Inspiration

**Classifier-Free Diffusion Guidance** (2021)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* The notion of trading off fidelity and conditioning strength in diffusion sampling inspired the paper’s flexible guidance mechanism that balances competing driving objectives without rule-based post-processing.

### 📊 Baseline

**DiffAD: End-to-End Diffusion-Based Autonomous Driving** (2023)
- *Authors:* Li et al.
- *Direct Connection:* As a diffusion-based driving baseline that still relies on heuristic refinements, DiffAD’s limitations directly motivated the proposed planner’s no-rule, guidance-driven trajectory quality assurance.

### 🔧 Extension

**Planning with Diffusion for Control** (2022)
- *Authors:* Michael Janner et al.
- *Direct Connection:* The Diffusion Planner directly extends Janner et al.’s idea of trajectory-level diffusion planning by incorporating multi-objective guidance and closed-loop execution tailored to autonomous driving.

### 🔗 Related Problem

**Diffusion Policy: Visuomotor Policy Learning via Action Diffusion** (2023)
- *Authors:* Michele Chi et al.
- *Direct Connection:* Diffusion Policy’s demonstration that action-sequence diffusion yields robust, closed-loop multi-modal control informed the choice to model driving trajectories with a transformer-based diffusion policy.

---

## Synthesis: How Prior Work Led to This Paper

Diffusion models were adapted to control by Janner et al., who proposed planning with trajectory-level diffusion and showed that sampling could be steered by objective signals, seeding the idea that generative denoising could serve as a planner. Dhariwal and Nichol established classifier-guided diffusion, computing gradients of conditional likelihoods to guide denoising toward desired attributes—a mechanism that generalizes naturally to multi-objective control signals. Ho and Salimans introduced classifier-free guidance, formalizing a tractable way to trade off data fidelity and conditioning strength during sampling, clarifying the knob to balance competing preferences. In robotics, Diffusion Policy showed that action-diffusion policies yield robust closed-loop control while preserving multi-modality, validating diffusion policies as controllers rather than one-shot generators. Within autonomous driving, UniAD argued for a unified architecture that jointly models prediction and planning so that downstream planning can account for interactive agents, laying a template for cooperative behaviors. DiffAD demonstrated diffusion-based end-to-end driving but still depended on rule-based refinements, revealing the need for principled guidance that enforces safety and objective balance during sampling. Together these works expose a gap: trajectory diffusion can plan, guidance can steer generation, and unified architectures enable cooperation, yet driving needs a flexible, multi-objective guidance scheme that removes hand-crafted fallbacks. The present work synthesizes trajectory diffusion with classifier-style guidance to learn a trajectory score and apply adjustable, differentiable objectives during denoising, unifying prediction and planning in a transformer policy that achieves safe, multi-modal, closed-loop driving without rule-based refinement.

---

*Analysis generated on: 2026-01-06T06:13:15.088516*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
