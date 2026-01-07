# Prior Work Analysis Report

## Target Paper
**Title:** 4yHWV3B6g4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Raptor’s core contribution—train-free, semantically rich embeddings for 3D medical volumes built from frozen 2D foundation models and random spatial compression—emerges from two converging lines of work. First, MVCNN and 2.5D/orthogonal-view medical approaches (e.g., Setio et al.) established that 3D objects or volumes can be effectively represented by aggregating multiple 2D projections or slices. Raptor adopts this view-centric decomposition but scales it by sampling random planes across the volume rather than relying on fixed orthogonal views or learned renderings.
Second, advances in large-scale 2D representation learning (BiT; DINO) showed that pretrained natural-image encoders produce highly transferable, token-level semantic features. Raptor capitalizes on this by extracting robust patch tokens from each slice using a frozen 2D ViT/CNN, eliminating the need for expensive 3D pretraining on medical volumes.
To make the aggregated representation computationally tractable, Raptor draws on randomized linear algebra: JL-style random projections (Achlioptas) and sketching methods (Pham & Pagh) provide the theoretical and algorithmic underpinning for compressing high-dimensional token grids while approximately preserving pairwise structure. The train-free, similarity-preserving spirit of Random Features (Rahimi & Recht) further supports using fixed random mappings instead of learned bottlenecks. Together, these works directly motivate Raptor’s design: represent a 3D volume as a set of 2D tokens from a powerful frozen encoder, then apply random planar tensor reduction to compress and aggregate them into compact, semantically faithful embeddings that transfer across diverse medical tasks without training.

---
*Generated: 2026-01-07T00:21:32.364328*
