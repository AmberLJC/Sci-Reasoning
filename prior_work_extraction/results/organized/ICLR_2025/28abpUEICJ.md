# Prior Work Analysis Report

## Target Paper

**Title:** CREIMBO: Cross-Regional Ensemble Interactions in Multi-view Brain Observations

**Conference:** ICLR 2025 (spotlight)

**Authors:** Noga Mudrik, Ryan Ly, Oliver Ruebel, Adam Shabti Charles

**Keywords:** computational neuroscience, multi-regional brain interactions, sparsity, cross-session variability, dynamical systems modeling, neural dynamics, non-simultaneous neural recordings

**Abstract:** 
> Modern recordings of neural activity provide diverse observations of neurons across brain areas, behavioral conditions, and subjects; presenting an exciting opportunity to reveal the fundamentals of brain-wide dynamics. Current analysis methods, however, often fail to fully harness the richness of such data, as they provide either uninterpretable representations (e.g., via deep networks) or oversimplify models (e.g., by assuming stationary dynamics or analyzing each session independently). Here,...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**A Reduced-Dimension fMRI Shared Response Model** (2015)
- *Authors:* P.-H. Chen et al.
- *Direct Connection:* SRM introduced the multi-view shared-latent formulation with subject-specific loadings, which CREIMBO generalizes to neural recordings across regions/sessions by learning shared global interaction bases without neuron identity alignment.

### 💡 Inspiration

**Cortical areas interact through a communication subspace** (2019)
- *Authors:* R. E. M. Semedo et al.
- *Direct Connection:* The notion that inter-areal interactions are mediated by a low-dimensional 'communication subspace' directly motivates CREIMBO’s representation of cross-regional coupling as a small set of global basis interaction sub-circuits.

**Bayesian Group Factor Analysis** (2012)
- *Authors:* S. Virtanen et al.
- *Direct Connection:* Group factor analysis’s idea of group-sparse loadings across views informs CREIMBO’s ensemble-to-subcircuit assignments that yield interpretable, sparse cross-regional interaction structure.

### 🔍 Gap Identification

**Inferring single-trial neural population dynamics using sequential auto-encoders** (2018)
- *Authors:* C. Pandarinath et al.
- *Direct Connection:* While powerful for recovering latent dynamics, LFADS produces largely uninterpretable latent factors and is typically trained per session, a limitation CREIMBO addresses by imposing sparse, ensemble-structured interaction bases shared across datasets.

**Long-term stability of cortical population dynamics underlying consistent behavior** (2020)
- *Authors:* J. A. Gallego et al.
- *Direct Connection:* This work established stable latent manifolds across days using explicit alignment procedures, whose reliance on alignment and simultaneous structure CREIMBO replaces with a generative, shared-interaction model learned from asynchronous data.

### 📊 Baseline

**AutoLFADS: automated inference of neural population dynamics at scale** (2022)
- *Authors:* A. A. Keshtkaran et al.
- *Direct Connection:* AutoLFADS pools across sessions but does not learn shared, interpretable cross-regional interaction bases or handle non-simultaneous, multi-area recordings without alignment, which CREIMBO is designed to do.

### 🔗 Related Problem

**Modeling behaviorally relevant neural dynamics using preferential subspace identification** (2021)
- *Authors:* A. M. Sani et al.
- *Direct Connection:* PSID’s linear state-space identification under partial observation informs CREIMBO’s use of interpretable, low-dimensional dynamical structure while CREIMBO extends this perspective to multi-view, cross-regional coupling.

---

## Synthesis: How Prior Work Led to This Paper

Semedo and colleagues showed that inter-areal communication is constrained to a low-dimensional subspace, evidencing that cross-regional coupling can be captured parsimoniously by a few interaction modes. LFADS established that latent dynamical systems can recover single-trial population dynamics but did so with opaque latent factors and typically per-session training. AutoLFADS pooled across sessions to scale LFADS, yet it did not impose interpretable structure for cross-area coupling nor address non-simultaneous recordings without alignment. Gallego and collaborators demonstrated that latent manifolds can remain stable across days, but depended on explicit alignment procedures to stitch sessions, implying a need for generative models that naturally integrate asynchronous, non-identical recordings. PSID framed interpretable linear state-space identification under partial observation, separating behaviorally relevant dynamics, highlighting how principled system identification can recover structured latent dynamics without deep black boxes. The Shared Response Model introduced a multi-view shared-latent formulation with subject-specific loadings, offering a template for learning shared latent structure without voxel/neuron identity. Bayesian Group Factor Analysis provided group-sparse loadings across views, a mechanism to assign interpretable, view-specific participation in shared factors. Together, these works suggested that cross-area interactions are low dimensional and sparse, that multi-session integration should avoid brittle alignment, and that multi-view generative factorization can share structure while allowing view-specific variability. Building on these insights, the natural next step is to learn a unified, interpretable dynamical model where global sub-circuit bases mediate cross-regional ensemble interactions and accommodate asynchronous, non-simultaneous recordings via shared interaction structure with sparse, ensemble-level loadings.

---

*Analysis generated on: 2026-01-06T13:05:49.363034*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
