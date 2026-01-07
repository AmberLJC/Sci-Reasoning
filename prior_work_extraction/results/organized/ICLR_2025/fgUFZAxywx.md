# Prior Work Analysis Report

## Target Paper
**Title:** fgUFZAxywx
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Linear Spherical Sliced Optimal Transport (LSSOT) fuses two lines of work: (i) slicing-based reductions of optimal transport and (ii) linear optimal transport embeddings. The sliced OT paradigm, crystallized by Bonneel et al., showed that projecting high-dimensional measures onto 1D lines makes OT computations fast and scalable; Kolouri et al. further demonstrated that aggregating these projections can yield efficient, kernelizable similarities. In parallel, the cumulative distribution transform (CDT/LOT) established that 1D probability measures admit an exact L2 embedding whose Euclidean distance equals the 2-Wasserstein distance, and Radon-CDT extended this idea by aggregating 1D LOT embeddings across directions for higher-dimensional data.
Recent advances adapted slicing to spherical domains: spherical sliced Wasserstein defined geometry-respecting spherical slices, and stereographic spherical sliced Wasserstein leveraged stereographic projection to enable practical computations while approximating spherical geometry. These works, together with manifold OT theory (e.g., Kim–McCann) grounding geodesic costs on spheres, set the stage for LSSOT.
LSSOT’s key contribution is to marry spherical slicing with the LOT embedding: it computes slice-wise linear OT embeddings of spherical distributions and aggregates them into an L2 representation that preserves intrinsic spherical geometry and yields a bona fide metric. This delivers a fast, scalable distance for spherical probability measures with theoretical metricity, paralleling Radon-CDT’s linearization but tailored to the sphere and informed by spherical/sereographic slicing schemes.

---
*Generated: 2026-01-07T00:02:04.907816*
