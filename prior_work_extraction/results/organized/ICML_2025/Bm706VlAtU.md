# Prior Work Analysis Report

## Target Paper
**Title:** Bm706VlAtU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Denoising Diffusion Probabilistic Models** (2020)
- *Authors:* Ho et al.
- *Connection:* Provides the core forward (isotropic Gaussian) and reverse denoising framework whose isotropic corruption we reinterpret in the Fourier domain, motivating our modification to avoid uniform damage across frequencies.

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Song et al.
- *Connection:* Supplies the reverse-time score-based denoising machinery that our purification pipeline leverages; we adapt this framework to operate in a frequency-selective manner.

**A Fourier Perspective on Model Robustness in Computer Vision** (2019)
- *Authors:* Yin et al.
- *Connection:* Establishes that robustness is strongly tied to frequency, motivating our frequency-domain analysis and the key finding that adversarial damage increases monotonically with frequency.

**The Importance of Phase in Signals** (1981)
- *Authors:* Oppenheim and Lim
- *Connection:* Provides the classic result that phase encodes structural information, grounding our design that exploits low-frequency phase (and amplitude) components to retain image structure during purification.

### 💡 Inspiration

**SDEdit: Guided Image Synthesis for Stochastic Image Editing with Score-Based Models** (2022)
- *Authors:* Meng et al.
- *Connection:* Inspires the ‘add noise then denoise’ view as an editing/purification operation preserving structure; we extend this idea by preserving content/structure via selectively using less-damaged frequency bands.

### 📊 Baseline

**DiffPure: Purifying Adversarial Perturbations with Diffusion Models** (2023)
- *Authors:* Nie et al.
- *Connection:* Serves as the primary diffusion-based purification baseline that adds isotropic noise in pixel space and denoises; our method directly addresses its limitation of indiscriminately damaging all frequency components by designing frequency-aware purification.

### 🔗 Related Problem

**FDA: Fourier Domain Adaptation for Semantic Segmentation** (2020)
- *Authors:* Yang and Soatto
- *Connection:* Demonstrates amplitude–phase decomposition and that low-frequency amplitude manipulations preserve structure, informing our use of amplitude/phase to recover clean content from less-damaged frequencies.

---

## Synthesis

This paper’s core innovation—frequency-aware diffusion-based adversarial purification—emerges from two converging threads: diffusion purification and frequency-domain understanding of images and robustness. On the generative side, DDPM establishes a forward isotropic Gaussian noising and reverse denoising framework, while score-based SDEs generalize the reverse-time denoising machinery used in practice. SDEdit reframes noising–denoising as structure-preserving editing, a perspective later adopted by diffusion-based defenses such as DiffPure, which “drown” adversarial perturbations in noise and then denoise. However, DiffPure (and the DDPM forward process it inherits) treats all pixels—and thus all frequencies—equally, often eroding semantic content. On the frequency side, Yin et al. show that robustness is frequency dependent, motivating a defense that reasons explicitly in the Fourier domain. Classical signal processing (Oppenheim & Lim) and modern computer vision (FDA by Yang & Soatto) further decompose images into amplitude and phase, with phase carrying structure and low-frequency amplitude controlling global content/style. Building on these insights, the present work analyzes diffusion purification through the Fourier lens, finding adversarial damage rises monotonically with frequency for both amplitude and phase. It then redesigns purification to preferentially preserve low-damage frequency components, extracting content and structure while removing high-frequency adversarial artifacts—directly remedying the indiscriminate damage inherent to prior diffusion-based purification.

---
*Generated: 2026-01-06T23:07:19.631495*
