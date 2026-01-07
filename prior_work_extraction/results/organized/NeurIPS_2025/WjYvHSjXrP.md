# Prior Work Analysis Report

## Target Paper
**Title:** WjYvHSjXrP
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

InstructHOI shifts HOI detection from prompt-driven feature transfer to instruction-guided multi-modal reasoning. This pivot is anchored in two complementary lines of prior art. First, CLIP established a robust image–text alignment space that underlies modern HOI methods; CoOp and CoCoOp then demonstrated that adapting CLIP with learnable (and context-conditional) prompts can significantly improve downstream performance, a strategy widely adopted by prompt-based HOI detectors. InstructHOI explicitly moves beyond these discriminative prompts by using instructions to elicit reasoning, addressing the ambiguity and open-world nature of interactions.
Second, the visual instruction tuning literature—BLIP-2, InstructBLIP, and LLaVA—showed how to connect strong image encoders to language models and to fine-tune them with synthetic, LLM-authored instruction data so models can follow task directives and produce context-aware rationales. InstructHOI directly instantiates this recipe for the HOI domain: it constructs a large-scale (140K) interaction–reasoning corpus, fine-tunes a VLM to bridge the HOI knowledge gap, and introduces a Context-aware Instruction Generator to tailor instructions to detected humans/objects and scene context.
Finally, GLIP’s grounded pretraining provides the open-vocabulary localization and language grounding capabilities needed to tie instructions about verbs and objects to specific regions. Together, these works enable InstructHOI’s core innovation: context-aware instruction generation and instruction-tuned multi-modal reasoning that materially improves ambiguous and open-world HOI detection.

---
*Generated: 2026-01-07T00:02:04.960557*
