# Prior Work Analysis Report

## Target Paper
**Title:** cjjPn1EIwq
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ESCA’s core idea is to strengthen embodied agents’ grounding by generating spatio-temporal scene graphs with an open-domain, promptable foundation model (SGCLIP) trained without human annotations. This builds directly on CLIP’s text–image alignment and promptability, which provide the open-vocabulary scaffold SGCLIP needs to name objects, attributes, and relations from free-form prompts. The scene-graph formulation itself follows the classic SGG paradigm introduced by Iterative Message Passing and later refined by Neural Motifs, but ESCA departs from closed-set, frequency-driven relation prediction by leveraging CLIP’s semantic space and prompt conditioning for robust open-domain relations. The representational schema and evaluation tradition trace to Visual Genome, whose objects–attributes–relations ontology ESCA generalizes from static images to videos and embodied settings. Critically, ESCA’s label-free, neurosymbolic training pipeline aligns automatically generated captions with the model’s own scene graphs—a direct conceptual echo of NS-CL, which married neural perception with symbolic structure through language. High-quality captions from modern captioners such as BLIP-2 enable rich, open-domain textual supervision that describes entities and interactions in diverse videos. Finally, the self-training dynamic—using the model’s predictions as supervisory signals—draws on Noisy Student’s pseudo-labeling recipe to scale learning without manual annotations. Together, these lines of work converge in ESCA: a promptable, CLIP-based scene-graph generator trained via neurosymbolic alignment to captions, delivering stronger grounding for embodied agents and state-of-the-art performance in scene-graph generation and action localization.

---
*Generated: 2026-01-07T00:21:32.267638*
