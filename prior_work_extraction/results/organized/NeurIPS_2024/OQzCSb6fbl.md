# Prior Work Analysis Report

## Target Paper
**Title:** OQzCSb6fbl
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Parallel Backpropagation for Shared-Feature Visualization marries two strands of work: (1) modeling biological neurons with deep network latents and (2) top-down visualization via backpropagation. The encoding-model foundation—pioneered by Yamins et al.—justifies predicting neural responses from DNN features, while Representational Similarity Analysis (Kriegeskorte et al.) motivates choosing a preferred-category reference image that matches an out-of-category stimulus in latent space. Once a pair is established, the method adapts the backpropagation-to-input paradigm of Zeiler & Fergus and Simonyan et al., ensuring that latent activations are rendered into pixel-space evidence.
Crucially, the approach does not merely backpropagate each image separately; inspired by rule-based and attention-like top-down propagation (LRP; Excitation Backprop), it emphasizes the feature dimensions shared between the two activation patterns and suppresses idiosyncratic, non-shared components. This selective redistribution creates a joint relevance signal that visualizes the common visual features responsible for the neuron’s strong response across category boundaries. Mahendran & Vedaldi’s principled inversion of intermediate representations informs the choice of layers and the stability of reconstructions during propagation.
Together, these prior works directly underpin the paper’s core innovation: a paired, parallel backpropagation scheme that uses representational matching to localize shared, neuron-driving features in pixels, thereby clarifying why out-of-category images can robustly activate category-selective brain regions.

---
*Generated: 2026-01-06T23:33:35.552894*
