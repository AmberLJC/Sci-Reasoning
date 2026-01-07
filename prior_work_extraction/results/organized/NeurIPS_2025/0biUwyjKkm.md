# Prior Work Analysis Report

## Target Paper
**Title:** 0biUwyjKkm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

OpenHOI’s core contribution—open-world HOI synthesis that follows free-form language while generalizing to novel objects—emerges from the convergence of three research lines. First, SayCan established that LLMs become actionable planners when grounded in affordances and cost-to-go estimates, which OpenHOI adapts to hand–object manipulation by jointly learning semantic task decomposition and affordance grounding in a single 3D MLLM. Second, visual-instruction-tuned MLLMs (LLaVA) and their 3D counterparts (3D-LLM) provide the training recipe and representational interface to align language with geometric context; OpenHOI extends this to localize interaction-relevant parts (e.g., handles, buttons) and to parse complex, long-horizon commands into executable sub-tasks in 3D. Third, for physically plausible synthesis, diffusion-based motion generation (MDM) gives the backbone for producing long, coherent interaction trajectories. This is complemented by physics-aware guidance exemplified by PhysDiff, inspiring OpenHOI’s training-free refinement to enforce contact and feasibility without extra learning. Finally, HOI- and articulation-focused work such as Where2Act and ArtiGrasp directly inform OpenHOI’s affordance-driven conditioning: predicting actionable regions on articulated objects and modeling contact/part interactions. Together, these works concretely enable OpenHOI’s key innovation: an affordance-conditioned diffusion pipeline steered by a 3D MLLM that both grounds open-vocabulary semantics in object parts and decomposes tasks, yielding long-horizon, physically consistent hand–object interactions for unseen objects.

---
*Generated: 2026-01-07T00:21:32.300756*
