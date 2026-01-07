# Prior Work Analysis Report

## Target Paper
**Title:** blm1pqiOXe
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Paxion’s core contribution—patching explicit action knowledge into frozen video-language models with a discriminative dynamics objective—sits at the intersection of three lines of work. First, vision-language pretraining established by CLIP and extended to video in Frozen-in-Time provides the frozen backbones and contrastive alignment paradigm that Paxion augments. These VidLMs excel at object-centric cues but underperform on temporal action understanding, motivating the need for targeted intervention. Second, parameter-efficient model augmentation via Adapters and their non-destructive composition in AdapterFusion directly inspire Paxion’s two-component architecture: a Knowledge Patcher (an adapter-like module specialized for action dynamics) and a Knowledge Fuser that integrates this patch without eroding existing capabilities. This design explicitly operationalizes non-destructive knowledge injection for multimodal, temporal skills.
Third, classic self-supervised video representation learning from temporal discrimination—Shuffle and Learn and OPN—demonstrates that predicting order and reversals is a powerful supervisory signal for motion and temporal direction. Paxion’s Discriminative Video Dynamics Modeling (DVDM) inherits this insight, but couples it with video–text alignment to encode action semantics, not just motion patterns. Complementing this, the Something-Something dataset’s antonymic, fine-grained actions motivate ActionBench’s Action Antonym and Video Reversal probes, which diagnose object-shortcut reliance. Together, these prior works directly scaffold Paxion’s diagnostic benchmark, its adapter-style patch-and-fuse mechanism, and its dynamics-aware objective to endow VidLMs with robust action knowledge.

---
*Generated: 2026-01-06T23:42:49.071957*
