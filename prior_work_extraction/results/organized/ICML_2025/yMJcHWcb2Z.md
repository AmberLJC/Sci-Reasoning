# Prior Work Analysis Report

## Target Paper
**Title:** yMJcHWcb2Z
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Two-Stream Convolutional Networks for Action Recognition in Videos** (2014)
- *Authors:* Karen Simonyan and Andrew Zisserman
- *Connection:* The core idea that motion is a distinct signal from appearance directly motivates VideoJAM’s training objective to learn a single representation that must explain both pixels (appearance) and their motion (e.g., flow), generalizing two-stream principles to the generative setting.

**Classifier-Free Diffusion Guidance** (2022)
- *Authors:* Jonathan Ho and Tim Salimans
- *Connection:* VideoJAM’s Inner-Guidance extends the guidance paradigm by replacing external conditions with the model’s own evolving motion prediction as a dynamic guidance signal during sampling.

### 💡 Inspiration

**MoCoGAN: Decomposing Motion and Content for Video Generation** (2018)
- *Authors:* Sergey Tulyakov et al.
- *Connection:* MoCoGAN’s explicit separation of motion and content established that treating motion as a first-class factor improves video realism; VideoJAM adopts this insight but enforces a joint appearance–motion latent that simultaneously predicts pixels and motion, addressing diffusion-era models’ motion deficits.

### 🔍 Gap Identification

**Make-A-Video: Text-to-Video Generation without Text-Video Data** (2022)
- *Authors:* Uriel Singer et al.
- *Connection:* Make-A-Video leveraged strong image priors but exhibited typical shortcomings in temporal consistency and physics; VideoJAM is explicitly designed to remedy these gaps by injecting a motion prior via joint appearance–motion learning and motion-steered sampling.

### 📊 Baseline

**Video Diffusion Models** (2022)
- *Authors:* Jonathan Ho et al.
- *Connection:* VDM popularized diffusion for video with a pixel reconstruction objective; VideoJAM modifies this baseline by augmenting the loss with motion prediction and adding motion-based inner guidance at sampling to fix VDM’s motion-coherence weaknesses.

**Stable Video Diffusion: Scaling Latent Video Diffusion Models** (2023)
- *Authors:* Andreas Blattmann et al.
- *Connection:* As a strong latent video diffusion baseline trained with pixel-centric objectives, Stable Video Diffusion highlights the appearance-over-motion bias that VideoJAM counteracts via motion prediction during training and inner guidance at inference.

### 🔧 Extension

**RAFT: Recurrent All-Pairs Field Transforms for Optical Flow** (2020)
- *Authors:* Ethan Teed and Jia Deng
- *Connection:* VideoJAM supervises its motion head using dense optical flow; high-fidelity RAFT flow provides the concrete motion target that enables learning the joint appearance–motion representation.

---

## Synthesis

VideoJAM’s core innovation—learning a joint appearance–motion representation and using the model’s own motion prediction as dynamic guidance—emerges from two converging lineages. From video understanding, Two-Stream CNNs established motion as a distinct and essential signal, while MoCoGAN demonstrated in generative modeling that explicitly modeling motion markedly improves realism. VideoJAM synthesizes these insights but departs from explicit disentanglement: it trains a single latent to simultaneously predict pixels and their motion, compelling the representation to internalize dynamics rather than overfit to appearance.

From diffusion-based video generation, Video Diffusion Models and Stable Video Diffusion offered powerful baselines yet exposed a central limitation: pixel reconstruction objectives bias models toward appearance fidelity at the expense of temporal coherence and physical plausibility. VideoJAM directly addresses this by adding a motion prediction head and loss, using accurate optical flow (e.g., RAFT) as supervision to instill a motion prior. At inference, VideoJAM reframes guidance—traditionally external in Classifier-Free Guidance—into an internal mechanism: Inner-Guidance steers sampling using the model’s own evolving motion estimates, aligning denoising updates with coherent dynamics. Finally, Make-A-Video exemplified the appearance-driven bias inherited from image priors; VideoJAM targets precisely this gap, delivering a drop-in training and sampling strategy that transfers across video diffusion architectures to produce motion that is consistent, physically plausible, and temporally stable.

---
*Generated: 2026-01-06T23:07:19.634684*
