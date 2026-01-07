# Prior Work Analysis Report

## Target Paper
**Title:** 9VqMaSjf7U
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

BrainDiVE’s core innovation—using brain-guided diffusion to synthesize images predicted to activate specific cortical regions—emerges at the intersection of three lines of work. First, deep generative priors for fMRI, inaugurated by Shen et al., showed that brain activity can steer image generators to reconstruct percepts. Takagi and Nishimoto advanced this with latent diffusion models (LDMs), proving that modern diffusion backbones and latent conditioning are effective for high-fidelity, brain-conditioned synthesis. Second, activation-maximization with generators (Nguyen et al.) and closed-loop brain-guided stimulus optimization for neuronal populations (Bashivan et al.) established the methodological blueprint for optimizing images to maximize neural responses, which BrainDiVE extends from single-unit electrophysiology and GANs to population-level human fMRI and diffusion models. Third, LDMs (Rombach et al.) and guidance strategies for diffusion sampling (Ho & Salimans) provide the scalable, controllable generative substrate; BrainDiVE replaces standard text/classifier signals with a differentiable brain-encoding objective, effectively turning ROI activation predictions into a guidance signal during sampling. Crucially, the Natural Scenes Dataset (Allen et al.) supplies the large, naturalistic paired image–fMRI data needed to train strong encoding models whose gradients are reliable enough to direct diffusion. Together, these works directly inform BrainDiVE’s design: an encoding model trained on NSD predicts ROI responses; its gradients guide an LDM via classifier-free-like guidance to synthesize images that explore and reveal fine-grained functional organization without hand-curated categorical stimuli.

---
*Generated: 2026-01-06T23:42:49.072869*
