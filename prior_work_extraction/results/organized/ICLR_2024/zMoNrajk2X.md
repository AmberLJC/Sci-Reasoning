# Prior Work Analysis Report

## Target Paper

**Title:** CADS: Unleashing the Diversity of Diffusion Models through Condition-Annealed Sampling

**Conference:** ICLR 2024 (spotlight)

**Authors:** Seyedmorteza Sadat, Jakob Buhmann, Derek Bradley, Otmar Hilliges, Romann M. Weber

**Keywords:** diffusion models, diversity, generative models

**Abstract:** 
> While conditional diffusion models are known to have good coverage of the data distribution, they still face limitations in output diversity, particularly when sampled with a high classifier-free guidance scale for optimal image quality or when trained on small datasets. We attribute this problem to the role of the conditioning signal in inference and offer an improved sampling strategy for diffusion models that can increase generation diversity, especially at high guidance scales, with minimal ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Classifier-Free Diffusion Guidance** (2022)
- *Authors:* Jonathan Ho and Tim Salimans
- *Direct Connection:* CADS directly targets the diversity loss introduced by strong classifier-free guidance and is designed to be a drop-in modification that preserves CFG’s mechanism while mitigating its high-scale mode contraction by perturbing the conditioning vector.

**Diffusion Models Beat GANs on Image Synthesis** (2021)
- *Authors:* Prafulla Dhariwal and Alex Nichol
- *Direct Connection:* This work established guidance as a central lever in diffusion sampling and demonstrated the fidelity–diversity trade-off under strong guidance, the precise trade-off CADS resolves via condition-annealed sampling.

### 💡 Inspiration

**StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks** (2017)
- *Authors:* Han Zhang et al.
- *Direct Connection:* StackGAN’s conditioning augmentation (adding Gaussian noise to text embeddings to encourage diversity) directly inspires CADS’s key idea of injecting Gaussian noise into the conditioning vector—now performed at inference with an annealed schedule in diffusion models.

### 🔍 Gap Identification

**GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models** (2022)
- *Authors:* Alex Nichol et al.
- *Direct Connection:* GLIDE popularized text-conditioned diffusion with classifier-free guidance and documented that increasing guidance improves quality but reduces diversity, a limitation CADS explicitly addresses by injecting scheduled noise into the text condition.

**Imagen: Photorealistic Text-to-Image Diffusion Models** (2022)
- *Authors:* Chitwan Saharia et al.
- *Direct Connection:* Imagen relies heavily on strong classifier-free guidance to maximize fidelity, highlighting the diversity collapse at high scales that CADS remedies without retraining by annealing noise on the conditioning embedding.

### 🔗 Related Problem

**SDEdit: Image Synthesis and Editing with Stochastic Differential Equations** (2021)
- *Authors:* Chenlin Meng et al.
- *Direct Connection:* SDEdit shows that controlled noise schedules during diffusion can balance adherence and diversity, a principle CADS adapts by scheduling noise on the conditioning channel rather than the data trajectory.

---

## Synthesis: How Prior Work Led to This Paper

Classifier-free guidance formalized a powerful way to steer diffusion models by interpolating between conditional and unconditional predictions, but it also tightly linked higher guidance scales to reduced sample diversity. Guided Diffusion cemented guidance as the central tool for quality control and empirically highlighted the fidelity–diversity trade-off under strong guidance. GLIDE scaled text conditioning in diffusion and documented that pushing guidance improves sharpness and alignment at the cost of variety, while Imagen crystallized this practice at larger scales, depending on strong guidance to reach top image quality and thereby exacerbating diversity collapse. From the GAN literature, StackGAN introduced conditioning augmentation—adding Gaussian noise to the text embedding—to improve robustness and diversity of conditional generation, demonstrating that perturbing the condition can beneficially widen support. SDEdit showed that injecting and annealing noise within the diffusion process can trade off adherence and realism through a schedule, underscoring the utility of time-varying noise control.
Bringing these threads together, CADS recognizes that the core source of diversity loss is the untempered dominance of the conditioning signal under strong classifier-free guidance and leverages the StackGAN insight to perturb the condition itself, but does so within diffusion by annealing Gaussian noise over timesteps. This condition-annealed schedule, inspired by SDEdit’s noise scheduling principle yet applied to the conditioning channel, preserves alignment while restoring coverage, giving a training-free, sampler-agnostic remedy to the fidelity–diversity tension established by Guided Diffusion, GLIDE, and Imagen.

---

*Analysis generated on: 2026-01-06T17:39:01.636257*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
