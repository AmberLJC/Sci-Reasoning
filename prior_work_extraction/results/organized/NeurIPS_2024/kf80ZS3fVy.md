# Prior Work Analysis Report

## Target Paper
**Title:** kf80ZS3fVy
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

UniKE’s core contribution is to unify intrinsic knowledge editing and external knowledge resorting for multimodal LLMs by casting both as operations over vectorized key–value memories, and by disentangling semantic carriers from truthfulness signals to promote collaborative knowledge use. This perspective is grounded in Geva et al., who showed that transformer feed-forward layers function as key–value memories—an insight that lets UniKE model in-weight facts as structured memories. Building on this, ROME operationalizes precise intrinsic edits by manipulating subject–relation associations at targeted MLP sites, providing a template for UniKE’s intrinsic pathway and for separating semantic keys (entity/subject representations) from factual values (relations/truths). MEMIT extends this view to scalable, multi-fact memory injection, directly informing UniKE’s goal of reliable, batchable intrinsic edits.
At the same time, UniKE’s external resorting path draws on retrieval-based overlays. kNN-LM introduced a vector datastore that plugs into generation as a key–value lookup, while RAG formalized end-to-end retrieval-augmented generation—both shaping UniKE’s representation of external knowledge as vector memories aligned with internal semantics. SERAC specifically frames edited knowledge as an external memory with gating to ensure locality and reliability, which UniKE adapts in a multimodal context to decide when to rely on external versus intrinsic stores. Finally, MEND informs UniKE’s training and evaluation priorities—preserving locality and generality—while UniKE extends these principles across modalities and introduces an explicit semantic-versus-truthfulness disentanglement to coordinate intrinsic assimilation and external accommodation at the same semantic levels.

---
*Generated: 2026-01-07T00:02:04.768357*
