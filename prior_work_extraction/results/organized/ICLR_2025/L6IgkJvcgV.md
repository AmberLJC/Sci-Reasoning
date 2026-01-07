# Prior Work Analysis Report

## Target Paper
**Title:** L6IgkJvcgV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

OASIS reframes stereotype measurement in text-to-image models by grounding it in association-based, concept-aligned analyses rather than parity counts. This framing traces directly to WEAT, which formalized stereotypes as measurable associations along attribute axes; OASIS adapts this idea to vision by quantifying how generated images align with stereotypical attributes. Complementing this, prior work on bias amplification in vision (e.g., Men Also Like Shopping) established distributional comparisons between model outputs and reference distributions, informing OASIS’s Stereotype Score for detecting systematic deviations in generated datasets.
To turn stereotypes into measurable directions within models, OASIS leverages the projection-based philosophy of TCAV—quantifying sensitivity along human-meaningful concept axes—and operationalizes it at scale using CLIP’s joint vision–language embeddings to automatically score images for attributes. The WALS score extends this direction-based analysis by examining spectral/variance structure along attributes, an idea resonant with GANSpace’s principal-component view of semantic control.
Understanding where stereotypes arise within T2I pipelines requires peering into contemporary architectures. OASIS’s origin analyses target the cross-attention and latent machinery of Latent Diffusion/Stable Diffusion, drawing on methods like Prompt-to-Prompt that attribute and control image content at the token level. Together, these strands—association-based stereotype theory, distributional auditing, concept-direction quantification, multimodal embeddings, and cross-attention interpretability—compose the conceptual and technical scaffold that OASIS unifies into stereotype-aligned measurement and origin tracing for modern T2I models.

---
*Generated: 2026-01-07T00:02:04.914451*
