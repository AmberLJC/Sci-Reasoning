# Prior Work Analysis Report

## Target Paper
**Title:** Ms6IXbfzzX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

ZeroS emerges from the kernel-based linear attention lineage while tackling two structural limitations that prior efficient Transformers implicitly inherit. Katharopoulos et al. (Linear Transformers) and Choromanski et al. (Performer) showed how softmax attention can be linearized via kernel features or random features to achieve O(N) complexity, but their constructions enforce nonnegative, probability-like weights—i.e., convex combinations—through a global normalization that accumulates a uniform component over time. Schlag et al. analyzed such models as fast-weight memories, diagnosing denominator-induced diffusion and interference that worsen with longer contexts. Concurrently, low-rank and Nyström approximations (Linformer, Nyströmformer) demonstrated scalable attention yet still preserved softmax’s nonnegative weighting and its attendant dilution on long sequences. ZeroS reframes the kernel view using insights from random-feature linearizations: decompose the softmax kernel into a zero-order uniform term plus zero-sum residuals, then remove the uniform baseline and reweight the residuals. This yields mathematically stable signed weights computable with associative scans, enabling contrastive operations in a single layer while retaining O(N) cost. By breaking the convex-combination restriction and eliminating the uniform accumulator, ZeroS expands the function class representable by linear attention and directly addresses the long-context bias identified in earlier analyses, closing the performance gap to standard softmax attention without sacrificing efficiency.

---
*Generated: 2026-01-06T23:42:48.119813*
