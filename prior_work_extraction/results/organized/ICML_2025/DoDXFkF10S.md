# Prior Work Analysis Report

## Target Paper
**Title:** DoDXFkF10S
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

FlatVI targets a long-standing mismatch between how single-cell VAEs are used and the geometry those models actually induce. scVI established the practical and statistical foundation for VAEs with discrete likelihoods tailored to scRNA-seq count data, providing the core framework FlatVI operates within. Building on that, applications like scGen popularized linear latent arithmetic and straight-line interpolations to model cellular state shifts, implicitly assuming Euclidean geometry in the latent space. However, theoretical work by Arvanitidis, Hansen, and Hauberg demonstrated that decoders endow latent spaces with a non-Euclidean pullback Riemannian metric; straight lines in latent coordinates rarely trace geodesics on the decoded data manifold. Their subsequent contributions on computing geodesic paths in deep generative models defined the geometric target for faithful interpolation but at a substantial computational cost.

FlatVI’s key contribution is to reconcile practice and geometry by regularizing the VAE so that straight lines in latent space approximate manifold geodesics for single-cell count likelihoods. Two strands of prior methodology inform how to achieve this: contractive autoencoders introduced derivative-based penalties to sculpt local manifold geometry, and StyleGAN2’s path length regularization showed that controlling the generator’s Jacobian can yield isotropic, Euclidean-like latent behavior. FlatVI integrates these insights into a variational framework with discrete likelihoods, explicitly steering the decoder’s pullback metric toward identity. The result is a latent space whose linear paths better correspond to geodesic interpolations on the single-cell manifold, increasing the validity and utility of downstream methods that assume Euclidean latent geometry.

---
*Generated: 2026-01-07T00:04:09.140975*
