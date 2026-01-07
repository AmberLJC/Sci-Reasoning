# Prior Work Analysis Report

## Target Paper
**Title:** PhIWEbewAz
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

PropInfer’s core contribution—benchmarking and attacking dataset-level property leakage from fine-tuned LLMs—roots itself in the property inference literature and the recent auditing toolkit for generative LMs. The basic threat model and learning-to-infer paradigm trace to Ganju et al., who formalized property inference for discriminative networks, and to Melis et al., who showed practical leakage in collaborative learning via auxiliary/shadow models and distributional cues. Shokri et al.’s seminal shadow-model methodology underpins PropInfer’s second attack: training auxiliary models to map observable outputs to hidden training-set attributes, here realized with word-frequency features tailored to text generation.

On the generative side, Carlini et al. (2019; 2021) demonstrated that LMs memorize and can be prompted to reveal training data, introducing exposure-style measurement and concrete prompt-based extraction tactics. PropInfer’s prompt-based generation attack transposes these insights from individual-record leakage to aggregate property inference, probing whether fine-tuning imprints detectable distributional signatures into LLM outputs. Jagielski et al.’s auditing recipe further informs PropInfer’s black-box evaluation and probing strategies, emphasizing output statistics as a robust signal for privacy audits.

Finally, to ground the study in a realistic, high-stakes domain, PropInfer leverages the ChatDoctor medical dataset and conversational setup, enabling QA and chat-completion fine-tuning regimes where confidential cohort-level attributes (e.g., demographics, prevalence) are salient. Together, these prior works directly shape PropInfer’s benchmark design and its two tailored attacks, bridging classic property inference with modern LLM auditing to expose dataset-level privacy risks in fine-tuned language models.

---
*Generated: 2026-01-07T00:05:12.514236*
