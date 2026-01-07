# Prior Work Analysis Report

## Target Paper

**Title:** Controlling Language and Diffusion Models by Transporting Activations

**Conference:** ICLR 2025 (spotlight)

**Authors:** Pau Rodriguez, Arno Blaas, Michal Klein, Luca Zappella, Nicholas Apostoloff, marco cuturi, Xavier Suau

**Keywords:** controllability, generative models, toxicity, diffusion

**Abstract:** 
> The increasing capabilities of large generative models and their ever more widespread deployment have raised concerns about their reliability, safety, and potential misuse. To address these issues, recent works have proposed to control model generation by steering model activations in order to effectively induce or prevent the emergence of concepts or behaviors in the generated output.
In this paper we introduce Activation Transport (AcT), a general framework to steer activations guided by optim...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Plug and Play Language Models: A Simple Approach to Controlled Text Generation** (2020)
- *Authors:* Shrimai Dathathri et al.
- *Direct Connection:* AcT adopts the core idea of controllable generation by directly intervening on hidden activations during inference, but replaces PPLM’s gradient-based, compute-heavy updates with an optimal-transport formulation that yields lightweight, targeted shifts.

**Sinkhorn Distances: Lightspeed Computation of Optimal Transport** (2013)
- *Authors:* Marco Cuturi
- *Direct Connection:* AcT relies on entropically regularized optimal transport and Sinkhorn iterations to compute efficient activation couplings that minimally move representations while achieving the desired control signal.

### 🔍 Gap Identification

**Null It Out: Guarding Protected Attributes in Neural Representations by Iterative Nullspace Projection (INLP)** (2020)
- *Authors:* Shauli Ravfogel et al.
- *Direct Connection:* By showing that linear projection-based concept removal can over-suppress and hurt capabilities, INLP motivates AcT’s minimal-transport criterion that steers away from undesired attributes while preserving model ability.

### 📊 Baseline

**Representation Engineering: A Top-Down Approach to Steering Language Models** (2023)
- *Authors:* Rimsky et al.
- *Direct Connection:* AcT directly builds on representation engineering’s practice of constructing contrastive activation interventions, replacing a single global direction with a data-adaptive OT transport that provides finer, layer- and token-wise control.

### 🔧 Extension

**Activation Addition: Steering Language Models Without Optimization** (2023)
- *Authors:* Turner et al.
- *Direct Connection:* AcT generalizes activation addition by interpreting simple direction-based shifts as a special case of an optimal-transport coupling that translates activations from a source to a target distribution.

### 🔗 Related Problem

**Prompt-to-Prompt Image Editing with Cross Attention Control** (2022)
- *Authors:* Amir Hertz et al.
- *Direct Connection:* AcT extends the idea of diffusion-time control via internal feature manipulation by providing a unified activation-transport mechanism (rather than cross-attention map replacement) that applies broadly across U-Net layers and tasks.

---

## Synthesis: How Prior Work Led to This Paper

Controllable generation by intervening on hidden states was first operationalized in Plug and Play Language Models, which demonstrated that attribute-guided inference-time activation updates can steer outputs but at significant computational cost and with sensitivity to optimization dynamics. Representation-level edits evolved with Representation Engineering, which distilled contrastive behaviors into activation directions applied at specific layers, offering practical, optimization-free control but largely relying on a single global shift. Activation Addition further simplified this paradigm by adding fixed direction vectors computed from contrasting prompts or datasets, making steering extremely lightweight but limited in granularity and adaptability. In diffusion, Prompt-to-Prompt revealed that modifying internal conditioning signals—specifically cross-attention maps—enables precise semantic edits without retraining, highlighting the power of activation-space interventions beyond language. Parallelly, INLP showed that linear subspace removal can suppress protected attributes but often over-prunes representational capacity, underlining the need for more conservative, behavior-preserving edits. Entropic optimal transport (Sinkhorn) introduced an efficient way to compute minimal-cost couplings between distributions, offering a principled tool for targeted, small shifts.
Synthesizing these threads, a clear opportunity emerged: retain the efficiency of direction-based activation steering while moving beyond a single global vector to a minimal, data-adaptive transformation that preserves model ability across modalities. Activation Transport realizes this by casting steering as an optimal-transport problem over activations, generalizing direction addition and attention editing into a unified, fine-grained coupling with negligible overhead, directly addressing the limitations of optimization-heavy methods and over-aggressive linear projections.

---

*Analysis generated on: 2026-01-06T15:26:08.365508*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
