# Prior Work Analysis Report

## Target Paper
**Title:** kEQFjKqiqM
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DRAGON’s core contribution—learning a probability distribution over fractional derivative orders to govern continuous-time graph propagation—sits at the intersection of continuous-depth neural modeling, graph diffusion, and fractional kinetics. Neural ODEs established how to parameterize and train continuous-time dynamics end-to-end, which DRAGON adopts on graphs. On the graph side, spectral filtering and diffusion-based propagation (via ChebNet and spectral wavelets) showed that mixing powers of the Laplacian effectively blends multi-hop information, while APPNP made this idea explicit by weighting a distribution over walk lengths to improve long-range propagation. Fractional dynamics supply the missing physical lens: classic results by Metzler and Klafter link fractional derivatives to non-Markovian dynamics and anomalous diffusion with power-law memory kernels, providing the theoretical mechanism DRAGON exploits to encode history dependence in feature updates. Crucially, distributed-order fractional calculus (Chechkin–Gorenflo–Sokolov) generalizes single fractional orders to mixtures over orders, capturing heterogeneous, multi-scale diffusion—precisely the flexibility DRAGON renders learnable. Finally, anomalous diffusion on networks and Lévy-style random walks (Riascos–Mateos) connect fractional kinetics to graph domains, grounding DRAGON’s interpretation as a non-Markovian random walk-driven update process. Together, these strands motivate and enable DRAGON’s learnable distributed-order operator, which unifies and extends diffusion-based GNNs and continuous-time models to capture richer, multi-scale, memoryful dynamics on graphs.

---
*Generated: 2026-01-06T23:33:35.542074*
