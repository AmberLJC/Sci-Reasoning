# Prior Work Analysis Report

## Target Paper
**Title:** P37GIj4wB7
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—JNE, a Jacobian-based metric that quantifies nonlinearity in neural encoding models by measuring dispersion of local linear mappings—emerges at the intersection of fMRI encoding traditions and Jacobian-centric views of neural networks. Foundational voxel-wise encoding work (Kay et al., 2008) and the broader framework for encoding/decoding (Naselaris et al., 2011) established linear readouts from feature spaces to BOLD as the default, setting the baseline that JNE evaluates and generalizes beyond. As deep neural network features became standard for modeling brain responses (Güçlü & van Gerven, 2015), linear readouts remained prevalent, leaving the extent and locus of nonlinearity between ANN representations and BOLD under-characterized. Interpretable but largely linear architectures like fwRF (St-Yves & Naselaris, 2018) reinforced the need to know when nonlinear heads are justified.
On the methodological side, gradient-based interpretability (Simonyan et al., 2013) framed Jacobians as local linear explanations, while the neural tangent kernel (Jacot et al., 2018) formalized network behavior as a collection of local linearizations governed by Jacobians. Nonlinear deep encoding/decoding for naturalistic stimuli (Wen et al., 2018) further underscored the practical need to measure nonlinearity in end-to-end models. JNE synthesizes these strands: it adopts the Jacobian-as-local-linear-map perspective to the representation-to-BOLD function and operationalizes nonlinearity as the statistical dispersion of these Jacobians across stimuli, providing a principled, model-agnostic metric that complements accuracy and interpretability analyses in modern fMRI encoding.

---
*Generated: 2026-01-07T00:29:42.070587*
