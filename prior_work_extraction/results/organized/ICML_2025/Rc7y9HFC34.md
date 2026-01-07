# Prior Work Analysis Report

## Target Paper
**Title:** Rc7y9HFC34
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ConceptAttention emerges at the intersection of three lines of work: conditioning in diffusion models, interpretability of transformer attention, and concept-based linear probing. Latent Diffusion Models established cross-attention as the mechanism binding text to spatial image synthesis, and follow-up editing methods like Prompt-to-Prompt validated that these cross-attention maps carry usable spatial signals—but also exposed their coarseness and instability as explanations. In parallel, Diffusion Transformers (DiT) re-architected diffusion to operate entirely with transformer attention layers, yielding rich, uniform attention blocks whose parameters and outputs can be systematically analyzed.
Work on transformer interpretability underscored that attention weights alone are incomplete as explanations. Chefer et al. introduced parameter-aware attribution, advocating that meaningful explanations should incorporate the model’s learned projections rather than visualizing raw weights. Complementarily, the ViT literature (e.g., DINO) showed that attention representations naturally encode object-level structure that can be converted into segmentation masks, suggesting that attention outputs may be a better substrate than cross-attention weights for localization. Finally, TCAV demonstrated that linear directions in deep representation spaces can correspond to human-understandable concepts.
Synthesizing these insights, ConceptAttention repurposes the learned projections within DiT attention layers and applies linear projections in the attention output space to form contextualized concept embeddings, yielding sharper, more faithful saliency maps than cross-attention maps. This design leverages DiT’s homogeneous attention blocks, TCAV’s linear concept directions, and established text–image alignment (CLIP) to achieve state-of-the-art zero-shot segmentation, with a formulation that also transfers to video diffusion transformers.

---
*Generated: 2026-01-07T00:21:32.365526*
