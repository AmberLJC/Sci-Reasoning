# Prior Work Analysis Report

## Target Paper
**Title:** oJ84bedrtM
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**LoRA: Low-Rank Adaptation of Large Language Models** (2022)
- *Authors:* Edward J. Hu et al.
- *Connection:* MokA directly builds on LoRA’s low‑rank weight update mechanism, extending it to multimodal settings by splitting low‑rank parameters into modality‑specific (unimodal) paths and an explicit cross‑modal enhancement path.

**Flamingo: a Visual Language Model for Few-Shot Learning** (2022)
- *Authors:* Jean-Baptiste Alayrac et al.
- *Connection:* Flamingo’s gated cross‑attention layers established the importance of explicit cross‑modal interaction in MLLMs, which MokA preserves under a parameter‑efficient form via a dedicated cross‑modal adaptation component.

### 💡 Inspiration

**BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models** (2023)
- *Authors:* Junnan Li et al.
- *Connection:* BLIP‑2’s Q‑Former demonstrated that learnable modules explicitly mediating image–text alignment are critical; MokA adopts this insight by adding an explicit cross‑modal enhancement branch instead of relying solely on unimodal updates.

### 📊 Baseline

**LLaVA: Large Language and Vision Assistant** (2023)
- *Authors:* Haotian Liu et al.
- *Connection:* LLaVA popularized applying standard LoRA to MLLMs without modality-aware design; MokA explicitly targets this baseline’s limitation by separating unimodal adaptation from cross‑modal interaction to improve fine‑tuning effectiveness.

### 🔗 Related Problem

**LLaMA-Adapter V2: Parameter-Efficient Visual Instruction Model** (2023)
- *Authors:* Renrui Zhang et al.
- *Connection:* LLaMA‑Adapter V2 shows parameter‑efficient visual instruction tuning via lightweight cross‑modal connectors; MokA pursues the same goal but implements it through multimodal-aware low‑rank updates that jointly handle unimodal and cross‑modal adaptation.

**Visual Prompt Tuning** (2022)
- *Authors:* Menglin Jia et al.
- *Connection:* VPT evidenced that small, modality‑specific parameters can effectively adapt a frozen visual backbone; MokA generalizes this idea to MLLMs by assigning modality‑specific low‑rank parameters for unimodal compression.

---

## Synthesis

MokA’s core idea—decoupling unimodal adaptation from cross‑modal adaptation within a parameter‑efficient scheme—emerges from two converging lines of work. First, LoRA provided the crucial mechanism for lightweight fine‑tuning, but when ported to MLLMs (as in LLaVA), it was typically applied uniformly across the model without acknowledging modality structure. This created the gap MokA targets: standard PEFT borrowed from LLMs underutilizes multimodal cues. Second, large‑scale multimodal architectures such as Flamingo and BLIP‑2 established that explicit cross‑modal interaction modules (gated cross‑attention, Q‑Former) are vital for aligning modalities, highlighting that cross‑modal adaptation should be treated distinctly from unimodal processing.

MokA synthesizes these insights by reshaping LoRA into a multimodal‑aware design: modality‑specific low‑rank parameters compress unimodal information, while an explicit cross‑modal enhancement path directly strengthens inter‑modal interaction. This design goal resonates with parameter‑efficient MLLM adapters (e.g., LLaMA‑Adapter V2), yet MokA accomplishes it natively within a low‑rank formulation rather than adding heavy cross‑modal blocks. Additionally, results from visual prompt tuning reinforce the value of small, modality‑scoped parameters, which MokA extends beyond vision to audio, speech, and text. In sum, MokA unifies the efficiency of LoRA with the architectural lesson from Flamingo/BLIP‑2—that cross‑modal alignment must be explicit—thereby addressing the LLaVA‑style gap and yielding a principled, multimodal‑aware PEFT approach.

---
*Generated: 2026-01-06T23:08:23.965162*
