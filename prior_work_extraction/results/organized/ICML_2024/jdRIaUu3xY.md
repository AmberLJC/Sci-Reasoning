# Prior Work Analysis Report

## Target Paper
**Title:** jdRIaUu3xY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

BBox-Adapter’s central contribution is a lightweight, external adapter that adapts black-box LLMs using only API interactions, trained with a ranking-based NCE objective and online feedback. Two strands of prior work directly converge here. First, contrastive estimation—particularly Noise-Contrastive Estimation (Gutmann & Hyvärinen) and InfoNCE via Contrastive Predictive Coding (van den Oord et al.)—establishes that models can be trained from relative comparisons between positives and negatives without normalized probabilities. BBox-Adapter operationalizes this insight for LLM adaptation: it treats target-domain data as positives and source-domain or previously produced outputs as negatives, optimizing a ranking-style NCE to shift the model’s implicit likelihoods while never accessing logits.

Second, the feedback-driven alignment literature—RLHF (Christiano et al.) and InstructGPT (Ouyang et al.)—shows that pairwise or preference-like signals can robustly steer model behavior. BBox-Adapter inherits this idea but makes it compatible with black-box constraints, enabling online incorporation of positives drawn from ground-truth, human, or AI feedback. Constitutional AI (Bai et al.) further motivates replacing costly human labels with AI feedback, which BBox-Adapter explicitly supports.

Finally, parameter-efficient control of LMs—Prefix-Tuning (Li & Liang) and Prompt Tuning (Lester et al.)—demonstrates the power of small controllers to retarget LMs without full fine-tuning. BBox-Adapter adapts this paradigm to the hardest setting: closed-source, API-only models that may not expose probabilities, combining lightweight control with contrastive, preference-style learning to yield practical black-box adaptation.

---
*Generated: 2026-01-06T23:42:48.051960*
