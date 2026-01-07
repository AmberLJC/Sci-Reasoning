# Prior Work Analysis Report

## Target Paper
**Title:** qN5hmLkBtC
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

SAILOR’s key contribution is to move imitation beyond action matching toward decision-time planning that achieves expert outcomes even after errors. This builds on three converging threads. First, DAgger and SEARN crystallized the core failure of behavioral cloning—covariate shift—and proposed the learning-to-search view: train components that enable recovery during sequential decision making. SAILOR embraces this framing but shifts the recovery mechanism from interactive relabeling to online search at test time.
Second, advances in imitation via reward learning (GAIL, AIRL) replaced next-action supervision with objectives over outcomes/occupancies. AIRL in particular emphasizes learning a reward that transfers and supports planning. SAILOR adopts this insight by explicitly learning a reward model from demonstrations, using it as the objective for search rather than relying solely on a discriminative policy.
Third, model-based planning with learned dynamics (PETS, PlaNet) and unified model-and-search systems (MuZero) demonstrated that learned world models, paired with MPC or tree search, can be both robust and sample-efficient. SAILOR combines these ingredients: it learns a compact world model and a reward model from expert data, then performs decision-time search (e.g., CEM/MCTS) to select actions that optimize the learned reward under the learned dynamics. Through careful algorithmic choices inspired by these works—ensembles/latents for stability, planning horizons and objectives for robustness—SAILOR operationalizes learning-to-search specifically for imitation, delivering recovery from off-demonstration states without requiring expert queries.

---
*Generated: 2026-01-07T00:02:04.973195*
