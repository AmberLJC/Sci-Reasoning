# Prior Work Analysis Report

## Target Paper
**Title:** gtU2eLSAmO
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Brain-JEPA’s core innovation marries the JEPA learning principle with neurobiologically grounded positional encoding and fMRI-specific masking. At the architectural level, LeCun’s JEPA concept and the concrete I-JEPA formulation supply the training objective and context–target predictor design that avoid reconstructing raw signals, enabling learning predictive embeddings directly from fMRI. The model’s spatiotemporal masking strategy is inspired by masked modeling advances: MAE established heavy random masking as a scalable self-supervised signal, while VideoMAE showed that temporally coherent (tube-like) masking can better exploit sequential structure. Brain-JEPA adapts these ideas to heterogeneous ROI time series, crafting a masking scheme aligned to fMRI’s spatial and temporal idiosyncrasies. The second pillar—Brain Gradient Positioning—derives from the macroscale functional gradient literature. Margulies et al. introduced principal gradients as a low-dimensional functional coordinate system of the cortex, and BrainSpace operationalized robust gradient computation and alignment across individuals. Brain-JEPA embeds ROIs within this gradient-based manifold to supply biologically meaningful positional encodings that surpass naive anatomical or index-based embeddings. Finally, widely adopted functional parcellations (Schaefer et al.) provide the ROI substrate that Brain-JEPA tokenizes and then enriches with gradient coordinates. Together, these lines of work directly shape Brain-JEPA’s key contribution: a JEPA-based foundation model for brain dynamics that couples functionally principled positional encoding with fMRI-tailored spatiotemporal masking to achieve strong generalization and transfer.

---
*Generated: 2026-01-06T23:33:35.566774*
