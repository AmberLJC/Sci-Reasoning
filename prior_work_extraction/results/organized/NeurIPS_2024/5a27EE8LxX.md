# Prior Work Analysis Report

## Target Paper
**Title:** 5a27EE8LxX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MULI’s core insight—that an aligned LLM’s first-response-token logits encode a strong signal about a prompt’s harmfulness—rests on two intertwined lines of prior work: safety alignment shaping refusal behavior and the use of model-internal probability signals for downstream detection. RLHF (Ouyang et al.) and Constitutional AI (Bai et al.) established consistent refusal patterns for unsafe inputs, implicitly concentrating probability mass on stereotypical refusal openings. RealToxicityPrompts framed and measured toxic prompting, while ToxiGen contributed adversarial data and strong baselines, clarifying the shortcomings of standalone text classifiers at low FPRs—precisely the regime MULI targets.

On the methodological side, GPT-3’s few-shot learning demonstrated how LM logits can drive classification, and DetectGPT showed that introspective likelihood structure enables robust detectors. SelfCheckGPT further validated the principle of LLM self-assessment for safety and reliability. MULI fuses these threads into a practical, low-cost moderation mechanism: instead of generating and then judging text, it inspects the pre-generation probability distribution of the very first token and applies a sparse logistic regression to those logits. This leverages alignment-induced refusal priors while achieving high TPR at low FPR and minimizing inference overhead. The result is a simple, robust detector that directly harnesses the model’s internal safety signal, outperforming traditional toxicity classifiers that lack access to this alignment-shaped logit geometry.

---
*Generated: 2026-01-06T23:39:42.953817*
