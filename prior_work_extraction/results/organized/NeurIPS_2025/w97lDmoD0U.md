# Prior Work Analysis Report

## Target Paper
**Title:** w97lDmoD0U
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s central claim—that the widely observed accuracy-on-the-line relation between ID and OOD accuracy can be an artifact of aggregating heterogeneous OOD data—builds directly on empirical evidence and benchmarks that popularized the aggregate perspective. Recht et al. (2019) showed that ImageNet classifiers preserve their rankings on ImageNetV2, and Hendrycks & Dietterich (2019) found clean accuracy to be strongly correlated with corruption robustness on ImageNet-C. Taori et al. (2020) extended this theme to multiple natural shifts, reinforcing the inference that better ID models are generally better OOD. In parallel, the group-robustness literature, especially Sagawa et al. (2020), demonstrated that aggregate metrics can conceal worst-group failures driven by spurious correlations, offering a conceptual lens for why aggregate OOD accuracy may be misleading. WILDS (Koh et al., 2021) consolidated real-world distribution-shift datasets with group structure, enabling rigorous subgroup analyses and serving as a primary testbed for this paper’s claims. To move from the observation of hidden failures to a practical discovery tool, the authors adopt a gradient-based selection strategy (OODSelect), conceptually grounded in influence-based ideas from Koh & Liang (2017) that use gradients to relate examples and model behavior. Together, these works provide the phenomenon to question (aggregate accuracy-on-the-line), the robustness framing (group/worst-case performance under spurious correlations), the benchmarks to evaluate on, and the methodological inspiration for gradient-based identification of semantically coherent OOD subsets where the correlation breaks down.

---
*Generated: 2026-01-07T00:21:32.318674*
