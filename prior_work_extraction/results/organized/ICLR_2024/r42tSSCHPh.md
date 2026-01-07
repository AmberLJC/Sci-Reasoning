# Prior Work Analysis Report

## Target Paper

**Title:** Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yangsibo Huang, Samyak Gupta, Mengzhou Xia, Kai Li, Danqi Chen

**Keywords:** Large Language Model, Alignment, Attack

**Abstract:** 
> The rapid progress in open-source large language models (LLMs) is significantly advancing AI development. Extensive efforts have been made before model release to align their behavior with human values, with the primary goal of ensuring their helpfulness and harmlessness. However, even carefully aligned models can be manipulated maliciously, leading to unintended behaviors, known as ``jailbreaks". These jailbreaks are typically triggered by specific text inputs, often referred to as adversarial ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Curious Case of Neural Text Degeneration** (2020)
- *Authors:* Ari Holtzman et al.
- *Direct Connection:* The attack explicitly exploits the top-k/top-p/temperature sampling behaviors characterized by Holtzman et al., showing that simply shifting these decoding hyperparameters can flip aligned models from refusal to harmful completions.

**Red Teaming Language Models with Language Models** (2022)
- *Authors:* Ethan Perez et al.
- *Direct Connection:* This work formalized automated red teaming through adversarial prompts under fixed decoding, providing the jailbreak problem framing and evaluation setup that this paper adopts while exposing a new attack surface at decoding time.

### 💡 Inspiration

**RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models** (2020)
- *Authors:* Samuel Gehman et al.
- *Direct Connection:* Gehman et al. empirically demonstrated that toxicity is highly sensitive to decoding choices (e.g., higher temperature and nucleus sampling), directly motivating the idea that decoding-only changes can elicit unsafe outputs without altering the prompt.

### 🔍 Gap Identification

**Jailbroken: How Does LLM Safety Training Fail?** (2023)
- *Authors:* Shen et al.
- *Direct Connection:* By cataloging failures of safety training under prompt manipulations but assuming fixed decoding, this work leaves open the overlooked vulnerability that we address: decoding variation alone can catastrophically defeat alignment.

### 📊 Baseline

**Universal and Transferable Adversarial Attacks on Aligned Language Models** (2023)
- *Authors:* Andy Zou et al.
- *Direct Connection:* We use their AdvBench harmful-instruction set and directly compare against their GCG adversarial-suffix method, showing that generation-exploitation attains higher attack success with ~30× fewer queries.

### 🔗 Related Problem

**Plug and Play Language Models: A Simple Approach to Controlled Text Generation** (2020)
- *Authors:* Sumanth Dathathri et al.
- *Direct Connection:* PPLM showed that decoding-time interventions can steer a fixed model toward targeted attributes without updating weights, a principle echoed here by steering aligned chat models into unsafe behaviors via generation-only control.

---

## Synthesis: How Prior Work Led to This Paper

Top-k, nucleus sampling, and temperature were dissected by Holtzman et al., who showed that decoding choices fundamentally reshape model output distributions, establishing that sampling hyperparameters are a first-class lever on model behavior. Gehman et al. then revealed that these same levers systematically modulate toxicity, with higher-temperature and nucleus sampling regimes increasing unsafe continuations, highlighting a direct linkage between decoding settings and safety. Dathathri et al. demonstrated that one can steer a frozen model toward targeted attributes purely at decoding time, proving that generation-time control—without weight changes—can strongly shift semantics. In parallel, Perez et al. formalized the jailbreak/red-teaming problem as inducing harmful behavior with adversarial prompts under fixed decoding setups, providing a canonical task framing and evaluation practices. Building on that framing, Zou et al. introduced GCG adversarial suffixes and the AdvBench harmful-instruction set, establishing state-of-the-art prompt-based jailbreaks and widely used benchmarks. Complementing these, “Jailbroken: How Does LLM Safety Training Fail?” systematically surfaced alignment failure modes but focused on prompt-space manipulations while keeping decoding fixed. Taken together, these works revealed that (1) decoding choices strongly change content and safety, (2) jailbreaks were pursued almost exclusively via prompt engineering, and (3) evaluations largely assumed fixed generation settings. The natural next step was to treat decoding itself as an attack surface: by systematically varying temperature, top-k/top-p, and sampling methods, one can shift the model’s generation distribution away from refusal and toward harmful completions. The current paper synthesizes these insights to show that generation-only manipulation, with minimal or no prompt changes, yields dramatically higher jailbreak success at a fraction of the query cost across open-source chat models.

---

*Analysis generated on: 2026-01-06T08:17:24.601399*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
