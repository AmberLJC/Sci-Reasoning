# Prior Work Analysis Report

## Target Paper

**Title:** Likelihood Training of Cascaded Diffusion Models via Hierarchical Volume-preserving Maps

**Conference:** ICLR 2024 (spotlight)

**Authors:** Henry Li, Ronen Basri, Yuval Kluger

**Keywords:** likelihood-based modeling, diffusion modeling, density estimation

**Abstract:** 
> Cascaded models are multi-scale generative models with a marked capacity for producing perceptually impressive samples at high resolutions. In this work, we show that they can also be excellent likelihood models, so long as we overcome a fundamental difficulty with probabilistic multi-scale models: the intractability of the likelihood function. Chiefly, in cascaded models each intermediary scale introduces extraneous variables that cannot be tractably marginalized out for likelihood evaluation. ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**The Laplacian Pyramid as a Compact Image Code** (1983)
- *Authors:* Peter J. Burt et al.
- *Direct Connection:* This classic paper introduced the Laplacian pyramid transform that the present work adopts as a concrete hierarchical volume-preserving map to decompose images into multi-scale bands without local distortion.

### 💡 Inspiration

**Deep Generative Image Models using a Laplacian Pyramid of Adversarial Networks** (2015)
- *Authors:* Emily Denton et al.
- *Direct Connection:* By showing that Laplacian pyramid decompositions enable effective multi-scale generative cascades, this work directly inspired using the Laplacian pyramid as a hierarchical volume-preserving map for tractable likelihood in cascaded diffusion.

**NICE: Non-linear Independent Components Estimation** (2014)
- *Authors:* Laurent Dinh et al.
- *Direct Connection:* NICE introduced the key idea of volume-preserving invertible transformations yielding zero log-determinant in change-of-variables, which this paper extends to hierarchical, spatially-structured maps across scales.

### 🔍 Gap Identification

**High-Resolution Image Synthesis with Latent Diffusion Models** (2022)
- *Authors:* Robin Rombach et al.
- *Direct Connection:* Latent diffusion relies on autoencoder latents that are not volume-preserving (and thus not directly likelihood-traceable), motivating the present work’s replacement with hierarchical volume-preserving maps to obtain exact likelihood in multi-scale settings.

### 📊 Baseline

**Cascaded Diffusion Models for High Fidelity Image Generation** (2021)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* This work established the cascaded multi-scale diffusion pipeline whose intermediate variables make likelihood intractable, and the present paper directly resolves this by reparameterizing each scale with hierarchical volume-preserving maps to enable exact likelihood.

### 🔧 Extension

**Integer Discrete Flows and Lossless Compression** (2019)
- *Authors:* Emiel Hoogeboom et al.
- *Direct Connection:* This work demonstrated using invertible wavelet/Haar transforms as volume-preserving steps in likelihood-based models, and the present paper leverages the same class of wavelet transforms as hierarchical volume-preserving maps for diffusion cascades.

### 🔗 Related Problem

**Image Super-Resolution via Iterative Refinement** (2021)
- *Authors:* Chitwan Saharia et al.
- *Direct Connection:* SR3 formalized diffusion-based super-resolution modules used as stages in cascades, and the current paper makes these super-resolution stages likelihood-trainable by operating in a volume-preserving hierarchical latent space.

---

## Synthesis: How Prior Work Led to This Paper

Cascaded Diffusion Models showed that chaining diffusion models across resolutions yields high-fidelity images, but their construction introduces intermediate variables that make marginal likelihood of the final image intractable. SR3 clarified the mechanics of diffusion-based super-resolution modules used within such cascades, cementing the conditional multi-scale formulation but leaving likelihood evaluation unaddressed. Earlier, Laplacian Pyramid GANs demonstrated that decomposing images into multi-scale residual bands via a Laplacian pyramid yields effective generative cascades, pointing to pyramid decompositions as a powerful scaffold for hierarchical generation. The Laplacian pyramid itself, originating from Burt and Adelson, provides an invertible multi-scale transform that cleanly separates frequency bands without local distortions—precisely the structure needed to decouple scales. In parallel, NICE introduced volume-preserving invertible transformations whose unit Jacobian simplifies change-of-variables, highlighting that volume preservation can make likelihood computations especially tractable. Integer Discrete Flows operationalized this idea with Haar/wavelet transforms, showing that orthonormal, invertible filter banks can serve as volume-preserving steps within exact-likelihood models. Conversely, Latent Diffusion Models achieved efficiency by learning compressive autoencoder latents that are not volume-preserving, thereby sacrificing direct likelihood access. Together, these works suggest a natural path: keep the multi-scale generative benefits of cascades and pyramids, but choose hierarchical transforms that are invertible and volume-preserving so that diffusion can be performed in a latent space where the likelihood is directly computable. The present paper synthesizes these insights by training cascaded diffusion models on hierarchical volume-preserving maps (e.g., Laplacian pyramids and wavelets), removing extraneous variables and enabling exact likelihood while retaining multi-scale generative advantages.

---

*Analysis generated on: 2026-01-06T07:29:40.836201*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
