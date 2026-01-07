# Prior Work Analysis Report

## Target Paper

**Title:** Gradual Domain Adaptation via Gradient Flow

**Conference:** ICLR 2024 (spotlight)

**Authors:** Zhan Zhuang, Yu Zhang, Ying Wei

**Keywords:** Domain adaptation, gradual domain adaptation, gradient flow

**Abstract:** 
> Domain shift degrades classification models on new data distributions. Conventional unsupervised domain adaptation (UDA) aims to learn features that bridge labeled source and unlabeled target domains. In contrast to feature learning, gradual domain adaptation (GDA) leverages extra continuous intermediate domains with pseudo-labels to boost the source classifier. However, real intermediate domains are sometimes unavailable or ineffective. In this paper, we propose $\textbf{G}$radual Domain Adapta...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Variational Formulation of the Fokker–Planck Equation** (1998)
- *Authors:* Richard Jordan et al.
- *Direct Connection:* Established that KL divergence admits a Wasserstein gradient-flow dynamics (JKO scheme), which GGF uses to formally define the continuous transport from source to target distributions that yields intermediate domains.

**Class-Balanced Self-Training for Unsupervised Domain Adaptation** (2018)
- *Authors:* Yang Zou et al.
- *Direct Connection:* Pioneered pseudo-label based progressive fine-tuning in UDA, which GGF adopts as the training mechanism on its generated intermediate domains.

### 💡 Inspiration

**JDOT: Joint Distribution Optimal Transport for Domain Adaptation** (2017)
- *Authors:* Nicolas Courty et al.
- *Direct Connection:* Showed that transport should be label-aware by coupling features and labels in the cost, a principle GGF embeds as potentials to preserve labels along its gradient-flow path.

**Geodesic Flow Kernel for Unsupervised Domain Adaptation** (2012)
- *Authors:* Boqing Gong et al.
- *Direct Connection:* Demonstrated bridging domains along a continuous path via geodesic flow, which GGF generalizes from feature subspaces to data distributions using Wasserstein gradient flow to generate intermediate domains.

### 🔍 Gap Identification

**DLOW: Domain Flow for Adaptation and Generalization** (2019)
- *Authors:* Rui Gong et al.
- *Direct Connection:* Introduced continuous intermediate domains (domain flow) to ease adaptation but relied on image translation/stylization, motivating GGF to synthesize intermediate domains directly by gradient flow when real intermediates are unavailable.

### 🔧 Extension

**Diffusion Models Beat GANs on Image Synthesis** (2021)
- *Authors:* Prafulla Dhariwal et al.
- *Direct Connection:* Its classifier-guidance mechanism for diffusion provides the template for GGF’s classifier-based potential that steers Langevin dynamics to remain label-consistent during domain transport.

---

## Synthesis: How Prior Work Led to This Paper

Jordan, Kinderlehrer, and Otto established that the Kullback–Leibler divergence induces a gradient flow in the Wasserstein metric, giving a variational characterization of Fokker–Planck dynamics and a principled way to evolve one distribution toward another. Dhariwal and Nichol later showed that diffusion processes can be steered to desired classes by adding classifier gradients, illustrating how to inject label information into noisy dynamics. Courty and colleagues argued in domain adaptation that transport must be label-aware by coupling features and labels in the optimal transport objective, highlighting the risk of class-mismatched mappings. Gong and collaborators earlier proposed the Geodesic Flow Kernel, integrating features along a continuous path on the Grassmann manifold to bridge domain shift through intermediate representations. DLOW operationalized the idea of a continuous “domain flow,” generating intermediate domains via image translation controlled by a domainness variable, but depended on stylization machinery and access to suitable intermediate styles. Zou and coauthors demonstrated that pseudo-label driven, progressive self-training can effectively adapt models without target labels.
Together, these works suggested a natural opportunity: use a principled continuous transport to synthesize intermediate domains, but make the dynamics explicitly label-aware and compatible with pseudo-label fine-tuning. GGF does exactly this by instantiating the KL Wasserstein gradient flow and simulating it with Langevin dynamics, then injecting classifier-based and sample-based potentials—akin to classifier guidance and label-aware transport—to preserve labels and suppress diffusion noise, yielding reliable intermediate domains for gradual, pseudo-label fine-tuning.

---

*Analysis generated on: 2026-01-06T11:38:23.784179*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
