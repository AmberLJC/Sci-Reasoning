# Prior Work Analysis Report

## Target Paper

**Title:** Controlled Text Generation via Language Model Arithmetic

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jasper Dekoninck, Marc Fischer, Luca Beurer-Kellner, Martin Vechev

**Keywords:** Controlled text generation, LLM, Natural Language Processing

**Abstract:** 
> As Large Language Models (LLMs) are deployed more widely, customization with respect to vocabulary, style, and character becomes more important. In this work, we introduce model arithmetic, a novel inference framework for composing and biasing LLMs without the need for model (re)training or highly specific datasets. In addition, the framework allows for more precise control of generated text than direct prompting and prior controlled text generation (CTG) techniques. Using model arithmetic, we c...

---

## Key Prior Works (7 papers with direct influence)

### 🔍 Gap Identification

**Plug and Play Language Models: A Simple Approach to Controlled Text Generation** (2020)
- *Authors:* Dathathri et al.
- *Direct Connection:* The work targets PPLM’s gradient-in-the-loop inefficiency and instability by replacing per-step hidden-state optimization with closed-form logit arithmetic that yields cheaper, more precise control at inference.

### 🔧 Extension

**DExperts: Decoding-Time Controlled Text Generation with Experts and Anti-Experts** (2021)
- *Authors:* Liu et al.
- *Direct Connection:* The paper recasts DExperts’ expert/anti-expert ratio as linear logit-space arithmetic and generalizes it to compose multiple controllers with tunable strengths without additional finetuning.

**GeDi: Generative Discriminator Guided Sequence Generation** (2021)
- *Authors:* Krause et al.
- *Direct Connection:* GeDi’s Bayes-guided class-conditional steering is expressed as adding discriminator LM log-likelihoods to the base model’s logits, which the paper unifies and extends within a single arithmetic framework.

**FUDGE: Controlled Text Generation with Future Discriminators** (2021)
- *Authors:* Yang and Klein
- *Direct Connection:* FUDGE’s future-conditioned discriminator update corresponds to additive log-probability adjustments that the paper incorporates as a special case of its model arithmetic for attribute composition.

**Self-Debiasing for Generative Language Models** (2021)
- *Authors:* Schick et al.
- *Direct Connection:* Self-Debiasing’s subtractive logit adjustment using a bias-only prompt is captured as anti-expert subtraction in the model arithmetic, which the paper extends to multi-attribute, multi-model compositions.

**Fast Inference from Transformers via Speculative Decoding** (2023)
- *Authors:* Leviathan et al.
- *Direct Connection:* The paper extends speculative decoding to verify and accelerate sequences generated under composed-model logits, showing compatibility that preserves near single-model runtime.

### 🔗 Related Problem

**Contrastive Decoding for Open-Ended Text Generation** (2022)
- *Authors:* Li et al.
- *Direct Connection:* The paper generalizes contrastive decoding’s difference-of-models guidance (strong vs. weak LM) as a ratio in logit space, enabling broader, attribute-driven composition beyond quality control.

---

## Synthesis: How Prior Work Led to This Paper

A line of controlled generation methods established that decoding-time probability shaping can steer language models without retraining. DExperts introduced a ratio between an expert and anti-expert LM to bias outputs toward or away from attributes, operationalized as logit additions that realize a product-of-experts view. GeDi framed control as Bayes-guided class-conditional steering with a generative discriminator, effectively adding the discriminator’s class likelihoods to the base model’s token logits. FUDGE showed that a future-conditioned discriminator can adjust next-token probabilities via additive log-prob updates computed from partial continuations. PPLM demonstrated strong attribute control by iteratively perturbing hidden states using gradient signals but suffered from instability and substantial decoding overhead. Self-Debiasing revealed a simple subtractive logit trick by contrasting biased versus neutral prompts to reduce unwanted attributes. In parallel, contrastive decoding reduced degeneration by penalizing continuations favored by a weaker LM, operationally a difference-of-models ratio in logit space. Finally, speculative decoding provided a general mechanism to accelerate sampling by drafting tokens and verifying them with a target distribution.
These ingredients collectively suggested a unifying perspective: many CTG techniques are instances of simple arithmetic on model logits or log-likelihoods. By making that arithmetic explicit, one can compose multiple controllers, tune strengths continuously, and subsume prior methods as special cases while avoiding PPLM’s gradient costs. Extending speculative decoding to these composed distributions yields practical, efficient sampling, enabling scalable, fine-grained control at near single-model latency.

---

*Analysis generated on: 2026-01-06T05:52:52.022602*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
