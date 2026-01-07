# Prior Work Analysis Report

## Target Paper
**Title:** Oo7dlLgqQX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper challenges the growing practice of inferring LLM demographics, values, and ideology from survey-style prompts. That practice was catalyzed by Argyle et al.’s use of LLMs as simulated survey populations and reinforced by studies like Rozado’s that mapped models onto political scales. The present work interrogates the validity of those inferences by drawing on two strands of prior evidence about response sensitivity. First, classic survey methodology (Schuman & Presser) documents strong order and wording effects in human respondents, suggesting that careful randomization and controls are necessary. Second, the LLM prompting literature has repeatedly uncovered option and order sensitivity: Perez et al. showed large variance from prompt/choice ordering; Zhao et al. identified label/position biases and proposed calibration; and Min et al. demonstrated that superficial label forms and ordering can drive in-context learning behavior. These insights motivate the paper’s core methodological move—randomizing answer ordering and examining label effects—and its central finding that, once such artifacts are controlled, many LLMs’ survey responses collapse toward uniform randomness rather than stable preferences. Finally, the pervasiveness of letter-labeled multiple-choice formats in LM evaluation (e.g., MMLU) contextualizes the observed systematic biases toward particular option labels (such as “A”). Together, these works directly inform the paper’s critique: much of the apparent alignment between LLM survey responses and specific human subgroups arises from prompt-induced artifacts, not from genuine latent attitudes.

---
*Generated: 2026-01-06T23:39:42.951495*
