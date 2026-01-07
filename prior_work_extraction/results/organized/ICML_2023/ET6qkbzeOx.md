# Prior Work Analysis Report

## Target Paper
**Title:** ET6qkbzeOx
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Lexically Constrained Decoding for Sequence Generation Using Grid Beam Search** (2017)
- *Authors:* Chris Hokamp et al.
- *Connection:* This paper formalized the problem of enforcing lexical constraints during decoding, directly defining the control objective that GeLaTo seeks to satisfy but without offering a tractable probabilistic mechanism.

**A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition** (1989)
- *Authors:* Lawrence R. Rabiner
- *Connection:* Rabiner established HMMs and their exact forward–backward inference, the tractable machinery GeLaTo exploits to compute and sample from p(text | lexical constraints) once the HMM is aligned with the LM.

### 💡 Inspiration

**GeDi: Generative Discriminator Guided Sequence Generation** (2021)
- *Authors:* Ben Krause et al.
- *Connection:* GeDi’s Bayes-inspired reweighting with a generative controller directly inspired GeLaTo’s key idea, which replaces GeDi’s neural controller with a tractable probabilistic model (distilled HMM) to make conditioning efficient and principled.

### 🔍 Gap Identification

**Fast Lexically Constrained Decoding for Sequence Generation** (2018)
- *Authors:* Matt Post et al.
- *Connection:* By improving the efficiency of lexically constrained beam search yet still facing combinatorial complexity and limited expressivity, this work highlights the need for a principled, tractable approach that GeLaTo provides via TPM-based conditioning.

**Plug and Play Language Models: A Simple Approach to Controlled Text Generation** (2020)
- *Authors:* Archit Dathathri et al.
- *Connection:* PPLM demonstrated steering LMs with auxiliary signals but relied on heuristic gradient-based updates without exact constraint satisfaction; GeLaTo addresses this gap by computing p(text | constraints) with a tractable model.

**FUDGE: Controlled Text Generation With Future Discriminators** (2021)
- *Authors:* Kevin Yang et al.
- *Connection:* FUDGE conditions decoding on a learned discriminator estimating future constraint satisfaction, motivating GeLaTo’s shift to a generative, tractable controller that yields exact probabilistic guidance instead of learned proxies.

### 🔧 Extension

**Distilling the Knowledge in a Neural Network** (2015)
- *Authors:* Geoffrey Hinton et al.
- *Connection:* GeLaTo directly applies the knowledge-distillation paradigm to transfer GPT-2’s distribution into a compact HMM, enabling a tractable controller that faithfully guides the base LM under constraints.

---

## Synthesis

GeLaTo’s core contribution—using a tractable probabilistic model to compute p(text | constraints) and guide an autoregressive LM—sits at the intersection of constrained decoding and controllable generation, while crucially introducing tractability via a distilled HMM. The constrained decoding lineage begins with Hokamp and Liu’s grid beam search, which formulated lexical constraints during decoding, and Post and Vilar’s faster variant. These works defined the problem but remained combinatorial and limited in expressivity, motivating a probabilistic alternative. Controllable generation methods like PPLM and FUDGE showed how auxiliary models can steer generation, but they relied on approximate gradients or learned future discriminators that do not provide exact conditioning or guarantees. GeDi took a decisive step by reframing control through Bayes with a generative controller, directly inspiring GeLaTo’s approach of pairing the base LM with an auxiliary generative model. GeLaTo advances this idea by selecting a tractable probabilistic model—an HMM—for which exact conditional inference is possible, grounded in Rabiner’s forward–backward algorithms. To align this tractable controller with a powerful LM, GeLaTo leverages knowledge distillation (Hinton et al.), transferring GPT‑2’s behavior into the HMM so that the controller’s probabilities faithfully reflect the LM’s distribution. Together, these works shaped GeLaTo’s insight: make constraint satisfaction tractable by distilling a strong LM into a TPM and using its exact conditional computations to guide autoregressive decoding.

---
*Generated: 2026-01-06T23:09:26.515251*
