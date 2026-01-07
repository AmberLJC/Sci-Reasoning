# Prior Work Analysis Report

## Target Paper
**Title:** w0xYx9CJhY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MARINE addresses object hallucination in LVLMs by injecting image-grounded, object-level guidance during inference—training-free and API-free. Rohrbach et al. (2018) crystallized the hallucination problem and introduced object-level evaluation (e.g., CHAIR), defining the precise failure mode MARINE targets. The object-centric lineage from Anderson et al. (2018) showed that using detector-derived region features yields more grounded text, establishing the utility of explicit object signals for language generation. VinVL (2021) further evidenced that stronger detection improves caption faithfulness, reinforcing the idea that high-quality object cues can curb hallucinations.
Crucially, modern open-source detectors make such cues broadly accessible. OWL-ViT (2022) provides open-vocabulary detection, while Grounding DINO (2023) enables robust phrase grounding—together they furnish the flexible, object-level evidence MARINE aggregates to validate or veto candidate tokens. On the algorithmic side, MARINE’s training-free integration philosophy is influenced by Socratic Models (2022), which compose frozen vision and language systems via lightweight messaging, and by Plug-and-Play Language Models (2020), which pioneered inference-time guidance without fine-tuning. MARINE adapts these ideas to the multimodal setting: instead of gradient or classifier signals, it leverages detector-derived object lists and grounding scores to steer LVLM decoding, ensuring generated content remains consistent with the image. By uniting object-centric vision backbones with plug-and-play, inference-time control, MARINE delivers a practical, model-agnostic approach to suppress object hallucinations.

---
*Generated: 2026-01-07T00:21:32.369078*
