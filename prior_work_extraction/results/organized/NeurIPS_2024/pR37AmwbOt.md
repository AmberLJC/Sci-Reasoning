# Prior Work Analysis Report

## Target Paper
**Title:** pR37AmwbOt
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core idea—leveraging catastrophic forgetting as a protective asset—sits at the intersection of safety for diffusion models, fine-tuning dynamics, and contrastive representation learning. Early safety efforts in diffusion centered on external guidance or filters, as exemplified by Guided Diffusion and Safe Latent Diffusion. These methods steer sampling using classifiers and safety heads but leave the base model parameters largely unchanged, rendering them susceptible to circumvention via subsequent adaptation. Parallel work on unlearning, notably Erasing Concepts from Diffusion Models, directly edits diffusion parameters to remove unsafe concepts but has been shown to be fragile: later fine-tuning can reintroduce or route around erased content.

The rise of practical fine-tuning tools—DreamBooth for personalization and LoRA for parameter-efficient adaptation—exposed a concrete adversarial vector. These methods can induce distributional shifts and catastrophic forgetting of safety-relevant distinctions, undoing both external filters and naive unlearning. Drawing on foundational insights from catastrophic forgetting (EWC), the present work flips the narrative: rather than merely preventing forgetting, it engineers the representation so that harmful concepts occupy a distinct, isolated region in latent space. Supervised contrastive learning provides the mechanism, explicitly maximizing separation between clean and harmful distributions. As a result, when attackers apply small fine-tuning steps (e.g., LoRA/DreamBooth), the model preferentially “forgets” or fails to acquire harmful generations, preserving safety. Together, these prior works shape a defense that internalizes safety, is resilient to malicious fine-tuning, and uses forgetting as a feature rather than a liability.

---
*Generated: 2026-01-06T23:33:35.541170*
