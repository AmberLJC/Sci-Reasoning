# Prior Work Analysis Report

## Target Paper
**Title:** fykjplMc0V
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ReFT’s central move is to shift parameter-efficient adaptation from weight space to representation space and to do so with compact, structured updates. This advances a trajectory launched by PEFT methods—Adapters, Prefix-Tuning, and P-Tuning v2—that kept base weights frozen while injecting compact task information to influence internal activations. LoRA contributed the crucial low-rank parameterization lens, showing that much of fine-tuning’s effect can be captured by low-dimensional updates; LoReFT transfers this economy to hidden states by learning low-rank linear subspace transforms at selected layers, yielding large parameter savings while preserving expressivity.
Interpretability and model-editing work directly motivate operating on representations. The structural probe of Hewitt and Manning demonstrated that core linguistic structure is linearly embedded in hidden states, suggesting that linear subspace manipulations can be both principled and effective. ROME and MEMIT then showed that small, localized interventions can reliably alter model behavior, with MEMIT further illustrating scalability and composability. ReFT synthesizes these insights: it treats finetuning as learning targeted, low-rank representation interventions that are drop-in replacements for PEFT modules but far more parameter-efficient. By focusing on hidden-state transformations rather than weight updates or large prompt tensors, ReFT captures the benefits of earlier PEFT techniques, the causal precision of model editing, and the linear structure revealed by interpretability—yielding a practical, general recipe for efficient adaptation across reasoning and instruction-following tasks.

---
*Generated: 2026-01-06T23:33:35.539187*
