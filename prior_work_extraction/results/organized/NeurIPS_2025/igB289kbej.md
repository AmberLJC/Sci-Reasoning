# Prior Work Analysis Report

## Target Paper
**Title:** igB289kbej
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EraseFlow’s core insight—casting concept erasure as exploration over denoising trajectories and optimizing the process with GFlowNets—stands on two pillars: the trajectory-centric view of diffusion sampling and the trajectory-sampling capabilities of GFlowNets. The diffusion backbone from DDPM formalized the generative process as sequential denoising, while classifier-free guidance demonstrated how policies applied along this path can steer outputs without corrupting the model prior. Prompt-to-Prompt further revealed that interventions across denoising steps, not just final images, crucially determine semantic content, underscoring the value of trajectory-level control.
On the safety side, ESD established a concrete paradigm for erasing concepts via adversarial fine-tuning, but also exposed quality degradation and brittleness. In parallel, ImageReward exemplified alignment via learned reward models, highlighting the susceptibility of such rewards to hacking and limited generalization. EraseFlow directly responds to these limitations by replacing handcrafted or adversarial objectives with a learned stochastic policy over trajectories.
Methodologically, Generative Flow Networks provide the mechanism to sample diverse, high-reward objects by learning flow-consistent policies; Trajectory Balance supplies a stable, end-to-end training objective with good credit assignment across paths. By mapping denoising sequences to GFlowNet trajectories and optimizing with trajectory balance, EraseFlow learns to divert sampling away from unwanted concepts while preserving the prior, achieving robust, generalizable erasure without retraining cycles or fragile reward models.

---
*Generated: 2026-01-07T00:21:32.286274*
