# Prior Work Analysis Report

## Target Paper
**Title:** TiFMYdQiqp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The key contribution of Bayesian target optimisation sits at the intersection of optical advances enabling precise multi-site two-photon stimulation and probabilistic modeling that can learn and exploit neural response structure. Early demonstrations of two-photon optogenetics (Rickgauer & Tank) defined the achievable spatial precision and revealed the challenge of light spread and variable sensitivity. Holographic, scanless stimulation and temporal focusing (Papagiakoumou et al.) then created the practical pathway to stimulate many cells simultaneously, while all-optical physiology (Packer et al.) exposed the real-world impact of off-target stimulation during ensemble control. Three-dimensional SHOT (Pégard et al.) further expanded the controllable parameter space—3D positions with per-target power modulation—making the problem of selecting powers and locations a high-dimensional optimisation task. Concurrently, soma-targeted opsins and ensemble protocols (Mardinly et al.) mitigated but did not eliminate off-target effects, underscoring the need for computational calibration that accounts for neuron-specific dose–response heterogeneity. On the modeling side, Gaussian processes (Rasmussen & Williams) provide a principled nonparametric Bayesian framework to learn smooth response surfaces with quantified uncertainty; GP-based receptive field estimation in neuroscience (Park & Pillow) showed how to extract structured neural sensitivity from sparse measurements. Building directly on these threads, the present paper formalizes an ‘optogenetic response field’ learned with GP inference and uses uncertainty-aware Bayesian optimisation to select laser powers and target locations that achieve desired population activity while actively suppressing off-target stimulation, complementing and extending the optical toolkit with a data-driven control layer.

---
*Generated: 2026-01-06T23:42:49.075992*
