# Prior Work Analysis Report

## Target Paper
**Title:** ZwBtDbuzjY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

InfiFPO’s core innovation—implicit model fusion within preference optimization—rests on rethinking the DPO reference model as a fused, probability-preserving aggregator of multiple sources. Direct Preference Optimization (Rafailov et al., 2023) provides the foundational log-ratio structure that InfiFPO modifies: rather than anchoring to a single fixed reference, it constructs an implicit reference that synthesizes multi-model sequence probabilities, thereby retaining fine-grained uncertainty information lost by output-only fusion approaches (e.g., WRPO). Concurrently, ORPO (Hong et al., 2024) demonstrates the sensitivity of preference learning to the treatment of the reference term, motivating InfiFPO’s choice to control—not discard—the reference through a principled fusion.
Weight-space fusion methods like Model Soup (Wortsman et al., 2022) and Task Arithmetic (Ilharco et al., 2023) established the appeal of combining specialized models but suffer from architecture/tokenizer constraints and interference. InfiFPO sidesteps these issues by operating at the sequence-probability level, eliminating vocabulary-alignment burdens common in weight/logit-space merges across heterogeneous tokenizers.
The design of InfiFPO’s fusion mechanism is informed by probability-combination and distillation literature. Multi-teacher knowledge distillation (Hinton et al., 2015) underscores the value of transferring soft probabilities, while Products of Experts (Hinton, 2002) offers a theoretical lens for multiplicative/log-linear combination of distributions that guides InfiFPO’s max-margin fusion. Finally, stability considerations from PPO (Schulman et al., 2017) motivate probability clipping, ensuring robust optimization when aggregating heterogeneous model confidences. Together, these threads yield a preference-alignment-centric fusion method that preserves uncertainty, avoids tokenizer alignment, and stabilizes training.

---
*Generated: 2026-01-07T00:02:04.963843*
