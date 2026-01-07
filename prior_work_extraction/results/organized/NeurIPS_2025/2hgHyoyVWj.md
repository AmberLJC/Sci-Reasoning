# Prior Work Analysis Report

## Target Paper
**Title:** 2hgHyoyVWj
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

AuroRA’s core idea—placing an adaptive nonlinear layer between two low-rank projections to form an MLP-like block—emerges at the intersection of LoRA’s linear parameterization and adapter-style nonlinear bottlenecks. LoRA (Hu et al., 2022) established the dominant PEFT paradigm via linear low-rank deltas, but its performance often scales only by raising rank, increasing parameters. Classical adapter work (Houlsby et al., 2019) demonstrated that a down–activation–up bottleneck can be highly expressive with few parameters, a theme reinforced by Compacter (Karimi Mahabadi et al., 2021), which further improved adapter efficiency while retaining nonlinearity. These insights suggested that the path to breaking LoRA’s bottleneck is not more linear maps but a strategically placed nonlinearity.
At the same time, theory on intrinsic dimensionality (Aghajanyan et al., 2021) explained why small subspaces can suffice, but also hinted at limits when the target function deviates from what a fixed linear low-rank map can capture. The Eckart–Young theorem formalizes those limits for linear low-rank approximation, motivating a nonlinear augmentation that can reduce approximation error without inflating linear rank. Recent LoRA variants such as AdaLoRA (adaptive rank) and DoRA (weight reparameterization) sought to mitigate the bottleneck while staying linear, underscoring the need for a fundamentally different approach. Integrating these lines, AuroRA introduces an adaptive nonlinear layer—mixing fixed and learnable nonlinearities—between low-rank projectors, achieving higher expressivity under tight parameter budgets and theoretically lowering approximation error compared with purely linear low-rank updates.

---
*Generated: 2026-01-07T00:21:32.350016*
